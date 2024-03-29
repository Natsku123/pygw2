import pytest
from pygw2.models import *

import unittest
import aiounittest
from tests.helpers import ids_helper


@pytest.mark.usefixtures("get_api")
class BackStoryTests(aiounittest.AsyncTestCase):
    async def test_answers(self):
        await ids_helper(self, self.api.backstory.answers, BiographyAnswer)

    async def test_questions(self):
        await ids_helper(self, self.api.backstory.questions, BiographyQuestion)

    async def test_stories(self):
        await ids_helper(self, self.api.backstory.stories, Story)

    async def test_seasons(self):
        await ids_helper(self, self.api.backstory.seasons, Season)

    async def test_quests(self):
        await ids_helper(self, self.api.backstory.quests, Quest)


if __name__ == "__main__":
    unittest.main()
