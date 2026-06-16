from pydantic import BaseModel


class ChapterRequest(BaseModel):
    module: str
    chapter: str