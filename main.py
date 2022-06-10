from extensions import web3
from extensions import uniswap_wrapper
from config import config
import requests
from utils import get_abi_code_by_address
from utils import get_token_price_by_address
import json

contract = web3.eth.contract(address=config.FACTORY_ADDRESS, abi=config.FACTORY_ABI)


def main():
    pairs_length = contract.functions.allPairsLength().call()
    all_pairs_addresses = [contract.functions.allPairs(i).call() for i in range(pairs_length - 1)]
    with open('all_pairs_addresses.json', 'w') as fp:
        json.dump(all_pairs_addresses, fp)

    results = []
    for pair_address in all_pairs_addresses:
        abi = get_abi_code_by_address(pair_address)
        pair_contract = web3.eth.contract(address=pair_address, abi=abi)

        token_0_address = pair_contract.functions.token0().call()
        token_1_address = pair_contract.functions.token1().call()

        token_0 = uniswap_wrapper.get_token(token_0_address, 'erc20')
        token_1 = uniswap_wrapper.get_token(token_1_address, 'erc20')

        reserves = pair_contract.functions.getReserves().call()

        results.append({
            'pool_address': pair_address,
            'token0': {
                'address': token_0_address,
                'symbol': token_0.symbol,
                'price:': get_token_price_by_address(token_0_address),
                'decimals': token_0.decimals,
                'reserves': reserves[0]

            },
            'token1': {
                'address': token_1_address,
                'symbol': token_1.symbol,
                'price:': get_token_price_by_address(token_1_address),
                'decimals': token_1.decimals,
                'reserves': reserves[1],

            }
        }
        )
    with open('data.json', 'w') as fp:
        json.dump(results, fp)

    return results


if __name__ == '__main__':
    print(main())
