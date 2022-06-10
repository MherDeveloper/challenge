import requests
from config import config
from extensions import web3


def get_abi_code_by_address(address):
    url = f"https://api.etherscan.io/api?module=contract&action=getabi&address=" \
          f"{address}&apikey={config.ETHERSCAN_API_TOKEN}"
    return requests.get(url).json()['result']


def get_token_price_by_address(address):
    url = f"https://api.coingecko.com/api/v3/simple/token_price/ethereum?contract_addresses={address}&vs_currencies=usd"

    # return requests.get(url).json()[web3.toChecksumAddress(f"{address}")]['usd']
    token_info = requests.get(url).json()
    if token_info:
        return token_info[f"{address}".lower()]['usd']
    else:
        return 0

    # if bool(requests.get(url).json()[f"{address}".lower()]['usd']):
    #     return requests.get(url).json()[f"{address}".lower()]['usd']
    # else:
    #     return 0
