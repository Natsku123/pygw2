from __future__ import annotations
from typing import ForwardRef

from pygw2.utils import LazyLoader, BaseModel
from pygw2.core.enums import Professions, Races, StoryFlags

BiographyQuestion = ForwardRef("BiographyQuestion")
BiographyAnswer = ForwardRef("BiographyAnswer")
Story = ForwardRef("Story")
Season = ForwardRef("Season")


class BiographyAnswer(BaseModel):
    id: str
    title: str
    description: str
    journal: str
    question_: LazyLoader

    @property
    def question(self) -> BiographyQuestion:
        return self.question_()

    professions: list[Professions] | None
    races: list[Races] | None


class BiographyQuestion(BaseModel):
    id: int
    title: str
    description: str
    answers_: LazyLoader

    @property
    def answers(self) -> list[BiographyAnswer]:
        return self.answers_()

    order: int
    races: list[Races] | None
    professions: list[Professions] | None


class StoryChapter(BaseModel):
    name: str


class Story(BaseModel):
    id: int
    season_: LazyLoader

    @property
    def season(self) -> Season:
        return self.season_()

    name: str
    description: str
    timeline: str
    level: int
    order: int
    chapters: list[StoryChapter]
    races: list[Races] | None
    flags: list[StoryFlags] | None


class Season(BaseModel):
    id: str
    name: str
    order: int
    stories_: LazyLoader

    @property
    def stories(self) -> list[Story]:
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
    def story(self) -> Story:
        return self.story_()

    goals: list[QuestGoal]
