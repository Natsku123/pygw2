from pygw2.api import api
from pygw2.core.models.crafting import Recipe
from pygw2.core.models.items import Item

import unittest


class ItemTests(unittest.TestCase):
    def test_get(self):
        got_items = api.items.get()
        self.assertIsInstance(got_items, list)

    def test_armor(self):
        item = api.items.get(6542)
        self.assertIsInstance(item, Item)

    def test_weapon(self):
        item = api.items.get(6)
        self.assertIsInstance(item, Item)

    def test_consumable(self):
        item = api.items.get(24)
        self.assertIsInstance(item, Item)

    def test_back(self):
        item = api.items.get(56)
        self.assertIsInstance(item, Item)

    def test_item(self):
        item = api.items.get(72421)
        self.assertIsInstance(item, Item)

    def test_container(self):
        item = api.items.get(9338)
        self.assertIsInstance(item, Item)

    def test_miniature(self):
        item = api.items.get(86528)
        self.assertIsInstance(item, Item)

    def test_upgrade(self):
        item = api.items.get(24597)
        self.assertIsInstance(item, Item)

    def test_gizmo(self):
        item = api.items.get(67835)
        self.assertIsInstance(item, Item)

    def test_trinket(self):
        item = api.items.get(13464)
        self.assertIsInstance(item, Item)

    def test_gathering(self):
        item = api.items.get(23005)
        self.assertIsInstance(item, Item)

    def test_not_found(self):
        item = api.items.get(45022)
        self.assertIsNone(item)

    def test_get_multiple(self):
        some_items = api.items.get(6542, 6, 24)
        self.assertIsInstance(some_items, list)
        self.assertIs(len(some_items) > 0, True)
        self.assertIsInstance(some_items[0], Item)

    def test_recipe(self):
        recipe = api.items.recipes(7314)
        self.assertIsInstance(recipe, Recipe)

    def test_search_input(self):
        recipes = api.items.search_recipes(input=46731)
        self.assertIsInstance(recipes, list)
        self.assertIs(len(recipes) > 0, True)
        self.assertIsInstance(recipes[0], Recipe)

    def test_search_output(self):
        recipes = api.items.search_recipes(output=50065)
        self.assertIsInstance(recipes, list)
        self.assertIs(len(recipes) > 0, True)
        self.assertIsInstance(recipes[0], Recipe)


if __name__ == '__main__':
    unittest.main()
