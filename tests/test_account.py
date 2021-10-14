import aiounittest
import unittest
import pytest

from pygw2.models import *

from .helpers import subset


@pytest.mark.usefixtures("get_api")
class AccountTests(aiounittest.AsyncTestCase):
    async def test_account_get(self):
        acc = await self.api.account.get()
        self.assertIsInstance(acc, Account)

    async def test_account_achievements(self):
        acc = await self.api.account.achievements()
        self.assertIsInstance(acc, list)

        acc = subset(acc, 10)

        for a in acc:
            self.assertIsInstance(a, AchievementProgress)
            if a.achievement:
                self.assertIsInstance(a.achievement, Achievement)

    async def test_bank(self):
        bank = await self.api.account.bank()
        self.assertIsInstance(bank, list)

    async def test_shared_inventory(self):
        inventory = await self.api.account.inventory()
        self.assertIsInstance(inventory, list)
        for slot in inventory:
            self.assertIsInstance(slot, SharedInventorySlot)
            if slot.item:
                self.assertIsInstance(slot.item, Item)

    async def test_dailycrafting(self):
        dc = await self.api.account.dailycrafting()
        self.assertIsInstance(dc, list)
        dc = subset(dc, 10)
        for d in dc:
            self.assertIsInstance(d, DailyCrafting)

    async def test_dyes(self):
        dyes = await self.api.account.dyes()
        self.assertIsInstance(dyes, list)
        dyes = subset(dyes, 10)
        for d in dyes:
            self.assertIsInstance(d, Color)

    async def test_finishers(self):
        finishers = await self.api.account.finishers()
        self.assertIsInstance(finishers, list)
        finishers = subset(finishers, 10)
        for f in finishers:
            self.assertIsInstance(f, UnlockedFinisher)
            if f.finisher:
                self.assertIsInstance(f.finisher, Finisher)

    async def test_gliders(self):
        gliders = await self.api.account.gliders()
        self.assertIsInstance(gliders, list)
        gliders = subset(gliders, 10)
        for g in gliders:
            self.assertIsInstance(g, Glider)

    async def test_mailcarriers(self):
        mc = await self.api.account.mailcarriers()
        self.assertIsInstance(mc, list)
        mc = subset(mc, 10)
        for m in mc:
            self.assertIsInstance(m, Mailcarrier)

    async def test_mapchests(self):
        mc = await self.api.account.mapchests()
        self.assertIsInstance(mc, list)
        mc = subset(mc, 10)
        for m in mc:
            self.assertIsInstance(m, DailyMapChest)

    async def test_masteries(self):
        masteries = await self.api.account.masteries()
        self.assertIsInstance(masteries, list)
        masteries = subset(masteries, 10)
        for m in masteries:
            self.assertIsInstance(m, MasteryProgress)
            if m.mastery:
                self.assertIsInstance(m.mastery, Mastery)

    async def test_materials(self):
        materials = await self.api.account.materials()
        self.assertIsInstance(materials, list)
        materials = subset(materials, 10)
        for m in materials:
            self.assertIsInstance(m, StorageMaterial)
            if m.item:
                self.assertIsInstance(m.item, Item)

    async def test_minis(self):
        minis = await self.api.account.minis()
        self.assertIsInstance(minis, list)
        minis = subset(minis, 10)
        for m in minis:
            self.assertIsInstance(m, Mini)
            if m.item:
                self.assertIsInstance(m.item, Item)

    async def test_novelties(self):
        novelties = await self.api.account.novelties()
        self.assertIsInstance(novelties, list)
        novelties = subset(novelties, 10)
        for n in novelties:
            self.assertIsInstance(n, Novelty)
            if n.unlock_item and isinstance(n.unlock_item, list):
                self.assertIsInstance(n.unlock_item[0], Item)
            elif n.unlock_item:
                self.assertIsInstance(n.unlock_item, Item)

    async def test_outfits(self):
        outfits = await self.api.account.outfits()
        self.assertIsInstance(outfits, list)
        outfits = subset(outfits, 10)
        for o in outfits:
            self.assertIsInstance(o, Outfit)
            if o.unlock_items and isinstance(o.unlock_items, list):
                self.assertIsInstance(o.unlock_items[0], Item)
            elif o.unlock_items:
                self.assertIsInstance(o.unlock_items, Item)

    # TODO sort this out
    # async def test_pvp_heroes(self):
    #     ph = await self.api.account.pvp_heroes()
    #     self.assertIsInstance(ph, list)
    #     ph = subset(ph, 10)
    #     for h in ph:
    #         self.assertIsInstance(h, PvpHero)

    async def test_recipes(self):
        recipes = await self.api.account.recipes()
        self.assertIsInstance(recipes, list)
        recipes = subset(recipes, 10)
        for r in recipes:
            self.assertIsInstance(r, Recipe)

    async def test_skins(self):
        skins = await self.api.account.skins()
        self.assertIsInstance(skins, list)
        skins = subset(skins, 10)
        for s in skins:
            self.assertIsInstance(s, Skin)

    async def test_titles(self):
        titles = await self.api.account.titles()
        self.assertIsInstance(titles, list)
        titles = subset(titles, 10)
        for t in titles:
            self.assertIsInstance(t, Title)

    async def test_wallet(self):
        wallet = await self.api.account.wallet()
        self.assertIsInstance(wallet, list)
        wallet = subset(wallet, 10)
        for w in wallet:
            self.assertIsInstance(w, WalletCurrency)

    async def test_worldbosses(self):
        wb = await self.api.account.worldbosses()
        self.assertIsInstance(wb, list)
        wb = subset(wb, 10)
        for b in wb:
            self.assertIsInstance(b, DailyWorldBoss)


@pytest.mark.usefixtures("get_api")
class CharacterTests(aiounittest.AsyncTestCase):
    async def test_characters(self):
        chars = await self.api.account.characters()
        char = chars[0]
        char = await self.api.account.character(char).get()
        self.assertIsInstance(char, Character)


if __name__ == "__main__":
    unittest.main()
