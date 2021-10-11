from typing import Optional, List
from pydantic import BaseModel
from pygw2.core.enums import Professions, Races, StoryFlags


class BiographyAnswer(BaseModel):
    id: str
    title: str
    description: str
    journal: str
    question: Optional["BiographyQuestion"]
    professions: Optional[List[Professions]]
    races: Optional[List[Races]]


class BiographyQuestion(BaseModel):
    id: int
    title: str
    description: str
    answers: Optional[List[BiographyAnswer]]
    order: int
    races: Optional[List[Races]]
    professions: Optional[List[Professions]]


class StoryChapter(BaseModel):
    name: str


class Story(BaseModel):
    id: int
    season: Optional["Season"]
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
    stories: Optional[List[Story]]


class QuestGoal(BaseModel):
    active: str
    complete: str


class Quest(BaseModel):
    id: int
    name: str
    level: int
    story: Story
    goals: List[QuestGoal]
