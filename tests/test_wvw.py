import aiounittest
import unittest
import pytest

from pygw2.models import *

from .helpers import ids_helper


@pytest.mark.usefixtures("get_api")
class WvWTests(aiounittest.AsyncTestCase):
    async def test_abilities(self):
        await ids_helper(self, self.api.wvw.abilities, WvWAbility)

    async def test_upgrades(self):
        await ids_helper(self, self.api.wvw.upgrades, WvWUpgrade)

    async def test_objectives(self):
        await ids_helper(self, self.api.wvw.objectives, WvWObjective)

    async def test_ranks(self):
        await ids_helper(self, self.api.wvw.ranks, WvWRank)


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
