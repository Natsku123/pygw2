from pygw2.api import api
from pygw2.core.models.backstory import (
    BiographyAnswer,
    BiographyQuestion,
    Story,
    Season,
    Quest,
)

import unittest
import aiounittest
from tests.helpers import ids_helper


class BackStoryTests(aiounittest.AsyncTestCase):
    async def test_answers(self):
        await ids_helper(self, api.backstory.answers, BiographyAnswer)

    async def test_questions(self):
        await ids_helper(self, api.backstory.questions, BiographyQuestion)

    async def test_stories(self):
        await ids_helper(self, api.backstory.stories, Story)

    async def test_seasons(self):
        await ids_helper(self, api.backstory.seasons, Season)

    async def test_quests(self):
        await ids_helper(self, api.backstory.quests, Quest)


if __name__ == "__main__":
    unittest.main()
