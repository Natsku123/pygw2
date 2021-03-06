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
    race: Races
    gender: Gender
    profession: Professions
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
    restrictions: List[Races]
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


class MountSkin(BaseModel):
    id: int = 0
    name: str = ""
    icon: str = ""
    mount: str = ""     # TODO resolve against mount types
    dye_slots: List[DyeSlot]


class MountSkill(BaseModel):
    id: int
    slot: str


class MountType(BaseModel):
    id: str = ""
    name: str = ""
    default_skin: int   # TODO resolve against mount skins
    skins: List[int]    # TODO resolve against mount skins
    skills: List[MountSkill]


class Outfit(BaseModel):
    id: int = 0
    name: str = ""
    icon: str = ""
    unlock_items: List[int] = []    # TODO resolve against items


class PetSkill(BaseModel):
    id: int     # TODO resolve against skills


class Pet(BaseModel):
    id: int = 0
    name: str = ""
    description: str = ""
    icon: str = ""
    skills: List[PetSkill]


class ProfessionTrainingTrack(BaseModel):
    cost: int = 0
    type: ProfessionTrainingTrackType
    skill_id: Optional[int]     # TODO resolve against skills
    trait_id: Optional[int]     # TODO resolve against traits


class ProfessionTraining(BaseModel):
    id: int     # TODO resolve against skills or specializations
    category: ProfessionTrainingCategory
    name: str
    track: List[ProfessionTrainingTrack]


class WeaponSkill(BaseModel):
    id: int     # TODO resolve against skills
    slot: ProfessionWeaponSkillSlot
    offhand: str = ""
    attunement: str = ""
    source: str = ""


class ProfessionWeapon(BaseModel):
    flag: List[ProfessionWeaponFlag]
    specialization: Optional[int]   # TODO resolve against specializations
    skills: List[WeaponSkill]


class ProfessionWeapons(BaseModel):
    Axe: Optional['ProfessionWeapon']
    Dagger: Optional['ProfessionWeapon']
    Mace: Optional['ProfessionWeapon']
    Pistol: Optional['ProfessionWeapon']
    Sword: Optional['ProfessionWeapon']
    Scepter: Optional['ProfessionWeapon']
    Focus: Optional['ProfessionWeapon']
    Shield: Optional['ProfessionWeapon']
    Torch: Optional['ProfessionWeapon']
    Warhorn: Optional['ProfessionWeapon']
    Greatsword: Optional['ProfessionWeapon']
    Hammer: Optional['ProfessionWeapon']
    Longbow: Optional['ProfessionWeapon']
    Rifle: Optional['ProfessionWeapon']
    Shortbow: Optional['ProfessionWeapon']
    Staff: Optional['ProfessionWeapon']
    Speargun: Optional['ProfessionWeapon']
    Spear: Optional['ProfessionWeapon']
    Trident: Optional['ProfessionWeapon']


class Profession(BaseModel):
    id: str = ""
    name: str = ""
    icon: str = ""
    icon_big: str = ""
    specializations: List[int] = 0  # TODO resolve against specializations
    training: List[ProfessionTraining]
    weapons: ProfessionWeapons


class Race(BaseModel):
    id: str
    skills: List[int] = []      # TODO resolve against skills


class Specialization(BaseModel):
    id: int
    name: str
    profession: str
    elite: bool = False
    icon: str
    background: str
    minor_traits: List[int]     # TODO resolve against traits
    major_traits: List[int]     # TODO resolve against traits


class SkillFactPrefix(BaseModel):
    text: str
    icon: str
    status: str
    description: str


class SkillFact(BaseModel):
    text: str
    icon: Optional[str]
    type: SkillFactType
    value: Optional[Union[int, bool]]
    target: Optional[str]
    status: Optional[str]
    description: Optional[str]
    apply_count: Optional[int]
    duration: Optional[int]
    field_type: Optional[ComboFieldType]
    finisher_type: Optional[ComboFinisherType]
    percent: Optional[int]
    hit_count: Optional[int]
    dmg_multiplier: Optional[int]
    distance: Optional[int]
    prefix: Optional[SkillFactPrefix]


class SkillTraitedFact(SkillFact):
    requires_trait: int     # TODO resolve against traits
    overrides: Optional[int]    # TODO resolve from facts


class Skill(BaseModel):
    id: int
    name: str
    description: Optional[str]
    icon: str
    chat_link: str
    type: SkillType
    weapon_type: Optional[str]
    professions: List[str]
    slot: SkillSlot
    facts: Optional[List[SkillFact]]
    traited_facts: Optional[List[SkillTraitedFact]]
    categories: Optional[List[SkillCategories]]
    attunement: Optional[Attunement]
    cost: Optional[int]
    dual_wield: Optional[str]
    flip_skill: Optional[int]
    initiative: Optional[int]
    next_chain: Optional[int]   # TODO resolve against skills
    prev_chain: Optional[int]   # TODO resolve against skills
    transform_skills: Optional[List[int]]   # TODO resolve against skills
    bundle_skills: Optional[List[int]]      # TODO resolve against skills
    toolbelt_skill: Optional[int]   # TODO resolve against skills


class TraitSkill(BaseModel):
    id: int
    name: str
    description: str
    icon: str
    facts: Optional[List[SkillFact]]
    traited_facts: Optional[List[SkillTraitedFact]]


class Trait(BaseModel):
    id: int
    name: str
    icon: str
    description: str
    specialization: int     # TODO resolve against specialization
    tier: TraitTier
    slot: TraitSlot
    facts: Optional[List[SkillFact]]
    traited_facts: Optional[List[SkillTraitedFact]]
    skills: Optional[List[TraitSkill]]


