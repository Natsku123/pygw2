from __future__ import annotations

import datetime
from typing import TYPE_CHECKING, ForwardRef

from pygw2.core.enums import WvWMapTypes, WvWObjectiveTypes, WvWTeams, WvWMapBonusTypes
from pygw2.utils import BaseModel, LazyLoader

if TYPE_CHECKING:
    from pygw2.core.models.misc import World
    from pygw2.core.models.guild import Guild, GuildUpgrade
    from pygw2.core.models.map import MapSector, Map
else:
    World = ForwardRef("World")
    Guild = ForwardRef("Guild")
    GuildUpgrade = ForwardRef("GuildUpgrade")
    MapSector = ForwardRef("MapSector")
    Map = ForwardRef("Map")


class WvWAbilityRank(BaseModel):
    cost: int
    effect: str


class WvWAbility(BaseModel):
    id: int
    name: str
    description: str
    icon: str
    ranks: list[WvWAbilityRank]


class WvWStats(BaseModel):
    red: int
    blue: int
    green: int


class WvWMatchWorlds(BaseModel):
    red_: LazyLoader
    blue_: LazyLoader
    green_: LazyLoader

    @property
    def red(self) -> World | list[World]:
        return self.red_()

    @property
    def blue(self) -> World | list[World]:
        return self.blue_()

    @property
    def green(self) -> World | list[World]:
        return self.green_()


class WvWMapObjectives(BaseModel):
    id: str
    type: WvWObjectiveTypes
    owner: WvWTeams
    last_flipped: datetime.datetime
    claimed_by_: LazyLoader | None

    @property
    def claimed_by(self) -> Guild | None:
        return self.claimed_by_() if self.claimed_by_ else None

    claimed_at: datetime.datetime | None
    points_tick: int
    points_capture: int
    guild_upgrades_: LazyLoader | None

    @property
    def guild_upgrades(self) -> list[GuildUpgrade] | None:
        return self.guild_upgrades_() if self.guild_upgrades_ else None

    yaks_delivered: int | None


class WvWMapBonus(BaseModel):
    type: WvWMapBonusTypes
    owner: WvWTeams


class WvWMatchMap(BaseModel):
    id: int
    type: WvWMapTypes
    scores: WvWStats | None
    kills: WvWStats | None
    deaths: WvWStats | None
    objectives: list[WvWMapObjectives] | None
    bonuses: list[WvWMapBonus] | None


class WvWMapScores(BaseModel):
    type: WvWMapTypes
    scores: WvWStats


class WvWSkirmish(BaseModel):
    id: int
    scores: WvWStats
    map_scores: list[WvWMapScores]


class WvWMatch(BaseModel):
    id: str
    start_time: datetime.datetime | None
    end_time: datetime.datetime | None
    scores: WvWStats | None
    worlds: WvWMatchWorlds | None
    all_worlds: WvWMatchWorlds | None
    deaths: WvWStats | None
    kills: WvWStats | None
    victory_points: WvWStats | None
    maps: list[WvWMatchMap] | None
    skirmishes: list[WvWSkirmish] | None


class WvWUpgradeTierUpgrade(BaseModel):
    name: str
    description: str
    icon: str


class WvWUpgradeTier(BaseModel):
    name: str
    yaks_required: int
    upgrades: list[WvWUpgradeTierUpgrade]


class WvWUpgrade(BaseModel):
    id: int
    tiers: list[WvWUpgradeTier]


class WvWObjective(BaseModel):
    id: str
    name: str
    type: WvWObjectiveTypes
    sector_id: int
    sector: MapSector | None
    map_id: int
    map: Map | None
    map_type: WvWMapTypes
    coord: list[int] | None
    label_coord: list[int] | None
    marker: str | None
    chat_link: str
    upgrade_id: int | None
    upgrade: WvWUpgrade | None


class WvWRank(BaseModel):
    id: int
    title: str
    min_rank: int
