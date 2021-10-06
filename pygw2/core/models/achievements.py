from typing import Optional, List, TYPE_CHECKING
from pydantic import BaseModel

from pygw2.core.enums import (
    Region,
    AchievementBitsType,
    AchievementType,
    AchievementFlag,
)

if TYPE_CHECKING:
    from pygw2.core.models.account import ProductAccess


class AchievementCategory(BaseModel):
    id: int
    name: str
    description: str
    order: int
    icon: str
    achievements: List[int]  # TODO resolve against achievements


class AchievementGroup(BaseModel):
    id: str
    name: str
    description: str
    order: int
    categories: List[int]  # TODO resolve against achievement categories


class AchievementTier(BaseModel):
    count: int
    points: int


class AchievementRewardType(BaseModel):
    id: Optional[int]
    count: Optional[int]
    region: Optional[Region]


class AchievementReward(BaseModel):
    type: AchievementRewardType


class AchievementBits(BaseModel):
    type: AchievementBitsType
    id: Optional[int]
    text: Optional[str]


class Achievement(BaseModel):
    id: int
    icon: Optional[str]
    name: str
    description: str
    requirement: str
    locked_text: str
    type: AchievementType
    flags: List[AchievementFlag]
    tiers: List[AchievementTier]
    prerequisites: Optional[List[int]] = []  # TODO resolve achievements
    rewards: Optional[List[AchievementReward]]
    bits: Optional[List[AchievementBits]]
    point_cap: Optional[int]


class AchievementProgress(BaseModel):
    id: int  # TODO resolve against achievement
    bits: Optional[List[int]]
    current: Optional[int]
    max: Optional[int]
    done: bool
    repeated: Optional[int]
    unlocked: Optional[bool] = True


class DailyAchievementLevel(BaseModel):
    min: int
    max: int


class DailyAchievement(BaseModel):
    id: int  # TODO resolve achievement
    level: DailyAchievementLevel
    required_access: Optional[ProductAccess]


class DailyAchievements(BaseModel):
    pve: List[DailyAchievement]
    pvp: List[DailyAchievement]
    wvw: List[DailyAchievement]
    fractals: List[DailyAchievement]
    special: List[DailyAchievement]
