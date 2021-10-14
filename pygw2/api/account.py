from typing import List, Union, Optional

from ..core.models.account import (
    Account,
    VaultSlot,
    HomeNode,
    HomeCat,
    MountType,
    UnlockedFinisher,
    SharedInventorySlot,
    StorageMaterial,
    WalletCurrency,
    MasteryProgress,
)
from ..core.models.achievements import AchievementProgress
from ..core.models.character import (
    Character,
    CharacterCore,
    Crafting,
    Equipment,
    Bag,
    Skills,
    Specializations,
    SkillTree,
)
from ..core.models.general import (
    MountSkin,
    DailyCrafting,
    DailyMapChest,
    Skin,
    DailyWorldBoss,
)
from ..core.models.items import Glider, Mailcarrier, Outfit
from ..core.models.backstory import BiographyAnswer
from ..core.models.crafting import Recipe
from ..core.models.misc import Color, Mini, Novelty, Title
from ..core.models.sab import SAB
from ..core.models.pvp import PvpHero
from ..utils import endpoint, LazyLoader, object_parse
from ..core import parse_item


class AccountHomeApi:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.api_key: str = ""

    def setup(self, api_key: str):
        self.api_key = api_key

    @endpoint("/v2/account/home/cats")
    async def cats(self, *, data) -> List[HomeCat]:
        """
        Get unlocked home instance cats from API.
        :param data: Data from wrapper
        :return:
        """
        from .home import HomeApi

        home_api = HomeApi()

        return await home_api.cats(*data)

    @endpoint("/v2/account/home/nodes")
    async def nodes(self, *, data) -> List[HomeNode]:
        """
        Get unlocked home instance nodes from API.
        :param data: Data from wrapper
        :return:
        """
        from .home import HomeApi

        home_api = HomeApi()

        return await home_api.nodes(*data)


class AccountMountsApi:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.api_key: str = ""

    def setup(self, api_key: str):
        self.api_key = api_key

    @endpoint("/v2/account/mounts/skins")
    async def skins(self, *, data) -> List[MountSkin]:
        """
        Get unlocked skins for mounts from API.
        :param data: Data from wrapper
        :return:
        """
        from .mechanics import MechanicsApi

        mecha_api = MechanicsApi()

        return await mecha_api.mounts.skins(*data)

    @endpoint("/v2/account/mounts/types")
    async def types(self, *, data) -> List[MountType]:
        """
        Get unlocked mounts from API.
        :param data: Data from wrapper
        :return:
        """
        from .mechanics import MechanicsApi

        mecha_api = MechanicsApi()

        return await mecha_api.mounts.types(*data)


