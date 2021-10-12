import datetime
from typing import Optional, List, Union, TYPE_CHECKING
from pydantic import BaseModel

from pygw2.core.enums import *
from pygw2.utils import LazyLoader

if TYPE_CHECKING:
    from pygw2.core.models.pvp import PvPEquipment
    from pygw2.core.models.sab import SAB
    from pygw2.core.models.guild import Guild
    from pygw2.core.models.misc import Title, Color
    from pygw2.core.models.backstory import BiographyAnswer
    from pygw2.core.models.items import Item
    from pygw2.core.models.general import Skin, ItemStat
    from pygw2.core.models.wvw import WvWAbility


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
    id: int
    _values: LazyLoader

    @property
    def values(self) -> "ItemStat":
        return self._values()

    attributes: Attributes


class Equipment(BaseModel):
    id: int
    _item: LazyLoader

    @property
    def item(self) -> "Item":
        return self._item()

    slot: EquipmentSlot
    _infusions: Optional[LazyLoader]

    @property
    def infusions(self) -> List["Item"]:
        return self._infusions() if self._infusions is not None else None

    _upgrades: Optional[LazyLoader]

    @property
    def upgrades(self) -> List["Item"]:
        return self._upgrades() if self._upgrades is not None else None

    _skin: Optional[LazyLoader]

    @property
    def skin(self) -> List["Skin"]:
        return self._skin() if self._skin is not None else None

    stats: Optional[Stats] = None
    binding: Optional[Binding] = None
    charges: Optional[int] = None
    bound_to: Optional[str] = None
    _dyes: Optional[LazyLoader]

    @property
    def dyes(self) -> List["Color"]:
        return self._dyes() if self._dyes is not None else None


class ItemInventory(BaseModel):
    id: int
    _item: LazyLoader

    @property
    def item(self) -> "Item":
        return self._item()

    count: int
    _infusions: Optional[LazyLoader]

    @property
    def infusions(self) -> List["Item"]:
        return self._infusions() if self._infusions is not None else None

    _upgrades: Optional[LazyLoader]

    @property
    def upgrades(self) -> List["Item"]:
        return self._upgrades() if self._upgrades is not None else None

    _skin: Optional[LazyLoader]

    @property
    def skin(self) -> List["Skin"]:
        return self._skin() if self._skin is not None else None

    stats: Optional[Stats] = None
    binding: Optional[Binding] = None
    bound_to: Optional[str] = None


class Bag(BaseModel):
    id: int
    _item: LazyLoader

    @property
    def item(self) -> "Item":
        return self._item()

    size: int
    inventory: List[Union[ItemInventory, None]]


class SkillsBase(BaseModel):
    _heal: LazyLoader

    @property
    def heal(self) -> "Skill":
        return self._heal()

    _utilities: LazyLoader

    @property
    def utilities(self) -> List["Skill"]:
        return self._utilities()

    _elite: LazyLoader

    @property
    def elite(self):
        return self._elite()

    _legends: Optional[LazyLoader]

    @property
    def legends(self):
        return self._legends() if self._legends is not None else None


class SkillTree(BaseModel):
    id: int  # TODO compared against the training section for each /v2/professions
    spent: int
    done: bool


class Skills(BaseModel):
    pve: SkillsBase
    pvp: SkillsBase
    wvw: SkillsBase


class SpecializationBase(BaseModel):
    id: int
    _specialization: LazyLoader

    @property
    def specialization(self) -> "Specialization":
        return self._specialization()

    _traits: LazyLoader

    @property
    def traits(self) -> List["Trait"]:
        return self._traits()


class Specializations(BaseModel):
    pve: SpecializationBase
    pvp: SpecializationBase
    wvw: SpecializationBase


class CharacterCore(BaseModel):
    name: str
    race: Races
    gender: Gender
    profession: Professions
    lvl: int
    _guild: Optional[LazyLoader] = None

    @property
    def guild(self) -> "Guild":
        return self._guild() if self._guild is not None else None

    age: int
    created: datetime.datetime
    deaths: int
    _title: Optional[LazyLoader] = None

    @property
    def title(self) -> "Title":
        return self._title() if self._title is not None else None


class Character(BaseModel):
    name: str
    race: Races
    gender: Gender
    profession: Professions
    lvl: int
    _guild: Optional[LazyLoader] = None

    @property
    def guild(self) -> "Guild":
        return self._guild() if self._guild is not None else None

    age: int
    created: datetime.datetime
    deaths: int
    _title: Optional[LazyLoader] = None

    @property
    def title(self) -> "Title":
        return self._title() if self._title is not None else None

    _backstory: LazyLoader

    @property
    def backstory(self) -> List["BiographyAnswer"]:
        return self._backstory()

    crafting: List["Crafting"]
    equipment: List["Equipment"]
    _heropoints: LazyLoader

    @property
    def heropoints(self) -> List["str"]:  # TODO replace with proper lookup
        return self._heropoints()

    bags: List[Bag] = []

    @property
    def inventory(self) -> List[Bag]:
        return self.bags

    skills: List[Skills] = []
    specializations: Optional[Specializations]
    training: List[SkillTree]
    _sab: LazyLoader

    @property
    def sab(self) -> "SAB":
        return self._sab()

    wvw_abilities: List["CharacterWvWAbility"]
    equipment_pvp: "PvPEquipment"
    flags: List[CharacterFlag] = []


