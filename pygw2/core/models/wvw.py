import datetime
from typing import Optional, List, Union, TYPE_CHECKING

from pygw2.core.enums import WvWMapTypes, WvWObjectiveTypes, WvWTeams, WvWMapBonusTypes
from pygw2.utils import BaseModel, LazyLoader

if TYPE_CHECKING:
    from pygw2.core.models.misc import World
    from pygw2.core.models.guild import Guild, GuildUpgrade
    from pygw2.core.models.map import MapSector, Map


class WvWAbilityRank(BaseModel):
    cost: int
    effect: str


class WvWAbility(BaseModel):
    id: int
    name: str
    description: str
    icon: str
    ranks: List[WvWAbilityRank]


class WvWStats(BaseModel):
    red: int
    blue: int
    green: int


class WvWMatchWorlds(BaseModel):
    red: Union["World", List["World"]]
    blue: Union["World", List["World"]]
    green: Union["World", List["World"]]


class WvWMapObjectives(BaseModel):
    id: int
    type: WvWObjectiveTypes
    owner: WvWTeams
    last_flipped: datetime.datetime
    claimed_by: Optional["Guild"]
    claimed_at: Optional[datetime.datetime]
    points_tick: int
    points_capture: int
    guild_upgrades: Optional[List["GuildUpgrade"]]
    yaks_delivered: Optional[int]


class WvWMapBonus(BaseModel):
    type: WvWMapBonusTypes
    owner: WvWTeams


class WvWMatchMap(BaseModel):
    id: int
    type: WvWMapTypes
    scores: Optional[WvWStats]
    kills: Optional[WvWStats]
    deaths: Optional[WvWStats]
    objectives: Optional[List[WvWMapObjectives]]
    bonuses: Optional[List[WvWMapBonus]]


class WvWMapScores(BaseModel):
    type: WvWMapTypes
    scores: WvWStats


class WvWSkirmish(BaseModel):
    id: int
    scores: WvWStats
    map_scores: List[WvWMapScores]


class WvWMatch(BaseModel):
    id: str
    start_time: Optional[datetime.datetime]
    end_time: Optional[datetime.datetime]
    scores: Optional[WvWStats]
    worlds: Optional[WvWMatchWorlds]
    all_worlds: Optional[WvWMatchWorlds]
    deaths: Optional[WvWStats]
    kills: Optional[WvWStats]
    victory_points: Optional[WvWStats]
    maps: Optional[List[WvWMatchMap]]
    skirmishes: Optional[List[WvWSkirmish]]


class WvWUpgradeTierUpgrade(BaseModel):
    name: str
    description: str
    icon: str


class WvWUpgradeTier(BaseModel):
    name: str
    yaks_required: int
    upgrades: List[WvWUpgradeTierUpgrade]


class WvWUpgrade(BaseModel):
    id: int
    tiers: List[WvWUpgradeTier]


class WvWObjective(BaseModel):
    id: str
    name: str
    type: WvWObjectiveTypes
    sector_id: int
    sector: "MapSector"
    map_id: int
    map: "Map"
    map_type: WvWMapTypes
    coord: List[int]
    label_coord: List[int]
    marker: str
    chat_link: str
    upgrade_id: Optional[int]
    upgrade: Optional[WvWUpgrade]


class WvWRank(BaseModel):
    id: int
    title: str
    min_rank: int
