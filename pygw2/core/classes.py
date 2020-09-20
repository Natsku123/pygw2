import datetime

from pygw2.core.enums import *

from typing import Optional, List, Union
from pydantic import BaseModel


class ApiError(Exception):
    """Raised if API returns something unexpected."""
    pass


class Coins(BaseModel):
    count: int
    type: Optional[str]


class Attributes(BaseModel):
    Power: Optional[int] = 0
    Precision: Optional[int] = 0
    Toughness: Optional[int] = 0
    Vitality: Optional[int] = 0
    ConditionDamage: Optional[int] = 0
    ConditionDuration: Optional[int] = 0
    Healing: Optional[int] = 0
    BoonDuration: Optional[int] = 0


class Stats(BaseModel):
    id: int     # TODO resolve against /v2/itemstats
    attributes: Attributes


class Equipment(BaseModel):
    id: int                              # TODO resolve against /v2/items
    slot: EquipmentSlot
    infusions: Optional[List[int]] = []  # TODO resolve against /v2/items
    upgrades: Optional[List[int]] = []   # TODO resolve against /v2/items
    skin: Optional[int] = None           # TODO resolve against /v2/skins
    stats: Optional[Stats] = None
    binding: Optional[Binding] = None
    charges: Optional[int] = None
    bound_to: Optional[str] = None
    dyes: Optional[List[int]] = None     # TODO resolve against /v2/colors


class Crafting(BaseModel):
    discipline: Discipline
    rating: int
    active: bool


class ItemInventory(BaseModel):
    id: int     # TODO resolve against /v2/items
    count: int
    infusions: Optional[List[int]] = []  # TODO resolve against /v2/items
    upgrades: Optional[List[int]] = []  # TODO resolve against /v2/items
    skin: Optional[int] = None  # TODO resolve against /v2/skins
    stats: Optional[Stats] = None
    binding: Optional[Binding] = None
    bound_to: Optional[str] = None


class Bag(BaseModel):
    id: int     # TODO resolve against /v2/items
    size: int
    inventory: List[Union[ItemInventory, None]]


class SkillsBase(BaseModel):
    heal: int               # TODO resolve against /v2/skills
    utilities: List[int]    # TODO resolve against /v2/skills
    elite: int              # TODO resolve against /v2/skills
    legends: Optional[List[str]] = None     # TODO resolve against /v2/legends


class SkillTree(BaseModel):
    id: int                 # TODO compared against the training section for each /v2/professions
    spent: int
    done: bool


class Skills(BaseModel):
    pve: SkillsBase
    pvp: SkillsBase
    wvw: SkillsBase


class SpecializationBase(BaseModel):
    id: int                     # TODO resolve against /v2/specializations
    traits: List[int] = []      # TODO resolve agaisnt /v2/traits


class Specializations(BaseModel):
    pve: SpecializationBase
    pvp: SpecializationBase
    wvw: SpecializationBase


class SABZones(BaseModel):
    id: int
    mode: str
    world: int
    zone: int


class SABUnlocks(BaseModel):
    id: int
    name: str


class SABSong(BaseModel):
    id: int
    name: str


class SAB(BaseModel):
    zones: List[SABZones] = []
    unlocks: List[SABUnlocks] = []
    songs: List[SABSong] = []


class WvWAbility(BaseModel):
    id: int     # TODO resolve against /v2/wvw/abilities
    rank: int


class PvPEquipment(BaseModel):
    amulet: int         # TODO resolve agaisnt /v2/pvp/amulets
    rune: int           # TODO resolve against /v2/items
    sigils: List[int]   # TODO resolve agaisnt /v2/items


class Character(BaseModel):
    name: str
    race: Race
    gender: Gender
    profession: Profession
    lvl: int
    guild: Optional[str] = None
    age: int
    created: datetime.datetime
    deaths: int
    title: Optional[int] = None      # TODO resolve against /v2/titles
    backstory: List[int] = []        # TODO resolve against /v2/backstory/answers
    crafting: List[Crafting] = []    # TODO get /v2/characters/:id/crafting
    equipment: List[Equipment] = []  # TODO get /v2/characters/:id/equipment
    heropoints: List[str] = []       # TODO checked against entries skill_challenges in /v2/continents maps
    inventory: List[Bag] = []        # TODO get /v2/characters/:id/inventory
    skils: List[Skills] = []         # TODO get /v2/characters/:id/skills
    specialization: Optional[Specializations]  # TODO get /v2/characters/:id/specializations
    training: List[SkillTree]        # TODO get /v2/characters/:id/training
    sab: Optional[SAB]               # TODO get /v2/characters/:id/sab
    wvw_abilities: List[WvWAbility]
    equipment_pvp: PvPEquipment
    flags: List[CharacterFlag] = []


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
    restrictions: List[Union[Race, Profession]] = []
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


