from pydantic import BaseModel


class RoadmapRequest(BaseModel):
    role: str