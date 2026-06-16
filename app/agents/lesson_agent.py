import json

from app.services.llm_service import client


class LessonAgent:

    def run(self, module, chapter):

        prompt = f"""
You are an expert technical instructor.

Create a detailed lesson.

Module:
{module}

Chapter:
{chapter}

Generate:

1. Introduction
2. Learning Objectives
3. Core Concepts
4. Real World Analogy
5. Real World Use Cases
6. Code Examples
7. Common Mistakes
8. Best Practices
9. Summary

Return ONLY valid JSON.

Format:

{{
    "chapter": "",
    "lesson": {{
        "introduction": "",
        "learning_objectives": [],
        "core_concepts": [],
        "real_world_analogy": "",
        "real_world_use_cases": [],
        "code_examples": [],
        "common_mistakes": [],
        "best_practices": [],
        "summary": ""
    }}
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
            response_text = response_text[start:end + 1]

        return json.loads(response_text)