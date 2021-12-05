from .account import AccountApi
from .achievements import AchievementsApi
from .items import ItemsApi
from .daily import DailyApi
from .mechanics import MechanicsApi
from .guild import GuildApi
from .home import HomeApi
from .mapinfo import MapInfoApi
from .misc import MiscellaneousApi
from .backstory import BackstoryApi
from .pvp import PvpApi
from .commerce import TradingPostApi
from .wvw import WvWApi


class Api:
    """
    Main class for API usage.
    """

    _instances = {}

    def __new__(cls, *args, api_key: str = "", **kwargs):
        if api_key not in cls._instances:
            cls._instances[api_key] = super().__new__(cls, *args, **kwargs)
        return cls._instances[api_key]

    def __init__(self, *, api_key: str = ""):
        self.api_key: str = api_key
        self._account = AccountApi(api_key=api_key)
        self._achievements = AchievementsApi(api_key=api_key)
        self._items = ItemsApi(api_key=api_key)
        self._daily = DailyApi(api_key=api_key)
        self._mechanics = MechanicsApi(api_key=api_key)
        self._guild = GuildApi
        self._home = HomeApi(api_key=api_key)
        self._mapinfo = MapInfoApi(api_key=api_key)
        self._misc = MiscellaneousApi(api_key=api_key)
        self._backstory = BackstoryApi(api_key=api_key)
        self._trading = TradingPostApi(api_key=api_key)
        self._pvp = PvpApi(api_key=api_key)
        self._wvw = WvWApi(api_key=api_key)

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

    @property
    def mechanics(self):
        return self._mechanics

    @property
    def guild(self):
        return self._guild

    @property
    def home(self):
        return self._home

    @property
    def mapinfo(self):
        return self._mapinfo

    @property
    def miscellaneous(self):
        return self._misc

    @property
    def backstory(self):
        return self._backstory

    @property
    def commerce(self):
        return self._trading

    @property
    def pvp(self):
        return self._pvp

    @property
    def wvw(self):
        return self._wvw
