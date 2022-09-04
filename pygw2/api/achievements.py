from ..core.exceptions import ApiError
from ..core.models.achievements import (
    Achievement,
    DailyAchievements,
    AchievementGroup,
    AchievementCategory,
)

from ..core.enums import AchievementRewardType
from ..utils import endpoint, object_parse, LazyLoader


class AchievementsApi:
    _instances = {}

    def __new__(cls, *args, api_key: str = "", **kwargs):
        if api_key not in cls._instances:
            cls._instances[api_key] = super().__new__(cls, *args, **kwargs)
        return cls._instances[api_key]

    def __init__(self, *, api_key: str = ""):
        self.api_key: str = api_key

    @endpoint("/v2/achievements", has_ids=True)
    async def get(self, *, data, ids: list = None):
        """
        Get achievements from API by list of IDs.
        https://api.guildwars2.com/v2/achievements
        :param data: Data from endpoint wrapper
        :param ids: list=[]
        :return: list
        """
        from .misc import MiscellaneousApi

        misc_api = MiscellaneousApi(api_key=self.api_key)

        from .items import ItemsApi

        items_api = ItemsApi(api_key=self.api_key)

        from .mechanics import MechanicsApi

        mecha_api = MechanicsApi(api_key=self.api_key)

        # Return list of ids.
        if ids is None:
            return data

        # Return list of Achievements.
        for a in data:
            if "rewards" in a and a["rewards"]:
                for r in a["rewards"]:
                    if r["type"] == AchievementRewardType.Title:
                        r["title_"] = LazyLoader(misc_api.titles, r["id"])
                    elif r["type"] == AchievementRewardType.Item:
                        r["item_"] = LazyLoader(items_api.get, r["id"])
                    elif r["type"] == AchievementRewardType.Mastery:
                        r["mastery_"] = LazyLoader(mecha_api.masteries, r["id"])
        return object_parse(data, Achievement)

    @endpoint("/v2/achievements/daily")
    async def daily(self, *, data):
        """
        Get daily achievements from API.
        https://api.guildwars2.com/v2/achievements/daily
        :param data: Data from wrapper
        :return: dict
        """

        for k in data.keys():
            for a in data[k]:
                a["achievement_"] = LazyLoader(self.get, a["id"])

        return object_parse(data, DailyAchievements)

    @endpoint("/v2/achievements/daily/tomorrow")
    async def daily_tomorrow(self, *, data):
        """
        Get daily achievements for tomorrow from API.
        https://api.guildwars2.com/v2/achievements/daily/tomorrow
        :param data: Data from wrapper
        :return: dict
        """

        for k in data.keys():
            for a in data[k]:
                a["achievement_"] = LazyLoader(self.get, a["id"])

        return object_parse(data, DailyAchievements)

    @endpoint("/v2/achievements/groups", has_ids=True)
    async def groups(self, *, data, ids: list = None):
        """
        Get groups for achievements from API by list of IDs or one ID.
        https://api.guildwars2.com/v2/achievements/groups
        :param data: Data from wrapper
        :param ids: list=[]
        :return: list
        """

        # Return list of group ids.
        if ids is None:
            return data

        # Return list of groups.
        else:
            for g in data:
                g["categories"] = LazyLoader(self.categories, g["categories"])
            return object_parse(data, AchievementGroup)

    @endpoint("/v2/achievements/categories", has_ids=True)
    async def categories(self, *, data, ids: list = None):
        """
        Get categories for achievements from API by list of IDs or one ID.
        https://api.guildwars2.com/v2/achievements/categories
        :param data: Data from wrapper
        :param ids: list=[]
        :return: list
        """

        # Check for errors
        if "text" in data:
            raise ApiError(data["text"])

        # Return list of category ids.
        if ids is None:
            return data

        # Return list of categories.
        else:
            for c in data:
                c["achievements"] = LazyLoader(self.get, c["achievements"])
            return object_parse(data, AchievementCategory)
