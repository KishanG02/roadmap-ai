from app.services.ocr_service import extract_text

from app.agents.topic_extractor_agent import TopicExtractorAgent
from app.agents.roadmap_agent import RoadmapAgent
from app.agents.curriculum_agent import CurriculumAgent


def run_image_workflow(image_path: str):

    ocr_text = extract_text(image_path)

    extracted = TopicExtractorAgent().run(ocr_text)

    role = extracted["role"]

    roadmap = RoadmapAgent().run(role)

    curriculum = CurriculumAgent().run(
        roadmap["modules"]
    )

    return {
        "ocr_text": ocr_text,
        "topic_analysis": extracted,
        "roadmap": roadmap,
        "curriculum": curriculum
    }