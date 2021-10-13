from typing import List, Optional

from pygw2.utils import BaseModel


class Continent(BaseModel):
    id: int
    name: str
    continent_dims: List[int]
    min_zoom: int
    max_zoom: int
    floors: List[int]  # TODO parse subendpoints?


class MapSector(BaseModel):
    id: int
    name: str
    level: int
    coord: List[int]
    bounds: List[List[int]]
    chat_link: str


class Map(BaseModel):
    id: int
    name: str
    min_level: int
    max_level: int
    default_floor: int
    floors: List[int]  # TODO resolve?
    region_id: int  # TODO resolve region?
    region_name: Optional[str]
    continent_id: int  # TODO resolve continent?
    continent_name: str
    map_rect: List[List[int]]
    continent_rect: List[List[int]]
