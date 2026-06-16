import json
import re

from app.services.llm_service import client


class PlannerAgent:

    def run(self, role, modules):

        prompt = f"""
You are an expert learning roadmap planner.

Create:

1. 30 Day Learning Plan
2. 60 Day Learning Plan
3. 90 Day Learning Plan

Based on:

Role:
{role}

Modules:
{modules}

IMPORTANT RULES:

- Return ONLY valid JSON.
- Do NOT return markdown.
- Do NOT return explanations.
- Do NOT return comments.
- Use day_range as a STRING.
- NEVER use: "day": 1-5
- ALWAYS use: "day_range": "1-5"

Example:

{{
  "30_day_plan": [
    {{
      "day_range": "1-5",
      "module": "Python Programming",
      "level": "Beginner"
    }}
  ],

  "60_day_plan": [
    {{
      "day_range": "1-10",
      "module": "Python Programming",
      "level": "Beginner"
    }}
  ],

  "90_day_plan": [
    {{
      "day_range": "1-15",
      "module": "Python Programming",
      "level": "Beginner"
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

        print("=" * 50)
        print("RAW PLANNER RESPONSE")
        print(response_text)
        print("=" * 50)

        # Remove markdown wrappers
        response_text = (
            response_text
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        # Auto-fix invalid day ranges if model returns:
        # {"day": 1-5}
        response_text = re.sub(
            r'"day"\s*:\s*(\d+)-(\d+)',
            r'"day_range":"\1-\2"',
            response_text
        )

        # Extract JSON block
        start = response_text.find("{")
        end = response_text.rfind("}")

        if start != -1 and end != -1:
            response_text = response_text[start:end + 1]

        try:
            return json.loads(response_text)

        except Exception as e:

            print("=" * 50)
            print("JSON ERROR")
            print(response_text)
            print("=" * 50)

            raise e