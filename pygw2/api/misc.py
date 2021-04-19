from ..utils import endpoint, object_parse
from ..core.models.misc import Color, Currency


class MiscellaneousApi:
    def __init__(self):
        self.api_key: str = ""

    def setup(self, api_key: str):
        self.api_key = api_key

    @endpoint("/v2/build")
    async def build(self, *, data):
        """
        Get current build id from API
        :param data: Data from wrapper
        :return:
        """
        return data

    @endpoint("/v2/colors", has_ids=True)
    async def colors(self, *, data, ids: list = None):
        """
        Get colors from API by list of IDs or one ID.
        :param data: Data from wrapper
        :param ids: List of IDs
        :return: list
        """

        # Return ids
        if ids is None:
            return data

        # Return object(s)
        return object_parse(data, Color)

    @endpoint("/v2/currencies", has_ids=True)
    async def currencies(self, *, data, ids: list = None):
        """
        Get currencies from API by list of IDs or one ID.
        :param data: Data from wrapper
        :param ids: List of IDs
        :return: list
        """

        # Return ids
        if ids is None:
            return data

        # Return object(s)
        return object_parse(data, Currency)
