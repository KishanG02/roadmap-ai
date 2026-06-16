from pydantic import BaseModel


class LessonRequest(BaseModel):
    module: str
    chapter: str