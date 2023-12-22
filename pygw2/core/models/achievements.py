from __future__ import annotations

from typing import TYPE_CHECKING, ForwardRef

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
else:
    ProductAccess = ForwardRef("ProductAccess")
    Mastery = ForwardRef("Mastery")
    Item = ForwardRef("Item")
    Title = ForwardRef("Title")


class AchievementCategory(BaseModel):
    id: int
    name: str
    description: str
    order: int
    icon: str
    achievements_: LazyLoader

    @property
    def achievements(self) -> list[Achievement]:
        return self.achievements_()


class AchievementGroup(BaseModel):
    id: str
    name: str
    description: str
    order: int
    categories_: LazyLoader

    @property
    def categories(self) -> list[AchievementCategory]:
        return self.categories_()


class AchievementTier(BaseModel):
    count: int
    points: int


class AchievementReward(BaseModel):
    type: AchievementRewardType
    id: int | None
    item_: LazyLoader | None

    @property
    def item(self) -> Item | None:
        return self.item_() if self.item_ is not None else None

    title_: LazyLoader | None

    @property
    def title(self) -> Title | None:
        return self.title_() if self.title_ is not None else None

    mastery_: LazyLoader | None

    @property
    def mastery(self) -> Mastery | None:
        return self.mastery_() if self.mastery_ is not None else None

    count: int | None
    region: Region | None


class AchievementBits(BaseModel):
    type: AchievementBitsType
    id: int | None
    text: str | None


class Achievement(BaseModel):
    id: int
    icon: str | None
    name: str
    description: str
    requirement: str
    locked_text: str
    type: AchievementType
    flags: list[AchievementFlag]
    tiers: list[AchievementTier]
    prerequisites: list[int] | None = []  # TODO resolve achievements
    rewards: list[AchievementReward] | None
    bits: list[AchievementBits] | None
    point_cap: int | None


class AchievementProgress(BaseModel):
    id: int
    achievement_: LazyLoader

    @property
    def achievement(self) -> Achievement:
        return self.achievement_()

    bits: list[int] | None
    current: int | None
    max: int | None
    done: bool
    repeated: int | None
    unlocked: bool | None = True


class DailyAchievementLevel(BaseModel):
    min: int
    max: int


class DailyAchievement(BaseModel):
    id: int
    achievement_: LazyLoader

    @property
    def achievement(self) -> Achievement:
        return self.achievement_()

    level: DailyAchievementLevel
    required_access: ProductAccess | None


class DailyAchievements(BaseModel):
    pve: list[DailyAchievement]
    pvp: list[DailyAchievement]
    wvw: list[DailyAchievement]
    fractals: list[DailyAchievement]
    special: list[DailyAchievement]
