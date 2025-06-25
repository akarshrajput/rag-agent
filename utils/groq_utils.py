import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_groq(message: str, model: str = "llama3-8b-8192") -> str:
    """
    Send a chat completion request to GroqCloud and return the response text.
    """
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message},
            ],
            model=model,
            temperature=0.7,
            max_tokens=256,
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        print(f"Groq API call failed: {e}")
        return f"Error: {e}"
