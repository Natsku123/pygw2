from ..utils import endpoint
from pygw2.core.classes import Item


class ItemsApi:
    def __init__(self):
        pass

    @endpoint("/v2/items")
    def get(self, data, ids: list = [], json=False):
        """
        Get items from API by list of IDs or one ID.
        None returns all item IDs.
        https://api.guildwars2.com/v2/items
        :param data: Data from wrapper
        :param ids: list
        :param json:
        :return: list
        """

        # Return list of ids.
        if len(ids) == 0 or json:
            return data

        # Return list of Achievements.
        else:
            items = []
            for item in data:

                items.append(Item(**item))

            if len(items) > 1:
                return items
            else:
                return items[0]
