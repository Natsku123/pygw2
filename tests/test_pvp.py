import aiounittest
import pytest

from pygw2.models import PvpHero, PvpLeaderboard, PvpRank, PvpSeason
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
        seasons = subset(seasons, 3)
        # TODO handle exceptions better
        for s in seasons:
            try:
                eu = await self.api.pvp.leaderboards(s).ladder_eu()
            except ApiError:
                eu = None
            if not eu:
                try:
                    eu = await self.api.pvp.leaderboards(s).legendary_eu()
                except ApiError:
                    eu = None
            if eu:
                for i in eu:
                    self.assertIsInstance(i, PvpLeaderboard)

            try:
                na = await self.api.pvp.leaderboards(s).ladder_na()
            except ApiError:
                na = None
            if not na:
                try:
                    na = await self.api.pvp.leaderboards(s).legendary_na()
                except ApiError:
                    na = None
            if na:
                for i in na:
                    self.assertIsInstance(i, PvpLeaderboard)
