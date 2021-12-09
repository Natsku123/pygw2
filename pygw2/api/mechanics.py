from ..core.models.account import MountType, Mastery, Pet, Legendary
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

from typing import Union, List


class MechanicsMountsApi:
    _instances = {}

    def __new__(cls, *args, api_key: str = "", **kwargs):
        if api_key not in cls._instances:
            cls._instances[api_key] = super().__new__(cls, *args, **kwargs)
        return cls._instances[api_key]

    def __init__(self, *, api_key: str = ""):
        self.api_key: str = api_key

    @endpoint("/v2/mounts/skins", has_ids=True)
    async def skins(
        self, *, data, ids: list = None
    ) -> Union[MountSkin, List[MountSkin], List[str], List[int]]:
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
    async def types(
        self, *, data, ids: list = None
    ) -> Union[MountType, List[MountType], List[str], List[int]]:
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
    _instances = {}

    def __new__(cls, *args, api_key: str = "", **kwargs):
        if api_key not in cls._instances:
            cls._instances[api_key] = super().__new__(cls, *args, **kwargs)
        return cls._instances[api_key]

    def __init__(self, *, api_key: str = ""):
        self.api_key: str = api_key
        self._mounts = MechanicsMountsApi(api_key=api_key)

    @property
    def mounts(self) -> MechanicsMountsApi:
        return self._mounts

    @endpoint("/v2/masteries", has_ids=True)
    async def masteries(
        self, *, data, ids: list = None
    ) -> Union[Mastery, List[Mastery], List[str], List[int]]:
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
    async def outfits(
        self, *, data, ids: list = None
    ) -> Union[Outfit, List[Outfit], List[str], List[int]]:
        """
        Get outfits by ID(s).
        None returns all IDs.
        :param data:
        :param ids:
        :return:
        """
        from .items import ItemsApi

        items_api = ItemsApi(api_key=self.api_key)

        if ids is None:
            return data

        for o in data:
            o["unlock_items_"] = LazyLoader(items_api.get, *o["unlock_items"])

        return object_parse(data, Outfit)

    @endpoint("/v2/pets", has_ids=True)
    async def pets(
        self, *, data, ids: list = None
    ) -> Union[Pet, List[Pet], List[str], List[int]]:
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
    async def professions(
        self, *, data, ids: list = None
    ) -> Union[Profession, List[Profession], List[str], List[int]]:
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
            p["specializations_"] = LazyLoader(
                self.specializations, *p["specializations"]
            )
            for w in p["weapons"].values():
                if "specialization" in w and w["specialization"]:
                    w["specialization_"] = LazyLoader(
                        self.specializations, w["specialization"]
                    )
                for s in w["skills"]:
                    s["skill_"] = LazyLoader(self.skills, s["id"])
            for t in p["training"]:
                t["skill_"] = LazyLoader(self.skills, t["id"])
                t["specialization_"] = LazyLoader(self.specializations, t["id"])

                if "tracks" in t:
                    for track in t["tracks"]:
                        if "skill_id" in track and track["skill_id"]:
                            track["skill_"] = LazyLoader(self.skills, track["skill_id"])
                        if "trait_id" in track and track["trait_id"]:
                            track["trait_"] = LazyLoader(self.traits, track["trait_id"])
        return object_parse(data, Profession)

    @endpoint("/v2/races", has_ids=True)
    async def races(
        self, *, data, ids: list = None
    ) -> Union[Race, List[Race], List[str], List[int]]:
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
            r["skills_"] = LazyLoader(self.skills, r["skills"])
        return object_parse(data, Race)

    @endpoint("/v2/specializations", has_ids=True)
    async def specializations(
        self, *, data, ids: list = None
    ) -> Union[Specialization, List[Specialization], List[str], List[int]]:
        """

        :param data:
        :param ids:
        :return:
        """
        if ids is None:
            return data

        for s in data:
            s["minor_traits_"] = LazyLoader(self.traits, *s["minor_traits"])
            s["major_traits_"] = LazyLoader(self.traits, *s["major_traits"])

        return object_parse(data, Specialization)

    @endpoint("/v2/skills", has_ids=True)
    async def skills(
        self, *, data, ids: list = None
    ) -> Union[Skill, List[Skill], List[str], List[int]]:
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
            if "flip_skill" in s and s["flip_skill"]:
                s["flip_skill_"] = LazyLoader(self.skills, s["flip_skill"])
            if "next_chain" in s and s["next_chain"]:
                s["next_chain_"] = LazyLoader(self.skills, s["next_chain"])
            if "prev_chain" in s and s["prev_chain"]:
                s["prev_chain_"] = LazyLoader(self.skills, s["prev_chain"])
            if "transform_skills" in s and s["transform_skills"]:
                s["transform_skills_"] = LazyLoader(self.skills, *s["transform_skills"])
            if "bundle_skills" in s and s["bundle_skills"]:
                s["bundle_skills_"] = LazyLoader(self.skills, *s["bundle_skills"])
            if "toolbelt_skill" in s and s["toolbelt_skill"]:
                s["toolbelt_skill_"] = LazyLoader(self.skills, *s["toolbelt_skill"])

            if "traited_facts" in s and s["traited_facts"]:
                for tf in s["traited_facts"]:
                    tf["requires_trait_"] = LazyLoader(
                        self.traits, tf["requires_trait"]
                    )
        return object_parse(data, Skill)

    @endpoint("/v2/traits", has_ids=True)
    async def traits(
        self, *, data, ids: list = None
    ) -> Union[Trait, List[Trait], List[str], List[int]]:
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
            trait["specialization_"] = LazyLoader(
                self.specializations, trait["specialization"]
            )
        return object_parse(data, Trait)

    @endpoint("/v2/legends", has_ids=True)
    async def legends(
        self, *, data, ids: list = None
    ) -> Union[Legend, List[Legend], List[str], List[int]]:
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
            legend["swap_"] = LazyLoader(self.skills, legend["swap"])
            legend["heal_"] = LazyLoader(self.skills, legend["heal"])
            legend["elite_"] = LazyLoader(self.skills, legend["elite"])
            legend["utilities_"] = LazyLoader(self.skills, *legend["utilities"])

        return object_parse(data, Legend)

    @endpoint("/v2/legendaryarmory", has_ids=True)
    async def legendary_armory(
        self, *, data, ids: list = None
    ) -> Union[Legendary, List[Legendary], List[str], List[int]]:
        """
        Get Legendary Armory items by ID(s).
        None returns all IDs.
        :param data:
        :param ids:
        :return:
        """
        if ids is None:
            return data

        from .items import ItemsApi

        items_api = ItemsApi(api_key=self.api_key)

        for item in data:
            item["item_"] = LazyLoader(items_api.get, item["id"])

        return object_parse(data, Legendary)
