from typing import List, Union

from ..utils import endpoint, object_parse, LazyLoader
from ..api.items import ItemsApi
from ..core.models.pvp import PvpRank, PvpSeason, PvpLeaderboard, PvpHero

items_api = ItemsApi()


class PvpLeaderboardsApi:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, season_id: str):
        self.api_key: str = ""
        self.season_id = season_id

    def setup(self, api_key: str):
        self.api_key = api_key

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
    async def legendary_eu(self, *, data) -> List[PvpLeaderboard]:
        """
        Get leaderboards for EU guild from API
        :param data: data from wrapper
        :return: list
        """

        return object_parse(data, PvpLeaderboard)

    @endpoint("/v2/pvp/seasons", subendpoint="/leaderboards/guild/na")
    async def legendary_na(self, *, data) -> List[PvpLeaderboard]:
        """
        Get leaderboards for NA guild from API
        :param data: data from wrapper
        :return: list
        """

        return object_parse(data, PvpLeaderboard)


class PvpApi:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.api_key: str = ""
        self._leaderboards = PvpLeaderboardsApi

    def setup(self, api_key: str):
        self.api_key = api_key

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

        for h in data:
            for skin in h["skins"]:
                if skin["unlock_items"]:
                    skin["unlock_items_"] = LazyLoader(
                        items_api.get, *skin["unlock_items"]
                    )

        return object_parse(data, PvpHero)

    def leaderboards(self, season_id: str):
        return self._leaderboards(season_id)
