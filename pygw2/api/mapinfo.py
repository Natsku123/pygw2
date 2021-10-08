from ..core.models.map import MapSector, Continent, Map
from ..utils import endpoint, object_parse


class ContinentApi:
    def __init__(self, continent_id: int = None):
        self.continent_id = continent_id
        self._floor_api = ContinentFloorApi

    @endpoint('/v2/continents', subendpoint='/floors')
    async def floors(self, *, data):
        """
        Get floors of continent.
        :param data:
        :return:
        """
        # TODO check format
        return data

    def floor(self, floor_id):
        return self._floor_api(
            self.continent_id,
            floor_id
        )


class ContinentFloorApi:
    def __init__(self, continent_id: int, floor_id: int = None):
        self.continent_id = continent_id
        self.floor_id = floor_id
        self._region_api = ContinentFloorRegionApi

    @endpoint('/v2/continents', subendpoint='/regions')
    async def regions(self, *, data):
        """
        Get regions of floor.
        :param data:
        :return:
        """
        # TODO check format
        return data

    def region(self, region_id: int):
        return self._region_api(
            self.continent_id,
            self.floor_id,
            region_id
        )


class ContinentFloorRegionApi:
    def __init__(self, continent_id: int, floor_id: int, region_id: int = None):
        self.continent_id = continent_id
        self.floor_id = floor_id
        self.region_id = region_id
        self._map_api = ContinentFloorRegionMapApi

    @endpoint('/v2/continents', subendpoint='/maps')
    async def maps(self, *, data):
        """
        Get maps of region.
        :param data:
        :return:
        """
        # TODO check format
        return data

    def map(self, map_id: int):
        return self._map_api(
            self.continent_id, self.floor_id, self.region_id, map_id
        )


class ContinentFloorRegionMapApi:
    def __init__(self, continent_id: int, floor_id: int, region_id: int,  map_id: int = None):
        self.continent_id = continent_id
        self.floor_id = floor_id
        self.region_id = region_id
        self.map_id = map_id

    @endpoint('/v2/continents', subendpoint='/sectors')
    async def sectors(self, *, data):
        """
        Get sectors of map.
        :param data:
        :return:
        """
        return object_parse(data, MapSector)

    @endpoint('/v2/continents', subendpoint='/pois')
    async def pois(self, *, data):
        """
        Get pois of map.
        :param data:
        :return:
        """
        # TODO check format
        return data

    @endpoint('/v2/continents', subendpoint='/tasks')
    async def tasks(self, *, data):
        """
        Get tasks of map.
        :param data:
        :return:
        """
        # TODO check format
        return data


class MapInfoApi:
    def __init__(self):
        self._continent = ContinentApi

    @endpoint('/v2/continents', has_ids=True)
    async def continents(self, *, data, ids: list = None):
        """
        Get continents by ID(s).
        None returns all IDs.
        :param data:
        :param ids:
        :return:
        """
        if ids is None:
            return data
        return object_parse(data, Continent)

    def continent(self, continent_id: int = None):
        return self._continent(continent_id)

    @endpoint('/v2/maps', has_ids=True)
    async def maps(self, *, data, ids: list = None):
        """
        Get maos by ID(s).
        None returns all IDs.
        :param data:
        :param ids:
        :return:
        """
        if ids is None:
            return data
        return object_parse(data, Map)
