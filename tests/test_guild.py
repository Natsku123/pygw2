import aiounittest
import unittest
import pytest

from pygw2.models import *

from .helpers import subset, ids_helper


TEST_GUILD_ID = "B95A726D-DD83-E511-AEFB-AC162DC05865"


@pytest.mark.usefixtures("get_api")
class GuildTests(aiounittest.AsyncTestCase):
    async def test_get(self):
        guild = await self.api.guild(TEST_GUILD_ID).get()
        self.assertIsInstance(guild, Guild)

    async def test_permissions(self):
        await ids_helper(self, self.api.guild().permissions, GuildPermission)

    async def test_upgrades(self):
        await ids_helper(self, self.api.guild().upgrades, GuildUpgrade)

    async def test_log(self):
        logs = await self.api.guild(TEST_GUILD_ID).log()
        for l in logs:
            self.assertIsInstance(l, GuildLogEntry)

    async def test_members(self):
        members = await self.api.guild(TEST_GUILD_ID).members()
        for m in members:
            self.assertIsInstance(m, GuildMember)

    async def test_rank(self):
        ranks = await self.api.guild(TEST_GUILD_ID).ranks()
        for r in ranks:
            self.assertIsInstance(r, GuildRank)

    async def test_stash(self):
        stash = await self.api.guild(TEST_GUILD_ID).stash()
        for s in stash:
            self.assertIsInstance(s, GuildStash)

    async def test_treasury(self):
        treasury = await self.api.guild(TEST_GUILD_ID).treasury()
        for t in treasury:
            self.assertIsInstance(t, GuildTreasury)

    async def test_teams(self):
        teams = await self.api.guild(TEST_GUILD_ID).teams()
        for t in teams:
            self.assertIsInstance(t, GuildTeam)

    async def test_upgraded(self):
        upgrades = await self.api.guild(TEST_GUILD_ID).upgraded()
        for u in upgrades:
            self.assertIsInstance(u, GuildUpgrade)
