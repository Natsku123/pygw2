from __future__ import annotations

import datetime
from typing import TYPE_CHECKING, ForwardRef

from pygw2.utils import LazyLoader, BaseModel

if TYPE_CHECKING:
    from pygw2.core.models.items import Item
else:
    Item = ForwardRef("Item")


class DeliveryBoxItem(BaseModel):
    id: int
    count: int
    item_: LazyLoader

    @property
    def item(self) -> Item:
        return self.item_()


class DeliveryBox(BaseModel):
    coins: int
    items: list[DeliveryBoxItem]


class ExchangeRate(BaseModel):
    coins_per_gem: int
    quantity: int


class Listing(BaseModel):
    listings: int
    unit_price: int
    quantity: int


class ItemListing(BaseModel):
    id: int
    item_: LazyLoader

    @property
    def item(self) -> Item:
        return self.item_()

    buys: list[Listing]
    sells: list[Listing]


class PriceInfo(BaseModel):
    quantity: int
    unit_price: int


class Price(BaseModel):
    id: int
    item_: LazyLoader

    @property
    def item(self) -> Item:
        return self.item_()

    whitelisted: bool
    buys: PriceInfo
    sells: PriceInfo


class Transaction(BaseModel):
    id: int
    item_id: int
    item_: LazyLoader

    @property
    def item(self) -> Item:
        return self.item_()

    price: int
    quantity: int
    created: datetime.datetime
    purchased: datetime.datetime | None = None
