import os

from dotenv import load_dotenv
from google import genai

from ai.prompts import BUG_REPORT_PROMPT

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)


def generate_bug_report(
    application: str,
    error: str,
) -> str:
    """
    Generate an AI bug report.
    """

    prompt = BUG_REPORT_PROMPT.format(
        application=application,
        error=error,
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    if not response.text:
        raise RuntimeError("Gemini returned an empty response.")

    return response.text