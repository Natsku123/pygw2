from ..utils import endpoint, object_parse
from pygw2.core.classes import Mastery, MountSkin, MountType


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


