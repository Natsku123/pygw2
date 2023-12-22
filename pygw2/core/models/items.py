from __future__ import annotations

from pygw2.core.enums import *

from typing import TYPE_CHECKING, ForwardRef

from pygw2.utils import LazyLoader, BaseModel

if TYPE_CHECKING:
    from pygw2.core.models.misc import Color, Mini
    from pygw2.core.models.general import Skin, ItemStat
    from pygw2.core.models.crafting import Recipe
    from pygw2.core.models.guild import GuildUpgrade
else:
    Color = ForwardRef("Color")
    Mini = ForwardRef("Mini")
    Skin = ForwardRef("Skin")
    ItemStat = ForwardRef("ItemStat")
    Recipe = ForwardRef("Recipe")
    GuildUpgrade = ForwardRef("GuildUpgrade")
    ArmorDetails = ForwardRef("ArmorDetails")
    BackDetails = ForwardRef("BackDetails")
    BagDetails = ForwardRef("BagDetails")
    ConsumableDetails = ForwardRef("ConsumableDetails")
    ContainerDetails = ForwardRef("ContainerDetails")
    GatheringToolDetails = ForwardRef("GatheringToolDetails")
    GizmoDetails = ForwardRef("GizmoDetails")
    MiniatureDetails = ForwardRef("MiniatureDetails")
    SalvageKitDetails = ForwardRef("SalvageKitDetails")
    TrinketDetails = ForwardRef("TrinketDetails")
    UpgradeComponentDetails = ForwardRef("UpgradeComponentDetails")
    WeaponDetails = ForwardRef("WeaponDetails")


class Upgrade(BaseModel):
    upgrade: UpgradeType
    item_id: int


class Item(BaseModel):
    id: int
    chat_link: str
    name: str
    icon: str | None = None
    description: str | None = None
    type: ItemType
    rarity: ItemRarity
    level: int
    vendor_value: int
    default_skin_: LazyLoader | None = None

    @property
    def default_skin(self) -> Skin | None:
        return self.default_skin_() if self.default_skin_ is not None else None

    flags: list[ItemFlags] = []
    game_types: list[GameTypes] = []
    restrictions: list[Races | Professions] = []
    upgrades_into: list[Upgrade] | None = []
    upgrades_from: list[Upgrade] | None = []
    details: ArmorDetails | BackDetails | BagDetails | ConsumableDetails | ContainerDetails | GatheringToolDetails | GizmoDetails | MiniatureDetails | SalvageKitDetails | TrinketDetails | UpgradeComponentDetails | WeaponDetails | None = (
        None
    )


class InfixAttribute(BaseModel):
    attribute: Attribute
    modifier: int


class InfixBuff(BaseModel):
    skill_id: int
    description: str | None = None


class InfixUpgrade(BaseModel):
    id: int
    attributes: list[InfixAttribute]
    buff: InfixBuff | None = None


class InfusionSlot(BaseModel):
    flags: list[InfusionSlotType]
    item_id: int | None = None


class ArmorDetails(BaseModel):
    type: ArmorSlot
    weight_class: WeightClass
    defense: int
    infusion_slots: list[InfusionSlot] = []
    attribute_adjustment: float
    infix_upgrade: InfixUpgrade | None = None
    suffix_item_id: int | None = None
    secondary_suffix_item_id: str = ""
    stat_choices_: LazyLoader | None = None

    @property
    def stat_choices(self) -> list[ItemStat] | None:
        return self.stat_choices_() if self.stat_choices_ is not None else None


class BackDetails(BaseModel):
    infusion_slots: list[InfusionSlot] = []
    attribute_adjustment: float
    infix_upgrade: InfixUpgrade | None = None
    suffix_item_id: int | None = None
    secondary_suffix_item_id: str = ""
    stat_choices_: LazyLoader | None = None

    @property
    def stat_choices(self) -> list[ItemStat] | None:
        return self.stat_choices_() if self.stat_choices_ is not None else None


class BagDetails(BaseModel):
    size: int
    no_sell_or_sort: bool


