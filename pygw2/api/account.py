from .items import get as get_item
from ..classes import *
from ..utils import *


@endpoint("/v2/account")
def get(data, api_key: str):
    """
    Get account from API with api key.
    :param data: Data from wrapper
    :param api_key: str
    :return: Account
    """

    return Account(data)


@endpoint("/v2/account/achievements")
def get_achievements(data, api_key: str):
    """
    Get achievements progress from API with api key.
    :param data: Data from wrapper
    :param api_key: str
    :return: list
    """

    achis = []

    # Get all achievement ids
    completed = []
    ids = [i['id'] for i in data]

    all_ids = achievements.get()

    # Spare all ids that can be found and there is progress
    for ido in all_ids:
        if ido in ids:
            completed.append(ido)

    # Cut list into several 'packages' since endpoint supports max 200 ids.
    package_size = 200

    if len(completed) > package_size:
        new_com = []

        # Cut to 200 ids per get.
        for i in range(0, package_size, len(completed)):
            if len(completed) - i >= package_size:
                new_com.append(completed[i:package_size+i])
            else:
                new_com.append(completed[i:len(completed)])

        achios_t = []

        # Get all ids.
        for i in new_com:
            achios_t.append(achievements.get(ids=i, json=True))

        achios = []

        # Combine lists.
        for i in achios_t:
            for n in i:
                achios.append(n)
    else:
        achios = achievements.get(ids=completed, json=True)

    # Match all achievement objects
    for achi in data:
        found = False
        for achio in achios:
            if achi['id'] == achio['id']:
                found = True
                achis.append(AchievementProgress(achi, achio))
                break
        if not found:
            achis.append(AchievementProgress(achi, {}))

    return achis


@endpoint("/v2/account/bank")
def get_bank(data, api_key: str):
    """
    Get bank data from API with api key.
    :param data: Data from wrapper
    :param api_key:
    :return:
    """

    bank = []

    # Blacklist of purged IDs
    blacklist = [45022, 45023, 45024, 45025]

    # Optimizing api calls to batches of ids
    item_ids = []
    i = 0
    batch = 0
    for item in data:
        if item is not None and item['id'] not in blacklist:
            if i % 200 == 0 or i == 0:
                item_ids.append([])
                batch = batch + 1

            item_ids[batch-1].append(item['id'])
            i = i + 1

    items_ready = {}
    for items in item_ids:
        items_fetched = get_item(ids=items)
        if isinstance(items_fetched, list):
            for item in items_fetched:
                items_ready[item.id] = item
        else:
            items_ready[items_fetched.id] = items_fetched
    for item in data:
        # TODO create more accurate item object

        if item is None:
            bank.append(None)
        elif not item['id'] in blacklist:
            bank.append({
                "item": items_ready[item['id']],
                "count": item['count'],
                "charges": item.get('charges', None),
                "skin": item.get('skin', None),
                "upgrades": item.get('upgrades', None),
                "infusions": item.get('infusions', None),
                "binding": item.get('binding', None),
                "bound_to": item.get('bound_to', None)
            })
        else:
            bank.append({
                "item_id": item['id'],
                "count": item['count'],
                "charges": item.get('charges', None),
                "skin": item.get('skin', None),
                "upgrades": item.get('upgrades', None),
                "infusions": item.get('infusions', None),
                "binding": item.get('binding', None),
                "bound_to": item.get('bound_to', None)
            })

    return bank


@endpoint("/v2/account/dailycrafting")
def get_dailycrafting(data, api_key: str):
    """
    Get crafted time-gated items from API.
    :param data: Data from wrapper
    :param api_key:
    :return:
    """
    # TODO resolve against /v2/dailycrafting
    return data


@endpoint("/v2/account/dungeons")
def get_dungeons(data, api_key: str):
    """
    Get completed dungeon paths after last daily reset from API.
    :param data: Data from wrapper
    :param api_key:
    :return:
    """
    # TODO resolve against /v2/dungeons
    return data


@endpoint("/v2/account/dyes")
def get_dyes(data, api_key: str):
    """
    Get unlocked dyes from API.
    :param data: Data from wrapper
    :param api_key:
    :return:
    """

    # TODO resolve against /v2/colors
    return data


@endpoint("/v2/account/finishers")
def get_finishers(data, api_key: str):
    """
    Get unlocked finishers from API.
    :param data: Data from wrapper
    :param api_key:
    :return:
    """

    finishers = []
    for finisher in data:
        # TODO change finisher_id to finisher with resolve against /v2/finishers
        finishers.append({
            "finisher_id": finisher['id'],
            "permanent": finisher['permanent'],
            "quantity": finisher.get('quantity', None)
        })
    return finishers


@endpoint("/v2/account/gliders")
def get_gliders(data, api_key: str):
    """
    Get unlocked gliders from API.
    :param data: Data from wrapper
    :param api_key:
    :return:
    """

    # TODO resolve against /v2/gliders
    return data


@endpoint("/v2/account/home/cats")
def get_home_cats(data, api_key: str):
    """
    Get unlocked home instance cats from API.
    :param data: Data from wrapper
    :param api_key:
    :return:
    """

    # TODO resolve against /v2/cats
    return data


@endpoint("/v2/account/home/nodes")
def get_home_nodes(data, api_key: str):
    """
    Get unlocked home instance nodes from API.
    :param data: Data from wrapper
    :param api_key:
    :return:
    """

    # TODO resolve against /v2/home/nodes
    return data


@endpoint("/v2/account/inventory")
def get_inventory(data, api_key: str):
    """
    Get shared inventory from API.
    :param data: Data from wrapper
    :param api_key:
    :return:
    """
    inventory = []
    for item in data:
        # TODO change to more specific items
        inventory.append({
            "item": get_item(ids=[item['id']]),
            "count": item['count'],
            "charges": item.get('charges', None),
            "skin": item.get('skin', None),
            "upgrades": item.get('upgrades', None),
            "infusions": item.get('infusions', None),
            "binding": item.get('binding', None)
        })
    return inventory



