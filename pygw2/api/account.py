from typing import List, Union

from ..core.models.account import Account, VaultSlot, HomeNode, HomeCat, MountType
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
from ..core.models.general import MountSkin
from ..core.models.backstory import BiographyAnswer
from ..core.models.sab import SAB
from ..utils import endpoint, LazyLoader, object_parse
from ..core import parse_item

from .achievements import AchievementsApi
from .items import ItemsApi
from .home import HomeApi
from .misc import MiscellaneousApi
from .mechanics import MechanicsApi
from .guild import GuildApi
from .backstory import BackstoryApi
from .wvw import WvWApi

achievements_api = AchievementsApi()
items_api = ItemsApi()
home_api = HomeApi()
misc_api = MiscellaneousApi()
mecha_api = MechanicsApi()
guild_api = GuildApi()
backstory_api = BackstoryApi()
wvw_api = WvWApi()


class AccountHomeApi:
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

        return await home_api.cats(*data)

    @endpoint("/v2/account/home/nodes")
    async def nodes(self, *, data) -> List[HomeNode]:
        """
        Get unlocked home instance nodes from API.
        :param data: Data from wrapper
        :return:
        """

        return await home_api.nodes(*data)


class AccountMountsApi:
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

        return await mecha_api.mounts.skins(*data)

    @endpoint("/v2/account/mounts/types")
    async def types(self, *, data) -> List[MountType]:
        """
        Get unlocked mounts from API.
        :param data: Data from wrapper
        :return:
        """

        return await mecha_api.mounts.types(*data)


