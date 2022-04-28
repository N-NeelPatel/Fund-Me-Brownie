from brownie import network, config, accounts

NETWORKS = ["development", "ganache-local"]


def get_account():
    if network.show_active() in NETWORKS:
        return accounts[0]
    else:
        return accounts.add(config["wallet"]["from_key"])
