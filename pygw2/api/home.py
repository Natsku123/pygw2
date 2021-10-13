from ..core.models.account import HomeCat, HomeNode
from ..utils import endpoint, object_parse


class HomeApi:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        pass

    @endpoint("/v2/home/cats", has_ids=True)
    async def cats(self, *, data, ids: list = None):
        """
        Get unlockable cats by ID(s).
        None returns all IDs.
        :param data:
        :param ids:
        :return:
        """
        if ids is None:
            return data
        return object_parse(data, HomeCat)

    @endpoint("/v2/home/nodes", has_ids=True)
    async def nodes(self, *, data, ids: list = None):
        """
        Get unlockable nodes by ID(s).
        None returns all IDs.
        :param data:
        :param ids:
        :return:
        """
        if ids is None:
            return data
        return object_parse(data, HomeNode)
