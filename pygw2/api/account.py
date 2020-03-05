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

    # Optimizing api calls to batches of 200 ids
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

    # Get dict of item and its id
    for items in item_ids:
        items_fetched = get_item(ids=items)
        if isinstance(items_fetched, list):
            for item in items_fetched:
                items_ready[item.id] = item
        else:
            items_ready[items_fetched.id] = items_fetched

    # Combine information
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
    ids = []
    for item in data:
        ids.append(item['id'])
    items = get_item(ids=ids)
    for item in data:
        corr_item = None
        for itm_obj in items:
            if item['id'] == itm_obj.id:
                corr_item = itm_obj
                break

        # TODO change to more specific items
        inventory.append({
            "item": corr_item,
            "count": item['count'],
            "charges": item.get('charges', None),
            "skin": item.get('skin', None),
            "upgrades": item.get('upgrades', None),
            "infusions": item.get('infusions', None),
            "binding": item.get('binding', None)
        })
    return inventory


@endpoint("/v2/account/luck")
def get_luck(data, api_key: str):
    """
    Get account luck from API.
    :param data: Data from wrapper
    :param api_key:
    :return:
    """

    # TODO edit data returned to 'better' format
    return data


@endpoint("/v2/account/mailcarriers")
def get_mailcarriers(data, api_key: str):
    """
    Get unlocked mailcarriers from API.
    :param data: Data from wrapper
    :param api_key:
    :return:
    """

    # TODO resolve against /v2/mailcarriers
    return data


@endpoint("/v2/account/mapchests")
def get_mapchests(data, api_key: str):
    """
    Get mapchest unlocked since daily reset from API.
    :param data: Data from wrapper
    :param api_key:
    :return:
    """

    # TODO resolve against /v2/mapchests
    return data


@endpoint("/v2/account/masteries")
def get_masteries(data, api_key: str):
    """
    Get unlocked masteries from API.
    :param data: Data from wrapper
    :param api_key:
    :return:
    """

    # TODO resolve against /v2/masteries
    return data


@endpoint("/v2/account/mastery/points")
def get_mastery_points(data, api_key: str):
    """
    Get account mastery points from API.
    :param data: Data from wrapper
    :param api_key:
    :return:
    """

    # TODO edit data to 'better' format
    return data


@endpoint("/v2/account/materials")
def get_materials(data, api_key: str):
    """
    Get contents of material storage from API.
    :param data: Data from wrapper
    :param api_key:
    :return:
    """

    # Optimizing api calls to batches of 200 ids
    item_ids = []
    i = 0
    batch = 0
    for item in data:
        if i % 200 == 0 or i == 0:
            item_ids.append([])
            batch = batch + 1

        item_ids[batch - 1].append(item['id'])
        i = i + 1

    items_ready = {}

    # Get dict of item and its id
    for items in item_ids:
        items_fetched = get_item(ids=items)
        if isinstance(items_fetched, list):
            for item in items_fetched:
                items_ready[item.id] = item
        else:
            items_ready[items_fetched.id] = items_fetched

    items = []
    for item in data:
        items.append({
            "item": items_ready[item['id']],
            "category": item['category'],
            "binding": item.get('binding', None),
            "count": item['count']
        })

    return items


@endpoint("/v2/account/minis")
def get_minis(data, api_key: str):
    """
    Get unlocked miniatures from API.
    :param data: Data from wrapper
    :param api_key:
    :return:
    """

    # TODO resolve against /v2/minis
    return data


@endpoint("/v2/account/mounts/skins")
def get_mounts_skins(data, api_key: str):
    """
    Get unlocked skins for mounts from API.
    :param data: Data from wrapper
    :param api_key:
    :return:
    """

    # TODO resolve against /v2/mounts/skins
    return data


@endpoint("/v2/account/mounts/types")
def get_mounts_types(data, api_key: str):
    """
    Get unlocked mounts from API.
    :param data: Data from wrapper
    :param api_key:
    :return:
    """

    # TODO resolve against /v2/mounts/types
    return data


