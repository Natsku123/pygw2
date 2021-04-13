import datetime
from pydantic import BaseModel
from typing import Optional, Union, List

from pygw2.core.enums import PvpRatingType


class PvPEquipment(BaseModel):
    amulet: int         # TODO resolve agaisnt /v2/pvp/amulets
    rune: int           # TODO resolve against /v2/items
    sigils: List[int]   # TODO resolve agaisnt /v2/items


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
