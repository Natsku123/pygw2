from .account import AccountApi
from .achievements import AchievementsApi
from .items import ItemsApi

account_api = AccountApi()
achievements_api = AchievementsApi()
items_api = ItemsApi()


class Api:
    """
    Main class for API usage.
    """
    def __init__(self):
        self.api_key: str = ""
        self._account = account_api
        self._achievements = achievements_api
        self._items = items_api

    def setup(self, api_key: str):
        self.api_key = api_key

        # Setup sub-APIs
        self._account.setup(api_key)

    @property
    def account(self):
        return self._account

    @property
    def achievements(self):
        return self._achievements

    @property
    def items(self):
        return self._items


api = Api()