class CharactersApi:
    _instance = None

    def __new__(cls, character_id: str, *args, api_key: str = "", **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, character_id: str, *, api_key: str = ""):
        self.api_key: str = api_key
        self.character_id: str = character_id

    def setup(self, api_key: str):
        self.api_key = api_key

    @endpoint("/v2/characters")
    async def get(self, *, data) -> Union[Character, List[str]]:
        """
        Get characters from API. Use item_id with character's name. If no item_id
        is specified, returns all characters.
        :param data: Data from wrapper
        :return:
        """
        from .items import ItemsApi

        items_api = ItemsApi()
        from .misc import MiscellaneousApi

        misc_api = MiscellaneousApi()
        from .mechanics import MechanicsApi

        mecha_api = MechanicsApi()
        from .guild import GuildApi

        guild_api = GuildApi()
        from .backstory import BackstoryApi

        backstory_api = BackstoryApi()
        from .wvw import WvWApi

        wvw_api = WvWApi()

        if isinstance(data, dict):
            if data["guild"]:
                data["guild_"] = LazyLoader(guild_api.get, data["guild"])
            if data["title"]:
                data["title_"] = LazyLoader(misc_api.titles, data["title"])
            data["backstory_"] = LazyLoader(backstory_api.answers, *data["backstory"])

            # Parse all items in equipment
            for i, e in enumerate(data["equipment"]):
                data["equipment"][i] = parse_item(e)

            data["heropoints_"] = LazyLoader(self.heropoints)

            # Parse all items in bags / inventory
            for b in data["bags"]:
                b["item_"] = LazyLoader(items_api.get, b["id"])

                for i, v in enumerate(b["inventory"]):
                    if v:
                        b["inventory"][i] = parse_item(v)

            # Parse all builds
            for tab in data["build_tabs"]:
                tab["build"]["skills"]["heal_"] = LazyLoader(
                    mecha_api.skills, tab["build"]["skills"]["heal"]
                )
                tab["build"]["skills"]["utilities_"] = LazyLoader(
                    mecha_api.skills, tab["build"]["skills"]["utilities"]
                )
                tab["build"]["skills"]["elite_"] = LazyLoader(
                    mecha_api.skills, tab["build"]["skills"]["elite"]
                )
                if (
                    "legends" in tab["build"]["skills"]
                    and tab["build"]["skills"]["legends"]
                ):
                    tab["build"]["skills"]["legends_"] = LazyLoader(
                        mecha_api.skills, tab["build"]["skills"]["legends"]
                    )
                tab["build"]["aquatic_skills"]["heal_"] = LazyLoader(
                    mecha_api.skills, tab["build"]["aquatic_skills"]["heal"]
                )
                tab["build"]["aquatic_skills"]["utilities_"] = LazyLoader(
                    mecha_api.skills, tab["build"]["aquatic_skills"]["utilities"]
                )
                tab["build"]["aquatic_skills"]["elite_"] = LazyLoader(
                    mecha_api.skills, tab["build"]["aquatic_skills"]["elite"]
                )
                if (
                    "legends" in tab["build"]["aquatic_skills"]
                    and tab["build"]["aquatic_skills"]["legends"]
                ):
                    tab["build"]["aquatic_skills"]["legends_"] = LazyLoader(
                        mecha_api.skills, tab["build"]["aquatic_skills"]["legends"]
                    )

                for v in tab["build"]["specializations"]:
                    v["specialization_"] = LazyLoader(
                        mecha_api.specializations, v["id"]
                    )
                    v["traits_"] = LazyLoader(mecha_api.traits, *v["traits"])

            for tab in data["equipment_tabs"]:
                for i, e in enumerate(tab["equipment"]):
                    tab["equipment"][i] = parse_item(e)
                if tab["equipment_pvp"]["amulet"]:
                    tab["equipment_pvp"]["amulet_"] = LazyLoader(
                        items_api.pvp_amulets, tab["equipment_pvp"]["amulet"]
                    )
                if tab["equipment_pvp"]["rune"]:
                    tab["equipment_pvp"]["rune_"] = LazyLoader(
                        items_api.get, tab["equipment_pvp"]["rune"]
                    )
                if tab["equipment_pvp"]["sigils"]:
                    tab["equipment_pvp"]["sigils_"] = LazyLoader(
                        items_api.get, tab["equipment_pvp"]["sigils"]
                    )

            data["sab_"] = LazyLoader(self.sab)

            # Parse all WvW abilities
            for a in data["wvw_abilities"]:
                a["ability_"] = LazyLoader(wvw_api.abilities, a["id"])

            # Parse PvP equipment
            if "equipment_pvp" in data:
                if data["equipment_pvp"]["amulet"]:
                    data["equipment_pvp"]["amulet_"] = LazyLoader(
                        items_api.pvp_amulets, data["equipment_pvp"]["amulet"]
                    )
                if data["equipment_pvp"]["rune"]:
                    data["equipment_pvp"]["rune_"] = LazyLoader(
                        items_api.get, data["equipment_pvp"]["rune"]
                    )
                if data["equipment_pvp"]["sigils"]:
                    data["equipment_pvp"]["sigils_"] = LazyLoader(
                        items_api.get, data["equipment_pvp"]["sigils"]
                    )

            return object_parse(data, Character)
        else:
            return data

    @endpoint("/v2/characters", subendpoint="/backstory")
    async def backstory(self, *, data) -> List[BiographyAnswer]:
        """
        Get character's backstory from API.
        :param data: Data from wrapper
        :return:
        """
        from .backstory import BackstoryApi

        backstory_api = BackstoryApi()

        return await backstory_api.answers(*data)

    @endpoint("/v2/characters", subendpoint="/core")
    async def core(self, *, data) -> CharacterCore:
        """
        Get character's core from API.
        :param data: Data from wrapper
        :return:
        """
        from .misc import MiscellaneousApi

        misc_api = MiscellaneousApi()
        from .guild import GuildApi

        guild_api = GuildApi()

        if data["guild"]:
            data["guild_"] = LazyLoader(guild_api.get, data["guild"])
        if data["title"]:
            data["title_"] = LazyLoader(misc_api.titles, data["title"])
        return object_parse(data, CharacterCore)

    @endpoint("/v2/characters", subendpoint="/crafting")
    async def crafting(self, *, data) -> Union[Crafting, List[Crafting]]:
        """
        Get character's crafting from API.
        :param data: Data from wrapper
        :return:
        """

        return object_parse(data, Crafting)

    @endpoint("/v2/characters", subendpoint="/equipment")
    async def equipment(self, *, data) -> Union[Equipment, List[Equipment]]:
        """
        Get character's equipment from API.
        :param data: Data from wrapper
        :return:
        """
        if isinstance(data, dict):
            data = data["equipment"]

        for i, e in enumerate(data):
            data[i] = parse_item(e)

        return object_parse(data, Equipment)

    @endpoint("/v2/characters", subendpoint="/heropoints")
    async def heropoints(self, *, data):
        """
        Get character's heropoints from API.
        :param data: Data from wrapper
        :return:
        """

        # TODO resolve against skill_challenges in /v2/continents
        return data

    @endpoint("/v2/characters", subendpoint="/inventory")
    async def inventory(self, *, data) -> Union[Bag, List[Bag]]:
        """
        Get character's inventory from API.
        :param data: Data from wrapper
        :return:
        """
        from .items import ItemsApi

        items_api = ItemsApi()

        if isinstance(data, dict):
            data = data["bags"]

        for b in data:
            b["item_"] = LazyLoader(items_api.get, b["id"])

            for i, v in enumerate(b["inventory"]):
                if v:
                    b["inventory"][i] = parse_item(v)

        return object_parse(data, Bag)

    @endpoint("/v2/characters", subendpoint="/skills")
    async def skills(self, *, data) -> Skills:
        """
        Get character's skills from API.
        :param data: Data from wrapper
        :return:
        """
        from .mechanics import MechanicsApi

        mecha_api = MechanicsApi()

        if "skills" in data:
            data = data["skills"]

        for v in data:
            v["heal_"] = LazyLoader(mecha_api.skills, v["heal"])
            v["utilities_"] = LazyLoader(mecha_api.skills, v["utilities"])
            v["elite_"] = LazyLoader(mecha_api.skills, v["elite"])
            if v["legends"]:
                v["legends_"] = LazyLoader(mecha_api.skills, v["legends"])

        return object_parse(data, Skills)

    @endpoint("/v2/characters", subendpoint="/specializations")
    async def specializations(self, *, data) -> Specializations:
        """
        Get character's specializations from API.
        :param data: Data from wrapper
        :return:
        """
        from .mechanics import MechanicsApi

        mecha_api = MechanicsApi()

        if "specializations" in data:
            data = data["specializations"]

        for v in data:
            for s in v:
                s["specialization_"] = LazyLoader(mecha_api.specializations, s["id"])
                s["traits_"] = LazyLoader(mecha_api.traits, *s["traits"])

        return object_parse(data, Specializations)

    @endpoint("/v2/characters", subendpoint="/training")
    async def training(self, *, data) -> Union[SkillTree, List[SkillTree]]:
        """
        Get character's training from API.
        :param data: Data from wrapper
        :return:
        """
        if "training" in data:
            data = data["training"]

        return object_parse(data, SkillTree)

    @endpoint("/v2/characters", subendpoint="/sab")
    async def sab(self, *, data) -> SAB:
        """
        Get character's Super Adventure Box completion from API.
        :param data: Data from wrapper
        :return:
        """

        return object_parse(data, SAB)


