import os
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env
load_dotenv()

# Get your Gemini API key from the environment
api_key = os.getenv("GEMINI_API_KEY")

# Initialize Gemini client
client = genai.Client(api_key=api_key)

# Make a request
response = client.models.generate_content(
    model="gemini-2.5-flash",  # Use the latest model you have access to
    contents="What is FastAPI?"
)

print(response.text)
