from typing import Optional, List
from pydantic import BaseModel

from pygw2.core.enums import RecipeType, Discipline, RecipeFlag


class Material(BaseModel):
    id: int
    name: str
    items: List[int]    # TODO resolve against items
    order: int


class RecipeIngredient(BaseModel):
    item_id: int    # TODO resolve against items
    count: int


class RecipeGuildIngredient(BaseModel):
    upgrade_id: int     # TODO resolve against guild upgrades
    count: int


class Recipe(BaseModel):
    id: int
    type: RecipeType
    output_item_id: int     # TODO resolve against items
    output_item_count: int
    time_to_craft_ms: int
    disciplines: List[Discipline]
    min_rating: int
    flags: List[RecipeFlag]
    ingredients: List[RecipeIngredient]
    guild_ingredients: Optional[List[RecipeGuildIngredient]]
    output_upgrade_id: Optional[int]    # TODO resolve against guild upgrades
    chat_link: str