class CharactersApi:
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

        if isinstance(data, dict):
            if data["guild"]:
                data["_guild"] = LazyLoader(guild_api.get, data["guild"])
            if data["title"]:
                data["_title"] = LazyLoader(misc_api.titles, data["title"])
            data["_backstory"] = LazyLoader(backstory_api.answers, *data["backstory"])

            # Parse all items in equipment
            for i, e in enumerate(data["equipment"]):
                data["equipment"][i] = parse_item(e)

            data["_heropoints"] = LazyLoader(self.heropoints)

            # Parse all items in bags / inventory
            for b in data["bags"]:
                b["_item"] = LazyLoader(items_api.get, b["id"])

                for i, v in enumerate(b["inventory"]):
                    if v:
                        b["inventory"][i] = parse_item(v)

            # Parse all skills
            for v in data["skills"]:
                v["_heal"] = LazyLoader(mecha_api.skills, v["heal"])
                v["_utilities"] = LazyLoader(mecha_api.skills, v["utilities"])
                v["_elite"] = LazyLoader(mecha_api.skills, v["elite"])
                if v["legends"]:
                    v["_legends"] = LazyLoader(mecha_api.skills, v["legends"])

            # Parse all specializations
            for v in data["specializations"]:
                for s in v:
                    s["_specialization"] = LazyLoader(
                        mecha_api.specializations, s["id"]
                    )
                    s["_traits"] = LazyLoader(mecha_api.traits, *s["traits"])

            data["_sab"] = LazyLoader(self.sab)

            # Parse all WvW abilities
            for a in data["wvw_abilities"]:
                a["_ability"] = LazyLoader(wvw_api.abilities, a["id"])

            # Parse PvP equipment
            if data["equipment_pvp"]["amulet"]:
                data["equipment_pvp"]["_amulet"] = LazyLoader(
                    items_api.pvp_amulets, data["equipment_pvp"]["amulet"]
                )
            if data["equipment_pvp"]["rune"]:
                data["equipment_pvp"]["_rune"] = LazyLoader(
                    items_api.get, data["equipment_pvp"]["rune"]
                )
            if data["equipment_pvp"]["sigils"]:
                data["equipment_pvp"]["_sigils"] = LazyLoader(
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

        return await backstory_api.answers(*data)

    @endpoint("/v2/characters", subendpoint="/core")
    async def core(self, *, data) -> CharacterCore:
        """
        Get character's core from API.
        :param data: Data from wrapper
        :return:
        """

        if data["guild"]:
            data["_guild"] = LazyLoader(guild_api.get, data["guild"])
        if data["title"]:
            data["_title"] = LazyLoader(misc_api.titles, data["title"])
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
        if isinstance(data, dict):
            data = data["bags"]

        for b in data:
            b["_item"] = LazyLoader(items_api.get, b["id"])

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
        if "skills" in data:
            data = data["skills"]

        for v in data:
            v["_heal"] = LazyLoader(mecha_api.skills, v["heal"])
            v["_utilities"] = LazyLoader(mecha_api.skills, v["utilities"])
            v["_elite"] = LazyLoader(mecha_api.skills, v["elite"])
            if v["legends"]:
                v["_legends"] = LazyLoader(mecha_api.skills, v["legends"])

        return object_parse(data, Skills)

    @endpoint("/v2/characters", subendpoint="/specializations")
    async def specializations(self, *, data) -> Specializations:
        """
        Get character's specializations from API.
        :param data: Data from wrapper
        :return:
        """
        if "specializations" in data:
            data = data["specializations"]

        for v in data:
            for s in v:
                s["_specialization"] = LazyLoader(mecha_api.specializations, s["id"])
                s["_traits"] = LazyLoader(mecha_api.traits, *s["traits"])

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

    @endpoint("/v2/account")
    async def get(self, *, data):
        """
        Get account from API with api key.
        :param data: Data from wrapper
        :return: Account
        """

        return Account(**data)

    @endpoint("/v2/account/achievements")
    async def achievements(self, *, data):
        """
        Get achievements progress from API with api key.
        :param data: Data from wrapper
        :return: list
        """

        achis = []

        # Get all achievement ids
        # completed = []
        # ids = [i['id'] for i in data]

        # all_ids = await achievements_api.get()

        # Spare all ids that can be found and there is progress
        # for ido in all_ids:
        #     if ido in ids:
        #         completed.append(ido)

        # Cut list into several 'packages' since endpoint supports max 200 ids.
        # package_size = 200

        # if len(completed) > package_size:
        #     new_com = []
        #
        #     # Cut to 200 ids per get.
        #     for i in range(0, package_size, len(completed)):
        #         if len(completed) - i >= package_size:
        #             new_com.append(completed[i:package_size+i])
        #         else:
        #             new_com.append(completed[i:len(completed)])

        #     achios_t = []

        #     # Get all ids.
        #     for i in new_com:
        #         achios_t.append(await achievements_api.get(ids=i))

        #     achios = []

        #     # Combine lists.
        #     for i in achios_t:
        #         for n in i:
        #             achios.append(n)
        # else:
        #     achios = await achievements_api.get(ids=completed)

        # Match all achievement objects
        # for achi in data:
        #     for achio in achios:
        #         if achi['id'] == achio.id:
        #             achis.append(AchievementProgress(**achios))
        #            break
        achis = []
        for achi in data:
            achis.append(AchievementProgress(**achi))
        return achis

    @endpoint("/v2/account/bank")
    async def bank(self, *, data):
        """
        Get bank data from API with api key.
        :param data: Data from wrapper
        :return:
        """

        bank = []

        # Blacklist of purged IDs
        blacklist = [45022, 45023, 45024, 45025]

        # Optimizing api calls to batches of 200 ids
        # item_ids = []
        # i = 0
        # batch = 0
        # for item in data:
        #     if item is not None and item['id'] not in blacklist:
        #         if i % 200 == 0 or i == 0:
        #             item_ids.append([])
        #             batch = batch + 1
        #
        #         item_ids[batch-1].append(item['id'])
        #         i = i + 1
        #
        # items_ready = {}
        #
        # Get dict of item and its id
        # for items in item_ids:
        #     items_fetched = await items_api.get(ids=items)
        #     if isinstance(items_fetched, list):
        #         for item in items_fetched:
        #             items_ready[item.id] = item
        #     else:
        #         items_ready[items_fetched.id] = items_fetched
        #
        # Combine information
        for item in data:
            # TODO create more accurate item object

            if item is None:
                bank.append(None)
            else:
                bank.append(VaultSlot(**item))

        return bank

    @endpoint("/v2/account/dailycrafting")
    async def dailycrafting(self, *, data):
        """
        Get crafted time-gated items from API.
        :param data: Data from wrapper
        :return:
        """
        # TODO resolve against /v2/dailycrafting
        return data

    @endpoint("/v2/account/dungeons")
    async def dungeons(self, *, data):
        """
        Get completed dungeon paths after last daily reset from API.
        :param data: Data from wrapper
        :return:
        """
        # TODO resolve against /v2/dungeons
        return data

    @endpoint("/v2/account/dyes")
    async def dyes(self, *, data):
        """
        Get unlocked dyes from API.
        :param data: Data from wrapper
        :return:
        """

        # TODO resolve against /v2/colors
        return data

    @endpoint("/v2/account/finishers")
    async def finishers(self, *, data):
        """
        Get unlocked finishers from API.
        :param data: Data from wrapper
        :return:
        """

        finishers = []
        for finisher in data:
            # TODO change finisher_id to finisher with resolve against /v2/finishers
            finishers.append(
                {
                    "finisher_id": finisher["id"],
                    "permanent": finisher["permanent"],
                    "quantity": finisher.get("quantity", None),
                }
            )
        return finishers

    @endpoint("/v2/account/gliders")
    async def gliders(self, *, data):
        """
        Get unlocked gliders from API.
        :param data: Data from wrapper
        :return:
        """

        # TODO resolve against /v2/gliders
        return data

    @endpoint("/v2/account/inventory")
    async def inventory(self, *, data):
        """
        Get shared inventory from API.
        :param data: Data from wrapper
        :return:
        """
        inventory = []
        ids = []
        for item in data:
            ids.append(item["id"])
        items = await items_api.get(*ids)
        for item in data:
            corr_item = None
            for itm_obj in items:
                if item["id"] == itm_obj.id:
                    corr_item = itm_obj
                    break

            # TODO change to more specific items
            inventory.append(
                {
                    "item": corr_item,
                    "count": item["count"],
                    "charges": item.get("charges", None),
                    "skin": item.get("skin", None),
                    "upgrades": item.get("upgrades", None),
                    "infusions": item.get("infusions", None),
                    "binding": item.get("binding", None),
                }
            )
        return inventory

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
    async def mailcarriers(self, *, data):
        """
        Get unlocked mailcarriers from API.
        :param data: Data from wrapper
        :return:
        """

        # TODO resolve against /v2/mailcarriers
        return data

    @endpoint("/v2/account/mapchests")
    async def mapchests(self, *, data):
        """
        Get mapchest unlocked since daily reset from API.
        :param data: Data from wrapper
        :return:
        """

        # TODO resolve against /v2/mapchests
        return data

    @endpoint("/v2/account/masteries")
    async def masteries(self, *, data):
        """
        Get unlocked masteries from API.
        :param data: Data from wrapper
        :return:
        """

        # TODO resolve against /v2/masteries
        return data

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
    async def materials(self, *, data):
        """
        Get contents of material storage from API.
        :param data: Data from wrapper
        :return:
        """

        # Optimizing api calls to batches of 200 ids
        item_ids = []
        i = 0
        batch = 0
        for item in data:
            if i % 200 == 0 or i == 0:
                item_ids.append([])
                batch = batch + 1

            item_ids[batch - 1].append(item["id"])
            i = i + 1

        items_ready = {}

        # Get dict of item and its id
        for items in item_ids:
            items_fetched = await items_api.get(*items)
            if isinstance(items_fetched, list):
                for item in items_fetched:
                    items_ready[item.id] = item
            else:
                items_ready[items_fetched.id] = items_fetched

        items = []
        for item in data:
            items.append(
                {
                    "item": items_ready[item["id"]],
                    "category": item["category"],
                    "binding": item.get("binding", None),
                    "count": item["count"],
                }
            )

        return items

    @endpoint("/v2/account/minis")
    async def minis(self, *, data):
        """
        Get unlocked miniatures from API.
        :param data: Data from wrapper
        :return:
        """

        # TODO resolve against /v2/minis
        return data

    @endpoint("/v2/account/novelties")
    async def novelties(self, *, data):
        """
        Get unlocked novelties from API.
        :param data: Data from wrapper
        :return:
        """

        # TODO resolve against /v2/novelties
        return data

    @endpoint("/v2/account/outfits")
    async def outfits(self, *, data):
        """
        Get unlocked outfits from API.
        :param data: Data from wrapper
        :return:
        """

        # TODO resolve against /v2/outfits
        return data

    @endpoint("/v2/account/pvp/heroes")
    async def pvp_heroes(self, *, data):
        """
        Get unlocked PvP heroes from API.
        :param data: Data from wrapper
        :return:
        """

        # TODO resolve against /v2/pvp/heroes
        return data

    @endpoint("/v2/account/raids")
    async def raids(self, *, data):
        """
        Get completed weekly raid encounters from API.
        :param data: Data from wrapper
        :return:
        """

        # TODO resolve against /v2/raids
        return data

    @endpoint("/v2/account/recipes")
    async def recipes(self, *, data):
        """
        Get unlocked recipes from API.
        :param data: Data from wrapper
        :return:
        """

        # TODO resolve against /v2/recipes
        return data

    @endpoint("/v2/account/skins")
    async def skins(self, *, data):
        """
        Get unlocked skins from API.
        :param data: Data from wrapper
        :return:
        """

        # TODO resolve against /v2/skins
        return data

    @endpoint("/v2/account/titles")
    async def titles(self, *, data):
        """
        Get unlocked titles from API.
        :param data: Data from wrapper
        :return:
        """

        # TODO resolve against /v2/titles
        return data

    @endpoint("/v2/account/wallet")
    async def wallet(self, *, data):
        """
        Get wallet from API.
        :param data: Data from wrapper
        :return:
        """

        # TODO resolve against /v2/currencies and 'better' format
        return data

    @endpoint("/v2/account/worldbosses")
    async def worldbosses(self, *, data):
        """
        Get world bosses defeated since daily reset from API.
        :param data: Data from wrapper
        :return:
        """

        # TODO resolve against /v2/worldbosses
        return data
