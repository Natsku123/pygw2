import pytest
from pygw2.core.models.achievements import (
    Achievement,
    DailyAchievements,
    AchievementCategory,
    AchievementGroup,
)

import unittest
import aiounittest


@pytest.mark.usefixtures("get_api")
class AchievementsTests(aiounittest.AsyncTestCase):
    async def test_get(self):
        a = await self.api.achievements.get(1)
        self.assertIsInstance(a, Achievement)

    async def test_get_dailies(self):
        d = await self.api.achievements.daily()
        self.assertIsInstance(d, DailyAchievements)

    async def test_get_group(self):
        g = await self.api.achievements.groups("65B4B678-607E-4D97-B458-076C3E96A810")
        self.assertIsInstance(g, AchievementGroup)

    async def test_get_category(self):
        c = await self.api.achievements.categories(1)
        self.assertIsInstance(c, AchievementCategory)


if __name__ == "__main__":
    unittest.main()
