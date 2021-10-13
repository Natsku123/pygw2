from typing import List, Union

from ..utils import endpoint, object_parse
from ..core.models.misc import (
    Color,
    Currency,
    Dungeon,
    File,
    Quaggan,
    Mini,
    Novelty,
    Raid,
    Title,
    World,
)


class MiscellaneousApi:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.api_key: str = ""

    def setup(self, api_key: str):
        self.api_key = api_key

    @endpoint("/v2/build")
    async def build(self, *, data):
        """
        Get current build id from API
        :param data: Data from wrapper
        :return:
        """
        return data

    @endpoint("/v2/colors", has_ids=True)
    async def colors(self, *, data, ids: list = None) -> List[Union[Color, int, str]]:
        """
        Get colors from API by list of IDs or one ID.
        :param data: Data from wrapper
        :param ids: List of IDs
        :return: list
        """

        # Return ids
        if ids is None:
            return data

        # Return object(s)
        return object_parse(data, Color)

    @endpoint("/v2/currencies", has_ids=True)
    async def currencies(
        self, *, data, ids: list = None
    ) -> List[Union[Currency, int, str]]:
        """
        Get currencies from API by list of IDs or one ID.
        :param data: Data from wrapper
        :param ids: List of IDs
        :return: list
        """

        # Return ids
        if ids is None:
            return data

        # Return object(s)
        return object_parse(data, Currency)

    @endpoint("/v2/dungeons", has_ids=True)
    async def dungeons(
        self, *, data, ids: list = None
    ) -> List[Union[Dungeon, int, str]]:
        """
        Get dungeons from API by list of IDs or one ID.
        :param data: Data from wrapper
        :param ids: List of IDs
        :return: list
        """

        if ids is None:
            return data

        return object_parse(data, Dungeon)

    @endpoint("/v2/files", has_ids=True)
    async def files(self, *, data, ids: list = None) -> List[Union[File, int, str]]:
        """
        Get files from API by list of IDs or one ID.
        :param data: Data from wrapper
        :param ids: List of IDs
        :return: list
        """

        if ids is None:
            return data

        return object_parse(data, File)

    @endpoint("/v2/quaggans", has_ids=True)
    async def quaggans(
        self, *, data, ids: list = None
    ) -> List[Union[Quaggan, int, str]]:
        """
        Get quaggan images from API by list of IDs or one ID.
        :param data: Data from wrapper
        :param ids: List of IDs
        :return: list
        """

        if ids is None:
            return data

        return object_parse(data, Quaggan)

    @endpoint("/v2/minis", has_ids=True)
    async def minis(self, *, data, ids: list = None) -> List[Union[Mini, int, str]]:
        """
        Get minis from API by list of IDs or one ID.
        :param data: Data from wrapper
        :param ids: List of IDs
        :return: list
        """

        from .items import ItemsApi

        items_api = ItemsApi()

        if ids is None:
            return data

        for mini in data:
            mini["item"] = await items_api.get(mini["item_id"])

        return object_parse(data, Mini)

    @endpoint("/v2/novelties", has_ids=True)
    async def novelties(
        self, *, data, ids: list = None
    ) -> List[Union[Novelty, int, str]]:
        """
        Get novelties from API by list of IDs or one ID.
        :param data: Data from wrapper
        :param ids: List of IDs
        :return: list
        """
        from .items import ItemsApi

        items_api = ItemsApi()

        if ids is None:
            return data

        for nov in data:
            nov["unlock_item"] = await items_api.get(*nov["unlock_item"])

        return object_parse(data, Novelty)

    @endpoint("/v2/raids", has_ids=True)
    async def raids(self, *, data, ids: list = None) -> List[Union[Raid, int, str]]:
        """
        Get raids from API by list of IDs or one ID.
        :param data: Data from wrapper
        :param ids: List of IDs
        :return: list
        """

        if ids is None:
            return data

        return object_parse(data, Raid)

    @endpoint("/v2/titles", has_ids=True)
    async def titles(self, *, data, ids: list = None) -> List[Union[Title, int, str]]:
        """
        Get titles from API by list of IDs or one ID.
        :param data: Data from wrapper
        :param ids: List of IDs
        :return: list
        """

        if ids is None:
            return data

        return object_parse(data, Title)

    @endpoint("/v2/worlds", has_ids=True)
    async def worlds(self, *, data, ids: list = None) -> List[Union[World, int, str]]:
        """
        Get worlds from API by list of IDs or one ID.
        :param data: Data from wrapper
        :param ids: List of IDs
        :return: list
        """

        if ids is None:
            return data

        for world in data:
            world["region"] = int(str(world["id"])[0])

        return object_parse(data, World)
