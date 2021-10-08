import inspect
from aiohttp import ClientSession
from pydantic import parse_obj_as, BaseModel
from typing import List, Dict, Union, Any, Type

from .core.exceptions import ApiError
from .settings import *


def list_to_str(l: list, delimiter: str = ","):
    """
    Convert list to string with delimiter.
    :param l: list
    :param delimiter: str=","
    :return: str
    """
    string = ""
    for item in l:
        if l.index(item) == len(l) - 1:
            string += str(item)
        else:
            string += str(item) + delimiter

    return string


def object_parse(
    data: Union[List[Dict[Any, Any]], Dict[Any, Any]], data_type: Type[BaseModel]
) -> Union[List[Any], Any]:
    """
    Parse object from incoming data
    :param data: Dict/list
    :param data_type: Type to convert to
    :return:
    """

    if isinstance(data, dict):
        return data_type(**data)
    elif isinstance(data, list):
        result = parse_obj_as(List[data_type], data)

        if len(result) == 1:
            return result[0]
        else:
            return result


def endpoint(
    path: str,
    subendpoint: str = "",
    *,
    has_ids: bool = False,
    is_search: bool = False,
    max_ids: int = 200,
    min_ids: int = 0,
    override_ids: str = None
):
    """
    Endpoint wrapper
    :param min_ids: Minimum number of IDs supported by endpoint.
    :param max_ids: Maximum number of IDs supported by endpoint.
    :param is_search: bool if input/output used to search
    :param has_ids: bool does it have IDs
    :param path: Endpoint path
    :param subendpoint: Path of sub-endpoint
    :param override_ids: Override 'ids' parameter name
    :return:
    """

    def decorate(func):
        async def get_data(self, *args, **kwargs):
            ids = []
            path_id = ""
            parameters = default_parameters.copy()

            # TODO better key checks

            # Check for api key
            if hasattr(self, "api_key") and self.api_key and self.api_key != "":
                parameters["access_token"] = getattr(self, "api_key")

            # Check for character_id
            if hasattr(self, "character_id") and self.character_id:
                if not path.endswith("/"):
                    path_id = "/" + str(self.character_id)
                else:
                    path_id = str(self.character_id)

            # Check for guild_id
            if hasattr(self, "guild_id") and self.guild_id is not None:
                if not path.endswith("/"):
                    path_id = "/" + str(self.guild_id)
                else:
                    path_id = str(self.guild_id)

            # Check for season_id
            if hasattr(self, "season_id") and self.season_id is not None:
                if not path.endswith("/"):
                    path_id = "/" + str(self.season_id)
                else:
                    path_id = str(self.season_id)

            # Continent path generation

            # Check for continent_id
            if hasattr(self, "continent_id") and self.continent_id is not None:
                if not path.endswith("/"):
                    path_id = "/" + str(self.continent_id)
                else:
                    path_id = str(self.continent_id)

                # Check for floor_id
                if hasattr(self, "floor_id") and self.floor_id is not None:
                    if not path.endswith("/"):
                        path_id += "/floors/" + str(self.floor_id)
                    else:
                        path_id += "floors/" + str(self.floor_id)

                    # Check for region_id
                    if hasattr(self, "region_id") and self.region_id is not None:
                        if not path.endswith("/"):
                            path_id += "/regions/" + str(self.region_id)
                        else:
                            path_id += "regions/" + str(self.region_id)

                        # Check for map_id
                        if hasattr(self, "map_id") and self.map_id is not None:
                            if not path.endswith("/"):
                                path_id += "/maps/" + str(self.map_id)
                            else:
                                path_id += "maps/" + str(self.map_id)

            # Construct fetch with ID(s)
            if has_ids:
                if len(args) > max_ids and path_id == "":
                    raise ApiError("Too many IDs for this endpoint.")
                if len(args) < min_ids and path_id == "":
                    raise ApiError("Not enough IDs for this endpoint.")

                for item_id in args:
                    ids.append(item_id)

                if len(ids) > 0:
                    if not override_ids:
                        parameters["ids"] = list_to_str(ids)
                    else:
                        parameters[override_ids] = list_to_str(ids)

            if is_search:
                for key, value in kwargs.items():
                    if key == "input":
                        parameters["input"] = value
                    elif key == "output":
                        parameters["output"] = value
                    elif key == "name":
                        parameters["name"] = value

            # Check obvious ID error
            if path.endswith("/") and path_id == "":
                raise ApiError("ID needed.")

            if "params" in kwargs:
                for key, value in kwargs["params"].items():
                    parameters[key] = value

            # Get data from API
            async with ClientSession() as session:
                async with session.get(
                    base_url + path + path_id + subendpoint, params=parameters
                ) as r:

                    # Check known status codes
                    if r.status == 414:
                        raise ApiError("Too many IDs.")
                    elif r.status == 404:
                        # Not found
                        return None

                    # Parse json
                    data = await r.json()

                    # Check for errors.
                    if "text" in data:
                        raise ApiError(data["text"])

                    # Check if IDs used
                    if has_ids:

                        # Check if fetched all
                        if len(args) == 0:
                            ids = None

                        return await func(self, **kwargs, data=data, ids=ids)
                    else:
                        return await func(self, **kwargs, data=data)

        return get_data

    return decorate
