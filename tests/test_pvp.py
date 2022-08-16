import aiounittest
import unittest
import pytest

from pygw2.models import *
from pygw2.utils import ApiError

from .helpers import ids_helper, subset


@pytest.mark.usefixtures("get_api")
class PvPTests(aiounittest.AsyncTestCase):
    async def test_ranks(self):
        await ids_helper(self, self.api.pvp.ranks, PvpRank)

    async def test_seasons(self):
        await ids_helper(self, self.api.pvp.seasons, PvpSeason)

    async def test_heroes(self):
        await ids_helper(self, self.api.pvp.heroes, PvpHero)


@pytest.mark.usefixtures("get_api")
class PvPLeaderboardsTests(aiounittest.AsyncTestCase):
    async def test_leaderboards(self):
        seasons = await self.api.pvp.seasons()
        # TODO handle exceptions better
        for s in seasons:
            try:
                eu = await self.api.pvp.leaderboards(s).ladder_eu()
            except ApiError:
                eu = None
            if not eu:
                eu = await self.api.pvp.leaderboards(s).legendary_eu()
            for i in eu:
                self.assertIsInstance(i, PvpLeaderboard)

            try:
                na = await self.api.pvp.leaderboards(s).ladder_na()
            except ApiError:
                na = None
            if not na:
                na = await self.api.pvp.leaderboards(s).legendary_na()
            for i in na:
                self.assertIsInstance(i, PvpLeaderboard)
