from typing import Optional, List, Union, TYPE_CHECKING
from pydantic import BaseModel
from pygw2.core.enums import (
    ColorCategoryHue,
    ColorCategoryRarity,
    ColorCategoryMaterial,
    DungeonPathType,
)

if TYPE_CHECKING:
    from pygw2.core.models.items import Item


class ColorDetails(BaseModel):
    brightness: int
    contrast: int
    hue: int
    saturation: int
    lightness: int
    rgb: List[int]


class Color(BaseModel):
    id: int
    name: str
    base_rgb: List[int]
    cloth: ColorDetails
    leather: ColorDetails
    metal: ColorDetails
    fur: Optional[ColorDetails] = None
    item: Optional[int] = None  # TODO Resolve with dye
    categories: List[
        Union[ColorCategoryHue, ColorCategoryRarity, ColorCategoryMaterial]
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
    paths: List[DungeonPath]


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
    item: Item
