from __future__ import annotations

import datetime
from typing import TYPE_CHECKING, ForwardRef

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
else:
    PvPEquipment = ForwardRef("PvPEquipment")
    SAB = ForwardRef("SAB")
    Guild = ForwardRef("Guild")
    Title = ForwardRef("Title")
    Color = ForwardRef("Color")
    BiographyAnswer = ForwardRef("BiographyAnswer")
    Item = ForwardRef("Item")
    Skin = ForwardRef("Skin")
    ItemStat = ForwardRef("ItemStat")
    WvWAbility = ForwardRef("WvWAbility")


class Crafting(BaseModel):
    discipline: Discipline
    rating: int
    active: bool


class Attributes(BaseModel):
    Power: int | None = 0
    Precision: int | None = 0
    Toughness: int | None = 0
    Vitality: int | None = 0
    ConditionDamage: int | None = 0
    ConditionDuration: int | None = 0
    Healing: int | None = 0
    BoonDuration: int | None = 0


class Stats(BaseModel):
    id: int
    values_: LazyLoader

    @property
    def values(self) -> ItemStat:
        return self.values_()

    attributes: Attributes


class Equipment(BaseModel):
    id: int
    item_: LazyLoader
    tabs: list[int] | None

    @property
    def item(self) -> Item:
        return self.item_()

    slot: EquipmentSlot | None
    location: EquipmentLocation
    infusions_: LazyLoader | None

    @property
    def infusions(self) -> list[Item]:
        return self.infusions_() if self.infusions_ is not None else None

    upgrades_: LazyLoader | None

    @property
    def upgrades(self) -> list[Item]:
        return self.upgrades_() if self.upgrades_ is not None else None

    skin_: LazyLoader | None

    @property
    def skin(self) -> list[Skin]:
        return self.skin_() if self.skin_ is not None else None

    stats: Stats | None = None
    binding: Binding | None = None
    charges: int | None = None
    bound_to: str | None = None
    dyes_: LazyLoader | None

    @property
    def dyes(self) -> list[Color]:
        return self.dyes_() if self.dyes_ is not None else None


class ItemInventory(BaseModel):
    id: int
    item_: LazyLoader

    @property
    def item(self) -> Item:
        return self.item_()

    count: int
    infusions_: LazyLoader | None

    @property
    def infusions(self) -> list[Item]:
        return self.infusions_() if self.infusions_ is not None else None

    upgrades_: LazyLoader | None

    @property
    def upgrades(self) -> list[Item]:
        return self.upgrades_() if self.upgrades_ is not None else None

    skin_: LazyLoader | None

    @property
    def skin(self) -> list[Skin]:
        return self.skin_() if self.skin_ is not None else None

    stats: Stats | None = None
    binding: Binding | None = None
    bound_to: str | None = None


class Bag(BaseModel):
    id: int
    item_: LazyLoader

    @property
    def item(self) -> Item:
        return self.item_()

    size: int
    inventory: list[ItemInventory | None]


class SkillsBase(BaseModel):
    heal_: LazyLoader | None

    @property
    def heal(self) -> Skill:
        return self.heal_() if self.heal_ else None

    utilities_: LazyLoader | None

    @property
    def utilities(self) -> list[Skill]:
        return self.utilities_() if self.utilities_ else None

    elite_: LazyLoader | None

    @property
    def elite(self):
        return self.elite_() if self.elite_ else None

    legends_: LazyLoader | None

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
    id: int | None
    specialization_: LazyLoader | None

    @property
    def specialization(self) -> Specialization:
        return self.specialization_() if self.specialization_ else None

    traits_: LazyLoader | None

    @property
    def traits(self) -> list[Trait]:
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
    guild_: LazyLoader | None = None

    @property
    def guild(self) -> Guild:
        return self.guild_() if self.guild_ is not None else None

    age: int
    created: datetime.datetime
    deaths: int
    title_: LazyLoader | None = None

    @property
    def title(self) -> Title:
        return self.title_() if self.title_ is not None else None


