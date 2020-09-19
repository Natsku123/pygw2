from pygw2.core.classes import *
from ..utils import endpoint


class AchievementsApi:
    def __init__(self):
        pass

    @endpoint("/v2/achievements", has_ids=True)
    def get(self, *, data, ids: list = None):
        """
        Get achievements from API by list of IDs.
        https://api.guildwars2.com/v2/achievements
        :param data: Data from endpoint wrapper
        :param ids: list=[]
        :return: list
        """

        # Return list of ids.
        if ids is None:
            return data

        # Return list of Achievements.
        else:
            if isinstance(data, dict):
                return Achievement(**data)
            elif isinstance(data, list):

                achis = []
                for achi in data:
                    achis.append(Achievement(**achi))

                if len(achis) > 1:
                    return achis
                else:
                    return achis[0]

    @endpoint("/v2/achievements/daily")
    def get_dailies(self, *, data):
        """
        Get daily achievements from API.
        https://api.guildwars2.com/v2/achievements/daily
        :param data: Data from wrapper
        :return: dict
        """
        return DailyAchievements(**data)

    @endpoint("/v2/achievements/daily/tomorrow")
    def get_dailies_tomorrow(self, *, data):
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
                achies[dtype].append({
                    "achievement": self.get(ids=[achi['id']]),
                    "level": achi['level'],
                    "required_access": achi.get('required_access', None)
                })

        return achies

    @endpoint("/v2/achievements/groups", has_ids=True)
    def get_groups(self, *, data, ids: list = None):
        """
        Get groups for achievements from API by list of IDs.
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
            groups = []
            for group in data:
                groups.append(AchievementGroup(**group))
            return groups

    @endpoint("/v2/achievements/groups/")
    def get_group(self, *, data):
        """
        Get group of achievements from API with ID.
        https://api.guildwars2.com/v2/achievements/groups/{g_id}
        :param data: Data from wrapper
        :return:
        """

        # Check for errors
        if 'text' in data:
            raise ApiError(data['text'])

        return AchievementGroup(**data)

    @endpoint("/v2/achievements/categories", has_ids=True)
    def get_categories(self, *, data, ids: list = None):
        """
        Get categories for achievements from API by list of IDs.
        https://api.guildwars2.com/v2/achievements/categories
        :param data: Data from wrapper
        :param ids: list=[]
        :return: list
        """

        # Check for errors
        if 'text' in data:
            raise ApiError(data['text'])

        # Return list of group ids.
        if ids is None:
            return data

        # Return list of groups.
        else:
            groups = []
            for group in data:
                print(data)
                groups.append(AchievementCategory(**group))
            return groups

    @endpoint("/v2/achievements/categories/")
    def get_category(self, *, data):
        """
        Get category of achievements from API with ID.
        https://api.guildwars2.com/v2/achievements/categories/{id}
        :param data: Data from wrapper
        :return:
        """

        # Check for errors
        if 'text' in data:
            raise ApiError(data['text'])

        return AchievementCategory(**data)
