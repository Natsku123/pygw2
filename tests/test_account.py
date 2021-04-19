from pygw2.api import api
import aiounittest
import unittest
import os

from pygw2.core.models.account import Account

api.setup(os.environ.get("api_key", "NO-KEY"))


class AccountTests(aiounittest.AsyncTestCase):
    async def test_account_get(self):
        acc = await api.account.get()
        self.assertIsInstance(acc, Account)

    async def test_account_achievements(self):
        acc = await api.account.achievements()
        self.assertIsInstance(acc, list)

    async def test_bank(self):
        bank = await api.account.bank()
        self.assertIsInstance(bank, list)

    async def test_shared_inventory(self):
        inventory = await api.account.inventory()
        self.assertIsInstance(inventory, list)


if __name__ == '__main__':
    unittest.main()