class Build(BaseModel):
    name: str
    profession: Professions
    specializations: list[SpecializationBase]
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
    equipment: list[Equipment]
    equipment_pvp: PvPEquipment


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
    guild_: LazyLoader | None = None

    @property
    def guild(self) -> Guild:
        return self.guild_() if self.guild_ is not None else None

    age: int
    created: datetime.datetime
    deaths: int
    title_: LazyLoader | None = None

    @property
    def title(self) -> Title:
        return self.title_() if self.title_ is not None else None

    backstory_: LazyLoader

    @property
    def backstory(self) -> list[BiographyAnswer]:
        return self.backstory_()

    crafting: list[Crafting]
    equipment: list[Equipment]
    build_tabs: list[BuildTab]
    equipment_tabs: list[EquipmentTab]
    heropoints_: LazyLoader

    @property
    def heropoints(self) -> list[str]:  # TODO replace with proper lookup
        return self.heropoints_()

    bags: list[Bag | None] = []

    @property
    def inventory(self) -> list[Bag | None]:
        return self.bags

    training: list[SkillTree]
    sab_: LazyLoader

    @property
    def sab(self) -> SAB:
        return self.sab_()

    wvw_abilities: list[CharacterWvWAbility]
    flags: list[CharacterFlag] = []


class CharacterWvWAbility(BaseModel):
    id: int
    ability_: LazyLoader

    @property
    def ability(self) -> WvWAbility:
        return self.ability_()

    rank: int


class ProfessionTrainingTrack(BaseModel):
    cost: int = 0
    type: ProfessionTrainingTrackType
    skill_id: int | None
    skill_: LazyLoader | None

    @property
    def skill(self) -> Skill | None:
        return self.skill_() if self.skill_ is not None else None

    trait_id: int | None
    trait_: LazyLoader | None

    @property
    def trait(self) -> Trait | None:
        return self.trait_() if self.trait_ is not None else None


class ProfessionTraining(BaseModel):
    id: int
    skill_: LazyLoader

    @property
    def skill(self) -> Skill:
        return self.skill_()

    specialization_: LazyLoader

    @property
    def specialization(self) -> Specialization:
        return self.specialization_()

    category: ProfessionTrainingCategory
    name: str
    track: list[ProfessionTrainingTrack]


class WeaponSkill(BaseModel):
    id: int
    skill_: LazyLoader

    @property
    def skill(self) -> Skill:
        return self.skill_()

    slot: SkillSlot
    offhand: str | None
    attunement: str | None
    source: str | None


class ProfessionWeapon(BaseModel):
    flag: list[ProfessionWeaponFlag] | None
    specialization_: LazyLoader | None

    @property
    def specialization(self) -> Specialization | None:
        return self.specialization_() if self.specialization_ is not None else None

    skills: list[WeaponSkill]


class ProfessionWeapons(BaseModel):
    Axe: ProfessionWeapon | None
    Dagger: ProfessionWeapon | None
    Mace: ProfessionWeapon | None
    Pistol: ProfessionWeapon | None
    Sword: ProfessionWeapon | None
    Scepter: ProfessionWeapon | None
    Focus: ProfessionWeapon | None
    Shield: ProfessionWeapon | None
    Torch: ProfessionWeapon | None
    Warhorn: ProfessionWeapon | None
    Greatsword: ProfessionWeapon | None
    Hammer: ProfessionWeapon | None
    Longbow: ProfessionWeapon | None
    Rifle: ProfessionWeapon | None
    Shortbow: ProfessionWeapon | None
    Staff: ProfessionWeapon | None
    Speargun: ProfessionWeapon | None
    Spear: ProfessionWeapon | None
    Trident: ProfessionWeapon | None


