from typing import Optional, List
from pydantic import BaseModel
from pygw2.utils import LazyLoader
from pygw2.core.enums import Professions, Races, StoryFlags


class BiographyAnswer(BaseModel):
    id: str
    title: str
    description: str
    journal: str
    _question: LazyLoader

    @property
    def question(self) -> "BiographyQuestion":
        return self._question()

    professions: Optional[List[Professions]]
    races: Optional[List[Races]]


class BiographyQuestion(BaseModel):
    id: int
    title: str
    description: str
    _answers: LazyLoader

    @property
    def answers(self) -> List["BiographyAnswer"]:
        return self._answers()

    order: int
    races: Optional[List[Races]]
    professions: Optional[List[Professions]]


class StoryChapter(BaseModel):
    name: str


class Story(BaseModel):
    id: int
    _season: LazyLoader

    @property
    def season(self) -> "Season":
        return self._season()

    name: str
    description: str
    timeline: str
    level: int
    order: int
    chapters: List[StoryChapter]
    races: Optional[List[Races]]
    flags: Optional[List[StoryFlags]]


class Season(BaseModel):
    id: str
    name: str
    order: int
    _stories: LazyLoader

    @property
    def stories(self) -> List["Story"]:
        return self._stories()


class QuestGoal(BaseModel):
    active: str
    complete: str


class Quest(BaseModel):
    id: int
    name: str
    level: int
    _story: LazyLoader

    @property
    def story(self) -> "Story":
        return self._story()

    goals: List[QuestGoal]
