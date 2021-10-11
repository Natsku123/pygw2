import pytest
from pygw2.core.models.commerce import (
    DeliveryBox,
    ExchangeRate,
    ItemListing,
    Price,
    Transaction,
)

import unittest
import aiounittest
from tests.helpers import ids_helper


@pytest.mark.usefixtures("get_api")
class CommerceTests(aiounittest.AsyncTestCase):
    async def test_delivery(self):
        delivery_box = await self.api.commerce.delivery()
        self.assertIsInstance(delivery_box, DeliveryBox)

    async def test_exchange_coins(self):
        rate = await self.api.commerce.exchange_coins(100)
        self.assertIsInstance(rate, ExchangeRate)

    async def test_exchange_gems(self):
        rate = await self.api.commerce.exchange_gems(100)
        self.assertIsInstance(rate, ExchangeRate)

    async def test_listings(self):
        await ids_helper(self, self.api.commerce.listings, ItemListing)

    async def test_prices(self):
        await ids_helper(self, self.api.commerce.prices, Price)

    async def test_current_buys(self):
        trans = await self.api.commerce.current_buys()
        self.assertIsInstance(trans, list)
        for t in trans:
            self.assertIsInstance(t, Transaction)

    async def test_current_sells(self):
        trans = await self.api.commerce.current_sells()
        self.assertIsInstance(trans, list)
        for t in trans:
            self.assertIsInstance(t, Transaction)

    async def test_history_buys(self):
        trans = await self.api.commerce.history_buys()
        self.assertIsInstance(trans, list)
        for t in trans:
            self.assertIsInstance(t, Transaction)

    async def test_history_sells(self):
        trans = await self.api.commerce.history_sells()
        self.assertIsInstance(trans, list)
        for t in trans:
            self.assertIsInstance(t, Transaction)


if __name__ == "__main__":
    unittest.main()
