from app.agents.roadmap_agent import RoadmapAgent
from app.agents.project_agent import ProjectAgent
from app.agents.curriculum_agent import CurriculumAgent
from app.agents.interview_agent import InterviewAgent
from app.agents.planner_agent import PlannerAgent
from app.agents.learning_module_agent import LearningModuleAgent

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
    
    learning_modules = LearningModuleAgent().run(
        roadmap["modules"]
    )

    return {
        "roadmap": roadmap,
        "learning_modules": learning_modules,
        "curriculum": curriculum,
        "projects": projects,
        "interviews": interviews,
        "planner": planner
    }