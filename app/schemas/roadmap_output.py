from pydantic import BaseModel


class Module(BaseModel):
    title: str
    level: str


class Project(BaseModel):
    title: str
    difficulty: str


class RoadmapOutput(BaseModel):
    role: str
    modules: list[Module]
    projects: list[Project]