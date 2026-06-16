from app.agents.roadmap_agent import RoadmapAgent
from app.agents.project_agent import ProjectAgent
from app.agents.curriculum_agent import CurriculumAgent


def run_workflow(role):

    roadmap = RoadmapAgent().run(role)

    curriculum = CurriculumAgent().run(
        roadmap["modules"]
    )

    projects = ProjectAgent().run(role)

    return {
        "roadmap": roadmap,
        "curriculum": curriculum,
        "projects": projects
    }