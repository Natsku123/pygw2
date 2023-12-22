from __future__ import annotations

import datetime

from typing import TYPE_CHECKING, ForwardRef

from pygw2.core.enums import (
    GuildEmblemFlags,
    GuildUpgradeCostType,
    GuildUpgradeType,
    GuildLogEntryType,
    GuildTeamMemberRole,
    GuildStashOperation,
    GuildUpgradeAction,
    PvpRatingType,
)

from pygw2.utils import BaseModel, LazyLoader

if TYPE_CHECKING:
    from pygw2.core.models.pvp import PvpScores
    from pygw2.core.models.items import Item, Recipe
else:
    PvpScores = ForwardRef("PvpScores")
    Item = ForwardRef("Item")
    Recipe = ForwardRef("Recipe")
    GuildUpgrade = ForwardRef("GuildUpgrade")
    GuildPvpWinLoss = ForwardRef("GuildPvpWinLoss")
    GuildPvpLadderStats = ForwardRef("GuildPvpLadderStats")
    GuildPvpGame = ForwardRef("GuildPvpGame")


class GuildEmblemBackground(BaseModel):
    id: int  # TODO resolve against backgrounds
    colors: list[int]  # TODO resolve against colors


class GuildEmblemForeground(BaseModel):
    id: int  # TODO resolve against foregrounds
    colors: list[int]  # TODO resolve against colors


class GuildEmblem(BaseModel):
    background: GuildEmblemBackground
    foreground: GuildEmblemForeground
    flags: list[GuildEmblemFlags]


class Guild(BaseModel):
    level: int
    motd: str
    influence: int
    aetherium: int
    favor: int
    member_count: int
    member_capacity: int
    id: str
    name: str
    tag: str
    emblem: GuildEmblem


class GuildEmblemImages(BaseModel):
    id: int
    layers: list[str]


class GuildPermission(BaseModel):
    id: str
    name: str
    description: str


class GuildUpgradeCost(BaseModel):
    type: GuildUpgradeCostType
    name: str | None = None
    count: int
    item_id: int | None = None
    item_: LazyLoader | None = None

    @property
    def item(self) -> Item | None:
        return self.item_() if self.item_ else None


class GuildUpgrade(BaseModel):
    id: int
    name: str
    description: str
    type: GuildUpgradeType
    icon: str
    build_time: int
    required_level: int
    experience: int
    prerequisites_: LazyLoader | None = None

    @property
    def prerequisites(self) -> list[GuildUpgrade]:
        return self.prerequisites_() if self.prerequisites_ else []

    bag_max_items: int | None = None
    bag_max_coins: int | None = None
    costs: list[GuildUpgradeCost]


class GuildLogEntry(BaseModel):
    id: int
    time: datetime.datetime
    user: str | None = None
    type: GuildLogEntryType
    invited_by: str | None = None
    kicked_by: str | None = None
    changed_by: str | None = None
    old_rank: str | None = None
    new_rank: str | None = None
    item_id: int | None = None
    item_: LazyLoader | None = None

    @property
    def item(self) -> Item | None:
        return self.item_() if self.item_ else None

    operation: GuildStashOperation | None = None
    count: int | None = None
    coins: int | None = None
    motd: str | None = None
    action: GuildUpgradeAction | None = None
    upgrade_id: int | None = None
    upgrade_: LazyLoader | None = None

    @property
    def upgrade(self) -> GuildUpgrade | None:
        return self.upgrade_() if self.upgrade_ else None

    recipe_id: int | None = None
    recipe_: LazyLoader | None = None

    @property
    def recipe(self) -> Recipe | None:
        return self.recipe_() if self.recipe_ else None


class GuildMember(BaseModel):
    name: str
    rank: str
    joined: datetime.datetime


class GuildRank(BaseModel):
    id: str
    order: int
    permissions_: LazyLoader

    @property
    def permissions(self) -> list[GuildPermission]:
        return self.permissions_()

    icon: str


class GuildStashSlot(BaseModel):
    id: int
    item_: LazyLoader

    @property
    def item(self) -> Item:
        return self.item_()

    count: int


class GuildStash(BaseModel):
    upgrade_id: int
    upgrade_: LazyLoader

    @property
    def upgrade(self) -> GuildUpgrade:
        return self.upgrade_()

    size: int
    coins: int
    note: str | None = None
    inventory: list[GuildStashSlot | None]


class GuildTreasuryNeeded(BaseModel):
    upgrade_id: int
    upgrade_: LazyLoader

    @property
    def upgrade(self) -> GuildUpgrade:
        return self.upgrade_()

    count: int


class GuildTreasury(BaseModel):
    item_id: int
    item_: LazyLoader

    @property
    def item(self) -> Item:
        return self.item_()

    count: int
    needed_by: list[GuildTreasuryNeeded]


class GuildTeamMember(BaseModel):
    name: str  # TODO resolve against guild members
    role: GuildTeamMemberRole


class GuildTeamSeason(BaseModel):
    id: str
    wins: int
    losses: int
    rating: int


class GuildTeam(BaseModel):
    id: int
    members: list
    name: str
    aggregate: GuildPvpWinLoss
    ladders: GuildPvpLadderStats
    games: list[GuildPvpGame]
    seasons: list[GuildTeamSeason] | None = None


class GuildPvpWinLoss(BaseModel):
    wins: int
    losses: int
    desertions: int
    byes: int
    forfeits: int


class GuildPvpLadderStats(BaseModel):
    ranked: GuildPvpWinLoss | None = None
    unranked: GuildPvpWinLoss | None = None


class GuildPvpGame(BaseModel):
    id: str
    map_id: int
    started: datetime.datetime
    ended: datetime.datetime
    result: str
    team: str
    rating_type: PvpRatingType | None = None
    rating_change: int | None = None
    scores: PvpScores


Guild.model_rebuild()
