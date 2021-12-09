from typing import Optional
from ..core.models.guild import (
    GuildEmblemImages,
    Guild,
    GuildPermission,
    GuildUpgrade,
    GuildLogEntry,
    GuildMember,
    GuildRank,
    GuildStash,
    GuildTreasury,
    GuildTeam,
)
from ..utils import endpoint, object_parse, LazyLoader


class GuildEmblemApi:
    _instances = {}

    def __new__(cls, *args, api_key: str = "", **kwargs):
        if api_key not in cls._instances:
            cls._instances[api_key] = super().__new__(cls)
        return cls._instances[api_key]

    def __init__(self, *, api_key: str = ""):
        self.api_key: str = api_key

    @endpoint("/v2/emblem/backgrounds", has_ids=True)
    async def backgrounds(self, *, data, ids: list = None):
        """
        Get Guild Emblem backgrounds by ID(s).
        None returns all IDs.
        :param data:
        :param ids:
        :return:
        """
        if ids is None:
            return data
        return object_parse(data, GuildEmblemImages)

    @endpoint("/v2/emblem/foregrounds", has_ids=True)
    async def foregrounds(self, *, data, ids: list = None):
        """
        Get Guild Emblem foregrounds by ID(s).
        None returns all IDs.
        :param data:
        :param ids:
        :return:
        """
        if ids is None:
            return data
        return object_parse(data, GuildEmblemImages)


class GuildApi:
    _instances = {}

    def __new__(
        cls, *args, api_key: str = "", guild_id: Optional[str] = None, **kwargs
    ):
        if (api_key, guild_id) not in cls._instances:
            cls._instances[(api_key, guild_id)] = super().__new__(cls)
        return cls._instances[(api_key, guild_id)]

    def __init__(self, guild_id: Optional[str] = None, *, api_key: str = ""):
        self.api_key: str = api_key
        self.guild_id: str = guild_id
        self._emblem = GuildEmblemApi(api_key=api_key)

    @property
    def emblem(self) -> GuildEmblemApi:
        return self._emblem

    @endpoint("/v2/guild", has_ids=True, max_ids=1, min_ids=1)
    async def get(self, *, data, ids: list = None):
        """
        Get info of Guild by ID.
        :param data: Guild data
        :param ids: Empty list
        :return:
        """
        return object_parse(data, Guild)

    @endpoint("/v2/guild/permissions", has_ids=True)
    async def permissions(self, *, data, ids: list = None):
        """
        Get Guild Permissions by ID(s).
        None returns all IDs.
        :param data:
        :param ids:
        :return:
        """
        if ids is None:
            return data
        return object_parse(data, GuildPermission)

    @endpoint("/v2/guild/search", is_search=True)
    async def search(self, *, data, name: str = None):
        """
        Search for guild by name.
        Returns Guild IDs.
        :param data:
        :param name:
        :return:
        """
        # TODO resolve guild?
        return data

    @endpoint("/v2/guild/upgrades", has_ids=True)
    async def upgrades(self, *, data, ids: list = None):
        """
        Get Guild Upgrades by ID(s).
        None returns all IDs.
        :param data:
        :param ids:
        :return:
        """
        if ids is None:
            return data

        from .items import ItemsApi

        items_api = ItemsApi(api_key=self.api_key)
        guild_api = GuildApi(api_key=self.api_key)

        for upgrade in data:
            if "prerequisites" in upgrade and upgrade["prerequisites"]:
                upgrade["prerequisites_"] = LazyLoader(
                    guild_api.upgrades, *upgrade["prerequisites"]
                )
            if "costs" in upgrade and upgrade["costs"]:
                for cost in upgrade["costs"]:
                    if "item_id" in cost and cost["item_id"]:
                        cost["item_"] = LazyLoader(items_api.get, cost["item_id"])
        return object_parse(data, GuildUpgrade)

    @endpoint("/v2/guild", subendpoint="/log")
    async def log(self, *, data):
        """
        Get Guild log.
        :param data:
        :return:
        """
        from .items import ItemsApi

        items_api = ItemsApi(api_key=self.api_key)
        guild_api = GuildApi(api_key=self.api_key)

        # TODO since parameter?
        for entry in data:
            if "item_id" in entry and entry["item_id"]:
                entry["item_"] = LazyLoader(items_api.get, entry["item_id"])
            if "upgrade_id" in entry and entry["upgrade_id"]:
                entry["upgrade_"] = LazyLoader(guild_api.upgrades, entry["upgrade_id"])
            if "recipe_id" in entry and entry["recipe_id"]:
                entry["recipe_"] = LazyLoader(items_api.recipes, entry["recipe_id"])
        return object_parse(data, GuildLogEntry)

    @endpoint("/v2/guild", subendpoint="/members")
    async def members(self, *, data):
        """
        Get members of the Guild.
        :param data:
        :return:
        """
        return object_parse(data, GuildMember)

    @endpoint("/v2/guild", subendpoint="/ranks")
    async def ranks(self, *, data):
        """
        Get ranks of the Guild.
        :param data:
        :return:
        """
        for rank in data:
            rank["permissions_"] = LazyLoader(self.permissions, *rank["permissions"])
        return object_parse(data, GuildRank)

    @endpoint("/v2/guild", subendpoint="/stash")
    async def stash(self, *, data):
        """
        Get Guild stash.
        :param data:
        :return:
        """
        from .items import ItemsApi

        items_api = ItemsApi(api_key=self.api_key)
        guild_api = GuildApi(api_key=self.api_key)

        for stash in data:
            stash["upgrade_"] = LazyLoader(guild_api.upgrades, stash["upgrade_id"])
            for slot in stash["inventory"]:
                if slot:
                    slot["item_"] = LazyLoader(items_api.get, slot["id"])
        return object_parse(data, GuildStash)

    @endpoint("/v2/guild", subendpoint="/treasury")
    async def treasury(self, *, data):
        """
        Get Guild treasury.
        :param data:
        :return:
        """
        from .items import ItemsApi

        items_api = ItemsApi(api_key=self.api_key)
        guild_api = GuildApi(api_key=self.api_key)

        for treasury in data:
            treasury["item_"] = LazyLoader(items_api.get, treasury["item_id"])
            for up in treasury["needed_by"]:
                up["upgrade_"] = LazyLoader(guild_api.upgrades, up["upgrade_id"])

        return object_parse(data, GuildTreasury)

    @endpoint("/v2/guild", subendpoint="/teams")
    async def teams(self, *, data):
        """
        Get Guild Teams.
        :param data:
        :return:
        """
        return object_parse(data, GuildTeam)

    @endpoint("/v2/guild", subendpoint="/upgrades")
    async def upgraded(self, *, data):
        """
        Get Guild's upgrades.
        :param data:
        :return:
        """
        guild_api = GuildApi(api_key=self.api_key)
        return await guild_api.upgrades(*data)
