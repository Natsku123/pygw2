from typing import List
from pydantic import BaseModel


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