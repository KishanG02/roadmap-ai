from pydantic import BaseModel


class LearningPathRequest(BaseModel):

    role: str

    module: str

    chapter: str

    chapter_order: int