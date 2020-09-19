from ..utils import endpoint
from pygw2.core.classes import Item, Finisher, Itemstat, Material, PvpAmulet


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
            if isinstance(data, dict):
                return Item(**data)
            elif isinstance(data, list):

                items = []
                print(data)
                for item in data:
                    items.append(Item(**item))

                if len(items) > 1:
                    return items
                else:
                    return items[0]

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
            finishers = []
            for finisher in data:
                finishers.append(Finisher(**finisher))

            if len(finishers) > 1:
                return finishers
            else:
                return finishers[0]

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
            itemstats = []
            for itemstat in data:
                itemstats.append(Itemstat(**itemstat))

            if len(itemstats) > 1:
                return itemstats
            else:
                return itemstats[0]

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
            materials = []
            for material in data:
                materials.append(Material(**material))

            if len(materials) > 1:
                return materials
            else:
                return materials[0]

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
            amulets = []
            for amulet in data:
                amulets.append(PvpAmulet(**amulet))

            if len(amulets) > 1:
                return amulets
            else:
                return amulets[0]
