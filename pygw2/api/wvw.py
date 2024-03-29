from typing import List, Union

from ..utils import endpoint, object_parse, LazyLoader
from ..core.models.wvw import WvWAbility, WvWMatch, WvWUpgrade, WvWObjective, WvWRank


class WvWMatchesApi:
    _instances = {}

    def __new__(cls, match_id, *args, api_key: str = "", **kwargs):
        if (match_id, api_key) not in cls._instances:
            cls._instances[(match_id, api_key)] = super().__new__(cls, *args, **kwargs)
        return cls._instances[(match_id, api_key)]

    def __init__(self, match_id, *, api_key: str = ""):
        self.api_key: str = api_key
        self.match_id: str = match_id

    @endpoint("/v2/wvw/matches")
    async def get(self, *, data) -> WvWMatch:
        """
        Get match data from API.
        :param data: Data from wrapper
        :return:
        """

        from .misc import MiscellaneousApi

        misc_api = MiscellaneousApi(api_key=self.api_key)

        from .guild import GuildApi

        guild_api = GuildApi(api_key=self.api_key)

        if "worlds" in data:
            data["worlds"] = {f"{k}_": v for k, v in data["worlds"].items()}
            for world in data["worlds"].keys():
                data["worlds"][world] = LazyLoader(
                    misc_api.worlds, data["worlds"][world]
                )

        if "all_worlds" in data:
            data["all_worlds"] = {f"{k}_": v for k, v in data["all_worlds"].items()}
            for world in data["all_worlds"].keys():
                data["all_worlds"][world] = LazyLoader(
                    misc_api.worlds, data["all_worlds"][world]
                )

        if "maps" in data:
            for m in data["maps"]:
                if "objectives" in m:
                    for objective in m["objectives"]:
                        if "claimed_by" in objective and objective["claimed_by"]:
                            objective["claimed_by_"] = LazyLoader(
                                GuildApi(
                                    objective["claimed_by"], api_key=self.api_key
                                ).get
                            )
                        if (
                            "guild_upgrades" in objective
                            and objective["guild_upgrades"]
                        ):
                            objective["guild_upgrades_"] = LazyLoader(
                                guild_api.upgrades, *objective["guild_upgrades"]
                            )

        return object_parse(data, WvWMatch)

    @endpoint(
        "/v2/wvw/matches/overview",
        has_ids=True,
        override_ids="world",
        min_ids=1,
        max_ids=1,
    )
    async def overview(self, *, data, ids: list = None) -> WvWMatch:
        """
        Get overview of match from API with World ID.
        :param data: Data from wrapper
        :param ids: Empty list
        :return:
        """

        from .misc import MiscellaneousApi

        misc_api = MiscellaneousApi(api_key=self.api_key)

        from .guild import GuildApi

        guild_api = GuildApi(api_key=self.api_key)

        if "worlds" in data:
            data["worlds"] = {f"{k}_": v for k, v in data["worlds"].items()}
            for world in data["worlds"].keys():
                data["worlds"][world] = LazyLoader(
                    misc_api.worlds, data["worlds"][world]
                )

        if "all_worlds" in data:
            data["all_worlds"] = {f"{k}_": v for k, v in data["all_worlds"].items()}
            for world in data["all_worlds"].keys():
                data["all_worlds"][world] = LazyLoader(
                    misc_api.worlds, data["all_worlds"][world]
                )

        if "maps" in data:
            for m in data["maps"]:
                if "objectives" in m:
                    for objective in m["objectives"]:
                        if "claimed_by" in objective and objective["claimed_by"]:
                            objective["claimed_by_"] = LazyLoader(
                                GuildApi(
                                    objective["claimed_by"], api_key=self.api_key
                                ).get
                            )
                        if (
                            "guild_upgrades" in objective
                            and objective["guild_upgrades"]
                        ):
                            objective["guild_upgrades_"] = LazyLoader(
                                guild_api.upgrades, *objective["guild_upgrades"]
                            )

        return object_parse(data, WvWMatch)

    @endpoint(
        "/v2/wvw/matches/scores",
        has_ids=True,
        override_ids="world",
        min_ids=1,
        max_ids=1,
    )
    async def scores(self, *, data, ids: list = None) -> WvWMatch:
        """
        Get scores of match from API with World ID.
        :param data: Data from wrapper
        :param ids: Empty list
        :return:
        """

        from .misc import MiscellaneousApi

        misc_api = MiscellaneousApi(api_key=self.api_key)

        from .guild import GuildApi

        guild_api = GuildApi(api_key=self.api_key)

        if "worlds" in data:
            data["worlds"] = {f"{k}_": v for k, v in data["worlds"].items()}
            for world in data["worlds"].keys():
                data["worlds"][world] = LazyLoader(
                    misc_api.worlds, data["worlds"][world]
                )

        if "all_worlds" in data:
            data["all_worlds"] = {f"{k}_": v for k, v in data["all_worlds"].items()}
            for world in data["all_worlds"].keys():
                data["all_worlds"][world] = LazyLoader(
                    misc_api.worlds, data["all_worlds"][world]
                )

        if "maps" in data:
            for m in data["maps"]:
                if "objectives" in m:
                    for objective in m["objectives"]:
                        if "claimed_by" in objective and objective["claimed_by"]:
                            objective["claimed_by_"] = LazyLoader(
                                GuildApi(
                                    objective["claimed_by"], api_key=self.api_key
                                ).get
                            )
                        if (
                            "guild_upgrades" in objective
                            and objective["guild_upgrades"]
                        ):
                            objective["guild_upgrades_"] = LazyLoader(
                                guild_api.upgrades, *objective["guild_upgrades"]
                            )

        return object_parse(data, WvWMatch)

    @endpoint(
        "/v2/wvw/matches/stats",
        has_ids=True,
        override_ids="world",
        min_ids=1,
        max_ids=1,
    )
    async def stats(self, *, data, ids: list = None) -> WvWMatch:
        """
        Get stats of match from API with World ID.
        :param data: Data from wrapper
        :param ids: Empty list
        :return:
        """

        from .misc import MiscellaneousApi

        misc_api = MiscellaneousApi(api_key=self.api_key)

        from .guild import GuildApi

        guild_api = GuildApi(api_key=self.api_key)

        if "worlds" in data:
            data["worlds"] = {f"{k}_": v for k, v in data["worlds"].items()}
            for world in data["worlds"].keys():
                data["worlds"][world] = LazyLoader(
                    misc_api.worlds, data["worlds"][world]
                )

        if "all_worlds" in data:
            data["all_worlds"] = {f"{k}_": v for k, v in data["all_worlds"].items()}
            for world in data["all_worlds"].keys():
                data["all_worlds"][world] = LazyLoader(
                    misc_api.worlds, data["all_worlds"][world]
                )

        if "maps" in data:
            for m in data["maps"]:
                if "objectives" in m:
                    for objective in m["objectives"]:
                        if "claimed_by" in objective and objective["claimed_by"]:
                            objective["claimed_by_"] = LazyLoader(
                                GuildApi(
                                    objective["claimed_by"], api_key=self.api_key
                                ).get
                            )
                        if (
                            "guild_upgrades" in objective
                            and objective["guild_upgrades"]
                        ):
                            objective["guild_upgrades_"] = LazyLoader(
                                guild_api.upgrades, *objective["guild_upgrades"]
                            )

        return object_parse(data, WvWMatch)


