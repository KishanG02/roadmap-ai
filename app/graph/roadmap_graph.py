from langgraph.graph import StateGraph

from app.graph.state import RoadmapState

from app.graph.nodes import (
    ocr_node,
    topic_node,
    roadmap_node
)

builder = StateGraph(RoadmapState)

builder.add_node(
    "ocr",
    ocr_node
)

builder.add_node(
    "topic",
    topic_node
)

builder.add_node(
    "roadmap",
    roadmap_node
)

builder.add_edge(
    "ocr",
    "topic"
)

builder.add_edge(
    "topic",
    "roadmap"
)

builder.set_entry_point("ocr")

graph = builder.compile()

def run_graph(image_path):

    return graph.invoke(
        {
            "image_path": image_path
        }
    )