class AchievementCategory(BaseModel):
    id: int
    name: str
    description: str
    order: int
    icon: str
    achievements: List[int]     # TODO resolve against achievements


class AchievementGroup(BaseModel):
    id: str
    name: str
    description: str
    order: int
    categories: List[int]   # TODO resolve against achievement categories


class AchievementTier(BaseModel):
    count: int
    points: int


class AchievementRewardType(BaseModel):
    id: Optional[int]
    count: Optional[int]
    region: Optional[Region]


class AchievementReward(BaseModel):
    type: AchievementRewardType


class AchievementBits(BaseModel):
    type: AchievementBitsType
    id: Optional[int]
    text: Optional[str]


class Achievement(BaseModel):
    id: int
    icon: Optional[str]
    name: str
    description: str
    requirement: str
    locked_text: str
    type: AchievementType
    flags: List[AchievementFlag]
    tiers: List[AchievementTier]
    prerequisites: Optional[List[int]] = []     # TODO resolve achievements
    rewards: Optional[List[AchievementReward]]
    bits: Optional[List[AchievementBits]]
    point_cap: Optional[int]


class AchievementProgress(BaseModel):
    id: int     # TODO resolve against achievement
    bits: Optional[List[int]]
    current: Optional[int]
    max: Optional[int]
    done: bool
    repeated: Optional[int]
    unlocked: Optional[bool] = True


class DailyAchievementLevel(BaseModel):
    min: int
    max: int


class ProductAccess(BaseModel):
    product: AccountAccess
    condition: str


class DailyAchievement(BaseModel):
    id: int     # TODO resolve achievement
    level: DailyAchievementLevel
    required_access: Optional[ProductAccess]


class DailyAchievements(BaseModel):
    pve: List[DailyAchievement]
    pvp: List[DailyAchievement]
    wvw: List[DailyAchievement]
    fractals: List[DailyAchievement]
    special: List[DailyAchievement]


class VaultSlot(BaseModel):
    id: int     # TODO resolve against items
    count: int
    charges: Optional[int]
    skin: Optional[int]     # TODO resolve against skins
    upgrades: Optional[List[int]]     # TODO resolve against items (?)
    infusions: Optional[List[int]]    # TODO resolve against items (?)
    binding: Optional[Binding]
    bound_to: Optional[str]


class Finisher(BaseModel):
    id: int = 0
    unlock_details: str = ""
    unlock_items: Optional[List[int]]   # TODO resolve against items
    order: int = 0
    icon: str = ""
    name: str = ""


class StatAttributes(BaseModel):
    attribute: Attribute
    multiplier: float
    value: int


class Itemstat(BaseModel):
    id: int = 0
    name: str = ""
    attributes: List[StatAttributes]


class Material(BaseModel):
    id: int
    name: str
    items: List[int]    # TODO resolve against items
    order: int


class PvpAttributes(BaseModel):
    AgonyResistance: Optional[float]
    BoonDuration: Optional[float]
    ConditionDamage: Optional[float]
    ConditionDuration: Optional[float]
    CritDamage: Optional[float]
    Healing: Optional[float]
    Power: Optional[float]
    Precision: Optional[float]
    Toughness: Optional[float]
    Vitality: Optional[float]


class PvpAmulet(BaseModel):
    id: int = 0
    name: str = ""
    icon: str = ""
    attributes: PvpAttributes


class RecipeIngredient(BaseModel):
    item_id: int    # TODO resolve against items
    count: int


class RecipeGuildIngredient(BaseModel):
    upgrade_id: int     # TODO resolve against guild upgrades
    count: int


class Recipe(BaseModel):
    id: int
    type: RecipeType
    output_item_id: int     # TODO resolve against items
    output_item_count: int
    time_to_craft_ms: int
    disciplines: List[Discipline]
    min_rating: int
    flags: List[RecipeFlag]
    ingredients: List[RecipeIngredient]
    guild_ingredients: Optional[List[RecipeGuildIngredient]]
    output_upgrade_id: Optional[int]    # TODO resolve against guild upgrades
    chat_link: str


class Skin(BaseModel):
    id: int
    name: str
    type: SkinType
    flags: List[SkinFlag]
    restrictions: List[Race]
    icon: str
    rarity: str     # TODO same as ItemRarity?
    description: str
    details: Optional[Union[
        'ArmorSkinDetails',
        'WeaponSkinDetails',
        'GatheringSkinDetails'
    ]]


class DyeSlot(BaseModel):
    color_id: int   # TODO resolve against colors
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


class DailyCrafting(BaseModel):
    id: str


class DailyMapChest(BaseModel):
    id: str


class DailyWorldBoss(BaseModel):
    id: str