@endpoint("/v2/account/novelties")
def get_novelties(data, api_key: str):
    """
    Get unlocked novelties from API.
    :param data: Data from wrapper
    :param api_key:
    :return:
    """

    # TODO resolve against /v2/novelties
    return data


@endpoint("/v2/account/outfits")
def get_outfits(data, api_key: str):
    """
    Get unlocked outfits from API.
    :param data: Data from wrapper
    :param api_key:
    :return:
    """

    # TODO resolve against /v2/outfits
    return data


@endpoint("/v2/account/pvp/heroes")
def get_pvp_heroes(data, api_key: str):
    """
    Get unlocked PvP heroes from API.
    :param data: Data from wrapper
    :param api_key:
    :return:
    """

    # TODO resolve against /v2/pvp/heroes
    return data


@endpoint("/v2/account/raids")
def get_raids(data, api_key: str):
    """
    Get completed weekly raid encounters from API.
    :param data: Data from wrapper
    :param api_key:
    :return:
    """

    # TODO resolve against /v2/raids
    return data


@endpoint("/v2/account/recipes")
def get_recipes(data, api_key: str):
    """
    Get unlocked recipes from API.
    :param data: Data from wrapper
    :param api_key:
    :return:
    """

    # TODO resolve against /v2/recipes
    return data


@endpoint("/v2/account/skins")
def get_skins(data, api_key: str):
    """
    Get unlocked skins from API.
    :param data: Data from wrapper
    :param api_key:
    :return:
    """

    # TODO resolve against /v2/skins
    return data


@endpoint("/v2/account/titles")
def get_skins(data, api_key: str):
    """
    Get unlocked titles from API.
    :param data: Data from wrapper
    :param api_key:
    :return:
    """

    # TODO resolve against /v2/titles
    return data


@endpoint("/v2/account/wallet")
def get_wallet(data, api_key: str):
    """
    Get wallet from API.
    :param data: Data from wrapper
    :param api_key:
    :return:
    """

    # TODO resolve against /v2/currencies and 'better' format
    return data


@endpoint("/v2/account/worldbosses")
def get_worldbosses(data, api_key: str):
    """
    Get world bosses defeated since daily reset from API.
    :param data: Data from wrapper
    :param api_key:
    :return:
    """

    # TODO resolve against /v2/worldbosses
    return data


@endpoint("/v2/characters")
def get_characters(data, api_key: str):
    """
    Get characters from API. Use item_id with character's name. If no item_id
    is specified, returns all characters.
    :param data: Data from wrapper
    :param api_key:
    :return:
    """

    if isinstance(data, dict):
        return Character(data)
    else:
        return data


@endpoint("/v2/characters", subendpoint="/backstory")
def get_character_backstory(data, item_id: str, api_key: str):
    """
    Get character's backstory from API.
    :param data: Data from wrapper
    :param item_id: Character name
    :param api_key:
    :return:
    """

    # TODO resolve against /v2/backstory/answers
    return data


@endpoint("/v2/characters", subendpoint="/core")
def get_character_core(data, item_id: str, api_key: str):
    """
    Get character's core from API.
    :param data: Data from wrapper
    :param item_id: Character name
    :param api_key:
    :return:
    """

    # TODO edit to 'better' format
    return data


@endpoint("/v2/characters", subendpoint="/crafting")
def get_character_crafting(data, item_id: str, api_key: str):
    """
    Get character's crafting from API.
    :param data: Data from wrapper
    :param item_id: Character name
    :param api_key:
    :return:
    """

    # TODO edit to 'better' format
    return data


