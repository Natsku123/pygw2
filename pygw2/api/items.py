from ..core.models.crafting import Material, Recipe
from ..core.models.general import Finisher, ItemStat, Skin
from ..core.models.items import Item, Glider, Mailcarrier
from ..core.models.pvp import PvpAmulet
from ..utils import endpoint, object_parse, LazyLoader

from ..api.misc import MiscellaneousApi


misc_api = MiscellaneousApi()


class ItemsApi:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        pass

    @endpoint("/v2/items", has_ids=True)
    async def get(self, *, data, ids: list = None):
        """
        Get items from API by list of IDs or one ID.
        None returns all item IDs.
        https://api.guildwars2.com/v2/items
        :param data: Data from wrapper
        :param ids: list
        :return: list
        """

        # Return list of ids.
        if ids is None:
            return data

        # Return list of Achievements.
        else:
            return object_parse(data, Item)

    @endpoint("/v2/finishers", has_ids=True)
    async def finishers(self, *, data, ids: list = None):
        """
        Get finishers from API by list of IDs or one ID.
        None returns all IDs.
        :param data: Data from wrapper
        :param ids: list
        :return: list
        """

        if ids is None:
            return data

        else:
            return object_parse(data, Finisher)

    @endpoint("/v2/itemstats", has_ids=True)
    async def itemstats(self, *, data, ids: list = None):
        """
        Get itemstats from API by list of IDs or one ID.
        None returns all IDs.
        :param data:
        :param ids:
        :return:
        """

        if ids is None:
            return data
        else:
            return object_parse(data, ItemStat)

    @endpoint("/v2/materials", has_ids=True)
    async def materials(self, *, data, ids: list = None):
        """
        Get materials from API by list of IDs or one ID.
        None returns all IDs.
        :param data:
        :param ids:
        :return:
        """

        if ids is None:
            return data
        else:
            return object_parse(data, Material)

    @endpoint("/v2/pvp/amulets", has_ids=True)
    async def pvp_amulets(self, *, data, ids: list = None):
        """
        Get Pvp amulets from API by list of IDs or one ID.
        None returns all IDs.
        :param data:
        :param ids:
        :return:
        """

        if ids is None:
            return data
        else:
            return object_parse(data, PvpAmulet)

    @endpoint("/v2/recipes", has_ids=True)
    async def recipes(self, *, data, ids: list = None):
        """
        Get Recipes from API by list of IDs or one ID.
        None returns all IDs.
        :param data:
        :param ids:
        :return:
        """
        if ids is None:
            return data
        else:
            return object_parse(data, Recipe)

    @endpoint("/v2/recipes/search", is_search=True)
    async def search_recipes(self, *, data, input=None, output=None):
        """
        Search for recipes as ingredient (input) or as result (output).
        :param output: as result
        :param input: as ingredient
        :param data:
        :return:
        """
        if data:
            return await self.recipes(*data)
        else:
            return data

    @endpoint("/v2/skins", has_ids=True)
    async def skins(self, *, data, ids: list = None):
        """
        Get Skins from API by list of IDs or one ID.
        None returns all IDs.
        :param data:
        :param ids:
        :return:
        """
        if ids is None:
            return data
        else:
            return object_parse(data, Skin)

    @endpoint("/v2/gliders", has_ids=True)
    async def gliders(self, *, data, ids: list = None):
        """
        Get gliders from API
        :param data: data from wrapper
        :param ids: list of IDs
        :return: list of gliders
        """
        if ids is None:
            return data

        for g in data:
            g["unlock_items_"] = LazyLoader(self.get, *g["unlock_items"])
            g["default_dyes_"] = LazyLoader(misc_api.colors, *g["default_dyes"])

        return object_parse(data, Glider)

    @endpoint("/v2/mailcarriers", has_ids=True)
    async def mailcarriers(self, *, data, ids: list = None):
        """
        Get mailcarriers from API
        :param data: data from wrapper
        :param ids: list of IDs
        :return: list of mailcarriers
        """

        if ids is None:
            return data

        for m in data:
            m["unlock_items_"] = LazyLoader(self.get, *m["unlock_items"])

        return object_parse(data, Mailcarrier)
