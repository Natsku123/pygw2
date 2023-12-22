from __future__ import annotations

import datetime
from typing import TYPE_CHECKING, ForwardRef

from pygw2.utils import LazyLoader, BaseModel

from pygw2.core.enums import Binding, AccountAccess, Region, TokenTypes

if TYPE_CHECKING:
    from pygw2.core.models.items import Item
    from pygw2.core.models.general import Skin, Finisher
    from pygw2.core.models.misc import Currency
    from pygw2.core.models.wvw import World
else:
    Item = ForwardRef("Item")
    Mastery = ForwardRef("Mastery")
    World = ForwardRef("World")
    Finisher = ForwardRef("Finisher")
    Currency = ForwardRef("Currency")


class VaultSlot(BaseModel):
    id: int  # TODO resolve against items
    item_: LazyLoader

    @property
    def item(self) -> Item:
        return self.item_()

    count: int
    charges: int | None = None
    skin_: LazyLoader | None = None

    @property
    def skin(self) -> Skin | None:
        return self.skin_() if self.skin_ is not None else None

    upgrades_: LazyLoader | None = None

    @property
    def upgrades(self) -> list[Item] | None:
        return self.upgrades_() if self.upgrades_ is not None else None

    infusions_: LazyLoader | None = None

    @property
    def infusions(self) -> list[Item] | None:
        return self.infusions_() if self.infusions_ is not None else None

    binding: Binding | None = None
    bound_to: str | None = None


class Coins(BaseModel):
    count: int
    type: str | None = None


class MasteryLevel(BaseModel):
    name: str = ""
    description: str = ""
    icon: str = ""
    point_cost: int = ""
    exp_cost: int = ""


class Mastery(BaseModel):
    id: int = 0
    name: str = ""
    requirement: str = ""
    order: int = 0
    background: str = ""
    region: Region
    levels: list[MasteryLevel]


class MasteryProgress(BaseModel):
    id: int
    mastery_: LazyLoader

    @property
    def mastery(self) -> Mastery:
        return self.mastery_()

    level: int


class Account(BaseModel):
    id: str
    age: int
    name: str
    world: int  # TODO resolve against /v2/worlds
    world_: LazyLoader

    @property
    def world(self) -> World:
        return self.world_()

    guilds: list[str] = []
    guild_leader: list[str] = []
    created: datetime.datetime
    access: list[AccountAccess]
    commander: bool
    fractal_level: int
    daily_ap: int
    monthly_ap: int
    wvw_rank: int
    last_modified: datetime.datetime


class ProductAccess(BaseModel):
    product: AccountAccess
    condition: str


class PetSkill(BaseModel):
    id: int  # TODO resolve against skills


class Pet(BaseModel):
    id: int = 0
    name: str = ""
    description: str = ""
    icon: str = ""
    skills: list[PetSkill]


class HomeCat(BaseModel):
    id: int
    hint: str | None = None


class HomeNode(BaseModel):
    id: str


class MountSkill(BaseModel):
    id: int
    slot: str


class MountType(BaseModel):
    id: str = ""
    name: str = ""
    default_skin: int  # TODO resolve against mount skins
    skins: list[int]  # TODO resolve against mount skins
    skills: list[MountSkill]


class UnlockedFinisher(BaseModel):
    id: int
    finisher_: LazyLoader

    @property
    def finisher(self) -> Finisher:
        return self.finisher_()

    permanent: bool
    quantity: int | None = None


class SharedInventorySlot(BaseModel):
    id: int
    item_: LazyLoader

    @property
    def item(self) -> Item:
        return self.item_()

    count: int
    charges: int | None = None
    skin_: LazyLoader | None = None

    @property
    def skin(self) -> Skin | None:
        return self.skin_() if self.skin_ is not None else None

    upgrades_: LazyLoader | None = None

    @property
    def upgrades(self) -> list[Item] | None:
        return self.upgrades_() if self.upgrades_ is not None else None

    infusions_: LazyLoader | None = None

    @property
    def infusions(self) -> list[Item] | None:
        return self.infusions_() if self.infusions_ is not None else None

    binding: Binding | None = None


class StorageMaterial(BaseModel):
    id: int
    item_: LazyLoader

    @property
    def item(self) -> Item:
        return self.item_()

    category: int
    count: int


class WalletCurrency(BaseModel):
    id: int
    currency_: LazyLoader

    @property
    def currency(self) -> Currency:
        return self.currency_()

    value: int


class Legendary(BaseModel):
    id: int
    max_count: int
    item_: LazyLoader

    @property
    def item(self) -> Item:
        return self.item_()


class OwnedLegendary(BaseModel):
    id: int
    count: int
    item_: LazyLoader

    @property
    def item(self) -> Item:
        return self.item_()

    armory_: LazyLoader

    @property
    def max_count(self) -> int:
        return self.armory_().max_count


class SubToken(BaseModel):
    subtoken: str


class TokenInfo(BaseModel):
    id: str
    name: str
    permissions: list[str]
    type: TokenTypes
    expires_at: str | None = None
    issued_at: str | None = None
    urls: list[str] | None = None