class CharacterWvWAbility(BaseModel):
    id: int
    _ability: LazyLoader

    @property
    def ability(self) -> "WvWAbility":
        return self._ability()

    rank: int


class ProfessionTrainingTrack(BaseModel):
    cost: int = 0
    type: ProfessionTrainingTrackType
    skill_id: Optional[int]
    _skill: Optional[LazyLoader]

    @property
    def skill(self) -> Optional["Skill"]:
        return self._skill() if self._skill is not None else None

    trait_id: Optional[int]
    _trait: Optional[LazyLoader]

    @property
    def trait(self) -> Optional["Trait"]:
        return self._trait() if self._trait is not None else None


class ProfessionTraining(BaseModel):
    id: int
    _skill: LazyLoader

    @property
    def skill(self) -> "Skill":
        return self._skill()

    _specialization: LazyLoader

    @property
    def specialization(self) -> "Specialization":
        return self._specialization()

    category: ProfessionTrainingCategory
    name: str
    track: List[ProfessionTrainingTrack]


class WeaponSkill(BaseModel):
    id: int
    _skill: LazyLoader

    @property
    def skill(self) -> "Skill":
        return self._skill()

    slot: ProfessionWeaponSkillSlot
    offhand: Optional[str]
    attunement: Optional[str]
    source: Optional[str]


class ProfessionWeapon(BaseModel):
    flag: List[ProfessionWeaponFlag]
    _specialization: Optional[LazyLoader]

    @property
    def specialization(self) -> Optional["Specialization"]:
        return self._specialization() if self._specialization is not None else None

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
    _specializations: LazyLoader

    @property
    def specializations(self) -> List["Specialization"]:
        return self._specializations()

    training: List[ProfessionTraining]
    weapons: ProfessionWeapons


class Race(BaseModel):
    id: str
    _skills: LazyLoader

    @property
    def skills(self) -> List["Skill"]:
        return self._skills()


class Specialization(BaseModel):
    id: int
    name: str
    profession: str
    elite: bool = False
    icon: str
    background: str
    _minor_traits: LazyLoader

    @property
    def minor_traits(self) -> List["Trait"]:
        return self._minor_traits()

    _major_traits: LazyLoader

    @property
    def major_traits(self) -> List["Trait"]:
        return self._major_traits()


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
    _requires_trait: LazyLoader

    @property
    def requires_trait(self) -> "Trait":
        return self._requires_trait()

    overrides: Optional[int]  # TODO resolve from facts


class Skill(BaseModel):
    id: int
    name: str
    description: Optional[str]
    icon: str
    chat_link: str
    type: Optional[SkillType]
    weapon_type: Optional[WeaponType]
    professions: List[Professions]
    slot: SkillSlot
    facts: Optional[List[SkillFact]]
    traited_facts: Optional[List[SkillTraitedFact]]
    categories: Optional[List[SkillCategories]]
    attunement: Optional[Attunement]
    cost: Optional[int]
    dual_wield: Optional[str]
    _flip_skill: Optional[LazyLoader]

    @property
    def flip_skill(self) -> Optional["Skill"]:
        return self._flip_skill() if self._flip_skill is not None else None

    initiative: Optional[int]
    _next_chain: Optional[LazyLoader]

    @property
    def next_chain(self) -> Optional["Skill"]:
        return self._next_chain() if self._next_chain is not None else None

    _prev_chain: Optional[LazyLoader]

    @property
    def prev_chain(self) -> Optional["Skill"]:
        return self._prev_chain if self._prev_chain is not None else None

    _transform_skills: Optional[LazyLoader]

    @property
    def transform_skills(self) -> Optional[List["Skill"]]:
        return self._transform_skills if self._transform_skills is not None else None

    _bundle_skills: Optional[LazyLoader]

    @property
    def bundle_skills(self) -> Optional[List["Skill"]]:
        return self._bundle_skills if self._bundle_skills is not None else None

    _toolbelt_skill: Optional[LazyLoader]

    @property
    def toolbelt_skill(self) -> Optional["Skill"]:
        return self._toolbelt_skill if self._toolbelt_skill is not None else None


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
    _specialization: LazyLoader

    @property
    def specialization(self) -> "Specialization":
        return self._specialization()

    tier: TraitTier
    slot: TraitSlot
    facts: Optional[List[SkillFact]]
    traited_facts: Optional[List[SkillTraitedFact]]
    skills: Optional[List[TraitSkill]]


class Legend(BaseModel):
    id: str = ""
    _swap: LazyLoader

    @property
    def swap(self) -> "Skill":
        return self._swap()

    _heal: LazyLoader

    @property
    def heal(self) -> "Skill":
        return self._heal()

    _elite: LazyLoader

    @property
    def elite(self) -> "Skill":
        return self._elite()

    _utilities: LazyLoader

    @property
    def utilities(self) -> List["Skill"]:
        return self._utilities()
