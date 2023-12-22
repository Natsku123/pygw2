from __future__ import annotations

import datetime
from typing import TYPE_CHECKING, ForwardRef

from pygw2.utils import LazyLoader, BaseModel
from pygw2.core.enums import PvpRatingType, PvpDivisionFlags

if TYPE_CHECKING:
    from pygw2.core.models.items import Item
else:
    Item = ForwardRef("Item")
    PvpAmulet = ForwardRef("PvpAmulet")
    PvpSeason = ForwardRef("PvpSeason")


class PvPEquipment(BaseModel):
    amulet_: LazyLoader | None = None

    @property
    def amulet(self) -> PvpAmulet | None:
        return self.amulet_() if self.amulet_ is not None else None

    rune_: LazyLoader | None = None

    @property
    def rune(self) -> Item | None:
        return self.rune_() if self.rune_ is not None else None

    sigils_: LazyLoader | None = None

    @property
    def sigils(self) -> list[Item]:
        return self.sigils_() if self.sigils_ is not None else None


class PvpAttributes(BaseModel):
    AgonyResistance: float | None = None
    BoonDuration: float | None = None
    ConditionDamage: float | None = None
    ConditionDuration: float | None = None
    CritDamage: float | None = None
    Healing: float | None = None
    Power: float | None = None
    Precision: float | None = None
    Toughness: float | None = None
    Vitality: float | None = None


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
    elementalist: PvpWinLoss | None = None
    engineer: PvpWinLoss | None = None
    guardian: PvpWinLoss | None = None
    mesmer: PvpWinLoss | None = None
    necromancer: PvpWinLoss | None = None
    ranger: PvpWinLoss | None = None
    revenant: PvpWinLoss | None = None
    thief: PvpWinLoss | None = None
    warrior: PvpWinLoss | None = None


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
    profession: str | None = None
    scores: PvpScores
    rating_type: PvpRatingType | None = None
    rating_change: int | None = None
    season_: LazyLoader | None = None

    @property
    def season(self) -> PvpSeason | None:
        return self.season_() if self.season_ else None


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
    levels: list[PvpRankLevel]


class PvpDivisionTier(BaseModel):
    points: int


class PvpDivision(BaseModel):
    name: str
    flags: list[PvpDivisionFlags]
    large_icon: str
    small_icon: str
    pip_icon: str
    tiers: list[PvpDivisionTier]


class PvpLeaderboardsLadderSettingsTier(BaseModel):
    range: list[int]


class PvpLeaderboardsLadderSettings(BaseModel):
    name: str
    duration: int | None = None
    scoring: str
    tiers: list[PvpLeaderboardsLadderSettingsTier]


class PvpLeaderboardsLadderScoring(BaseModel):
    id: str
    type: str
    description: str
    name: str
    ordering: str


class PvpLeaderboardsLadder(BaseModel):
    settings: PvpLeaderboardsLadderSettings
    scorings: list[PvpLeaderboardsLadderScoring]


class PvpLeaderboards(BaseModel):
    ladder: PvpLeaderboardsLadder | None = None


class PvpSeason(BaseModel):
    id: str
    name: str
    start: datetime.datetime
    end: datetime.datetime
    active: bool
    divisions: list[PvpDivision]
    leaderboards: PvpLeaderboards


class PvpLeaderboardScore(BaseModel):
    id: str
    value: int


class PvpLeaderboard(BaseModel):
    name: str
    rank: int
    id: str | None = None
    team: str | None = None
    team_id: str | None = None
    date: datetime.datetime
    scores: list[PvpLeaderboardScore]


class PvpHeroStats(BaseModel):
    offense: int
    defense: int
    speed: int


class PvpHeroSkin(BaseModel):
    id: int
    name: str
    icon: str
    default: bool
    unlock_items_: LazyLoader | None = None

    @property
    def unlock_items(self) -> list[Item] | Item:
        return self.unlock_items_() if self.unlock_items_ is not None else None


class PvpHero(BaseModel):
    id: str
    name: str
    type: str
    stats: PvpHeroStats
    overlay: str
    underlay: str
    skins: list[PvpHeroSkin]


class PvpStandingsCurrent(BaseModel):
    total_points: int
    division: int
    tier: int
    points: int
    repeats: int
    rating: int
    decay: int


class PvpStandingsBest(BaseModel):
    total_points: int
    division: int
    tier: int
    points: int
    repeats: int


class PvpStandings(BaseModel):
    current: PvpStandingsCurrent
    season_id: int
    season_: LazyLoader

    @property
    def season(self) -> PvpSeason:
        return self.season_()
