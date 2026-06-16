from app.agents.roadmap_agent import RoadmapAgent
from app.agents.project_agent import ProjectAgent
from app.agents.curriculum_agent import CurriculumAgent
from app.agents.interview_agent import InterviewAgent
from app.agents.planner_agent import PlannerAgent


def run_workflow(role):

    roadmap = RoadmapAgent().run(role)

    curriculum = CurriculumAgent().run(
        roadmap["modules"]
    )

    projects = ProjectAgent().run(role)

    interviews = InterviewAgent().run(
        roadmap["modules"]
    )

    planner = PlannerAgent().run(
        role,
        roadmap["modules"]
    )

    return {
        "roadmap": roadmap,
        "curriculum": curriculum,
        "projects": projects,
        "interviews": interviews,
        "planner": planner
    }