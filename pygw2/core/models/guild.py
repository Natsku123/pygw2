import datetime

from pydantic import BaseModel
from typing import List, Optional, Union, TYPE_CHECKING

from pygw2.core.enums import (
    GuildEmblemFlags,
    GuildUpgradeCostType,
    GuildUpgradeType,
    GuildLogEntryType,
    GuildTeamMemberRole,
)

if TYPE_CHECKING:
    from pygw2.core.models.pvp import PvpWinLoss, PvpLadderStats, PvpGame


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
    id: int
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
    name: str
    count: int
    item_id: Optional[int]  # TODO resolve against items


class GuildUpgrade(BaseModel):
    id: int
    name: str
    description: str
    type: GuildUpgradeType
    icon: str
    build_time: int
    required_level: int
    experience: int
    prerequisites: List[int]  # TODO resolve against other upgrades
    bag_max_items: Optional[int]
    bag_max_coins: Optional[int]
    costs: List[GuildUpgradeCost]


class GuildLogEntry(BaseModel):
    id: int
    time: datetime.datetime
    user: Optional[str]
    type: GuildLogEntryType
    invited_by: Optional[str]
    changed_by: Optional[str]
    old_rank: Optional[str]
    new_rank: Optional[str]
    item_id: Optional[int]  # TODO resolve against items
    count: Optional[int]
    coins: Optional[int]
    motd: Optional[str]
    upgrade_id: Optional[int]  # TODO resolve against upgrades
    recipe_id: Optional[int]  # TODO resolve against recipes


class GuildMember(BaseModel):
    name: str
    rank: str  # TODO resolve against guild ranks
    joined: datetime.datetime


class GuildRank(BaseModel):
    id: str
    order: int
    permissions: List[str]  # TODO resolve against permissions
    icon: str


class GuildStashSlot(BaseModel):
    id: int  # TODO resolve against items
    count: int


class GuildStash(BaseModel):
    upgrade_id: int  # TODO resolve against guild upgrades
    size: int
    coins: int
    note: str
    inventory: List[Union[GuildStashSlot, None]]


class GuildTreasuryNeeded(BaseModel):
    upgrade_id: int  # TODO resolve against upgrades
    count: int


class GuildTreasury(BaseModel):
    item_id: int  # TODO resolve against items
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
    aggregate: "PvpWinLoss"
    ladders: "PvpLadderStats"
    games: List["PvpGame"]
    seasons: List[GuildTeamSeason]


Guild.update_forward_refs()
