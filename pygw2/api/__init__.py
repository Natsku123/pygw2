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

account_api = AccountApi()
achievements_api = AchievementsApi()
items_api = ItemsApi()
daily_api = DailyApi()
mechanics_api = MechanicsApi()
guild_api = GuildApi()
home_api = HomeApi()
mapinfo_api = MapInfoApi()
misc_api = MiscellaneousApi()
backstory_api = BackstoryApi()
trading_api = TradingPostApi()
pvp_api = PvpApi()
wvw_api = WvWApi()


class Api:
    """
    Main class for API usage.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.api_key: str = ""
        self._account = account_api
        self._achievements = achievements_api
        self._items = items_api
        self._daily = daily_api
        self._mechanics = mechanics_api
        self._guild = GuildApi
        self._home = home_api
        self._mapinfo = mapinfo_api
        self._misc = misc_api
        self._backstory = backstory_api
        self._trading = trading_api
        self._pvp = pvp_api
        self._wvw = wvw_api

    def setup(self, api_key: str):
        self.api_key = api_key

        # Setup sub-APIs
        self._account.setup(api_key)
        self._trading.setup(api_key)

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


api = Api()
