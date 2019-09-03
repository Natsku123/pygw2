import requests
from ..classes import *
from ..utils import *
from ..settings import *


def get(api_key: str):
    """
    Get account from API with api key.
    :param api_key: str
    :return: Account
    """

    url = "/v2/account"

    parameters = default_parameters.copy()
    parameters['access_token'] = api_key

    r = requests.get(base_url + url, params=parameters)

    data = r.json()

    # Check for errors.
    if 'text' in data:
        raise ApiError(data['text'])

    return Account(data)


def get_achievements(api_key: str):
    """
    Get achievements progress from API with api key.
    :param api_key: str
    :return: list
    """

    url = "/v2/account/achievements"

    parameters = default_parameters
    parameters['access_token'] = api_key

    r = requests.get(base_url + url, params=parameters)

    data = r.json()

    # Check for errors.
    if 'text' in data:
        raise ApiError(data['text'])

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
            achios_t.append(achievements.get(i, json=True))

        achios = []

        # Combine lists.
        for i in achios_t:
            for n in i:
                achios.append(n)
    else:
        achios = achievements.get(completed, json=True)

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
