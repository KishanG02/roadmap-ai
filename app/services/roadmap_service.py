from app.agents.roadmap_agent import RoadmapAgent


def generate_roadmap(role):

    agent = RoadmapAgent()

    return agent.run(role)