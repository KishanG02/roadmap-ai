import json

from app.services.llm_service import client


class ChapterAgent:

    def run(self, module, chapter):

        prompt = f"""
You are a world-class technical instructor.

Create a complete learning lesson.

Module:
{module}

Chapter:
{chapter}

Generate:

1. Overview
2. Why It Matters
3. Theory
4. Examples
5. Hands-On Exercises
6. Assignments
7. Quiz
8. Revision Notes

Return ONLY valid JSON.

Format:

{{
  "chapter": "",

  "overview": "",

  "why_it_matters": "",

  "theory": "",

  "examples": [],

  "hands_on": [],

  "assignment": [],

  "quiz": [],

  "revision_notes": []
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