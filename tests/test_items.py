import pytest
from pygw2.models import *

import unittest
import aiounittest


@pytest.mark.usefixtures("get_api")
class ItemTests(aiounittest.AsyncTestCase):
    async def test_get(self):
        got_items = await self.api.items.get()
        self.assertIsInstance(got_items, list)

    async def test_armor(self):
        item = await self.api.items.get(6542)
        self.assertIsInstance(item, Item)

    async def test_weapon(self):
        item = await self.api.items.get(6)
        self.assertIsInstance(item, Item)

    async def test_consumable(self):
        item = await self.api.items.get(24)
        self.assertIsInstance(item, Item)

    async def test_back(self):
        item = await self.api.items.get(56)
        self.assertIsInstance(item, Item)

    async def test_item(self):
        item = await self.api.items.get(72421)
        self.assertIsInstance(item, Item)

    async def test_container(self):
        item = await self.api.items.get(9338)
        self.assertIsInstance(item, Item)

    async def test_miniature(self):
        item = await self.api.items.get(86528)
        self.assertIsInstance(item, Item)

    async def test_upgrade(self):
        item = await self.api.items.get(24597)
        self.assertIsInstance(item, Item)

    async def test_gizmo(self):
        item = await self.api.items.get(67835)
        self.assertIsInstance(item, Item)

    async def test_trinket(self):
        item = await self.api.items.get(13464)
        self.assertIsInstance(item, Item)

    async def test_gathering(self):
        item = await self.api.items.get(23005)
        self.assertIsInstance(item, Item)

    async def test_not_found(self):
        item = await self.api.items.get(45022)
        self.assertIsNone(item)

    async def test_get_multiple(self):
        some_items = await self.api.items.get(6542, 6, 24)
        self.assertIsInstance(some_items, list)
        self.assertIs(len(some_items) > 0, True)
        self.assertIsInstance(some_items[0], Item)

    async def test_recipe(self):
        recipe = await self.api.items.recipes(7314)
        self.assertIsInstance(recipe, Recipe)

    async def test_search_input(self):
        recipes = await self.api.items.search_recipes(input=46731)
        self.assertIsInstance(recipes, list)
        self.assertIs(len(recipes) > 0, True)
        self.assertIsInstance(recipes[0], Recipe)

    async def test_search_output(self):
        recipes = await self.api.items.search_recipes(output=50065)
        self.assertIsInstance(recipes, list)
        self.assertIs(len(recipes) > 0, True)
        self.assertIsInstance(recipes[0], Recipe)


if __name__ == "__main__":
    unittest.main()
