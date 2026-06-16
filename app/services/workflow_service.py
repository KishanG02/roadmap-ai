from app.agents.roadmap_agent import RoadmapAgent
from app.agents.project_agent import ProjectAgent


def run_workflow(role):

    roadmap = RoadmapAgent().run(role)

    projects = ProjectAgent().run(role)

    return {
        "roadmap": roadmap,
        "projects": projects
    }