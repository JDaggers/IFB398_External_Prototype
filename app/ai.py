import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment
openai.api_key = os.getenv("OPENAI_API_KEY")


prompt = "Tell me a fun fact"


def get_fact():
    # Send a prompt using the ChatCompletion API
    response = openai.ChatCompletion.create(
        model="gpt-4",  # or "gpt-4-turbo"
        messages=[{"role": "system", "content": "You are an AI assistant"}, {"role": "user", "content": prompt}],
        max_tokens=500,
    )

    # Print the response
    return response["choices"][0]["message"]["content"]
