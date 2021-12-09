from pygw2.core.enums import *

from typing import Optional, List, Union, TYPE_CHECKING

from pygw2.utils import LazyLoader, BaseModel

if TYPE_CHECKING:
    from pygw2.core.models.misc import Color, Mini
    from pygw2.core.models.general import Skin, ItemStat
    from pygw2.core.models.crafting import Recipe
    from pygw2.core.models.guild import GuildUpgrade


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
    default_skin_: Optional[LazyLoader]

    @property
    def default_skin(self) -> Optional["Skin"]:
        return self.default_skin_() if self.default_skin_ is not None else None

    flags: List[ItemFlags] = []
    game_types: List[GameTypes] = []
    restrictions: List[Union[Races, Professions]] = []
    upgrades_into: Optional[List[Upgrade]] = []
    upgrades_from: Optional[List[Upgrade]] = []
    details: Optional[
        Union[
            "ArmorDetails",
            "BackDetails",
            "BagDetails",
            "ConsumableDetails",
            "ContainerDetails",
            "GatheringToolDetails",
            "GizmoDetails",
            "MiniatureDetails",
            "SalvageKitDetails",
            "TrinketDetails",
            "UpgradeComponentDetails",
            "WeaponDetails",
        ]
    ]


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
    stat_choices_: Optional[LazyLoader]

    @property
    def stat_choices(self) -> Optional[List["ItemStat"]]:
        return self.stat_choices_() if self.stat_choices_ is not None else None


class BackDetails(BaseModel):
    infusion_slots: List[InfusionSlot] = []
    attribute_adjustment: int
    infix_upgrade: Optional[InfixUpgrade]
    suffix_item_id: Optional[int]
    secondary_suffix_item_id: str = ""
    stat_choices_: Optional[LazyLoader]

    @property
    def stat_choices(self) -> Optional[List["ItemStat"]]:
        return self.stat_choices_() if self.stat_choices_ is not None else None


class BagDetails(BaseModel):
    size: int
    no_sell_or_sort: bool


class ConsumableDetails(BaseModel):
    type: ConsumableType
    description: Optional[str]
    duration_ms: Optional[int]
    unlock_type: Optional[UnlockType]
    color_id: Optional[int]
    color_: Optional[LazyLoader]

    @property
    def color(self) -> Optional["Color"]:
        return self.color_() if self.color_ is not None else None

    recipe_id: Optional[int]
    recipe_: Optional[LazyLoader]

    @property
    def recipe(self) -> Optional["Recipe"]:
        return self.recipe_() if self.recipe_ is not None else None

    extra_recipe_ids: Optional[List[int]] = []
    extra_recipes_: Optional[LazyLoader]

    @property
    def extra_recipes(self) -> Optional[List["Recipe"]]:
        return self.extra_recipes_() if self.extra_recipes_ is not None else None

    guild_upgrade_id: Optional[int]
    guild_upgrade_: Optional[LazyLoader]

    @property
    def guild_upgrade(self) -> Optional["GuildUpgrade"]:
        return self.guild_upgrade_() if self.guild_upgrade_ is not None else None

    apply_count: Optional[int]
    name: Optional[str]
    icon: Optional[str]
    skins_: Optional[LazyLoader]

    @property
    def skins(self) -> Optional[List["Skin"]]:
        return self.skins_() if self.skins_ is not None else None


class ContainerDetails(BaseModel):
    type: ContainerType


class GatheringToolDetails(BaseModel):
    type: GatheringToolType


class GizmoDetails(BaseModel):
    type: GizmoType
    guild_upgrade_id: Optional[int]
    guild_upgrade_: Optional[LazyLoader]

    @property
    def guild_upgrade(self) -> Optional["GuildUpgrade"]:
        return self.guild_upgrade_() if self.guild_upgrade_ is not None else None

    vendor_ids: List[int] = []  # TODO resolve?


class MiniatureDetails(BaseModel):
    minipet_id: int
    minipet_: LazyLoader

    @property
    def minipet(self) -> "Mini":
        return self.minipet_()


class SalvageKitDetails(BaseModel):
    type: SalvageKitType
    charges: int


class TrinketDetails(BaseModel):
    infusion_slots: List[InfusionSlot] = []
    attribute_adjustment: int
    infix_upgrade: Optional[InfixUpgrade]
    suffix_item_id: Optional[int]
    secondary_suffix_item_id: str = ""
    stat_choices_: Optional[LazyLoader]

    @property
    def stat_choices(self) -> Optional[List["ItemStat"]]:
        return self.stat_choices_() if self.stat_choices_ is not None else None


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
    stat_choices_: Optional[LazyLoader]

    @property
    def stat_choices(self) -> Optional[List["ItemStat"]]:
        return self.stat_choices_() if self.stat_choices_ is not None else None


class Outfit(BaseModel):
    id: int = 0
    name: str = ""
    icon: str = ""
    unlock_items_: LazyLoader

    @property
    def unlock_items(self) -> List["Item"]:
        return self.unlock_items_()


class Glider(BaseModel):
    id: int
    unlock_items_: LazyLoader

    @property
    def unlock_items(self) -> Union[List["Item"], "Item"]:
        return self.unlock_items_()

    order: int
    icon: str
    name: str
    description: str
    default_dyes_: Optional[LazyLoader]

    @property
    def default_dyes(self) -> List["Color"]:
        return self.default_dyes_() if self.default_dyes_ is not None else None


class Mailcarrier(BaseModel):
    id: int
    unlock_items_: LazyLoader

    @property
    def unlock_items(self) -> Union[List["Item"], "Item"]:
        return self.unlock_items_()

    order: int
    icon: str
    name: str
    flags: List["MailcarrierFlags"]


Item.update_forward_refs()
