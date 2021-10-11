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
from helpers import test_with_ids


class BackStoryTests(aiounittest.AsyncTestCase):
    async def test_answers(self):
        await test_with_ids(self, api.backstory.answers, BiographyAnswer)

    async def test_questions(self):
        await test_with_ids(self, api.backstory.questions, BiographyQuestion)

    async def test_stories(self):
        await test_with_ids(self, api.backstory.stories, Story)

    async def test_seasons(self):
        await test_with_ids(self, api.backstory.seasons, Season)

    async def test_quests(self):
        await test_with_ids(self, api.backstory.quests, Quest)


if __name__ == "__main__":
    unittest.main()
