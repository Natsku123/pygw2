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
