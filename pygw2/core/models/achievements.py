from typing import Optional, List, TYPE_CHECKING

from pygw2.utils import LazyLoader, BaseModel

from pygw2.core.enums import (
    Region,
    AchievementBitsType,
    AchievementType,
    AchievementFlag,
    AchievementRewardType,
)

if TYPE_CHECKING:
    from pygw2.core.models.account import ProductAccess, Mastery
    from pygw2.core.models.items import Item
    from pygw2.core.models.misc import Title


class AchievementCategory(BaseModel):
    id: int
    name: str
    description: str
    order: int
    icon: str
    achievements_: LazyLoader

    @property
    def achievements(self) -> List["Achievement"]:
        return self.achievements_()


class AchievementGroup(BaseModel):
    id: str
    name: str
    description: str
    order: int
    categories_: LazyLoader

    @property
    def categories(self) -> List["AchievementCategory"]:
        return self.categories_()


class AchievementTier(BaseModel):
    count: int
    points: int


class AchievementReward(BaseModel):
    type: AchievementRewardType
    id: Optional[int]
    item_: Optional[LazyLoader]

    @property
    def item(self) -> Optional["Item"]:
        return self.item_() if self.item_ is not None else None

    title_: Optional[LazyLoader]

    @property
    def title(self) -> Optional["Title"]:
        return self.title_() if self.title_ is not None else None

    mastery_: Optional[LazyLoader]

    @property
    def mastery(self) -> Optional["Mastery"]:
        return self.mastery_() if self.mastery_ is not None else None

    count: Optional[int]
    region: Optional[Region]


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
    id: int
    achievement_: LazyLoader

    @property
    def achievement(self) -> "Achievement":
        return self.achievement_()

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
    id: int
    achievement_: LazyLoader

    @property
    def achievement(self) -> "Achievement":
        return self.achievement_()

    level: DailyAchievementLevel
    required_access: Optional["ProductAccess"]


class DailyAchievements(BaseModel):
    pve: List[DailyAchievement]
    pvp: List[DailyAchievement]
    wvw: List[DailyAchievement]
    fractals: List[DailyAchievement]
    special: List[DailyAchievement]
