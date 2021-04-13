import datetime
from typing import Optional, List
from pydantic import BaseModel

from pygw2.core.enums import Binding, AccountAccess


class VaultSlot(BaseModel):
    id: int     # TODO resolve against items
    count: int
    charges: Optional[int]
    skin: Optional[int]     # TODO resolve against skins
    upgrades: Optional[List[int]]     # TODO resolve against items (?)
    infusions: Optional[List[int]]    # TODO resolve against items (?)
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
    region: 'Region'
    levels: List[MasteryLevel]


class MasteryProgress(BaseModel):
    id: int     # TODO resolve against mastery
    level: int


class Title(BaseModel):
    id: int = 0
    name: str = ""
    achievement: int = 0            # TODO resolve against achievements
    achievements: List[int] = []    # TODO resolve against achievements
    ap_required: int


class Account(BaseModel):
    id: str
    age: int
    name: str
    world: int      # TODO resolve against /v2/worlds
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
    id: int     # TODO resolve against skills


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
    default_skin: int   # TODO resolve against mount skins
    skins: List[int]    # TODO resolve against mount skins
    skills: List[MountSkill]