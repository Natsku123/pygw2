from .account import AccountApi
from .achievements import AchievementsApi
from .items import ItemsApi
from .daily import DailyApi

account_api = AccountApi()
achievements_api = AchievementsApi()
items_api = ItemsApi()
daily_api = DailyApi()


class Api:
    """
    Main class for API usage.
    """
    def __init__(self):
        self.api_key: str = ""
        self._account = account_api
        self._achievements = achievements_api
        self._items = items_api
        self._daily = daily_api

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

    @property
    def daily(self):
        return self._daily


api = Api()
