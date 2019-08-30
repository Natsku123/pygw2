import requests
from .utils import *
from .classes import *

api_version = "2019-08-29T00:00:00Z"

base_url = "https://api.guildwars2.com"

parameters = {
    "v": api_version
}


def get_achievements(ids: list=[]):
    """
    Get achievements from API by list of IDs.
    https://api.guildwars2.com/v2/achievements
    :param ids: list=[]
    :return: list
    """
    url = "/v2/achievements"

    if len(ids) != 0:
        ids = list_to_str(ids)
        parameters['ids'] = ids

    r = requests.get(base_url + url, params=parameters)

    data = r.json()
    if len(ids) == 0:
        return data
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

    r = requests.get(base_url + url, params=parameters)

    achievements = {}

    for dtype in r.json():
        achievements[dtype] = []
        for achi in r.json()[dtype]:
            achievements[dtype].append({
                "achievement": get_achievements([achi['id']]),
                "level": achi['level'],
                "required_access": achi.get('required_access', None)
            })

    return achievements


def get_dailies_tomorrow():
    """
    Get daily achievements for tomorrow from API.
    https://api.guildwars2.com/v2/achievements/daily/tomorrow
    :return: dict
    """
    url = "/v2/achievements/daily/tomorrow"

    r = requests.get(base_url + url, params=parameters)

    achievements = {}

    for dtype in r.json():
        achievements[dtype] = []
        for achi in r.json()[dtype]:
            achievements[dtype].append({
                "achievement": get_achievements([achi['id']]),
                "level": achi['level'],
                "required_access": achi.get('required_access', None)
            })

    return achievements
