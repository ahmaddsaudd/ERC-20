from brownie import AhmedToken
from brownie import network
from scripts.helpful_scripts import get_account, initial_supply
from web3 import Web3


def deploy():
    account = get_account()
    ahmed_token = AhmedToken.deploy(initial_supply, {"from": account})
    token_name = ahmed_token.name({"from": account})
    print(f"name of this token is {token_name}")


def main():
    deploy()
