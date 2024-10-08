from web3 import Web3
from config import PROVIDER
import hashlib
import os


class ExchangeAccountData:
    address: str
    pubkey: str
    signature_r: str
    signature_s: str
    context: dict

    def __init__(self, address: str, pubkey: str, signature_r: str, signature_s: str):
        self.address = address
        self.pubkey = pubkey
        self.signature_r = signature_r
        self.signature_s = signature_s

        self.context = {}

    def set_value(self, key, value):
        self.context[key] = value

    def get_value(self, key):
        return self.context[key]

    @classmethod
    def load(cls, account_data):
        obj = cls(
            account_data["address"],
            account_data["pubkey"],
            account_data["signature"]["r"],
            account_data["signature"]["s"],
        )
        provider = Web3(Web3.HTTPProvider(PROVIDER))
        balance_wei = provider.eth.get_balance(obj.address)
        obj.set_value("balance", balance_wei)
        return obj

    def __hash__(self):
        return hash(self.address)


class UserAccountData:
    user_id: str
    amount: int

    context: dict

    def __init__(self, user_id: str, amount: int):
        self.user_id = user_id
        self.amount = amount

        self.context = {}

    def set_value(self, key, value):
        self.context[key] = value

    def get_value(self, key):
        return self.context[key]

    @property
    def id(self):
        return int(self.user_id, 16)