class Profession(BaseModel):
    id: str = ""
    name: str = ""
    icon: str = ""
    icon_big: str = ""
    specializations_: LazyLoader

    @property
    def specializations(self) -> list[Specialization]:
        return self.specializations_()

    training: list[ProfessionTraining]
    weapons: ProfessionWeapons


class Race(BaseModel):
    id: str
    skills_: LazyLoader

    @property
    def skills(self) -> list[Skill]:
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
    def minor_traits(self) -> list[Trait]:
        return self.minor_traits_()

    major_traits_: LazyLoader

    @property
    def major_traits(self) -> list[Trait]:
        return self.major_traits_()


class SkillFactPrefix(BaseModel):
    text: str
    icon: str
    status: str
    description: str


class SkillFact(BaseModel):
    text: str | None
    icon: str | None
    type: SkillFactType
    value: int | bool | None
    target: str | None
    status: str | None
    description: str | None
    apply_count: int | None
    duration: int | None
    field_type: ComboFieldType | None
    finisher_type: ComboFinisherType | None
    percent: int | None
    hit_count: int | None
    dmg_multiplier: int | None
    distance: int | None
    prefix: SkillFactPrefix | None


class SkillTraitedFact(SkillFact):
    requires_trait_: LazyLoader

    @property
    def requires_trait(self) -> Trait:
        return self.requires_trait_()

    overrides: int | None  # TODO resolve from facts


class Skill(BaseModel):
    id: int
    name: str
    description: str | None
    icon: str
    chat_link: str
    type: SkillType | None
    weapon_type: WeaponType | None
    professions: list[Professions]
    slot: SkillSlot
    facts: list[SkillFact] | None
    traited_facts: list[SkillTraitedFact] | None
    categories: list[SkillCategories] | None
    attunement: Attunement | None
    cost: int | None
    dual_wield: str | None
    flip_skill_: LazyLoader | None

    @property
    def flip_skill(self) -> Skill | None:
        return self.flip_skill_() if self.flip_skill_ is not None else None

    initiative: int | None
    next_chain_: LazyLoader | None

    @property
    def next_chain(self) -> Skill | None:
        return self.next_chain_() if self.next_chain_ is not None else None

    prev_chain_: LazyLoader | None

    @property
    def prev_chain(self) -> Skill | None:
        return self.prev_chain_ if self.prev_chain_ is not None else None

    transform_skills_: LazyLoader | None

    @property
    def transform_skills(self) -> list[Skill] | None:
        return self.transform_skills_ if self.transform_skills_ is not None else None

    bundle_skills_: LazyLoader | None

    @property
    def bundle_skills(self) -> list[Skill] | None:
        return self.bundle_skills_ if self.bundle_skills_ is not None else None

    toolbelt_skill_: LazyLoader | None

    @property
    def toolbelt_skill(self) -> Skill | None:
        return self.toolbelt_skill_ if self.toolbelt_skill_ is not None else None


class TraitSkill(BaseModel):
    id: int
    name: str
    description: str
    icon: str
    facts: list[SkillFact] | None
    traited_facts: list[SkillTraitedFact] | None


class Trait(BaseModel):
    id: int
    name: str
    icon: str
    description: str
    specialization_: LazyLoader

    @property
    def specialization(self) -> Specialization:
        return self.specialization_()

    tier: TraitTier
    slot: TraitSlot
    facts: list[SkillFact] | None
    traited_facts: list[SkillTraitedFact] | None
    skills: list[TraitSkill] | None


class Legend(BaseModel):
    id: str = ""
    swap_: LazyLoader

    @property
    def swap(self) -> Skill:
        return self.swap_()

    heal_: LazyLoader

    @property
    def heal(self) -> Skill:
        return self.heal_()

    elite_: LazyLoader

    @property
    def elite(self) -> Skill:
        return self.elite_()

    utilities_: LazyLoader

    @property
    def utilities(self) -> list[Skill]:
        return self.utilities_()
