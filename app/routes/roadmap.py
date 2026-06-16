import shutil

from fastapi import APIRouter
from fastapi import UploadFile, File

from app.schemas.roadmap import RoadmapRequest

from app.services.roadmap_service import generate_roadmap
from app.services.workflow_service import run_workflow
from app.services.ocr_service import extract_text

router = APIRouter()


@router.post("/generate")
def generate(data: RoadmapRequest):

    return generate_roadmap(data.role)


@router.post("/workflow")
def workflow(data: RoadmapRequest):

    return run_workflow(data.role)

@router.post("/upload-roadmap")
async def upload_roadmap( file: UploadFile = File(...) ):

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    extracted_text = extract_text(file_path)

    return {
        "filename": file.filename,
        "ocr_text": extracted_text
    }
