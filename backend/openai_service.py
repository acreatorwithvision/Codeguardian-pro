import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_code(code_snippet):
    try:
        response = openai.Completion.create(
          engine="davinci-codex",
          prompt=code_snippet,
          max_tokens=150,
          n=1,
          stop=None,
          temperature=0.5
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return str(e)
