import datetime
from typing import Optional, List, TYPE_CHECKING
from pydantic import BaseModel

from pygw2.utils import LazyLoader

from pygw2.core.enums import Binding, AccountAccess, Region

if TYPE_CHECKING:
    from pygw2.core.models.items import Item
    from pygw2.core.models.general import Skin, Finisher
    from pygw2.core.models.misc import Currency


class VaultSlot(BaseModel):
    id: int  # TODO resolve against items
    _item: LazyLoader

    @property
    def item(self) -> "Item":
        return self._item()

    count: int
    charges: Optional[int]
    _skin: Optional[LazyLoader]

    @property
    def skin(self) -> Optional["Skin"]:
        return self._skin() if self._skin is not None else None

    _upgrades: Optional[LazyLoader]

    @property
    def upgrades(self) -> Optional[List["Item"]]:
        return self._upgrades() if self._upgrades is not None else None

    _infusions: Optional[LazyLoader]

    @property
    def infusions(self) -> Optional[List["Item"]]:
        return self._infusions() if self._infusions is not None else None

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
    id: int  # TODO resolve against mastery
    level: int


class Account(BaseModel):
    id: str
    age: int
    name: str
    world: int  # TODO resolve against /v2/worlds
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
    _finisher: LazyLoader

    @property
    def finisher(self) -> "Finisher":
        return self._finisher()

    permanent: bool
    quantity: Optional[int]


class SharedInventorySlot(BaseModel):
    id: int
    _item: LazyLoader

    @property
    def item(self) -> "Item":
        return self._item()

    count: int
    charges: Optional[int]
    _skin: Optional[LazyLoader]

    @property
    def skin(self) -> Optional["Skin"]:
        return self._skin() if self._skin is not None else None

    _upgrades: Optional[LazyLoader]

    @property
    def upgrades(self) -> Optional[List["Item"]]:
        return self._upgrades() if self._upgrades is not None else None

    _infusions: Optional[LazyLoader]

    @property
    def infusions(self) -> Optional[List["Item"]]:
        return self._infusions() if self._infusions is not None else None

    binding: Optional[Binding]


class Material(BaseModel):
    id: int
    _item: LazyLoader

    @property
    def item(self) -> "Item":
        return self._item()

    category: int
    count: int


class WalletCurrency(BaseModel):
    id: int
    _currency: LazyLoader

    @property
    def currency(self) -> "Currency":
        return self._currency()

    value: int
