from __future__ import annotations

from typing import TYPE_CHECKING, ForwardRef
from pygw2.core.enums import (
    ColorCategoryHue,
    ColorCategoryRarity,
    ColorCategoryMaterial,
    DungeonPathType,
    NoveltySlot,
    RaidWingEventType,
    WorldPopulation,
    WorldRegion,
)

from pygw2.utils import BaseModel, LazyLoader

if TYPE_CHECKING:
    from pygw2.core.models.items import Item
    from pygw2.core.models.achievements import Achievement
else:
    Item = ForwardRef("Item")
    Achievement = ForwardRef("Achievement")


class ColorDetails(BaseModel):
    brightness: float
    contrast: float
    hue: float
    saturation: float
    lightness: float
    rgb: list[float]


class Color(BaseModel):
    id: int
    name: str
    base_rgb: list[int]
    cloth: ColorDetails
    leather: ColorDetails
    metal: ColorDetails
    fur: ColorDetails | None = None
    item_: LazyLoader | None = None

    @property
    def item(self) -> Item | None:
        return self.item_() if self.item_ is not None else None

    categories: list[
        ColorCategoryHue | ColorCategoryRarity | ColorCategoryMaterial
    ] = []


class Currency(BaseModel):
    id: int
    name: str
    description: str
    icon: str
    order: int


class DungeonPath(BaseModel):
    id: str
    type: DungeonPathType


class Dungeon(BaseModel):
    id: str
    paths: list[DungeonPath]


class File(BaseModel):
    id: str
    icon: str


class Quaggan(BaseModel):
    id: str
    url: str


class Mini(BaseModel):
    id: int
    name: str
    icon: str
    order: int
    item_id: int
    item_: LazyLoader

    @property
    def item(self) -> Item:
        return self.item_()


class Novelty(BaseModel):
    id: int
    name: str
    description: str
    icon: str
    slot: NoveltySlot
    unlock_item_: LazyLoader | None = None

    @property
    def unlock_item(self) -> list[Item] | None:
        return self.unlock_item_() if self.unlock_item_ is not None else None


class RaidWingEvent(BaseModel):
    id: str
    type: RaidWingEventType


class RaidWing(BaseModel):
    id: str
    events: list[RaidWingEvent]


class Raid(BaseModel):
    id: str
    wings: list[RaidWing]


class Title(BaseModel):
    id: int
    name: str
    achievements_: LazyLoader | None = None

    @property
    def achievements(self) -> list[Achievement] | None:
        return self.achievements_() if self.achievements_ is not None else None

    ap_required: int | None = None


class World(BaseModel):
    id: int
    name: str
    population: WorldPopulation
    region: WorldRegion
