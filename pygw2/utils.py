import requests
from .settings import *
from .core import classes


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


def endpoint(path: str, subendpoint: str = ""):
    """
    Endpoint wrapper
    :param path: Endpoint path
    :param subendpoint: Path of sub-endpoint
    :return:
    """
    def decorate(func):
        def get_data(self, *args, **kwargs):
            path_id = ""
            parameters = default_parameters.copy()

            if hasattr(self, "api_key") and self.api_key and self.api_key != "":
                parameters['access_token'] = getattr(self, "api_key")

            if hasattr(self, "character_id") and self.character_id:
                if not path.endswith("/"):
                    path_id = "/" + str(self.character_id)
                else:
                    path_id = str(self.character_id)

            for key, value in kwargs.items():
                if key == "ids":
                    if len(value) != 0:
                        parameters['ids'] = list_to_str(value)
                elif key == "item_id" and path_id == "":
                    if not path.endswith("/"):
                        path_id = "/" + str(value)
                    else:
                        path_id = str(value)

            if path.endswith("/") and path_id == "":
                raise classes.ApiError("ID needed.")
            r = requests.get(
                base_url + path + path_id + subendpoint,
                params=parameters
            )

            if r.status_code == 414:
                raise classes.ApiError("Too many IDs.")
            elif r.status_code == 404:
                raise classes.ApiError("File or directory not found: " +
                                       str(base_url + path + path_id + subendpoint)
                                       + " Parameters: " + str(parameters)
                                       )

            data = r.json()

            # Check for errors.
            if 'text' in data:
                raise classes.ApiError(data['text'])
            return func(self, data, *args, **kwargs)
        return get_data
    return decorate
