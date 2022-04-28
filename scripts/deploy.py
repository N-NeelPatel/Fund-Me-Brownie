from scripts.helpful_scripts import get_account


from scripts.helpful_scripts import get_account, NETWORKS
from brownie import FundMe


DECIMALS = 8
STARTING_PRICE = 200000000000


def get_fund_me():
    account = get_account()

    fund_me = FundMe.deploy(
        "0x8A753747A1Fa494EC906cE90E9f37563A8AF630e",
        {"from": account},
        publish_source=True,
    )
    print(f"Contract deployed... to {fund_me.address}")


def main():
    get_fund_me()