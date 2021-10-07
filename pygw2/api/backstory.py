from typing import List, Union

from ..utils import endpoint, object_parse
from ..core.models.backstory import (
    BiographyAnswer,
    BiographyQuestion,
    Story,
    Season,
    Quest,
)


class BackstoryApi:
    def __init__(self):
        self.api_key: str = ""

    def setup(self, api_key: str):
        self.api_key = api_key

    @endpoint("/v2/backstory/answers", has_ids=True)
    async def answers(
        self, *, data, ids: list = None, deep: bool = True
    ) -> List[Union[BiographyAnswer, int, str]]:
        """
        Get Biography answers from API by list of IDs or one ID.
        :param data: Data from wrapper
        :param ids: List of IDs
        :param deep:
        :return: list
        """

        if ids is None:
            return data

        for answer in data:
            if deep:
                answer["question"] = await self.questions(
                    answer["question"], deep=False
                )
            else:
                del answer["question"]

        return object_parse(data, BiographyAnswer)

    @endpoint("/v2/backstory/questions", has_ids=True)
    async def questions(
        self, *, data, ids: list = None, deep: bool = True
    ) -> List[Union[BiographyQuestion, int, str]]:
        """
        Get Biography questions from API by list of IDs or one ID.
        :param data: Data from wrapper
        :param ids: List of IDs
        :param deep:
        :return: list
        """

        if ids is None:
            return data

        for question in data:
            if deep:
                question["answers"] = await self.answers(
                    *question["answers"], deep=False
                )
            else:
                del question["answers"]

        return object_parse(data, BiographyQuestion)

    @endpoint("/v2/stories", has_ids=True)
    async def stories(
        self, *, data, ids: list = None, deep: bool = True
    ) -> List[Union[Story, int, str]]:
        """
        Get stories from API by list of IDs or one ID.
        :param data: Data from wrapper
        :param ids: List of IDs
        :param deep:
        :return: list
        """

        if ids is None:
            return data

        for story in data:
            if deep:
                story["season"] = await self.seasons(story["season"], deep=False)
            else:
                del story["season"]

        return object_parse(data, Story)

    @endpoint("/v2/stories/seasons", has_ids=True)
    async def seasons(
        self, *, data, ids: list = None, deep: bool = True
    ) -> List[Union[Season, int, str]]:
        """
        Get seasons from API by list of IDs or one ID.
        :param data: Data from wrapper
        :param ids: List of IDs
        :param deep:
        :return: list
        """

        if ids is None:
            return data

        for season in data:
            if deep:
                season["stories"] = await self.stories(*season["stories"], deep=False)
            else:
                del season["stories"]

        return object_parse(data, Season)

    @endpoint("/v2/quests", has_ids=True)
    async def quests(
        self, *, data, ids: list = None, deep: bool = True
    ) -> List[Union[Quest, int, str]]:
        """
        Get quests from API by list of IDs or one ID.
        :param data: Data from wrapper
        :param ids: List of IDs
        :param deep:
        :return: list
        """

        if ids is None:
            return data

        for quest in data:
            if deep:
                quest["story"] = await self.stories(quest["story"])
            else:
                del quest["story"]

        return object_parse(data, Quest)
