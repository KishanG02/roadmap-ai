import json

from app.services.llm_service import client


class LearningModuleAgent:

    def run(self, topics):

        prompt = f"""
You are an expert curriculum designer.

Create learning modules from these topics:

{topics}

For each topic generate:

1. Module Name
2. Estimated Days
3. Chapters in correct learning order

Return ONLY valid JSON.

Format:

{{
  "modules":[
    {{
      "module":"",
      "estimated_days":0,
      "chapters":[]
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

        start = response_text.find("{")
        end = response_text.rfind("}")

        if start != -1 and end != -1:
            response_text = response_text[start:end+1]

        return json.loads(response_text)