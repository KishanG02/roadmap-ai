import json

from app.services.llm_service import client


class InterviewAgent:

    def run(self, modules):

        prompt = f"""
Generate interview questions for:

{modules}

For every module provide:

- Beginner question
- Intermediate question
- Advanced question

Return ONLY valid JSON.

Format:

{{
  "questions":[
    {{
      "module":"",
      "level":"",
      "question":"",
      "answer":""
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
            response_text = response_text[start:end + 1]

        return json.loads(response_text)