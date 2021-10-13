from ..core.models.account import MountType, Mastery, Pet
from ..core.models.character import (
    Profession,
    Race,
    Skill,
    Trait,
    Legend,
    Specialization,
)
from ..core.models.general import MountSkin
from ..core.models.items import Outfit
from ..utils import endpoint, object_parse, LazyLoader


class MechanicsMountsApi:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        pass

    @endpoint("/v2/mounts/skins", has_ids=True)
    async def skins(self, *, data, ids: list = None):
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

    @endpoint("/v2/mounts/types", has_ids=True)
    async def types(self, *, data, ids: list = None):
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
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self._mounts = MechanicsMountsApi()

    @property
    def mounts(self):
        return self._mounts

    @endpoint("/v2/masteries", has_ids=True)
    async def masteries(self, *, data, ids: list = None):
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

    @endpoint("/v2/outfits", has_ids=True)
    async def outfits(self, *, data, ids: list = None):
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

    @endpoint("/v2/pets", has_ids=True)
    async def pets(self, *, data, ids: list = None):
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

    @endpoint("/v2/professions", has_ids=True)
    async def professions(self, *, data, ids: list = None):
        """
        Get professions by ID(s).
        None returns all IDs.
        :param data:
        :param ids:
        :return:
        """
        if ids is None:
            return data
        for p in data:
            p["_specializations"] = LazyLoader(
                self.specializations, *p["specializations"]
            )
            for w in p["weapons"]:
                if w["specialization"]:
                    w["_specialization"] = LazyLoader(
                        self.specializations, w["specialization"]
                    )
                for s in w["skills"]:
                    s["_skill"] = LazyLoader(self.skills, s["id"])
            for t in p["training"]:
                t["_skill"] = LazyLoader(self.skills, t["id"])
                t["_specialization"] = LazyLoader(self.specializations, t["id"])

                for track in t["tracks"]:
                    if track["skill_id"]:
                        track["_skill"] = LazyLoader(self.skills, track["skill_id"])
                    if track["trait_id"]:
                        track["_trait"] = LazyLoader(self.traits, track["trait_id"])
        return object_parse(data, Profession)

    @endpoint("/v2/races", has_ids=True)
    async def races(self, *, data, ids: list = None):
        """
        Get races by ID(s).
        None returns all IDs.
        :param data:
        :param ids:
        :return:
        """
        if ids is None:
            return data
        for r in data:
            r["_skills"] = LazyLoader(self.skills, r["skills"])
        return object_parse(data, Race)

    @endpoint("/v2/specializations", has_ids=True)
    async def specializations(self, *, data, ids: list = None):
        """

        :param data:
        :param ids:
        :return:
        """
        if ids is None:
            return data

        for s in data:
            s["_minor_traits"] = LazyLoader(self.traits, *s["minor_traits"])
            s["_major_traits"] = LazyLoader(self.traits, *s["major_traits"])

        return object_parse(data, Specialization)

    @endpoint("/v2/skills", has_ids=True)
    async def skills(self, *, data, ids: list = None):
        """
        Get skills by ID(s).
        None returns all IDs.
        :param data:
        :param ids:
        :return:
        """
        if ids is None:
            return data

        for s in data:
            if s["flip_skill"]:
                s["_flip_skill"] = LazyLoader(self.skills, s["flip_skill"])
            if s["next_chain"]:
                s["_next_chain"] = LazyLoader(self.skills, s["next_chain"])
            if s["prev_chain"]:
                s["_prev_chain"] = LazyLoader(self.skills, s["prev_chain"])
            if s["transform_skills"]:
                s["_transform_skills"] = LazyLoader(self.skills, *s["transform_skills"])
            if s["bundle_skills"]:
                s["_bundle_skills"] = LazyLoader(self.skills, *s["bundle_skills"])
            if s["toolbelt_skill"]:
                s["_toolbelt_skill"] = LazyLoader(self.skills, *s["toolbelt_skill"])

            if s["traited_facts"]:
                for tf in s["traited_facts"]:
                    tf["_requires_trait"] = LazyLoader(
                        self.traits, tf["requires_trait"]
                    )
        return object_parse(data, Skill)

    @endpoint("/v2/traits", has_ids=True)
    async def traits(self, *, data, ids: list = None):
        """
        Get traits by ID(s).
        None returns all IDs.
        :param data:
        :param ids:
        :return:
        """
        if ids is None:
            return data
        for trait in data:
            trait["_specialization"] = LazyLoader(
                self.specializations, trait["specialization"]
            )
        return object_parse(data, Trait)

    @endpoint("/v2/legends", has_ids=True)
    async def legends(self, *, data, ids: list = None):
        """
        Get legends by ID(s).
        None returns all IDs.
        :param data:
        :param ids:
        :return:
        """
        if ids is None:
            return data
        for legend in data:
            legend["_swap"] = LazyLoader(self.skills, legend["swap"])
            legend["_heal"] = LazyLoader(self.skills, legend["heal"])
            legend["_elite"] = LazyLoader(self.skills, legend["elite"])
            legend["_utilities"] = LazyLoader(self.skills, *legend["_utilities"])

        return object_parse(data, Legend)
