import requests
from ..utils import *
from ..classes import *
from ..settings import *


@endpoint("/v2/items")
def get(data, ids: list, json=False):
    """
    Get items from API by list of IDs or one ID.
    None returns all item IDs.
    https://api.guildwars2.com/v2/items
    :param data: Data from wrapper
    :param ids: list
    :return: list
    """
    url = "/v2/items"
    parameters = default_parameters.copy()
    #one = False

    #if isinstance(ids, list) and len(ids) != 0:
    #    ids = list_to_str(ids)
    #    parameters['ids'] = ids
    #elif isinstance(ids, int):
    #    one = True
    #    url += "/" + str(ids)

    # Return list of ids.
    if len(ids) == 0 or json:
        return data

    # Return list of Achievements.
    else:
        items = []
        for item in data:

            # Convert data to nice format
            item_type = item['type']
            del item['type']
            if 'details' in item:
                item_details = item['details']
                del item['details']
                item.update(item_details)

                # Add corresponding item object
                if item_type == "Armor":
                    items.append(ArmorItem(item))
                elif item_type == "Back":
                    items.append(BackItem(item))
                elif item_type == "Bag":
                    items.append(Bag(item))
                elif item_type == "Consumable":
                    items.append(ConsumableItem(item))
                elif item_type == "Container":
                    items.append(ContainerItem(item))
                elif item_type == "Gathering":
                    items.append(GatheringToolItem(item))
                elif item_type == "Gizmo":
                    items.append(GizmoItem(item))
                elif item_type == "MiniPet":
                    items.append(MiniatureItem(item))
                elif item_type == "Tool":
                    items.append(SalvageKitItem(item))
                elif item_type == "Trinket":
                    items.append(TrinketItem(item))
                elif item_type == "UpgradeComponent":
                    items.append(UpgradeComponentItem(item))
                elif item_type == "Weapon":
                    items.append(WeaponItem(item))
                else:
                    items.append(Item(item))
            else:
                items.append(Item(item))

            return items
        #else:
        #    item = data
        #    # Convert data to nice format
        #    item_type = item['type']
        #    del item['type']
        #    if 'details' in item:
        #        item_details = item['details']
        #        del item['details']
        #        item.update(item_details)

                # Return corresponding item object
        #        if item_type == "Armor":
        #            return ArmorItem(item)
        #        elif item_type == "Back":
        #            return BackItem(item)
        #        elif item_type == "Bag":
        #            return Bag(item)
        #        elif item_type == "Consumable":
        #            return ConsumableItem(item)
        #        elif item_type == "Container":
        #            return ContainerItem(item)
        #        elif item_type == "Gathering":
        #            return GatheringToolItem(item)
        #        elif item_type == "Gizmo":
        #            return GizmoItem(item)
        #        elif item_type == "MiniPet":
        #            return MiniatureItem(item)
        #        elif item_type == "Tool":
        #            return SalvageKitItem(item)
        #        elif item_type == "Trinket":
        #            return TrinketItem(item)
        #        elif item_type == "UpgradeComponent":
        #            return UpgradeComponentItem(item)
        #        elif item_type == "Weapon":
        #            return WeaponItem(item)
        #        else:
        #            return Item(item)
        #    else:
        #        return Item(item)
