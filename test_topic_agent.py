from app.agents.topic_extractor_agent import TopicExtractorAgent

sample = """
Python
Machine Learning
Deep Learning
NLP
RAG
Agents
"""

result = TopicExtractorAgent().run(sample)

print(result)