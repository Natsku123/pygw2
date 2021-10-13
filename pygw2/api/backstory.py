from typing import List, Union

from ..utils import endpoint, object_parse, LazyLoader
from ..core.models.backstory import (
    BiographyAnswer,
    BiographyQuestion,
    Story,
    Season,
    Quest,
)


class BackstoryApi:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.api_key: str = ""

    def setup(self, api_key: str):
        self.api_key = api_key

    @endpoint("/v2/backstory/answers", has_ids=True)
    async def answers(
        self, *, data, ids: list = None
    ) -> List[Union[BiographyAnswer, int, str]]:
        """
        Get Biography answers from API by list of IDs or one ID.
        :param data: Data from wrapper
        :param ids: List of IDs
        :return: list
        """

        if ids is None:
            return data

        for answer in data:
            answer["question_"] = LazyLoader(self.questions, answer["question"])

        return object_parse(data, BiographyAnswer)

    @endpoint("/v2/backstory/questions", has_ids=True)
    async def questions(
        self, *, data, ids: list = None
    ) -> List[Union[BiographyQuestion, int, str]]:
        """
        Get Biography questions from API by list of IDs or one ID.
        :param data: Data from wrapper
        :param ids: List of IDs
        :return: list
        """

        if ids is None:
            return data

        for question in data:
            question["answers_"] = LazyLoader(self.answers, *question["answers"])

        return object_parse(data, BiographyQuestion)

    @endpoint("/v2/stories", has_ids=True)
    async def stories(self, *, data, ids: list = None) -> List[Union[Story, int, str]]:
        """
        Get stories from API by list of IDs or one ID.
        :param data: Data from wrapper
        :param ids: List of IDs
        :return: list
        """

        if ids is None:
            return data

        for story in data:
            story["season_"] = LazyLoader(self.seasons, story["season"])

        return object_parse(data, Story)

    @endpoint("/v2/stories/seasons", has_ids=True)
    async def seasons(self, *, data, ids: list = None) -> List[Union[Season, int, str]]:
        """
        Get seasons from API by list of IDs or one ID.
        :param data: Data from wrapper
        :param ids: List of IDs
        :return: list
        """

        if ids is None:
            return data

        for season in data:
            season["stories_"] = LazyLoader(self.stories, *season["stories"])

        return object_parse(data, Season)

    @endpoint("/v2/quests", has_ids=True)
    async def quests(self, *, data, ids: list = None) -> List[Union[Quest, int, str]]:
        """
        Get quests from API by list of IDs or one ID.
        :param data: Data from wrapper
        :param ids: List of IDs
        :return: list
        """

        if ids is None:
            return data

        for quest in data:
            quest["story_"] = LazyLoader(self.stories, quest["story"])

        return object_parse(data, Quest)
