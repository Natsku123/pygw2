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
    for item in data:
        # TODO create more accurate item object

        # TODO remove blacklist once API responds to these
        blacklist = [45022, 45023, 45024, 45025]

        if item is None:
            bank.append(None)
        elif not item['id'] in blacklist:
            bank.append({
                "item": get_item(ids=[item['id']]),
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
