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


def object_parse(data, data_type):
    """
    Parse object from incoming data
    :param data: Dict/list
    :param data_type: Type to convert to
    :return:
    """

    if isinstance(data, dict):
        return data_type(**data)
    elif isinstance(data, list):

        objects = []
        for obj in data:
            objects.append(data_type(**obj))

        if len(objects) > 1:
            return objects
        else:
            return objects[0]


def endpoint(
        path: str,
        subendpoint: str = "",
        *,
        has_ids: bool = False,
        is_search: bool = False
):
    """
    Endpoint wrapper
    :param is_search: bool if input/output used to search
    :param has_ids: bool does it have IDs
    :param path: Endpoint path
    :param subendpoint: Path of sub-endpoint
    :return:
    """
    def decorate(func):
        def get_data(self, *args, **kwargs):
            ids = []
            path_id = ""
            parameters = default_parameters.copy()

            # Check for api key
            if hasattr(self, "api_key") and self.api_key and self.api_key != "":
                parameters['access_token'] = getattr(self, "api_key")

            # Check for character_id
            if hasattr(self, "character_id") and self.character_id:
                if not path.endswith("/"):
                    path_id = "/" + str(self.character_id)
                else:
                    path_id = str(self.character_id)

            # Construct fetch with ID(s)
            if has_ids:
                if len(args) == 1 and path_id == "":
                    if not path.endswith("/"):
                        path_id = "/" + str(args[0])
                    else:
                        path_id = str(args[0])
                else:
                    for item_id in args:
                        ids.append(item_id)

                    if len(ids) > 0:
                        parameters['ids'] = list_to_str(ids)

            if is_search:
                for key, value in kwargs.items():
                    if key == "input":
                        parameters['input'] = value
                    elif key == "output":
                        parameters['output'] = value

            # Check obvious ID error
            if path.endswith("/") and path_id == "":
                raise classes.ApiError("ID needed.")

            # Get data from API
            r = requests.get(
                base_url + path + path_id + subendpoint,
                params=parameters
            )

            # Check known status codes
            if r.status_code == 414:
                raise classes.ApiError("Too many IDs.")
            elif r.status_code == 404:
                # Not found
                return None

            # Parse json
            data = r.json()

            # Check for errors.
            if 'text' in data:
                raise classes.ApiError(data['text'])

            # Check if IDs used
            if has_ids:

                # Check if fetched all
                if len(args) == 0:
                    ids = None

                return func(self, **kwargs, data=data, ids=ids)
            else:
                return func(self, **kwargs, data=data)

        return get_data
    return decorate
