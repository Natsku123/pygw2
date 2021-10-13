import datetime
from pydantic import BaseModel
from typing import Optional, Union, List, TYPE_CHECKING

from pygw2.utils import LazyLoader
from pygw2.core.enums import PvpRatingType, PvpDivisionFlags

if TYPE_CHECKING:
    from pygw2.core.models.items import Item


class PvPEquipment(BaseModel):
    _amulet: Optional[LazyLoader]

    @property
    def amulet(self) -> Optional["PvpAmulet"]:
        return self._amulet() if self._amulet is not None else None

    _rune: Optional[LazyLoader]

    @property
    def rune(self) -> Optional["Item"]:
        return self._rune() if self._rune is not None else None

    _sigils: Optional[LazyLoader]

    @property
    def sigils(self) -> List["Item"]:
        return self._sigils() if self._sigils is not None else None


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
    map_id: int  # TODO resolve agaisnt pvp maps
    started: datetime.datetime
    ended: datetime.datetime
    result: str
    team: str
    profession: Optional[str]
    scores: PvpScores
    rating_type: Union[PvpRatingType, None]
    rating_change: int
    season: Optional[str]  # TODO resolve against pvp seasons


class PvpRankLevel(BaseModel):
    min_rank: int
    max_rank: int
    points: int


class PvpRank(BaseModel):
    id: int
    finisher_id: int  # TODO resolve against /v2/finishers
    name: str
    icon: str
    min_rank: int
    max_rank: int
    levels: List[PvpRankLevel]


class PvpDivisionTier(BaseModel):
    points: int


class PvpDivision(BaseModel):
    name: str
    flags: List[PvpDivisionFlags]
    large_icon: str
    small_icon: str
    pip_icon: str
    tiers: List[PvpDivisionTier]


class PvpLeaderboardsLadderSettingsTier(BaseModel):
    range: List[int]


class PvpLeaderboardsLadderSettings(BaseModel):
    name: str
    duration: Optional[int]
    scoring: str
    tiers: List[PvpLeaderboardsLadderSettingsTier]


class PvpLeaderboardsLadderScoring(BaseModel):
    id: str
    type: str
    description: str
    name: str
    ordering: str


class PvpLeaderboardsLadder(BaseModel):
    settings: PvpLeaderboardsLadderSettings
    scorings: List[PvpLeaderboardsLadderScoring]


class PvpLeaderboards(BaseModel):
    ladder: PvpLeaderboardsLadder


class PvpSeason(BaseModel):
    id: str
    name: str
    start: datetime.datetime
    end: datetime.datetime
    active: bool
    divisions: List[PvpDivision]
    leaderboards: PvpLeaderboards


class PvpLeaderboardScore(BaseModel):
    id: str
    value: int


class PvpLeaderboard(BaseModel):
    name: str
    rank: int
    id: str
    team: Optional[str]
    team_id: Optional[str]
    date: datetime.datetime
    scores: List[PvpLeaderboardScore]


class PvpHeroStats(BaseModel):
    offense: int
    defense: int
    speed: int


class PvpHeroSkin(BaseModel):
    id: int
    name: str
    icon: str
    default: bool
    _unlock_items: Optional[LazyLoader]

    @property
    def unlock_items(self) -> Union[List["Item"], "Item"]:
        return self._unlock_items() if self._unlock_items is not None else None


class PvpHero(BaseModel):
    id: str
    name: str
    type: str
    stats: PvpHeroStats
    overlay: str
    underlay: str
    skins: List[PvpHeroSkin]
