import asyncio
from pygw2.api import api
from pygw2.core.models.achievements import Achievement, DailyAchievements, \
    AchievementCategory, AchievementGroup

import unittest
import aiounittest


class AchievementsTests(aiounittest.AsyncTestCase):
    async def test_get(self):
        a = await api.achievements.get(1)
        self.assertIsInstance(a, Achievement)

    async def test_get_dailies(self):
        d = await api.achievements.daily()
        self.assertIsInstance(d, DailyAchievements)

    async def test_get_group(self):
        g = await api.achievements.groups("65B4B678-607E-4D97-B458-076C3E96A810")
        self.assertIsInstance(g, AchievementGroup)

    async def test_get_category(self):
        c = await api.achievements.categories(1)
        self.assertIsInstance(c, AchievementCategory)


if __name__ == '__main__':
    unittest.main()
