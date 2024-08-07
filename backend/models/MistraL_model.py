import os
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from ratelimit import limits, sleep_and_retry
import time
from dotenv import load_dotenv
import os

load_dotenv()

# openai_api_key = os.getenv('OPENAI_API_KEY')

# # Initialize Mistral client
# api_key = os.getenv("GtcvBNAZojjIj7tFD4eOe2Sy0QQuSDON")
# model = "mistral-large-latest"

# client = MistralClient(api_key=api_key)


# Initialize Mistral client
mistral_api_key = os.getenv('MISTRAL_API_KEY')   # Get API key from environment variable

if not mistral_api_key:
    raise ValueError("API key is missing. Set the MISTRAL_API_KEY environment variable.")

model = "mistral-large-latest"
client = MistralClient(api_key=mistral_api_key)

# Track the last request time
last_request_time = 0
request_interval = 60  # Interval in seconds

def get_mistral_response(prompt):
    """
    Get a response from the Mistral model for a given user message.
    """
    global last_request_time

    current_time = time.time()
    elapsed_time = current_time - last_request_time
    
    if elapsed_time < request_interval:
        time.sleep(request_interval - elapsed_time)

    messages = [ChatMessage(role="user", content=prompt)]
    
    try:
        chat_response = client.chat(
            model=model,
            messages=messages,
        )
        response_content = chat_response.choices[0].message.content
        
        # Add specific logic for stress and anxiety relief
        if "stress" in prompt.lower() or "anxiety" in prompt.lower():
            response_content += "\nHere are some tips to manage stress and anxiety:\n- Practice deep breathing exercises.\n- Try mindfulness or meditation.\n- Engage in physical activity like walking or yoga.\n- Talk to a mental health professional if needed."

        return response_content
    except Exception as e:
        return f"Error: {str(e)}"