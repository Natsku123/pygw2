import datetime

from typing import List, Optional, Union, TYPE_CHECKING

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


class GuildEmblemBackground(BaseModel):
    id: int  # TODO resolve against backgrounds
    colors: List[int]  # TODO resolve against colors


class GuildEmblemForeground(BaseModel):
    id: int  # TODO resolve against foregrounds
    colors: List[int]  # TODO resolve against colors


class GuildEmblem(BaseModel):
    background: GuildEmblemBackground
    foreground: GuildEmblemForeground
    flags: List[GuildEmblemFlags]


class Guild(BaseModel):
    level: int
    motd: str
    influence: int
    aetherium: str
    favor: int
    member_count: int
    member_capacity: int
    id: str
    name: str
    tag: str
    emblem: GuildEmblem


class GuildEmblemImages(BaseModel):
    id: int
    layers: List[str]


class GuildPermission(BaseModel):
    id: str
    name: str
    description: str


class GuildUpgradeCost(BaseModel):
    type: GuildUpgradeCostType
    name: Optional[str]
    count: int
    item_id: Optional[int]
    item_: Optional[LazyLoader]

    @property
    def item(self) -> Optional["Item"]:
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
    prerequisites_: Optional[LazyLoader]

    @property
    def prerequisites(self) -> List["GuildUpgrade"]:
        return self.prerequisites_() if self.prerequisites_ else []

    bag_max_items: Optional[int]
    bag_max_coins: Optional[int]
    costs: List[GuildUpgradeCost]


class GuildLogEntry(BaseModel):
    id: int
    time: datetime.datetime
    user: Optional[str]
    type: GuildLogEntryType
    invited_by: Optional[str]
    kicked_by: Optional[str]
    changed_by: Optional[str]
    old_rank: Optional[str]
    new_rank: Optional[str]
    item_id: Optional[int]
    item_: Optional[LazyLoader]

    @property
    def item(self) -> Optional["Item"]:
        return self.item_() if self.item_ else None

    operation: Optional[GuildStashOperation]
    count: Optional[int]
    coins: Optional[int]
    motd: Optional[str]
    action: Optional[GuildUpgradeAction]
    upgrade_id: Optional[int]
    upgrade_: Optional[LazyLoader]

    @property
    def upgrade(self) -> Optional["GuildUpgrade"]:
        return self.upgrade_() if self.upgrade_ else None

    recipe_id: Optional[int]
    recipe_: Optional[LazyLoader]

    @property
    def recipe(self) -> Optional["Recipe"]:
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
    def permissions(self) -> List[GuildPermission]:
        return self.permissions_()

    icon: str


class GuildStashSlot(BaseModel):
    id: int
    item_: LazyLoader

    @property
    def item(self) -> "Item":
        return self.item_()

    count: int


class GuildStash(BaseModel):
    upgrade_id: int
    upgrade_: LazyLoader

    @property
    def upgrade(self) -> "GuildUpgrade":
        return self.upgrade_()

    size: int
    coins: int
    note: Optional[str]
    inventory: List[Union[GuildStashSlot, None]]


class GuildTreasuryNeeded(BaseModel):
    upgrade_id: int
    upgrade_: LazyLoader

    @property
    def upgrade(self) -> "GuildUpgrade":
        return self.upgrade_()

    count: int


class GuildTreasury(BaseModel):
    item_id: int
    item_: LazyLoader

    @property
    def item(self) -> "Item":
        return self.item_()

    count: int
    needed_by: List[GuildTreasuryNeeded]


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
    members: List
    name: str
    aggregate: "GuildPvpWinLoss"
    ladders: "GuildPvpLadderStats"
    games: List["GuildPvpGame"]
    seasons: Optional[List[GuildTeamSeason]]


class GuildPvpWinLoss(BaseModel):
    wins: int
    losses: int
    desertions: int
    byes: int
    forfeits: int


class GuildPvpLadderStats(BaseModel):
    ranked: Optional[GuildPvpWinLoss]
    unranked: Optional[GuildPvpWinLoss]


class GuildPvpGame(BaseModel):
    id: str
    map_id: int
    started: datetime.datetime
    ended: datetime.datetime
    result: str
    team: str
    rating_type: Union[PvpRatingType, None]
    rating_change: Optional[int]
    scores: "PvpScores"


Guild.update_forward_refs()
