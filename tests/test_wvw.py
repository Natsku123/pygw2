import aiounittest
import unittest
import pytest

from pygw2.models import *

from .helpers import subset


@pytest.mark.usefixtures("get_api")
class WvWTests(aiounittest.AsyncTestCase):
    async def test_abilities(self):
        abils = await self.api.wvw.abilities()
        abils = subset(abils, 10)
        abils = await self.api.wvw.abilities(*abils)
        for a in abils:
            self.assertIsInstance(a, WvWAbility)

    async def test_upgrades(self):
        ups = await self.api.wvw.upgrades()
        ups = subset(ups, 10)
        ups = await self.api.wvw.upgrades(*ups)
        for u in ups:
            self.assertIsInstance(u, WvWUpgrade)

    async def test_objectives(self):
        objs = await self.api.wvw.objectives()
        objs = subset(objs, 10)
        objs = await self.api.wvw.objectives(*objs)
        for o in objs:
            self.assertIsInstance(o, WvWObjective)

    async def test_ranks(self):
        ranks = await self.api.wvw.ranks()
        ranks = subset(ranks, 10)
        ranks = await self.api.wvw.ranks(*ranks)
        for r in ranks:
            self.assertIsInstance(r, WvWRank)


@pytest.mark.usefixtures("get_api")
class WvWMatchTests(aiounittest.AsyncTestCase):
    async def test_get(self):
        matches = await self.api.wvw.matches()
        for m in matches:
            match = await self.api.wvw.match(m).get()
            self.assertIsInstance(match, WvWMatch)

    async def test_overview(self):
        matches = await self.api.wvw.matches()
        for m in matches:
            overview = await self.api.wvw.match(m).overview()
            self.assertIsInstance(overview, WvWMatch)

    async def test_scores(self):
        matches = await self.api.wvw.matches()
        for m in matches:
            scores = await self.api.wvw.match(m).scores()
            self.assertIsInstance(scores, WvWMatch)

    async def test_stats(self):
        matches = await self.api.wvw.matches()
        for m in matches:
            stats = await self.api.wvw.match(m).stats()
            self.assertIsInstance(stats, WvWMatch)
