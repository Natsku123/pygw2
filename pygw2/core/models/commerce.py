import datetime
from typing import Optional, List, Union, TYPE_CHECKING
from pydantic import BaseModel

if TYPE_CHECKING:
    from pygw2.core.models.items import Item


class DeliveryBoxItem(BaseModel):
    id: int
    count: int
    item: "Item"


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
    item: "Item"
    buys: List[Listing]
    sells: List[Listing]


class PriceInfo(BaseModel):
    quantity: int
    unit_price: int


class Price(BaseModel):
    id: int
    item: "Item"
    whitelisted: bool
    buys: PriceInfo
    sells: PriceInfo


class Transaction(BaseModel):
    id: int
    item_id: int
    item: "Item"
    price: int
    quantity: int
    created: datetime.datetime
    purchased: Optional[datetime.datetime]
