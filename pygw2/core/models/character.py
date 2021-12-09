import datetime
from typing import Optional, List, Union, TYPE_CHECKING

from pygw2.core.enums import *
from pygw2.utils import LazyLoader, BaseModel

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
    values_: LazyLoader

    @property
    def values(self) -> "ItemStat":
        return self.values_()

    attributes: Attributes


class Equipment(BaseModel):
    id: int
    item_: LazyLoader
    tabs: Optional[List[int]]

    @property
    def item(self) -> "Item":
        return self.item_()

    slot: Optional[EquipmentSlot]
    location: EquipmentLocation
    infusions_: Optional[LazyLoader]

    @property
    def infusions(self) -> List["Item"]:
        return self.infusions_() if self.infusions_ is not None else None

    upgrades_: Optional[LazyLoader]

    @property
    def upgrades(self) -> List["Item"]:
        return self.upgrades_() if self.upgrades_ is not None else None

    skin_: Optional[LazyLoader]

    @property
    def skin(self) -> List["Skin"]:
        return self.skin_() if self.skin_ is not None else None

    stats: Optional[Stats] = None
    binding: Optional[Binding] = None
    charges: Optional[int] = None
    bound_to: Optional[str] = None
    dyes_: Optional[LazyLoader]

    @property
    def dyes(self) -> List["Color"]:
        return self.dyes_() if self.dyes_ is not None else None


class ItemInventory(BaseModel):
    id: int
    item_: LazyLoader

    @property
    def item(self) -> "Item":
        return self.item_()

    count: int
    infusions_: Optional[LazyLoader]

    @property
    def infusions(self) -> List["Item"]:
        return self.infusions_() if self.infusions_ is not None else None

    upgrades_: Optional[LazyLoader]

    @property
    def upgrades(self) -> List["Item"]:
        return self.upgrades_() if self.upgrades_ is not None else None

    skin_: Optional[LazyLoader]

    @property
    def skin(self) -> List["Skin"]:
        return self.skin_() if self.skin_ is not None else None

    stats: Optional[Stats] = None
    binding: Optional[Binding] = None
    bound_to: Optional[str] = None


class Bag(BaseModel):
    id: int
    item_: LazyLoader

    @property
    def item(self) -> "Item":
        return self.item_()

    size: int
    inventory: List[Union[ItemInventory, None]]


class SkillsBase(BaseModel):
    heal_: Optional[LazyLoader]

    @property
    def heal(self) -> "Skill":
        return self.heal_() if self.heal_ else None

    utilities_: Optional[LazyLoader]

    @property
    def utilities(self) -> List["Skill"]:
        return self.utilities_() if self.utilities_ else None

    elite_: Optional[LazyLoader]

    @property
    def elite(self):
        return self.elite_() if self.elite_ else None

    legends_: Optional[LazyLoader]

    @property
    def legends(self):
        return self.legends_() if self.legends_ is not None else None


class SkillTree(BaseModel):
    id: int  # TODO compared against the training section for each /v2/professions
    spent: int
    done: bool


class Skills(BaseModel):
    pve: SkillsBase
    pvp: SkillsBase
    wvw: SkillsBase


class SpecializationBase(BaseModel):
    id: Optional[int]
    specialization_: Optional[LazyLoader]

    @property
    def specialization(self) -> "Specialization":
        return self.specialization_() if self.specialization_ else None

    traits_: Optional[LazyLoader]

    @property
    def traits(self) -> List["Trait"]:
        return self.traits_() if self.traits_ else None


class Specializations(BaseModel):
    pve: SpecializationBase
    pvp: SpecializationBase
    wvw: SpecializationBase


class CharacterCore(BaseModel):
    name: str
    race: Races
    gender: Gender
    profession: Professions
    level: int
    guild_: Optional[LazyLoader] = None

    @property
    def guild(self) -> "Guild":
        return self.guild_() if self.guild_ is not None else None

    age: int
    created: datetime.datetime
    deaths: int
    title_: Optional[LazyLoader] = None

    @property
    def title(self) -> "Title":
        return self.title_() if self.title_ is not None else None


class Build(BaseModel):
    name: str
    profession: Professions
    specializations: List[SpecializationBase]
    skills: SkillsBase
    aquatic_skills: SkillsBase


class BuildTab(BaseModel):
    tab: int
    is_active: bool
    build: Build


class EquipmentTab(BaseModel):
    tab: int
    name: str
    is_active: bool
    equipment: List["Equipment"]
    equipment_pvp: "PvPEquipment"


class Character(BaseModel):
    name: str
    race: Races
    gender: Gender
    profession: Professions
    level: int
    build_tabs_unlocked: int
    active_build_tab: int
    equipment_tabs_unlocked: int
    active_equipment_tab: int
    guild_: Optional[LazyLoader] = None

    @property
    def guild(self) -> "Guild":
        return self.guild_() if self.guild_ is not None else None

    age: int
    created: datetime.datetime
    deaths: int
    title_: Optional[LazyLoader] = None

    @property
    def title(self) -> "Title":
        return self.title_() if self.title_ is not None else None

    backstory_: LazyLoader

    @property
    def backstory(self) -> List["BiographyAnswer"]:
        return self.backstory_()

    crafting: List["Crafting"]
    equipment: List["Equipment"]
    build_tabs: List["BuildTab"]
    equipment_tabs: List["EquipmentTab"]
    heropoints_: LazyLoader

    @property
    def heropoints(self) -> List["str"]:  # TODO replace with proper lookup
        return self.heropoints_()

    bags: List[Optional[Bag]] = []

    @property
    def inventory(self) -> List[Optional[Bag]]:
        return self.bags

    training: List[SkillTree]
    sab_: LazyLoader

    @property
    def sab(self) -> "SAB":
        return self.sab_()

    wvw_abilities: List["CharacterWvWAbility"]
    flags: List[CharacterFlag] = []


