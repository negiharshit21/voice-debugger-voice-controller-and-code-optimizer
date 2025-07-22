import openai
from config import GEMINI_API_KEY

openai.api_key = GEMINI_API_KEY

def compile_and_debug(code):
    prompt = f"""
You're a code assistant. Analyze this code and explain any errors line by line. Suggest corrections.

Code:
{code}
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']