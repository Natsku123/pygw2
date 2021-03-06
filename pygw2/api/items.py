from ..utils import endpoint, object_parse
from pygw2.core.classes import Item, Finisher, Itemstat, Material, PvpAmulet, \
    Recipe, Skin


class ItemsApi:
    def __init__(self):
        pass

    @endpoint("/v2/items", has_ids=True)
    def get(self, *, data, ids: list = None):
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
    def finishers(self, *, data, ids: list = None):
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
    def itemstats(self, *, data, ids: list = None):
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
            return object_parse(data, Itemstat)

    @endpoint("/v2/materials", has_ids=True)
    def materials(self, *, data, ids: list = None):
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
    def pvp_amulets(self, *, data, ids: list = None):
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
    def recipes(self, *, data, ids: list = None):
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
    def search_recipes(self, *, data, input=None, output=None):
        """
        Search for recipes as ingredient (input) or as result (output).
        :param output: as result
        :param input: as ingredient
        :param data:
        :return:
        """
        if data:
            return self.recipes(*data)
        else:
            return data

    @endpoint("/v2/skins", has_ids=True)
    def skins(self, *, data, ids: list = None):
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
