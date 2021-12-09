from typing import Optional, List
from pygw2.utils import LazyLoader, BaseModel
from pygw2.core.enums import Professions, Races, StoryFlags


class BiographyAnswer(BaseModel):
    id: str
    title: str
    description: str
    journal: str
    question_: LazyLoader

    @property
    def question(self) -> "BiographyQuestion":
        return self.question_()

    professions: Optional[List[Professions]]
    races: Optional[List[Races]]


class BiographyQuestion(BaseModel):
    id: int
    title: str
    description: str
    answers_: LazyLoader

    @property
    def answers(self) -> List["BiographyAnswer"]:
        return self.answers_()

    order: int
    races: Optional[List[Races]]
    professions: Optional[List[Professions]]


class StoryChapter(BaseModel):
    name: str


class Story(BaseModel):
    id: int
    season_: LazyLoader

    @property
    def season(self) -> "Season":
        return self.season_()

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
    stories_: LazyLoader

    @property
    def stories(self) -> List["Story"]:
        return self.stories_()


class QuestGoal(BaseModel):
    active: str
    complete: str


class Quest(BaseModel):
    id: int
    name: str
    level: int
    story_: LazyLoader

    @property
    def story(self) -> "Story":
        return self.story_()

    goals: List[QuestGoal]
