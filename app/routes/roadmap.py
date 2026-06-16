from fastapi import APIRouter

from app.schemas.roadmap import RoadmapRequest
from app.services.roadmap_service import generate_roadmap

router = APIRouter()


@router.post("/generate")
def generate(data: RoadmapRequest):

    result = generate_roadmap(data.role)

    return {
        "content": result
    }