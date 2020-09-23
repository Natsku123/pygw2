from pygw2.core.classes import *
from ..utils import endpoint, object_parse


class GuildEmblemApi:
    def __init__(self):
        pass

    @endpoint('/v2/emblem/backgrounds', has_ids=True)
    def backgrounds(self, *, data, ids: list = None):
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

    @endpoint('/v2/emblem/foregrounds', has_ids=True)
    def foregrounds(self, *, data, ids: list = None):
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
    def __init__(self, guild_id=None):
        self.api_key: str = ""
        self.guild_id = guild_id
        self._emblem = GuildEmblemApi()

    def setup(self, api_key: str):
        self.api_key = api_key

    @property
    def emblem(self):
        return self._emblem

    @endpoint('/v2/guild', has_ids=True, max_ids=1, min_ids=1)
    def get(self, *, data, ids: list = None):
        """
        Get info of Guild by ID.
        :param data: Guild data
        :param ids: Empty list
        :return:
        """
        return object_parse(data, Guild)

    @endpoint('/v2/guild/permissions', has_ids=True)
    def permissions(self, *, data, ids: list = None):
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

    @endpoint('/v2/guild/search', is_search=True)
    def search(self, *, data, name: str = None):
        """
        Search for guild by name.
        Returns Guild IDs.
        :param data:
        :param name:
        :return:
        """
        # TODO resolve guild?
        return data

    @endpoint('/v2/guild/upgrades', has_ids=True)
    def upgrades(self, *, data, ids: list = None):
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

    @endpoint('/v2/guild', subendpoint='/log')
    def log(self, *, data):
        """
        Get Guild log.
        :param data:
        :return:
        """
        # TODO since parameter?
        return object_parse(data, GuildLogEntry)

    @endpoint('/v2/guild', subendpoint='/members')
    def members(self, *, data):
        """
        Get members of the Guild.
        :param data:
        :return:
        """
        return object_parse(data, GuildMember)

    @endpoint('/v2/guild', subendpoint='/ranks')
    def ranks(self, *, data):
        """
        Get ranks of the Guild.
        :param data:
        :return:
        """
        return object_parse(data, GuildRank)

    @endpoint('/v2/guild', subendpoint='/stash')
    def stash(self, *, data):
        """
        Get Guild stash.
        :param data:
        :return:
        """
        return object_parse(data, GuildStash)

    @endpoint('/v2/guild', subendpoint='/treasury')
    def treasury(self, *, data):
        """
        Get Guild treasury.
        :param data:
        :return:
        """
        return object_parse(data, GuildTreasury)

    @endpoint('/v2/guild', subendpoint='/teams')
    def teams(self, *, data):
        """
        Get Guild Teams.
        :param data:
        :return:
        """
        return object_parse(data, GuildTeam)

    @endpoint('/v2/guild', subendpoint='/upgrades')
    def upgrades(self, *, data):
        """
        Get Guild's upgrades.
        :param data:
        :return:
        """
        # TODO resolve against guild upgrades?
        return data
