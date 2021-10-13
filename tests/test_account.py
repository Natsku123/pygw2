import aiounittest
import unittest
import pytest

from pygw2.core.models.account import Account, SharedInventorySlot
from pygw2.core.models.items import Item


@pytest.mark.usefixtures("get_api")
class AccountTests(aiounittest.AsyncTestCase):
    async def test_account_get(self):
        acc = await self.api.account.get()
        self.assertIsInstance(acc, Account)

    async def test_account_achievements(self):
        acc = await self.api.account.achievements()
        self.assertIsInstance(acc, list)

    async def test_bank(self):
        bank = await self.api.account.bank()
        self.assertIsInstance(bank, list)

    async def test_shared_inventory(self):
        inventory = await self.api.account.inventory()
        self.assertIsInstance(inventory, list)
        for slot in inventory:
            self.assertIsInstance(slot, SharedInventorySlot)
            if slot.item:
                self.assertIsInstance(slot.item, Item)


if __name__ == "__main__":
    unittest.main()
