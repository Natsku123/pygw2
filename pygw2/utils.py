import requests
from .settings import *
from .classes import ApiError


def list_to_str(l: list, delimiter: str=","):
    """
    Convert list to string with delimiter.
    :param l: list
    :param delimiter: str=","
    :return: str
    """
    string = ""
    for item in l:
        if l.index(item) == len(l)-1:
            string += str(item)
        else:
            string += str(item) + delimiter

    return string


def endpoint(path: str):
    def decorate(func):
        def get_data(*args, **kwargs):

            path_id = ""
            parameters = default_parameters.copy()
            for key, value in kwargs.items():
                if key == "api_key":
                    parameters['access_token'] = value
                elif key == "ids":
                    if len(value) != 0:
                        parameters['ids'] = list_to_str(value)
                elif key == "item_id":
                    if not path.endswith("/"):
                        path_id = "/" + str(value)
                    else:
                        path_id = str(value)

            if path.endswith("/") and path_id == "":
                raise ApiError("ID needed.")
            r = requests.get(base_url + path + path_id, params=parameters)

            if r.status_code == 414:
                raise ApiError("Too many IDs.")
            elif r.status_code == 404:
                raise ApiError("File or directory not found: " + str(base_url + path + path_id) + " Parameters: " + str(parameters))

            data = r.json()

            # Check for errors.
            if 'text' in data:
                raise ApiError(data['text'])
            return func(data, *args, **kwargs)
        return get_data
    return decorate
