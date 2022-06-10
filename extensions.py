from web3 import Web3
from config import config
from uniswap import Uniswap

# node for web3 connection to blockchain

web3 = Web3(Web3.HTTPProvider(config.CHAIN_URI))
uniswap_wrapper = Uniswap(config.ADDRESS, config.PRIVATE_KEY, config.CHAIN_URI, version=2)