class Legend(BaseModel):
    id: str = ""
    swap: int = 0   # TODO resolve against skills
    heal: int = 0   # TODO resolve against skills
    elite: int = 0  # TODO resolve against skills
    utilities: List[int]    # TODO resolve against skills


class GuildEmblemBackground(BaseModel):
    id: int     # TODO resolve against backgrounds
    colors: List[int]   # TODO resolve against colors


class GuildEmblemForeground(BaseModel):
    id: int     # TODO resolve against foregrounds
    colors: List[int]   # TODO resolve against colors


class GuildEmblem(BaseModel):
    background: GuildEmblemBackground
    foreground: GuildEmblemForeground
    flags: List[GuildEmblemFlags]


class Guild(BaseModel):
    level: int
    motd: str
    influence: int
    aetherium: str
    favor: int
    member_count: int
    member_capacity: int
    id: int
    name: str
    tag: str
    emblem: GuildEmblem


class GuildEmblemImages(BaseModel):
    id: int
    layers: List[str]


class GuildPermission(BaseModel):
    id: str
    name: str
    description: str


class GuildUpgradeCost(BaseModel):
    type: GuildUpgradeCostType
    name: str
    count: int
    item_id: Optional[int]      # TODO resolve against items


class GuildUpgrade(BaseModel):
    id: int
    name: str
    description: str
    type: GuildUpgradeType
    icon: str
    build_time: int
    required_level: int
    experience: int
    prerequisites: List[int]    # TODO resolve against other upgrades
    bag_max_items: Optional[int]
    bag_max_coins: Optional[int]
    costs: List[GuildUpgradeCost]


class GuildLogEntry(BaseModel):
    id: int
    time: datetime.datetime
    user: Optional[str]
    type: GuildLogEntryType
    invited_by: Optional[str]
    changed_by: Optional[str]
    old_rank: Optional[str]
    new_rank: Optional[str]
    item_id: Optional[int]      # TODO resolve against items
    count: Optional[int]
    coins: Optional[int]
    motd: Optional[str]
    upgrade_id: Optional[int]   # TODO resolve against upgrades
    recipe_id: Optional[int]    # TODO resolve against recipes


class GuildMember(BaseModel):
    name: str
    rank: str   # TODO resolve against guild ranks
    joined: datetime.datetime


class GuildRank(BaseModel):
    id: str
    order: int
    permissions: List[str]      # TODO resolve against permissions
    icon: str


class GuildStashSlot(BaseModel):
    id: int     # TODO resolve against items
    count: int


class GuildStash(BaseModel):
    upgrade_id: int     # TODO resolve against guild upgrades
    size: int
    coins: int
    note: str
    inventory: List[Union[GuildStashSlot, None]]


class GuildTreasuryNeeded(BaseModel):
    upgrade_id: int     # TODO resolve against upgrades
    count: int


class GuildTreasury(BaseModel):
    item_id: int    # TODO resolve against items
    count: int
    needed_by: List[GuildTreasuryNeeded]


class GuildTeamMember(BaseModel):
    name: str   # TODO resolve against guild members
    role: GuildTeamMemberRole


class GuildTeamSeason(BaseModel):
    id: str
    wins: int
    losses: int
    rating: int


class GuildTeam(BaseModel):
    id: int
    members: List
    name: str
    aggregate: 'PvpWinLoss'
    ladders: 'PvpLadderStats'
    games: List['PvpGame']
    seasons: List[GuildTeamSeason]


class HomeCat(BaseModel):
    id: int
    hint: Optional[str]


class HomeNode(BaseModel):
    id: str


class Continent(BaseModel):
    id: int
    name: str
    continent_dims: List[int]
    min_zoom: int
    max_zoom: int
    floors: List[int]   # TODO parse subendpoints?


class MapSector(BaseModel):
    id: int
    name: str
    level: int
    coord: List[int]
    bounds: List[List[int]]
    chat_link: str


class Map(BaseModel):
    id: int
    name: str
    min_level: int
    max_level: int
    default_floor: int
    floors: List[int]   # TODO resolve?
    region_id: int      # TODO resolve region?
    region_name: Optional[str]
    continent_id: int   # TODO resolve continent?
    continent_name: str
    map_rect: List[List[int]]
    continent_rect: List[List[int]]


class PvpWinLoss(BaseModel):
    wins: int
    losses: int
    desertions: int
    byes: int
    forfeits: int


class PvpStatsProfessions(BaseModel):
    elementalist: Optional[PvpWinLoss]
    engineer: Optional[PvpWinLoss]
    guardian: Optional[PvpWinLoss]
    mesmer: Optional[PvpWinLoss]
    necromancer: Optional[PvpWinLoss]
    ranger: Optional[PvpWinLoss]
    revenant: Optional[PvpWinLoss]
    thief: Optional[PvpWinLoss]
    warrior: Optional[PvpWinLoss]


class PvpLadderStats(BaseModel):
    ranked: PvpWinLoss
    unranked: PvpWinLoss


class PvpStats(BaseModel):
    pvp_rank: int
    pvp_rank_points: int
    pvp_rank_rollovers: int
    aggregate: PvpWinLoss
    professions: PvpStatsProfessions
    ladders: PvpLadderStats


class PvpScores(BaseModel):
    red: int
    blue: int


class PvpGame(BaseModel):
    id: str
    map_id: int     # TODO resolve agaisnt pvp maps
    started: datetime.datetime
    ended: datetime.datetime
    result: str
    team: str
    profession: Optional[str]
    scores: PvpScores
    rating_type: Union[PvpRatingType, None]
    rating_change: int
    season: Optional[str]   # TODO resolve against pvp seasons
