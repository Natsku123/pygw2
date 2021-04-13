from pygw2.core.enums import *

from typing import Optional, List, Union
from pydantic import BaseModel


class Upgrade(BaseModel):
    upgrade: UpgradeType
    item_id: int


class Item(BaseModel):
    id: int
    chat_link: str
    name: str
    icon: Optional[str]
    description: Optional[str]
    type: ItemType
    rarity: ItemRarity
    level: int
    vendor_value: int
    default_skin: Optional[int]     # TODO resolve against /v2/skins
    flags: List[ItemFlags] = []
    game_types: List[GameTypes] = []
    restrictions: List[Union[Races, Professions]] = []
    upgrades_into: Optional[List[Upgrade]] = []
    upgrades_from: Optional[List[Upgrade]] = []
    details: Optional[Union[
        'ArmorDetails',
        'BackDetails',
        'BagDetails',
        'ConsumableDetails',
        'ContainerDetails',
        'GatheringToolDetails',
        'GizmoDetails',
        'MiniatureDetails',
        'SalvageKitDetails',
        'TrinketDetails',
        'UpgradeComponentDetails',
        'WeaponDetails'
    ]]


class InfixAttribute(BaseModel):
    attribute: Attribute
    modifier: int


class InfixBuff(BaseModel):
    skill_id: int
    description: Optional[str]


class InfixUpgrade(BaseModel):
    id: int
    attributes: List[InfixAttribute]
    buff: Optional[InfixBuff]


class InfusionSlot(BaseModel):
    flags: List[InfusionSlotType]
    item_id: Optional[int]


class ArmorDetails(BaseModel):
    type: ArmorSlot
    weight_class: WeightClass
    defense: int
    infusion_slots: List[InfusionSlot] = []
    attribute_adjustment: int
    infix_upgrade: Optional[InfixUpgrade]
    suffix_item_id: Optional[int]
    secondary_suffix_item_id: str = ""
    stat_choices: Optional[List[int]] = []      # TODO resolve against /v2/itemstats


class BackDetails(BaseModel):
    infusion_slots: List[InfusionSlot] = []
    attribute_adjustment: int
    infix_upgrade: Optional[InfixUpgrade]
    suffix_item_id: Optional[int]
    secondary_suffix_item_id: str = ""
    stat_choices: Optional[List[int]] = []      # TODO resolve against /v2/itemstats


class BagDetails(BaseModel):
    size: int
    no_sell_or_sort: bool


class ConsumableDetails(BaseModel):
    type: ConsumableType
    description: Optional[str]
    duration_ms: Optional[int]
    unlock_type: Optional[UnlockType]
    color_id: Optional[int]     # TODO resolve against dyes
    recipe_id: Optional[int]    # TODO resolve against recipes
    extra_recipe_ids: Optional[List[int]] = []      # TODO resolve against recipes
    guild_upgrade_id: Optional[int]     # TODO resolve against guild upgrades
    apply_count: Optional[int]
    name: Optional[str]
    icon: Optional[str]
    skins: Optional[List[int]] = []     # TODO resolve against skins


class ContainerDetails(BaseModel):
    type: ContainerType


class GatheringToolDetails(BaseModel):
    type: GatheringToolType


class GizmoDetails(BaseModel):
    type: GizmoType
    guild_upgrade_id: Optional[List[int]] = []      # TODO resolve guild upgrades
    vendor_ids: List[int] = []


class MiniatureDetails(BaseModel):
    minipet_id: int     # TODO resolve against minis


class SalvageKitDetails(BaseModel):
    type: SalvageKitType
    charges: int


class TrinketDetails(BaseModel):
    infusion_slots: List[InfusionSlot] = []
    attribute_adjustment: int
    infix_upgrade: Optional[InfixUpgrade]
    suffix_item_id: Optional[int]
    secondary_suffix_item_id: str = ""
    stat_choices: Optional[List[int]]   # TODO resolve against itemstats


class UpgradeComponentDetails(BaseModel):
    type: UpgradeComponentType
    flags: List[Union[WeaponType, UpgradeComponentFlag]] = []
    infusion_upgrade_flags: List[InfusionUpgradeFlag] = []
    suffix: str
    infix_upgrade: InfixUpgrade
    bonuses: List[str]


class WeaponDetails(BaseModel):
    type: Union[WeaponType, AdditionalWeaponType]
    damage_type: DamageType
    min_power: int
    max_power: int
    defense: int
    infusion_slots: List[InfusionSlot] = []
    attribute_adjustment: int
    infix_upgrade: Optional[InfixUpgrade]
    suffix_item_id: Optional[int]
    secondary_suffix_item_id: str
    stat_choices: List[int]     # TODO resolve itemstats


class Outfit(BaseModel):
    id: int = 0
    name: str = ""
    icon: str = ""
    unlock_items: List[int] = []    # TODO resolve against items


Item.update_forward_refs()
