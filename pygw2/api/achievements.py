import requests
from ..utils import *
from ..classes import *
from ..settings import *


def get(ids: list=[], json=False):
    """
    Get achievements from API by list of IDs.
    https://api.guildwars2.com/v2/achievements
    :param ids: list=[]
    :return: list
    """
    url = "/v2/achievements"
    parameters = default_parameters.copy()

    if len(ids) != 0:
        ids = list_to_str(ids)
        parameters['ids'] = ids

    r = requests.get(base_url + url, params=parameters)

    if r.status_code == 414:
        raise ApiError("Too many IDs.")
    elif r.status_code == 404:
        raise ApiError("File or directory not found")

    data = r.json()

    # Check for errors.
    if 'text' in data:
        raise ApiError(data['text'])

    # Return list of ids.
    if len(ids) == 0 or json:
        return data

    # Return list of Achievements.
    else:
        achis = []
        for achi in data:
            achis.append(Achievement(achi))
        return achis


def get_dailies():
    """
    Get daily achievements from API.
    https://api.guildwars2.com/v2/achievements/daily
    :return: dict
    """

    url = "/v2/achievements/daily"
    parameters = default_parameters.copy()

    r = requests.get(base_url + url, params=parameters)

    achies = {}

    # Process achievements.
    for dtype in r.json():
        achies[dtype] = []
        for achi in r.json()[dtype]:
            achies[dtype].append({
                "achievement": get([achi['id']]),
                "level": achi['level'],
                "required_access": achi.get('required_access', None)
            })

    return achies


def get_dailies_tomorrow():
    """
    Get daily achievements for tomorrow from API.
    https://api.guildwars2.com/v2/achievements/daily/tomorrow
    :return: dict
    """
    url = "/v2/achievements/daily/tomorrow"
    parameters = default_parameters.copy()

    r = requests.get(base_url + url, params=parameters)

    achies = {}

    # Process achievements.
    for dtype in r.json():
        achies[dtype] = []
        for achi in r.json()[dtype]:
            achies[dtype].append({
                "achievement": get([achi['id']]),
                "level": achi['level'],
                "required_access": achi.get('required_access', None)
            })

    return achies


def get_groups(ids: list=[]):
    """
    Get groups for achievements from API by list of IDs.
    https://api.guildwars2.com/v2/achievements/groups
    :param ids: list=[]
    :return: list
    """
    url = "/v2/achievements/groups"
    parameters = default_parameters.copy()

    if len(ids) != 0:
        ids = list_to_str(ids)
        parameters['ids'] = ids

    r = requests.get(base_url + url, params=parameters)

    data = r.json()

    # Check for errors
    if 'text' in data:
        raise ApiError(data['text'])

    # Return list of group ids.
    if len(ids) == 0:
        return data

    # Return list of groups.
    else:
        groups = []
        for group in data:
            groups.append(AchievementGroup(group))
        return groups


def get_group(g_id: str):
    """
    Get group of achievements from API with ID.
    https://api.guildwars2.com/v2/achievements/groups/{g_id}
    :param g_id:
    :return:
    """
    url = "/v2/achievements/groups/"
    parameters = default_parameters.copy()

    r = requests.get(base_url + url + g_id, params=parameters)

    data = r.json()

    # Check for errors
    if 'text' in data:
        raise ApiError(data['text'])

    return AchievementGroup(data)


def get_categories(ids: list=[]):
    """
    Get categories for achievements from API by list of IDs.
    https://api.guildwars2.com/v2/achievements/categories
    :param ids: list=[]
    :return: list
    """
    url = "/v2/achievements/categories"
    parameters = default_parameters.copy()

    if len(ids) != 0:
        ids = list_to_str(ids)
        parameters['ids'] = ids

    r = requests.get(base_url + url, params=parameters)

    data = r.json()

    # Check for errors
    if 'text' in data:
        raise ApiError(data['text'])

    # Return list of group ids.
    if len(ids) == 0:
        return data

    # Return list of groups.
    else:
        groups = []
        for group in data:
            print(data)
            groups.append(AchievementCategory(group))
        return groups


def get_category(c_id: int):
    """
    Get category of achievements from API with ID.
    https://api.guildwars2.com/v2/achievements/categories/{g_id}
    :param c_id:
    :return:
    """
    url = "/v2/achievements/categories/"
    parameters = default_parameters.copy()

    r = requests.get(base_url + url + str(c_id), params=parameters)

    data = r.json()

    # Check for errors
    if 'text' in data:
        raise ApiError(data['text'])

    return AchievementCategory(data)
