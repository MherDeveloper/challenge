import os


class Config(object):
    BASEDIR = os.path.abspath(os.path.dirname(__file__))


class EthereumDevelopmentConfig(Config):
    CHAIN_NAME = 'Ethereum'
    CHAIN_URI = 'https://mainnet.infura.io/v3/629f9c9a83b64e92b88203ad65c7ff2d'
    # CHAIN_URI = 'https://eth-mainnet.alchemyapi.io/v2/OCil3oXAMGtrFeptBPchZAL7CoYRAFJf'

    # Ethereum API_KEY and SECRET_KEY

    SECRET_KEY = 'eth-secret'
    ETHERSCAN_API_TOKEN = "IXU6IM6Q1MC1B6FP2PP2M2292CUFE7KN35"

    ADDRESS = "0x0000000000000000000000000000000000000000"
    PRIVATE_KEY = None

    FACTORY_ADDRESS = "0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f"
    FACTORY_ABI = '[{"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"payable":false,' \
                  '"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,' \
                  '"internalType":"address","name":"token0","type":"address"},{"indexed":true,"internalType":"address",' \
                  '"name":"token1","type":"address"},{"indexed":false,"internalType":"address","name":"pair",' \
                  '"type":"address"},{"indexed":false,"internalType":"uint256","name":"","type":"uint256"}],' \
                  '"name":"PairCreated","type":"event"},{"constant":true,"inputs":[{"internalType":"uint256",' \
                  '"name":"","type":"uint256"}],"name":"allPairs","outputs":[{"internalType":"address","name":"",' \
                  '"type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,' \
                  '"inputs":[],"name":"allPairsLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}]' \
                  ',"payable":false,"stateMutability":"view","type":"function"},{"constant":false,' \
                  '"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address",' \
                  '"name":"tokenB","type":"address"}],"name":"createPair","outputs":[{"internalType":"address",' \
                  '"name":"pair","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"function"},' \
                  '{"constant":true,"inputs":[],"name":"feeTo","outputs":[{"internalType":"address","name":"",' \
                  '"type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,' \
                  '"inputs":[],"name":"feeToSetter","outputs":[{"internalType":"address","name":"","type":"address"}],' \
                  '"payable":false,"stateMutability":"view","type":"function"},{"constant":true,' \
                  '"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":""' \
                  ',"type":"address"}],"name":"getPair","outputs":[{"internalType":"address","name":"","type":"address"}]' \
                  ',"payable":false,"stateMutability":"view","type":"function"},{"constant":false,' \
                  '"inputs":[{"internalType":"address","name":"_feeTo","type":"address"}],"name":"setFeeTo","outputs":[],' \
                  '"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,' \
                  '"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"name":"setFeeToSetter",' \
                  '"outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]'


config = EthereumDevelopmentConfig()
