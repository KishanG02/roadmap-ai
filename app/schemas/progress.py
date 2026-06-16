from pydantic import BaseModel


class ProgressRequest(BaseModel):

    role: str

    module: str

    chapter: str

    status: str