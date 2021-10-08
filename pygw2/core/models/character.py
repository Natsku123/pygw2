import datetime
from typing import Optional, List, Union, TYPE_CHECKING
from pydantic import BaseModel

from pygw2.core.enums import *

if TYPE_CHECKING:
    from pygw2.core.models.pvp import PvPEquipment
    from pygw2.core.models.sab import SAB


class Crafting(BaseModel):
    discipline: Discipline
    rating: int
    active: bool


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
    id: int  # TODO resolve against /v2/itemstats
    attributes: Attributes


class Equipment(BaseModel):
    id: int  # TODO resolve against /v2/items
    slot: EquipmentSlot
    infusions: Optional[List[int]] = []  # TODO resolve against /v2/items
    upgrades: Optional[List[int]] = []  # TODO resolve against /v2/items
    skin: Optional[int] = None  # TODO resolve against /v2/skins
    stats: Optional[Stats] = None
    binding: Optional[Binding] = None
    charges: Optional[int] = None
    bound_to: Optional[str] = None
    dyes: Optional[List[int]] = None  # TODO resolve against /v2/colors


class ItemInventory(BaseModel):
    id: int  # TODO resolve against /v2/items
    count: int
    infusions: Optional[List[int]] = []  # TODO resolve against /v2/items
    upgrades: Optional[List[int]] = []  # TODO resolve against /v2/items
    skin: Optional[int] = None  # TODO resolve against /v2/skins
    stats: Optional[Stats] = None
    binding: Optional[Binding] = None
    bound_to: Optional[str] = None


class Bag(BaseModel):
    id: int  # TODO resolve against /v2/items
    size: int
    inventory: List[Union[ItemInventory, None]]


class SkillsBase(BaseModel):
    heal: int  # TODO resolve against /v2/skills
    utilities: List[int]  # TODO resolve against /v2/skills
    elite: int  # TODO resolve against /v2/skills
    legends: Optional[List[str]] = None  # TODO resolve against /v2/legends


class SkillTree(BaseModel):
    id: int  # TODO compared against the training section for each /v2/professions
    spent: int
    done: bool


class Skills(BaseModel):
    pve: SkillsBase
    pvp: SkillsBase
    wvw: SkillsBase


class SpecializationBase(BaseModel):
    id: int  # TODO resolve against /v2/specializations
    traits: List[int] = []  # TODO resolve agaisnt /v2/traits


class Specializations(BaseModel):
    pve: SpecializationBase
    pvp: SpecializationBase
    wvw: SpecializationBase


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
    title: Optional[int] = None  # TODO resolve against /v2/titles
    backstory: List[int] = []  # TODO resolve against /v2/backstory/answers
    crafting: List[Crafting] = []  # TODO get /v2/characters/:id/crafting
    equipment: List[Equipment] = []  # TODO get /v2/characters/:id/equipment
    heropoints: List[
        str
    ] = []  # TODO checked against entries skill_challenges in /v2/continents maps
    inventory: List[Bag] = []  # TODO get /v2/characters/:id/inventory
    skils: List[Skills] = []  # TODO get /v2/characters/:id/skills
    specialization: Optional[
        Specializations
    ]  # TODO get /v2/characters/:id/specializations
    training: List[SkillTree]  # TODO get /v2/characters/:id/training
    sab: Optional["SAB"]  # TODO get /v2/characters/:id/sab
    wvw_abilities: List["CharacterWvWAbility"]
    equipment_pvp: "PvPEquipment"
    flags: List[CharacterFlag] = []


class CharacterWvWAbility(BaseModel):
    id: int  # TODO resolve against /v2/wvw/abilities
    rank: int


class ProfessionTrainingTrack(BaseModel):
    cost: int = 0
    type: ProfessionTrainingTrackType
    skill_id: Optional[int]  # TODO resolve against skills
    trait_id: Optional[int]  # TODO resolve against traits


class ProfessionTraining(BaseModel):
    id: int  # TODO resolve against skills or specializations
    category: ProfessionTrainingCategory
    name: str
    track: List[ProfessionTrainingTrack]


class WeaponSkill(BaseModel):
    id: int  # TODO resolve against skills
    slot: ProfessionWeaponSkillSlot
    offhand: str = ""
    attunement: str = ""
    source: str = ""


class ProfessionWeapon(BaseModel):
    flag: List[ProfessionWeaponFlag]
    specialization: Optional[int]  # TODO resolve against specializations
    skills: List[WeaponSkill]


class ProfessionWeapons(BaseModel):
    Axe: Optional["ProfessionWeapon"]
    Dagger: Optional["ProfessionWeapon"]
    Mace: Optional["ProfessionWeapon"]
    Pistol: Optional["ProfessionWeapon"]
    Sword: Optional["ProfessionWeapon"]
    Scepter: Optional["ProfessionWeapon"]
    Focus: Optional["ProfessionWeapon"]
    Shield: Optional["ProfessionWeapon"]
    Torch: Optional["ProfessionWeapon"]
    Warhorn: Optional["ProfessionWeapon"]
    Greatsword: Optional["ProfessionWeapon"]
    Hammer: Optional["ProfessionWeapon"]
    Longbow: Optional["ProfessionWeapon"]
    Rifle: Optional["ProfessionWeapon"]
    Shortbow: Optional["ProfessionWeapon"]
    Staff: Optional["ProfessionWeapon"]
    Speargun: Optional["ProfessionWeapon"]
    Spear: Optional["ProfessionWeapon"]
    Trident: Optional["ProfessionWeapon"]


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
    skills: List[int] = []  # TODO resolve against skills


class Specialization(BaseModel):
    id: int
    name: str
    profession: str
    elite: bool = False
    icon: str
    background: str
    minor_traits: List[int]  # TODO resolve against traits
    major_traits: List[int]  # TODO resolve against traits


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
    requires_trait: int  # TODO resolve against traits
    overrides: Optional[int]  # TODO resolve from facts


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
    next_chain: Optional[int]  # TODO resolve against skills
    prev_chain: Optional[int]  # TODO resolve against skills
    transform_skills: Optional[List[int]]  # TODO resolve against skills
    bundle_skills: Optional[List[int]]  # TODO resolve against skills
    toolbelt_skill: Optional[int]  # TODO resolve against skills


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
    specialization: int  # TODO resolve against specialization
    tier: TraitTier
    slot: TraitSlot
    facts: Optional[List[SkillFact]]
    traited_facts: Optional[List[SkillTraitedFact]]
    skills: Optional[List[TraitSkill]]


class Legend(BaseModel):
    id: str = ""
    swap: int = 0  # TODO resolve against skills
    heal: int = 0  # TODO resolve against skills
    elite: int = 0  # TODO resolve against skills
    utilities: List[int]  # TODO resolve against skills
