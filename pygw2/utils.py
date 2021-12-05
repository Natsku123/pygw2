import asyncio
import concurrent.futures
import datetime
from functools import wraps
from typing import List, Dict, Union, Any, Type, Callable, Optional

from aiohttp import ClientSession
from pydantic import parse_obj_as, BaseModel as PydanticBase

from .core.exceptions import ApiError
from .settings import *

pool = concurrent.futures.ThreadPoolExecutor()


class BaseModel(PydanticBase):
    class Config:
        arbitrary_types_allowed = True


class LimitedDict(dict):
    mapping = {}
    reverse_mapping = {}
    i = 0
    limit = 2000

    def __setitem__(self, k, v):
        key = self.i
        if key in self.reverse_mapping:
            if self.reverse_mapping[key] in self.mapping:
                del self.mapping[self.reverse_mapping[key]]
            del self.reverse_mapping[key]
        self.mapping[k] = key
        self.reverse_mapping[key] = k
        self.i = (self.i + 1) % self.limit
        super().__setitem__(key, v)

    def __getitem__(self, k):
        return super().__getitem__(self.mapping[k])

    def __delitem__(self, k):
        super().__delitem__(self.mapping[k])
        del self.reverse_mapping[self.mapping[k]]
        del self.mapping[k]

    def __contains__(self, item):
        return item in self.mapping and super().__contains__(self.mapping[item])


def function_call_key(func: Callable, args, kwargs) -> str:
    """
    Generate a key based on function called and arguments
    :param func:
    :param args:
    :param kwargs:
    :return:
    """
    return f"{func.__qualname__}{args}{kwargs}"


class LazyLoader:
    _loaded = LimitedDict({})

    def __new__(cls, func: Callable, *args, **kwargs):

        # Check if the function has already been loaded
        loader = cls._loaded.get(function_call_key(func, args, kwargs))

        # If found, return it instead of a new instance
        if loader is not None:
            return loader

        loader = super().__new__(cls)

        # Save new loader to be used in the future
        cls._loaded[function_call_key(func, args, kwargs)] = loader
        return loader

    def __init__(self, func: Callable, *args, **kwargs):
        """
        Lazy load with given function with arguments
        :param func: Function to be used in loading
        :param args: Arguments to be used
        :param kwargs: Keyword arguments to be used
        """
        self.__func = func
        self.__args = args
        self.__kwargs = kwargs
        self.__result = None
        self.__time: Optional[datetime.datetime] = None

    def __call__(self, force=False, *args, **kwargs) -> Union[List[Any], Any]:
        """
        Run lazy loaded function on call or return already found result
        :param force: Force reload
        :param args:
        :param kwargs:
        :return:
        """
        now = datetime.datetime.now()

        # Fetch new result, if not fetched already or is too old or is forced
        if (
            not self.__result
            or not force
            or (self.__time and (now - self.__time).seconds > cache_time)
        ):
            self.__result = pool.submit(
                asyncio.run, self.__func(*self.__args, **self.__kwargs)
            ).result()
            self.__time = now

        return self.__result


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
    data: Union[List[Dict[Any, Any]], Dict[Any, Any]],
    data_type: Type[BaseModel],
    *,
    force_list: bool = False,
) -> Union[List[Any], Any]:
    """
    Parse object from incoming data
    :param data: Dict/list
    :param data_type: Type to convert to
    :param force_list: Force output to be list
    :return:
    """

    if isinstance(data, dict):
        return data_type(**data)
    elif isinstance(data, list):
        result = parse_obj_as(List[data_type], data)

        if len(result) == 1 and not force_list:
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
    override_ids: str = None,
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
        @wraps(func)
        async def get_data(self, *args, **kwargs):
            ids = [[]]
            result = []
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

            # Check for season_id
            if hasattr(self, "match_id") and self.match_id is not None:
                if not path.endswith("/"):
                    path_id = "/" + str(self.match_id)
                else:
                    path_id = str(self.match_id)

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
                # if len(args) > max_ids and path_id == "":
                #     raise ApiError("Too many IDs for this endpoint.")
                if len(args) < min_ids and path_id == "":
                    raise ApiError("Not enough IDs for this endpoint.")

                # Slice given IDs into batches
                for i, item_id in enumerate(args):
                    if len(ids) < (i // max_ids) + 1:
                        ids.append([])
                    ids[i // max_ids].append(item_id)

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

                # Iterate over all batches
                for i in ids:

                    # Update parameters with IDs and
                    # make sure that there are no duplicate requests
                    if len(i) > 0:
                        if not override_ids:
                            parameters["ids"] = list_to_str(i)
                        else:
                            parameters[override_ids] = list_to_str(i)
                    else:
                        if not override_ids and "ids" in parameters:
                            del parameters["ids"]
                        elif override_ids in parameters:
                            del parameters[override_ids]

                    async with session.get(
                        base_url + path + path_id + subendpoint, params=parameters
                    ) as r:

                        # Check known status codes
                        if r.status == 414:
                            raise ApiError("Too many IDs.")
                        elif r.status == 404:
                            # Not found
                            result.append(None)
                            continue

                        # Parse json
                        data = await r.json()

                        # Check for errors.
                        if "text" in data:
                            raise ApiError(data["text"])

                        # Check if IDs used
                        if has_ids:

                            # Check if fetched all
                            if len(args) == 0:
                                i = None

                            result.append(await func(self, **kwargs, data=data, ids=i))
                        else:
                            result.append(await func(self, **kwargs, data=data))

            # If only one batch was fetched, return it
            # Else compile a single list
            if len(result) == 1:
                return result[0]
            else:
                final = []
                for r in result:
                    if isinstance(r, list):
                        final += r
                    else:
                        final.append(r)
                return final

        return get_data

    return decorate