class ConsumableDetails(BaseModel):
    type: ConsumableType
    description: str | None = None
    duration_ms: int | None = None
    unlock_type: UnlockType | None = None
    color_id: int | None = None
    color_: LazyLoader | None = None

    @property
    def color(self) -> Color | None:
        return self.color_() if self.color_ is not None else None

    recipe_id: int | None = None
    recipe_: LazyLoader | None = None

    @property
    def recipe(self) -> Recipe | None:
        return self.recipe_() if self.recipe_ is not None else None

    extra_recipe_ids: list[int] | None = []
    extra_recipes_: LazyLoader | None = None

    @property
    def extra_recipes(self) -> list[Recipe] | None:
        return self.extra_recipes_() if self.extra_recipes_ is not None else None

    guild_upgrade_id: int | None = None
    guild_upgrade_: LazyLoader | None = None

    @property
    def guild_upgrade(self) -> GuildUpgrade | None:
        return self.guild_upgrade_() if self.guild_upgrade_ is not None else None

    apply_count: int | None = None
    name: str | None = None
    icon: str | None = None
    skins_: LazyLoader | None = None

    @property
    def skins(self) -> list[Skin] | None:
        return self.skins_() if self.skins_ is not None else None


class ContainerDetails(BaseModel):
    type: ContainerType


class GatheringToolDetails(BaseModel):
    type: GatheringToolType


class GizmoDetails(BaseModel):
    type: GizmoType
    guild_upgrade_id: int | None = None
    guild_upgrade_: LazyLoader | None = None

    @property
    def guild_upgrade(self) -> GuildUpgrade | None:
        return self.guild_upgrade_() if self.guild_upgrade_ is not None else None

    vendor_ids: list[int] = []  # TODO resolve?


class MiniatureDetails(BaseModel):
    minipet_id: int
    minipet_: LazyLoader

    @property
    def minipet(self) -> Mini:
        return self.minipet_()


class SalvageKitDetails(BaseModel):
    type: SalvageKitType
    charges: int


class TrinketDetails(BaseModel):
    infusion_slots: list[InfusionSlot] = []
    attribute_adjustment: float
    infix_upgrade: InfixUpgrade | None = None
    suffix_item_id: int | None = None
    secondary_suffix_item_id: str = ""
    stat_choices_: LazyLoader | None = None

    @property
    def stat_choices(self) -> list[ItemStat] | None:
        return self.stat_choices_() if self.stat_choices_ is not None else None


class UpgradeComponentDetails(BaseModel):
    type: UpgradeComponentType
    flags: list[WeaponType | UpgradeComponentFlag] = []
    infusion_upgrade_flags: list[InfusionUpgradeFlag] = []
    suffix: str
    infix_upgrade: InfixUpgrade
    bonuses: list[str]


class WeaponDetails(BaseModel):
    type: WeaponType | AdditionalWeaponType
    damage_type: DamageType
    min_power: int
    max_power: int
    defense: int
    infusion_slots: list[InfusionSlot] = []
    attribute_adjustment: float
    infix_upgrade: InfixUpgrade | None = None
    suffix_item_id: int | None = None
    secondary_suffix_item_id: str
    stat_choices_: LazyLoader | None = None

    @property
    def stat_choices(self) -> list[ItemStat] | None:
        return self.stat_choices_() if self.stat_choices_ is not None else None


class Outfit(BaseModel):
    id: int = 0
    name: str = ""
    icon: str = ""
    unlock_items_: LazyLoader

    @property
    def unlock_items(self) -> list[Item]:
        return self.unlock_items_()


class Glider(BaseModel):
    id: int
    unlock_items_: LazyLoader

    @property
    def unlock_items(self) -> list[Item] | Item:
        return self.unlock_items_()

    order: int
    icon: str
    name: str
    description: str
    default_dyes_: LazyLoader | None = None

    @property
    def default_dyes(self) -> list[Color]:
        return self.default_dyes_() if self.default_dyes_ is not None else None


class Mailcarrier(BaseModel):
    id: int
    unlock_items_: LazyLoader

    @property
    def unlock_items(self) -> list[Item] | Item:
        return self.unlock_items_()

    order: int
    icon: str
    name: str
    flags: list[MailcarrierFlags]


Item.model_rebuild()
