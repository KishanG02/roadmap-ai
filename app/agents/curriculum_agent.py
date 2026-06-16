from app.services.llm_service import client
import json


class CurriculumAgent:

    def run(self, modules):

        prompt = f"""
Generate curriculum for:

{modules}

IMPORTANT:

Return ONLY valid JSON.

Do not include markdown.

Do not include explanations.

Do not include text before or after JSON.

Format:

{{
  "modules": [
    {{
      "title": "",
      "overview": "",
      "hands_on": []
    }}
  ]
}}
"""

        response = client.chat.completions.create(
            model="meta-llama/llama-3.3-70b-instruct",
            messages=[
                {
                    "role":"user",
                    "content":prompt
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

        return json.loads(response_text)