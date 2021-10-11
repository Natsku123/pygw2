from typing import List, Union

from ..utils import endpoint, object_parse
from ..core.models.commerce import (
    DeliveryBox,
    ExchangeRate,
    ItemListing,
    Price,
    Transaction,
)

from .items import ItemsApi

items_api = ItemsApi()


class TradingPostApi:
    def __init__(self):
        self.api_key: str = ""

    def setup(self, api_key: str):
        self.api_key = api_key

    @endpoint("/v2/commerce/delivery")
    async def delivery(self, *, data) -> DeliveryBox:
        """
        Get delivery box data from API.
        :param data: data from wrapper
        :return: object
        """
        for item in data["items"]:
            item["item"] = (await items_api.get(ids=[item["id"]]))[0]
        return object_parse(data, DeliveryBox)

    @endpoint(
        "/v2/commerce/exchange/coins",
        override_ids="quantity",
        has_ids=True,
        max_ids=1,
        min_ids=1,
    )
    async def exchange_coins(self, *, data, ids: list = None) -> ExchangeRate:
        """
        Get coins -> gems exchange rate from API.
        :param data: data from wrapper
        :param ids: List with number of coins
        :return: object
        """

        return object_parse(data, ExchangeRate)

    @endpoint(
        "/v2/commerce/exchange/gems",
        override_ids="quantity",
        has_ids=True,
        max_ids=1,
        min_ids=1,
    )
    async def exchange_gems(self, *, data, ids: list = None) -> ExchangeRate:
        """
        Get gems -> coins exchange rate from API.
        :param data: data from wrapper
        :param ids: List with number of gems
        :return: object
        """

        return object_parse(data, ExchangeRate)

    @endpoint("/v2/commerce/listings", has_ids=True)
    async def listings(
        self, *, data, ids: list = None
    ) -> List[Union[ItemListing, int, str]]:
        """
        Get Trading post listings from API.
        :param data: data from wrapper
        :param ids: list of IDs
        :return: list
        """

        if ids is None:
            return data

        for listing in data:
            listing["item"] = await items_api.get(listing["id"])

        return object_parse(data, ItemListing)

    @endpoint("/v2/commerce/prices", has_ids=True)
    async def prices(self, *, data, ids: list = None) -> List[Union[Price, int, str]]:
        """
        Get Trading post prices from API.
        :param data: data from wrapper
        :param ids: list of IDs
        :return: list
        """

        if ids is None:
            return data

        for price in data:
            price["item"] = await items_api.get(price["id"])

        return object_parse(data, Price)

    @endpoint("/v2/commerce/transactions/current/buys")
    async def current_buys(self, *, data) -> List[Transaction]:
        """
        Get current buy orders from API.
        :param data: data from wrapper
        :return: list
        """

        for transaction in data:
            transaction["item"] = await items_api.get(transaction["item_id"])

        return object_parse(data, Transaction)

    @endpoint("/v2/commerce/transactions/current/sells")
    async def current_sells(self, *, data) -> List[Transaction]:
        """
        Get current sell orders from API.
        :param data: data from wrapper
        :return: list
        """

        for transaction in data:
            transaction["item"] = await items_api.get(transaction["item_id"])

        return object_parse(data, Transaction)

    @endpoint("/v2/commerce/transactions/history/buys")
    async def history_buys(self, *, data) -> List[Transaction]:
        """
        Get buy order history from API.
        :param data: data from wrapper
        :return: list
        """

        for transaction in data:
            transaction["item"] = await items_api.get(transaction["item_id"])

        return object_parse(data, Transaction)

    @endpoint("/v2/commerce/transactions/history/sells")
    async def history_sells(self, *, data) -> List[Transaction]:
        """
        Get sell order history from API.
        :param data: data from wrapper
        :return: list
        """

        for transaction in data:
            transaction["item"] = await items_api.get(transaction["item_id"])

        return object_parse(data, Transaction)
