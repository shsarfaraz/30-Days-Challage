from openai import OpenAI
import json
import re
from dotenv import load_dotenv
import os

# -------- IMPORTANT: NEVER hardcode your real API key in code ----------
# Use environment variable instead:
# setx OPENAI_API_KEY "your_key_here"
# Then use:

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class StudyAgent:

    # ------------------ SUMMARY FUNCTION ------------------
    def summarize(self, text: str) -> str:
        prompt = f"""
        You are an academic assistant. Summarize the following study notes
        into clean, clear, structured paragraphs:

        TEXT:
        {text}
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You generate perfect summaries."},
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content


    # ------------------ QUIZ FUNCTION ------------------
    def create_quiz(self, text: str) -> dict:
        prompt = f"""
        You are a quiz generator AI.
        Generate a quiz in VALID JSON ONLY.

        Output format strictly:

        {{
            "mcq": [
                {{
                    "question": "string",
                    "options": {{
                        "a": "string",
                        "b": "string",
                        "c": "string",
                        "d": "string"
                    }},
                    "answer": "a"
                }}
            ],
            "short_answer": [
                {{
                    "question": "string",
                    "answer": "string"
                }}
            ]
        }}

        Text to generate quiz from:
        {text}
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You output perfectly formatted JSON only."},
                {"role": "user", "content": prompt}
            ]
        )

        raw = response.choices[0].message.content

        # Try extracting JSON using regex
        try:
            json_str = re.search(r"\{[\s\S]*\}", raw).group()
            quiz = json.loads(json_str)
        except Exception as e:
            print("⚠ Quiz JSON parsing failed. Raw output:")
            print(raw)
            quiz = {"mcq": [], "short_answer": []}

        return quiz


# --- Global agent instance ---
root_agent = StudyAgent()
