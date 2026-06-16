from pydantic import BaseModel


class LearnRequest(BaseModel):

    module: str

    chapter: str