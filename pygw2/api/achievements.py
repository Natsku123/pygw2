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
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        pass

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

        misc_api = MiscellaneousApi()

        from .items import ItemsApi

        items_api = ItemsApi()

        from .mechanics import MechanicsApi

        mecha_api = MechanicsApi()

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
        return object_parse(data, DailyAchievements)

    @endpoint("/v2/achievements/daily/tomorrow")
    async def daily_tomorrow(self, *, data):
        """
        Get daily achievements for tomorrow from API.
        https://api.guildwars2.com/v2/achievements/daily/tomorrow
        :param data: Data from wrapper
        :return: dict
        """

        achies = {}

        # Process achievements.
        for dtype in data:
            achies[dtype] = []
            for achi in data[dtype]:
                achies[dtype].append(
                    {
                        "achievement": await self.get(achi["id"]),
                        "level": achi["level"],
                        "required_access": achi.get("required_access", None),
                    }
                )

        return achies

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
            return object_parse(data, AchievementCategory)
