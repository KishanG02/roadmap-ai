import json

from app.services.llm_service import client
from app.prompts.roadmap_prompt import SYSTEM_PROMPT
from app.schemas.roadmap_output import RoadmapOutput


class RoadmapAgent:

    def run(self, role: str):

        response = client.chat.completions.create(
            model="meta-llama/llama-3.3-70b-instruct",
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": role
                }
            ]
        )

        response_text = response.choices[0].message.content

        roadmap = json.loads(response_text)

        return RoadmapOutput(**roadmap).model_dump()