from __future__ import annotations

from pygw2.utils import BaseModel


class Continent(BaseModel):
    id: int
    name: str
    continent_dims: list[int]
    min_zoom: int
    max_zoom: int
    floors: list[int]  # TODO parse subendpoints?


class MapSector(BaseModel):
    id: int
    name: str
    level: int
    coord: list[float]
    bounds: list[list[float]]
    chat_link: str


class Map(BaseModel):
    id: int
    name: str
    min_level: int
    max_level: int
    default_floor: int
    floors: list[int]  # TODO resolve?
    region_id: int  # TODO resolve region?
    region_name: str | None = None
    continent_id: int  # TODO resolve continent?
    continent_name: str
    map_rect: list[list[int]]
    continent_rect: list[list[int]]
