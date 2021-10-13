from typing import Optional, List, Union

from pygw2.core.enums import *
from pygw2.utils import LazyLoader, BaseModel


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
    description: str
    details: Optional[
        Union["ArmorSkinDetails", "WeaponSkinDetails", "GatheringSkinDetails"]
    ]


class DyeSlot(BaseModel):
    color_id: int  # TODO resolve against colors
    material: DyeSlotMaterial


class SkinDyeSlots(BaseModel):
    default: List[DyeSlot]
    overrides: DyeSlot


class ArmorSkinDetails(BaseModel):
    type: ArmorSlot
    weight_class: WeightClass
    dye_slots: SkinDyeSlots


class WeaponSkinDetails(BaseModel):
    type: WeaponType
    damage_type: DamageType


class GatheringSkinDetails(BaseModel):
    type: GatheringToolType


class MountSkin(BaseModel):
    id: int = 0
    name: str = ""
    icon: str = ""
    mount: str = ""  # TODO resolve against mount types
    dye_slots: List[DyeSlot]


Skin.update_forward_refs()
