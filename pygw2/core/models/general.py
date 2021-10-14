from typing import Optional, List, Union, TYPE_CHECKING

from pygw2.core.enums import *
from pygw2.utils import LazyLoader, BaseModel

if TYPE_CHECKING:
    from pygw2.core.models.misc import Color


class Finisher(BaseModel):
    id: int = 0
    unlock_details: str = ""
    unlock_items: Optional[List[int]]  # TODO resolve against items
    order: int = 0
    icon: str = ""
    name: str = ""


class StatAttributes(BaseModel):
    attribute: Attribute
    multiplier: float
    value: int


class ItemStat(BaseModel):
    id: int = 0
    name: str = ""
    attributes: List[StatAttributes]


class DailyCrafting(BaseModel):
    id: str


class DailyMapChest(BaseModel):
    id: str


class DailyWorldBoss(BaseModel):
    id: str


class Skin(BaseModel):
    id: int
    name: str
    type: SkinType
    flags: List[SkinFlag]
    restrictions: List[Races]
    icon: str
    rarity: str  # TODO same as ItemRarity?
    description: Optional[str]
    details: Optional[
        Union["ArmorSkinDetails", "WeaponSkinDetails", "GatheringSkinDetails"]
    ]


class DyeSlot(BaseModel):
    color_id: Optional[int]
    color_: Optional[LazyLoader]

    @property
    def color(self) -> Optional["Color"]:
        return self.color_() if self.color_ is not None else None

    material: Optional[DyeSlotMaterial]


class SkinDyeSlots(BaseModel):
    default: List[Optional[DyeSlot]]
    overrides: DyeSlot


class ArmorSkinDetails(BaseModel):
    type: ArmorSlot
    weight_class: WeightClass
    dye_slots: Optional[SkinDyeSlots]


class WeaponSkinDetails(BaseModel):
    type: WeaponType
    damage_type: Optional[DamageType]


class GatheringSkinDetails(BaseModel):
    type: GatheringToolType


class MountSkin(BaseModel):
    id: int = 0
    name: str = ""
    icon: str = ""
    mount: str = ""  # TODO resolve against mount types
    dye_slots: List[DyeSlot]


Skin.update_forward_refs()
