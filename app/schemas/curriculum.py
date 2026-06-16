from pydantic import BaseModel


class CurriculumModule(BaseModel):

    title: str

    overview: str

    why_it_matters: str

    learning_outcomes: list[str]

    hands_on: list[str]

    interview_questions: list[str]