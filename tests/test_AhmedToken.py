from scripts.helpful_scripts import get_account, initial_supply
from brownie import AhmedToken


def test_can_deploy_token():
    account = get_account()
    ahmed_token = AhmedToken.deploy(initial_supply, {"from": account})
    assert ahmed_token.name({"from": account}) == "AhmedToken"
