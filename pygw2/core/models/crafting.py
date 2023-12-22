from __future__ import annotations

from pygw2.core.enums import RecipeType, Discipline, RecipeFlag
from pygw2.utils import LazyLoader, BaseModel


class Material(BaseModel):
    id: int
    name: str
    items: list[int]  # TODO resolve against items
    order: int


class RecipeIngredient(BaseModel):
    id: int  # TODO resolve against items
    type: str  # TODO enumarate
    count: int


class RecipeGuildIngredient(BaseModel):
    upgrade_id: int  # TODO resolve against guild upgrades
    count: int


class Recipe(BaseModel):
    id: int
    type: RecipeType
    output_item_id: int  # TODO resolve against items
    output_item_count: int
    time_to_craft_ms: int
    disciplines: list[Discipline]
    min_rating: int
    flags: list[RecipeFlag]
    ingredients: list[RecipeIngredient]
    guild_ingredients: list[RecipeGuildIngredient] | None
    output_upgrade_id: int | None  # TODO resolve against guild upgrades
    chat_link: str
