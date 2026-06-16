import json

from app.services.llm_service import client


class QuizAgent:

    def run(self, module, chapter):

        prompt = f"""
Create 10 MCQs.

Module:
{module}

Chapter:
{chapter}

Return ONLY valid JSON.

Format:

{{
    "mcqs":[
        {{
            "question":"",
            "options":[],
            "answer":""
        }}
    ]
}}
"""

        response = client.chat.completions.create(
            model="meta-llama/llama-3.3-70b-instruct",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        response_text = response.choices[0].message.content

        response_text = (
            response_text
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        start = response_text.find("{")
        end = response_text.rfind("}")

        if start != -1 and end != -1:
            response_text = response_text[start:end+1]

        return json.loads(response_text)