import aiounittest
import unittest
import pytest

from pygw2.models import *

from .helpers import ids_helper


@pytest.mark.usefixtures("get_api")
class MechanicsTests(aiounittest.AsyncTestCase):
    async def test_masteries(self):
        await ids_helper(self, self.api.mechanics.masteries, Mastery)

    async def test_outfits(self):
        await ids_helper(self, self.api.mechanics.outfits, Outfit)

    async def test_pets(self):
        await ids_helper(self, self.api.mechanics.pets, Pet)

    async def test_professions(self):
        await ids_helper(self, self.api.mechanics.professions, Profession)

    async def test_races(self):
        await ids_helper(self, self.api.mechanics.races, Race)

    async def test_specializations(self):
        await ids_helper(self, self.api.mechanics.specializations, Specialization)

    async def test_skills(self):
        await ids_helper(self, self.api.mechanics.skills, Skill)

    async def test_traits(self):
        await ids_helper(self, self.api.mechanics.traits, Trait)

    async def test_legends(self):
        await ids_helper(self, self.api.mechanics.legends, Legend)


@pytest.mark.usefixtures("get_api")
class MechanicsMountsTests(aiounittest.AsyncTestCase):
    async def test_skins(self):
        await ids_helper(self, self.api.mechanics.mounts.skins, MountSkin)

    async def test_types(self):
        await ids_helper(self, self.api.mechanics.mounts.types, MountType)
