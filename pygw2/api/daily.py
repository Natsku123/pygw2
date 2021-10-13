from ..core.models.general import DailyCrafting, DailyMapChest, DailyWorldBoss
from ..utils import endpoint, object_parse


class DailyApi:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        pass

    @endpoint("/v2/dailycrafting", has_ids=True)
    async def crafting(self, *, data, ids: list = None):
        """
        Fetch daily craftable items by ID(s).
        None returns all time-gated crafting items.
        :param data:
        :param ids:
        :return:
        """
        if ids is None:
            return data
        return object_parse(data, DailyCrafting)

    @endpoint("/v2/mapchests", has_ids=True)
    async def mapchests(self, *, data, ids: list = None):
        """
        Fetch daily hero's choice chests by ID(s).
        None returns all time-gated hero's choice chests.
        :param data:
        :param ids:
        :return:
        """
        if ids is None:
            return data
        return object_parse(data, DailyMapChest)

    @endpoint("/v2/worldbosses", has_ids=True)
    async def worldbosses(self, *, data, ids: list = None):
        """
        Fetch daily world bosses by ID(s).
        None returns all world bosses.
        :param data:
        :param ids:
        :return:
        """
        if ids is None:
            return data
        return object_parse(data, DailyWorldBoss)
