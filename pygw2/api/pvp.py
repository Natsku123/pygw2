from typing import List, Union

from ..utils import endpoint, object_parse, LazyLoader
from ..core.models.pvp import PvpRank, PvpSeason, PvpLeaderboard, PvpHero


class PvpLeaderboardsApi:
    _instances = {}

    def __new__(cls, season_id: str, *args, api_key: str = "", **kwargs):
        if (api_key, season_id) not in cls._instances:
            cls._instances[(api_key, season_id)] = super().__new__(cls, *args, **kwargs)
        return cls._instances[(api_key, season_id)]

    def __init__(self, season_id: str, *, api_key: str = ""):
        self.api_key: str = api_key
        self.season_id = season_id

    @endpoint("/v2/pvp/seasons", subendpoint="/leaderboards/ladder/eu")
    async def ladder_eu(self, *, data) -> List[PvpLeaderboard]:
        """
        Get leaderboards for EU ladder from API
        :param data: data from wrapper
        :return: list
        """

        return object_parse(data, PvpLeaderboard)

    @endpoint("/v2/pvp/seasons", subendpoint="/leaderboards/ladder/na")
    async def ladder_na(self, *, data) -> List[PvpLeaderboard]:
        """
        Get leaderboards for NA ladder from API
        :param data: data from wrapper
        :return: list
        """

        return object_parse(data, PvpLeaderboard)

    @endpoint("/v2/pvp/seasons", subendpoint="/leaderboards/legendary/eu")
    async def legendary_eu(self, *, data) -> List[PvpLeaderboard]:
        """
        Get leaderboards for EU legendary from API
        :param data: data from wrapper
        :return: list
        """

        return object_parse(data, PvpLeaderboard)

    @endpoint("/v2/pvp/seasons", subendpoint="/leaderboards/legendary/na")
    async def legendary_na(self, *, data) -> List[PvpLeaderboard]:
        """
        Get leaderboards for NA legendary from API
        :param data: data from wrapper
        :return: list
        """

        return object_parse(data, PvpLeaderboard)

    @endpoint("/v2/pvp/seasons", subendpoint="/leaderboards/guild/eu")
    async def guild_eu(self, *, data) -> List[PvpLeaderboard]:
        """
        Get leaderboards for EU guild from API
        :param data: data from wrapper
        :return: list
        """

        return object_parse(data, PvpLeaderboard)

    @endpoint("/v2/pvp/seasons", subendpoint="/leaderboards/guild/na")
    async def guild_eu(self, *, data) -> List[PvpLeaderboard]:
        """
        Get leaderboards for NA guild from API
        :param data: data from wrapper
        :return: list
        """

        return object_parse(data, PvpLeaderboard)


class PvpApi:
    _instances = {}

    def __new__(cls, *args, api_key: str = "", **kwargs):
        if api_key not in cls._instances:
            cls._instances[api_key] = super().__new__(cls, *args, **kwargs)
        return cls._instances[api_key]

    def __init__(self, *, api_key: str = ""):
        self.api_key: str = api_key
        self._leaderboards = PvpLeaderboardsApi

    @endpoint("/v2/pvp/ranks", has_ids=True)
    async def ranks(self, *, data, ids: list = None) -> List[Union[PvpRank, int, str]]:
        """
        Get Pvp ranks from API by list of IDs or one ID.
        :param data: data from wrapper
        :param ids: list of IDs
        :return: list
        """

        if ids is None:
            return data

        return object_parse(data, PvpRank)

    @endpoint("/v2/pvp/seasons", has_ids=True)
    async def seasons(
        self, *, data, ids: list = None
    ) -> List[Union[PvpSeason, int, str]]:
        """
        Get Pvp seasons from API by list of IDs or one iD.
        :param data: data from wrapper
        :param ids: list of IDs
        :return: list
        """

        if ids is None:
            return data

        return object_parse(data, PvpSeason)

    @endpoint("/v2/pvp/heroes", has_ids=True)
    async def heroes(self, *, data, ids: list = None) -> List[Union[PvpHero, int, str]]:
        """
        Get Pvp heroes from API
        :param data: data from wrapper
        :param ids: lsit of IDs
        :return: list
        """

        if ids is None:
            return data

        from ..api.items import ItemsApi

        items_api = ItemsApi(api_key=self.api_key)

        for h in data:
            for skin in h["skins"]:
                if skin["unlock_items"]:
                    skin["unlock_items_"] = LazyLoader(
                        items_api.get, *skin["unlock_items"]
                    )

        return object_parse(data, PvpHero)

    def leaderboards(self, season_id: str) -> PvpLeaderboardsApi:
        return self._leaderboards(season_id, api_key=self.api_key)
