from pygw2.api import api
import unittest
import os

from pygw2.core.models.account import Account

api.setup(os.environ.get("api_key", "NO-KEY"))


class AccountTests(unittest.TestCase):
    def test_account_get(self):
        acc = api.account.get()
        self.assertIsInstance(acc, Account)

    def test_account_achievements(self):
        acc = api.account.achievements()
        self.assertIsInstance(acc, list)

    def test_bank(self):
        bank = api.account.bank()
        self.assertIsInstance(bank, list)

    def test_shared_inventory(self):
        inventory = api.account.inventory()
        self.assertIsInstance(inventory, list)


if __name__ == '__main__':
    unittest.main()
