from typing import TypedDict


class RoadmapState(TypedDict):

    image_path: str

    ocr_text: str

    role: str

    topics: list

    roadmap: dict

    curriculum: dict

    projects: dict

    interviews: dict

    planner: dict