@endpoint("/v2/characters", subendpoint="/equipment")
def get_character_equipment(data, item_id: str, api_key: str):
    """
    Get character's equipment from API.
    :param data: Data from wrapper
    :param item_id: Character name
    :param api_key:
    :return:
    """

    equipment = {}
    items = []
    for item in data:
        items.append(item['id'])
    items = get_item(ids=items)
    for item in data:

        infusions = item.get('infusions', None)
        if infusions is not None:
            infusions = get_item(ids=infusions)

        upgrades = item.get('upgrades', None)
        if upgrades is not None:
            upgrades = get_item(ids=upgrades)

        # TODO resolve skin against /v2/skins
        # TODO resolve itemstats against /v2/itemstats
        # TODO resolve dyes against /v2/colors
        equipment[item['slot']] = {
            "item": items[data.index(item)],
            "infusions": infusions,
            "upgrades": upgrades,
            "skin": item.get('skin', None),
            "stats": item.get('stats', None),
            "binding": item.get('binding', None),
            "charges": item.get('charges', None),
            "bound_to": item.get('bound_to', None),
            "dyes": item.get("dyes", None)
        }
    return equipment


@endpoint("/v2/characters", subendpoint="/heropoints")
def get_character_heropoints(data, item_id: str, api_key: str):
    """
    Get character's heropoints from API.
    :param data: Data from wrapper
    :param item_id: Character name
    :param api_key:
    :return:
    """

    # TODO resolve against skill_challenges in /v2/continents
    return data


@endpoint("/v2/characters", subendpoint="/inventory")
def get_character_inventory(data, item_id: str, api_key: str):
    """
    Get character's inventory from API.
    :param data: Data from wrapper
    :param item_id: Character name
    :param api_key:
    :return:
    """

    bags_ids = []
    for bag in data:
        bags_ids.append(bag['id'])
    bags_items = get_item(ids=bags_ids)
    bags = []
    i = 0
    for bag in data:
        items_ids = []
        for item in bag['inventory']:
            if item is not None:
                items_ids.append(item['id'])

        items = get_item(ids=items_ids)

        inventory = {}
        n = 0
        for item in bag['inventory']:
            if item is not None:
                for itm_obj in items:
                    if itm_obj.id == item['id']:
                        infusions = item.get('infusions', None)
                        if infusions is not None:
                            infusions = get_item(ids=infusions)

                        upgrades = item.get('upgrades', None)
                        if upgrades is not None:
                            upgrades = get_item(ids=upgrades)

                        # TODO resolve skin against /v2/skins
                        # TODO resolve itemstats against /v2/itemstats
                        # TODO make item object more 'precise'
                        inventory[n] = {
                            "item": itm_obj,
                            "count": item['count'],
                            "infusions": infusions,
                            "upgrades": upgrades,
                            "skin": item.get('skin', None),
                            "stats": item.get('stats', None),
                            "binding": item.get('binding', None),
                            "bound_to": item.get('bound_to', None)
                        }
                        break
            else:
                inventory[n] = None
            n = n + 1
        bags.append({
            "bag": bags_items[i],
            "size": bag['size'],
            "inventory": inventory
        })
        i = i + 1
    return bags


@endpoint("/v2/characters", subendpoint="/skills")
def get_character_skills(data, item_id: str, api_key: str):
    """
    Get character's skills from API.
    :param data: Data from wrapper
    :param item_id: Character name
    :param api_key:
    :return:
    """

    # TODO resolve against /v2/skills and /v2/legends
    return data


@endpoint("/v2/characters", subendpoint="/specializations")
def get_character_specializations(data, item_id: str, api_key: str):
    """
    Get character's specializations from API.
    :param data: Data from wrapper
    :param item_id: Character name
    :param api_key:
    :return:
    """

    # TODO resolve against /v2/specializations and /v2/traits
    return data


@endpoint("/v2/characters", subendpoint="/training")
def get_character_training(data, item_id: str, api_key: str):
    """
    Get character's training from API.
    :param data: Data from wrapper
    :param item_id: Character name
    :param api_key:
    :return:
    """

    # TODO resolve against /v2/professions
    return data


@endpoint("/v2/characters", subendpoint="/sab")
def get_character_sab(data, item_id: str, api_key: str):
    """
    Get character's Super Adventure Box completion from API.
    :param data: Data from wrapper
    :param item_id: Character name
    :param api_key:
    :return:
    """

    # TODO edit to 'better' format
    return data







