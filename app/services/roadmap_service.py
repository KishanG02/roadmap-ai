from app.prompts.roadmap_prompt import SYSTEM_PROMPT
from app.services.llm_service import client


def generate_roadmap(role):

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

    return response.choices[0].message.content