class WvWApi:
    _instances = {}

    def __new__(cls, *args, api_key: str = "", **kwargs):
        if api_key not in cls._instances:
            cls._instances[api_key] = super().__new__(cls, *args, **kwargs)
        return cls._instances[api_key]

    def __init__(self, *, api_key: str = ""):
        self.api_key: str = api_key
        self._matches = WvWMatchesApi

    @endpoint("/v2/wvw/abilities", has_ids=True)
    async def abilities(
        self, *, data, ids: list = None
    ) -> List[Union[WvWAbility, int, str]]:
        """
        Get WvW abilities from API
        :param data: data from wrapper
        :param ids: list of IDs
        :return: list
        """
        if ids is None:
            return data

        return object_parse(data, WvWAbility)

    def match(self, match_id) -> WvWMatchesApi:
        return self._matches(match_id, api_key=self.api_key)

    @endpoint("/v2/wvw/matches")
    async def matches(self, *, data) -> List[str]:
        """
        Get match IDs from API
        :param data: Data from wrapper
        :return: list of IDs
        """

        return data

    @endpoint("/v2/wvw/upgrades", has_ids=True)
    async def upgrades(
        self, *, data, ids: list = None
    ) -> List[Union[WvWUpgrade, int, str]]:
        """
        Get WvW upgrades from API
        :param data: Data from wrapper
        :param ids: list of IDs
        :return: list
        """
        if ids is None:
            return data

        return object_parse(data, WvWUpgrade)

    @endpoint("/v2/wvw/objectives", has_ids=True)
    async def objectives(
        self, *, data, ids: list = None
    ) -> List[Union[WvWObjective, int, str]]:
        """
        Get WvW objectives from API
        :param data: Data from wrapper
        :param ids: list of IDs
        :return: list
        """

        from .mapinfo import MapInfoApi

        map_api = MapInfoApi(api_key=self.api_key)

        if ids is None:
            return data

        for obj in data:
            obj["map"] = await map_api.maps(obj["map_id"])
            if obj["map"]:
                obj["sector"] = (
                    await map_api.continent(obj["map"].continent_id)
                    .floor(1)
                    .region(obj["map"].region_id)
                    .map(obj["map_id"])
                    .sectors(obj["sector_id"])
                )

        return object_parse(data, WvWObjective)

    @endpoint("/v2/wvw/ranks", has_ids=True)
    async def ranks(self, *, data, ids: list = None) -> List[Union[WvWRank, int, str]]:
        """
        Get WvW ranks from API
        :param data: Data from wrapper
        :param ids: list of IDs
        :return: list
        """

        if ids is None:
            return data

        return object_parse(data, WvWRank)
