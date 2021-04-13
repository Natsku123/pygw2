from ..core.models.account import MountType, Mastery, Pet
from ..core.models.character import Profession, Race, Skill, Trait, Legend
from ..core.models.general import MountSkin
from ..core.models.items import Outfit
from ..utils import endpoint, object_parse


class MechanicsMountsApi:
    def __init__(self):
        pass

    @endpoint('/v2/mounts/skins', has_ids=True)
    def skins(self, *, data, ids: list = None):
        """
        Get mount skins by ID(s).
        None returns all IDs.
        :param data:
        :param ids:
        :return:
        """
        if ids is None:
            return data
        return object_parse(data, MountSkin)

    @endpoint('/v2/mounts/types', has_ids=True)
    def types(self, *, data, ids: list = None):
        """
        Get mount types by ID(s).
        None returns all IDs.
        :param data:
        :param ids:
        :return:
        """
        if ids is None:
            return data
        return object_parse(data, MountType)


class MechanicsApi:
    def __init__(self):
        self._mounts = MechanicsMountsApi()

    @property
    def mounts(self):
        return self._mounts

    @endpoint('/v2/masteries', has_ids=True)
    def masteries(self, *, data, ids: list = None):
        """
        Get masteries by ID(s).
        None returns all IDs.
        :param data:
        :param ids:
        :return:
        """
        if ids is None:
            return data
        return object_parse(data, Mastery)

    @endpoint('/v2/outfits', has_ids=True)
    def outfits(self, *, data, ids: list = None):
        """
        Get outfits by ID(s).
        None returns all IDs.
        :param data:
        :param ids:
        :return:
        """
        if ids is None:
            return data
        return object_parse(data, Outfit)

    @endpoint('/v2/pets', has_ids=True)
    def pets(self, *, data, ids: list = None):
        """
        Get Ranger pets by ID(s).
        None returns all IDs.
        :param data:
        :param ids:
        :return:
        """
        if ids is None:
            return data
        return object_parse(data, Pet)

    @endpoint('/v2/professions', has_ids=True)
    def professions(self, *, data, ids: list = None):
        """
        Get professions by ID(s).
        None returns all IDs.
        :param data:
        :param ids:
        :return:
        """
        if ids is None:
            return data
        return object_parse(data, Profession)

    @endpoint('/v2/races', has_ids=True)
    def races(self, *, data, ids: list = None):
        """
        Get races by ID(s).
        None returns all IDs.
        :param data:
        :param ids:
        :return:
        """
        if ids is None:
            return data
        return object_parse(data, Race)

    @endpoint('/v2/skills', has_ids=True)
    def skills(self, *, data, ids: list = None):
        """
        Get skills by ID(s).
        None returns all IDs.
        :param data:
        :param ids:
        :return:
        """
        if ids is None:
            return data
        return object_parse(data, Skill)

    @endpoint('/v2/traits', has_ids=True)
    def traits(self, *, data, ids: list = None):
        """
        Get traits by ID(s).
        None returns all IDs.
        :param data:
        :param ids:
        :return:
        """
        if ids is None:
            return data
        return object_parse(data, Trait)

    @endpoint('/v2/legends', has_ids=True)
    def legends(self, *, data, ids: list = None):
        """
        Get legends by ID(s).
        None returns all IDs.
        :param data:
        :param ids:
        :return:
        """
        if ids is None:
            return data
        return object_parse(data, Legend)

