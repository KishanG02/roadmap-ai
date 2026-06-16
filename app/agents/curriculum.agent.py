from app.services.llm_service import client


class CurriculumAgent:

    def run(self, modules):

        prompt = f"""
Generate curriculum for:

{modules}

Return JSON.
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

        return response.choices[0].message.content