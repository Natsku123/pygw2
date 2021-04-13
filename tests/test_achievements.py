from pygw2.api import api
from pygw2.core.models.achievements import Achievement, DailyAchievements, \
    AchievementCategory, AchievementGroup

import unittest


class AchievementsTests(unittest.TestCase):
    def test_get(self):
        a = api.achievements.get(1)
        self.assertIsInstance(a, Achievement)

    def test_get_dailies(self):
        d = api.achievements.daily()
        self.assertIsInstance(d, DailyAchievements)

    def test_get_group(self):
        g = api.achievements.groups("65B4B678-607E-4D97-B458-076C3E96A810")
        self.assertIsInstance(g, AchievementGroup)

    def test_get_category(self):
        c = api.achievements.categories(1)
        self.assertIsInstance(c, AchievementCategory)


if __name__ == '__main__':
    unittest.main()
