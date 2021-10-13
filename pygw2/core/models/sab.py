from typing import List
from pygw2.utils import LazyLoader, BaseModel


class SABZones(BaseModel):
    id: int
    mode: str
    world: int
    zone: int


class SABUnlocks(BaseModel):
    id: int
    name: str


class SABSong(BaseModel):
    id: int
    name: str


class SAB(BaseModel):
    zones: List[SABZones] = []
    unlocks: List[SABUnlocks] = []
    songs: List[SABSong] = []
