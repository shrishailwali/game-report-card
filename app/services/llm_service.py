import os
from typing import Any
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


from groq import Groq



# Get API key
_GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize client
client = Groq(api_key=_GROQ_API_KEY) if Groq and _GROQ_API_KEY else None
print(f"LLM client initialized: {bool(client)}")


def generate_report(analytics: Any) -> str:
    """
    Generate a short post-game report using an LLM.

    If the Groq client isn't available or no API key is set,
    returns a deterministic fallback summary.
    """

    prompt = (
        "Generate a professional post-game performance summary.\n"
        f"Analytics data: {analytics}\n"
        "Highlight strengths and mistakes."
    )

    if not client:
        return (
            "(LLM unavailable) Summary: Review completed. "
            "No LLM configured — inspect analytics for details."
        )

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.6,
        )

        choice = response.choices[0]
        return choice.message.content.strip()

    except Exception as exc:
        return f"(LLM error) Could not generate report: {exc}"


# Example test
if __name__ == "__main__":
    sample_analytics = {
        "shots_on_target": 6,
        "possession": "58%",
        "passes_completed": 420,
        "mistakes": ["missed marking", "late tackles"]
    }

    report = generate_report(sample_analytics)
    print("\nGenerated Report:\n")
    print(report)