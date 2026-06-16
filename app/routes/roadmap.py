from fastapi import APIRouter

from app.schemas.roadmap import RoadmapRequest

from app.services.roadmap_service import generate_roadmap
from app.services.workflow_service import run_workflow

router = APIRouter()


@router.post("/generate")
def generate(data: RoadmapRequest):

    return generate_roadmap(data.role)


@router.post("/workflow")
def workflow(data: RoadmapRequest):

    return run_workflow(data.role)