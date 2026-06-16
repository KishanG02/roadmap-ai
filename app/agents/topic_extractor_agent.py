import json

from app.services.llm_service import client


class TopicExtractorAgent:

    def run(self, ocr_text: str):

        prompt = f"""
You are an expert roadmap analyzer.

OCR Text:

{ocr_text}

Tasks:

1. Identify role name
2. Extract topics
3. Remove duplicates
4. Arrange topics in learning order

Return ONLY valid JSON.

Format:

{{
    "role": "",
    "topics": []
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

        return json.loads(response_text)