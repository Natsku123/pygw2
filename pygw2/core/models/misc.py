from typing import Optional, List, Union
from pydantic import BaseModel
from pygw2.core.enums import ColorCategoryHue, ColorCategoryRarity, ColorCategoryMaterial


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
