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
from ..utils import endpoint, object_parse


class GuildEmblemApi:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        pass

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
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, guild_id=None):
        self.api_key: str = ""
        self.guild_id = guild_id
        self._emblem = GuildEmblemApi()

    def setup(self, api_key: str):
        self.api_key = api_key

    @property
    def emblem(self):
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
        return object_parse(data, GuildUpgrade)

    @endpoint("/v2/guild", subendpoint="/log")
    async def log(self, *, data):
        """
        Get Guild log.
        :param data:
        :return:
        """
        # TODO since parameter?
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
        return object_parse(data, GuildRank)

    @endpoint("/v2/guild", subendpoint="/stash")
    async def stash(self, *, data):
        """
        Get Guild stash.
        :param data:
        :return:
        """
        return object_parse(data, GuildStash)

    @endpoint("/v2/guild", subendpoint="/treasury")
    async def treasury(self, *, data):
        """
        Get Guild treasury.
        :param data:
        :return:
        """
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
    async def upgrades(self, *, data):
        """
        Get Guild's upgrades.
        :param data:
        :return:
        """
        # TODO resolve against guild upgrades?
        return data
