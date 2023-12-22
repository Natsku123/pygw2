from __future__ import annotations

from typing import TYPE_CHECKING, ForwardRef

from pygw2.core.enums import *
from pygw2.utils import LazyLoader, BaseModel

if TYPE_CHECKING:
    from pygw2.core.models.misc import Color
else:
    Color = ForwardRef("Color")
    ArmorSkinDetails = ForwardRef("ArmorSkinDetails")
    WeaponSkinDetails = ForwardRef("WeaponSkinDetails")
    GatheringSkinDetails = ForwardRef("GatheringSkinDetails")
    Foo = ForwardRef("Foo")


class Finisher(BaseModel):
    id: int = 0
    unlock_details: str = ""
    unlock_items: list[int] | None  # TODO resolve against items
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
    attributes: list[StatAttributes]


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
    flags: list[SkinFlag]
    restrictions: list[Races]
    icon: str
    rarity: str  # TODO same as ItemRarity?
    description: str | None
    details: ArmorSkinDetails | WeaponSkinDetails | GatheringSkinDetails | Foo | None


class DyeSlot(BaseModel):
    color_id: int | None
    color_: LazyLoader | None

    @property
    def color(self) -> Color | None:
        return self.color_() if self.color_ is not None else None

    material: DyeSlotMaterial | None


class SkinDyeSlots(BaseModel):
    default: list[DyeSlot | None]
    overrides: DyeSlot


class ArmorSkinDetails(BaseModel):
    type: ArmorSlot
    weight_class: WeightClass
    dye_slots: SkinDyeSlots | None


class WeaponSkinDetails(BaseModel):
    type: WeaponType
    damage_type: DamageType | None


class GatheringSkinDetails(BaseModel):
    type: GatheringToolType


class Foo(BaseModel):
    type: str


class MountSkin(BaseModel):
    id: int = 0
    name: str = ""
    icon: str = ""
    mount: str = ""  # TODO resolve against mount types
    dye_slots: list[DyeSlot]


Skin.model_rebuild()