class CharacterWvWAbility(BaseModel):
    id: int
    ability_: LazyLoader

    @property
    def ability(self) -> "WvWAbility":
        return self.ability_()

    rank: int


class ProfessionTrainingTrack(BaseModel):
    cost: int = 0
    type: ProfessionTrainingTrackType
    skill_id: Optional[int]
    skill_: Optional[LazyLoader]

    @property
    def skill(self) -> Optional["Skill"]:
        return self.skill_() if self.skill_ is not None else None

    trait_id: Optional[int]
    trait_: Optional[LazyLoader]

    @property
    def trait(self) -> Optional["Trait"]:
        return self.trait_() if self.trait_ is not None else None


class ProfessionTraining(BaseModel):
    id: int
    skill_: LazyLoader

    @property
    def skill(self) -> "Skill":
        return self.skill_()

    specialization_: LazyLoader

    @property
    def specialization(self) -> "Specialization":
        return self.specialization_()

    category: ProfessionTrainingCategory
    name: str
    track: List[ProfessionTrainingTrack]


class WeaponSkill(BaseModel):
    id: int
    skill_: LazyLoader

    @property
    def skill(self) -> "Skill":
        return self.skill_()

    slot: SkillSlot
    offhand: Optional[str]
    attunement: Optional[str]
    source: Optional[str]


class ProfessionWeapon(BaseModel):
    flag: Optional[List[ProfessionWeaponFlag]]
    specialization_: Optional[LazyLoader]

    @property
    def specialization(self) -> Optional["Specialization"]:
        return self.specialization_() if self.specialization_ is not None else None

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
    specializations_: LazyLoader

    @property
    def specializations(self) -> List["Specialization"]:
        return self.specializations_()

    training: List[ProfessionTraining]
    weapons: ProfessionWeapons


class Race(BaseModel):
    id: str
    skills_: LazyLoader

    @property
    def skills(self) -> List["Skill"]:
        return self.skills_()


class Specialization(BaseModel):
    id: int
    name: str
    profession: str
    elite: bool = False
    icon: str
    background: str
    minor_traits_: LazyLoader

    @property
    def minor_traits(self) -> List["Trait"]:
        return self.minor_traits_()

    major_traits_: LazyLoader

    @property
    def major_traits(self) -> List["Trait"]:
        return self.major_traits_()


class SkillFactPrefix(BaseModel):
    text: str
    icon: str
    status: str
    description: str


class SkillFact(BaseModel):
    text: Optional[str]
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
    requires_trait_: LazyLoader

    @property
    def requires_trait(self) -> "Trait":
        return self.requires_trait_()

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
    flip_skill_: Optional[LazyLoader]

    @property
    def flip_skill(self) -> Optional["Skill"]:
        return self.flip_skill_() if self.flip_skill_ is not None else None

    initiative: Optional[int]
    next_chain_: Optional[LazyLoader]

    @property
    def next_chain(self) -> Optional["Skill"]:
        return self.next_chain_() if self.next_chain_ is not None else None

    prev_chain_: Optional[LazyLoader]

    @property
    def prev_chain(self) -> Optional["Skill"]:
        return self.prev_chain_ if self.prev_chain_ is not None else None

    transform_skills_: Optional[LazyLoader]

    @property
    def transform_skills(self) -> Optional[List["Skill"]]:
        return self.transform_skills_ if self.transform_skills_ is not None else None

    bundle_skills_: Optional[LazyLoader]

    @property
    def bundle_skills(self) -> Optional[List["Skill"]]:
        return self.bundle_skills_ if self.bundle_skills_ is not None else None

    toolbelt_skill_: Optional[LazyLoader]

    @property
    def toolbelt_skill(self) -> Optional["Skill"]:
        return self.toolbelt_skill_ if self.toolbelt_skill_ is not None else None


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
    specialization_: LazyLoader

    @property
    def specialization(self) -> "Specialization":
        return self.specialization_()

    tier: TraitTier
    slot: TraitSlot
    facts: Optional[List[SkillFact]]
    traited_facts: Optional[List[SkillTraitedFact]]
    skills: Optional[List[TraitSkill]]


class Legend(BaseModel):
    id: str = ""
    swap_: LazyLoader

    @property
    def swap(self) -> "Skill":
        return self.swap_()

    heal_: LazyLoader

    @property
    def heal(self) -> "Skill":
        return self.heal_()

    elite_: LazyLoader

    @property
    def elite(self) -> "Skill":
        return self.elite_()

    utilities_: LazyLoader

    @property
    def utilities(self) -> List["Skill"]:
        return self.utilities_()