class AccountApi:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.api_key: str = ""
        self._home = AccountHomeApi()
        self._mounts = AccountMountsApi()
        self._character = CharactersApi

    def setup(self, api_key: str):
        self.api_key = api_key

        self._home.setup(api_key)
        self._mounts.setup(api_key)

    @property
    def home(self):
        return self._home

    @property
    def mounts(self):
        return self._mounts

    def character(self, character_id):
        return self._character(character_id, api_key=self.api_key)

    @endpoint("/v2/characters")
    async def characters(self, *, data) -> List[str]:
        """
        Get names of the characters from API
        :param data: data from wrapper
        :return: list of names
        """
        return data

    @endpoint("/v2/account")
    async def get(self, *, data) -> Account:
        """
        Get account from API with api key.
        :param data: Data from wrapper
        :return: Account
        """
        from .misc import MiscellaneousApi

        misc_api = MiscellaneousApi()

        data["world_"] = LazyLoader(misc_api.worlds, data["world"])
        return object_parse(data, Account)

    @endpoint("/v2/account/achievements")
    async def achievements(self, *, data) -> List[AchievementProgress]:
        """
        Get achievements progress from API with api key.
        :param data: Data from wrapper
        :return: list
        """
        from .achievements import AchievementsApi

        achievements_api = AchievementsApi()

        for a in data:
            a["achievement_"] = LazyLoader(achievements_api.get, a["id"])

        return object_parse(data, AchievementProgress)

    @endpoint("/v2/account/bank")
    async def bank(self, *, data) -> List[Optional[VaultSlot]]:
        """
        Get bank data from API with api key.
        :param data: Data from wrapper
        :return:
        """

        # Blacklist of purged IDs
        blacklist = [45022, 45023, 45024, 45025]

        for i, item in enumerate(data):
            data[i] = parse_item(item)

        return object_parse(data, Optional[VaultSlot])

    @endpoint("/v2/account/dailycrafting")
    async def dailycrafting(self, *, data) -> List["DailyCrafting"]:
        """
        Get crafted time-gated items from API.
        :param data: Data from wrapper
        :return:
        """
        from .daily import DailyApi

        daily_api = DailyApi()

        print("asd", data)

        if not data:
            return data

        return await daily_api.crafting(*data)

    @endpoint("/v2/account/dungeons")
    async def dungeons(self, *, data):
        """
        Get completed dungeon paths after last daily reset from API.
        :param data: Data from wrapper
        :return:
        """
        # TODO resolve against /v2/dungeons with path id!
        return data

    @endpoint("/v2/account/dyes")
    async def dyes(self, *, data) -> List["Color"]:
        """
        Get unlocked dyes from API.
        :param data: Data from wrapper
        :return:
        """
        from .misc import MiscellaneousApi

        misc_api = MiscellaneousApi()

        return await misc_api.colors(*data)

    @endpoint("/v2/account/finishers")
    async def finishers(self, *, data) -> UnlockedFinisher:
        """
        Get unlocked finishers from API.
        :param data: Data from wrapper
        :return:
        """
        from .items import ItemsApi

        items_api = ItemsApi()

        for f in data:
            f["finisher_"] = LazyLoader(items_api.finishers, f["id"])

        return object_parse(data, UnlockedFinisher)

    @endpoint("/v2/account/gliders")
    async def gliders(self, *, data) -> List["Glider"]:
        """
        Get unlocked gliders from API.
        :param data: Data from wrapper
        :return:
        """
        from .items import ItemsApi

        items_api = ItemsApi()

        return await items_api.gliders(*data)

    @endpoint("/v2/account/inventory")
    async def inventory(self, *, data) -> List[SharedInventorySlot]:
        """
        Get shared inventory from API.
        :param data: Data from wrapper
        :return:
        """
        for i, item in enumerate(data):
            data[i] = parse_item(item)
        return object_parse(data, SharedInventorySlot)

    @endpoint("/v2/account/luck")
    async def luck(self, *, data):
        """
        Get account luck from API.
        :param data: Data from wrapper
        :return:
        """

        # TODO edit data returned to 'better' format
        return data

    @endpoint("/v2/account/mailcarriers")
    async def mailcarriers(self, *, data) -> List["Mailcarrier"]:
        """
        Get unlocked mailcarriers from API.
        :param data: Data from wrapper
        :return:
        """
        from .items import ItemsApi

        items_api = ItemsApi()

        return await items_api.mailcarriers(*data)

    @endpoint("/v2/account/mapchests")
    async def mapchests(self, *, data) -> List["DailyMapChest"]:
        """
        Get mapchest unlocked since daily reset from API.
        :param data: Data from wrapper
        :return:
        """
        from .daily import DailyApi

        daily_api = DailyApi()

        if not data:
            return data

        return await daily_api.mapchests(*data)

    @endpoint("/v2/account/masteries")
    async def masteries(self, *, data) -> List["MasteryProgress"]:
        """
        Get unlocked masteries from API.
        :param data: Data from wrapper
        :return:
        """
        from .mechanics import MechanicsApi

        mecha_api = MechanicsApi()
        for m in data:
            m["mastery_"] = LazyLoader(mecha_api.masteries, m["id"])

        return object_parse(data, MasteryProgress)

    @endpoint("/v2/account/mastery/points")
    async def mastery_points(self, *, data):
        """
        Get account mastery points from API.
        :param data: Data from wrapper
        :return:
        """

        # TODO edit data to 'better' format
        return data

    @endpoint("/v2/account/materials")
    async def materials(self, *, data) -> List["StorageMaterial"]:
        """
        Get contents of material storage from API.
        :param data: Data from wrapper
        :return:
        """
        from .items import ItemsApi

        items_api = ItemsApi()

        for m in data:
            m["item_"] = LazyLoader(items_api.get, m["id"])

        return object_parse(data, StorageMaterial)

    @endpoint("/v2/account/minis")
    async def minis(self, *, data) -> List["Mini"]:
        """
        Get unlocked miniatures from API.
        :param data: Data from wrapper
        :return:
        """
        from .misc import MiscellaneousApi

        misc_api = MiscellaneousApi()

        if not data:
            return data

        return await misc_api.minis(*data)

    @endpoint("/v2/account/novelties")
    async def novelties(self, *, data) -> List["Novelty"]:
        """
        Get unlocked novelties from API.
        :param data: Data from wrapper
        :return:
        """
        from .misc import MiscellaneousApi

        misc_api = MiscellaneousApi()

        return await misc_api.novelties(*data)

    @endpoint("/v2/account/outfits")
    async def outfits(self, *, data) -> List["Outfit"]:
        """
        Get unlocked outfits from API.
        :param data: Data from wrapper
        :return:
        """
        from .mechanics import MechanicsApi

        mecha_api = MechanicsApi()

        if not data:
            return data

        return await mecha_api.outfits(*data)

    @endpoint("/v2/account/pvp/heroes")
    async def pvp_heroes(self, *, data) -> List["PvpHero"]:
        """
        Get unlocked PvP heroes from API.
        :param data: Data from wrapper
        :return:
        """
        from .pvp import PvpApi

        pvp_api = PvpApi()

        if not data:
            return data

        return await pvp_api.heroes(*data)

    @endpoint("/v2/account/raids")
    async def raids(self, *, data):
        """
        Get completed weekly raid encounters from API.
        :param data: Data from wrapper
        :return:
        """

        # TODO resolve against /v2/raids with encounter ID
        return data

    @endpoint("/v2/account/recipes")
    async def recipes(self, *, data) -> List["Recipe"]:
        """
        Get unlocked recipes from API.
        :param data: Data from wrapper
        :return:
        """
        from .items import ItemsApi

        items_api = ItemsApi()

        if not data:
            return data

        return await items_api.recipes(*data)

    @endpoint("/v2/account/skins")
    async def skins(self, *, data) -> List["Skin"]:
        """
        Get unlocked skins from API.
        :param data: Data from wrapper
        :return:
        """
        from .items import ItemsApi

        items_api = ItemsApi()

        if not data:
            return data

        return await items_api.skins(*data)

    @endpoint("/v2/account/titles")
    async def titles(self, *, data) -> List["Title"]:
        """
        Get unlocked titles from API.
        :param data: Data from wrapper
        :return:
        """
        from .misc import MiscellaneousApi

        misc_api = MiscellaneousApi()

        if not data:
            return data

        return await misc_api.titles(*data)

    @endpoint("/v2/account/wallet")
    async def wallet(self, *, data) -> List[WalletCurrency]:
        """
        Get wallet from API.
        :param data: Data from wrapper
        :return:
        """
        from .misc import MiscellaneousApi

        misc_api = MiscellaneousApi()

        for c in data:
            c["currency_"] = LazyLoader(misc_api.currencies, c["id"])

        return object_parse(data, WalletCurrency)

    @endpoint("/v2/account/worldbosses")
    async def worldbosses(self, *, data) -> List["DailyWorldBoss"]:
        """
        Get world bosses defeated since daily reset from API.
        :param data: Data from wrapper
        :return:
        """
        from .daily import DailyApi

        daily_api = DailyApi()

        if not data:
            return data

        return await daily_api.worldbosses(*data)
