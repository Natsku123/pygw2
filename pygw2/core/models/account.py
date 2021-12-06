import datetime
from typing import Optional, List, TYPE_CHECKING

from pygw2.utils import LazyLoader, BaseModel

from pygw2.core.enums import Binding, AccountAccess, Region

if TYPE_CHECKING:
    from pygw2.core.models.items import Item
    from pygw2.core.models.general import Skin, Finisher
    from pygw2.core.models.misc import Currency
    from pygw2.core.models.wvw import World


class VaultSlot(BaseModel):
    id: int  # TODO resolve against items
    item_: LazyLoader

    @property
    def item(self) -> "Item":
        return self.item_()

    count: int
    charges: Optional[int]
    skin_: Optional[LazyLoader]

    @property
    def skin(self) -> Optional["Skin"]:
        return self.skin_() if self.skin_ is not None else None

    upgrades_: Optional[LazyLoader]

    @property
    def upgrades(self) -> Optional[List["Item"]]:
        return self.upgrades_() if self.upgrades_ is not None else None

    infusions_: Optional[LazyLoader]

    @property
    def infusions(self) -> Optional[List["Item"]]:
        return self.infusions_() if self.infusions_ is not None else None

    binding: Optional[Binding]
    bound_to: Optional[str]


class Coins(BaseModel):
    count: int
    type: Optional[str]


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
    region: "Region"
    levels: List[MasteryLevel]


class MasteryProgress(BaseModel):
    id: int
    mastery_: LazyLoader

    @property
    def mastery(self) -> "Mastery":
        return self.mastery_()

    level: int


class Account(BaseModel):
    id: str
    age: int
    name: str
    world: int  # TODO resolve against /v2/worlds
    world_: LazyLoader

    @property
    def world(self) -> "World":
        return self.world_()

    guilds: List[str] = []
    guild_leader: List[str] = []
    created: datetime.datetime
    access: List[AccountAccess]
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
    skills: List[PetSkill]


class HomeCat(BaseModel):
    id: int
    hint: Optional[str]


class HomeNode(BaseModel):
    id: str


class MountSkill(BaseModel):
    id: int
    slot: str


class MountType(BaseModel):
    id: str = ""
    name: str = ""
    default_skin: int  # TODO resolve against mount skins
    skins: List[int]  # TODO resolve against mount skins
    skills: List[MountSkill]


class UnlockedFinisher(BaseModel):
    id: int
    finisher_: LazyLoader

    @property
    def finisher(self) -> "Finisher":
        return self.finisher_()

    permanent: bool
    quantity: Optional[int]


class SharedInventorySlot(BaseModel):
    id: int
    item_: LazyLoader

    @property
    def item(self) -> "Item":
        return self.item_()

    count: int
    charges: Optional[int]
    skin_: Optional[LazyLoader]

    @property
    def skin(self) -> Optional["Skin"]:
        return self.skin_() if self.skin_ is not None else None

    upgrades_: Optional[LazyLoader]

    @property
    def upgrades(self) -> Optional[List["Item"]]:
        return self.upgrades_() if self.upgrades_ is not None else None

    infusions_: Optional[LazyLoader]

    @property
    def infusions(self) -> Optional[List["Item"]]:
        return self.infusions_() if self.infusions_ is not None else None

    binding: Optional[Binding]


class StorageMaterial(BaseModel):
    id: int
    item_: LazyLoader

    @property
    def item(self) -> "Item":
        return self.item_()

    category: int
    count: int


class WalletCurrency(BaseModel):
    id: int
    currency_: LazyLoader

    @property
    def currency(self) -> "Currency":
        return self.currency_()

    value: int


class Legendary(BaseModel):
    id: int
    max_count: int
    item_: LazyLoader

    @property
    def item(self) -> "Item":
        return self.item_()


class OwnedLegendary(BaseModel):
    id: int
    count: int
    item_: LazyLoader

    @property
    def item(self) -> "Item":
        return self.item_()

    armory_: LazyLoader

    @property
    def max_count(self) -> int:
        return self.armory_().max_count
