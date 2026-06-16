from app.services.ocr_service import extract_text
from app.agents.topic_extractor_agent import TopicExtractorAgent
from app.agents.roadmap_agent import RoadmapAgent

def ocr_node(state):

    text = extract_text(state["image_path"])

    state["ocr_text"] = text

    return state

def topic_node(state):

    result = TopicExtractorAgent().run(
        state["ocr_text"]
    )

    state["role"] = result["role"]

    state["topics"] = result["topics"]

    return state

def roadmap_node(state):

    roadmap = RoadmapAgent().run(
        state["role"]
    )

    state["roadmap"] = roadmap

    return state