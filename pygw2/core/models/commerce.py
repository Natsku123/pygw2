import datetime
from typing import Optional, List, Union, TYPE_CHECKING
from pydantic import BaseModel

from pygw2.utils import LazyLoader

if TYPE_CHECKING:
    from pygw2.core.models.items import Item


class DeliveryBoxItem(BaseModel):
    id: int
    count: int
    _item: LazyLoader

    @property
    def item(self) -> "Item":
        return self._item()


class DeliveryBox(BaseModel):
    coins: int
    items: List[DeliveryBoxItem]


class ExchangeRate(BaseModel):
    coins_per_gem: int
    quantity: int


class Listing(BaseModel):
    listings: int
    unit_price: int
    quantity: int


class ItemListing(BaseModel):
    id: int
    _item: LazyLoader

    @property
    def item(self) -> "Item":
        return self._item()

    buys: List[Listing]
    sells: List[Listing]


class PriceInfo(BaseModel):
    quantity: int
    unit_price: int


class Price(BaseModel):
    id: int
    _item: LazyLoader

    @property
    def item(self) -> "Item":
        return self._item()

    whitelisted: bool
    buys: PriceInfo
    sells: PriceInfo


class Transaction(BaseModel):
    id: int
    item_id: int
    _item: LazyLoader

    @property
    def item(self) -> "Item":
        return self._item()

    price: int
    quantity: int
    created: datetime.datetime
    purchased: Optional[datetime.datetime]
