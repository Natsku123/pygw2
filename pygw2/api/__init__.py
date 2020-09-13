from .account import AccountApi
from .achievements import AchievementsApi
from .items import ItemsApi


class Api:
    """
    Main class for API usage.
    """
    def __init__(self):
        self.api_key: str = ""
        self._account = AccountApi()
        self._achievements = AchievementsApi()
        self._items = ItemsApi()

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
