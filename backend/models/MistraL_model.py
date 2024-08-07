import os
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from ratelimit import limits, sleep_and_retry
import time

# # Initialize Mistral client
# api_key = os.getenv("GtcvBNAZojjIj7tFD4eOe2Sy0QQuSDON")
# model = "mistral-large-latest"

# client = MistralClient(api_key=api_key)


# Initialize Mistral client
api_key =  'GtcvBNAZojjIj7tFD4eOe2Sy0QQuSDON'  # Get API key from environment variable

if not api_key:
    raise ValueError("API key is missing. Set the MISTRAL_API_KEY environment variable.")

model = "mistral-large-latest"
client = MistralClient(api_key=api_key)

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
        last_request_time = time.time()  # Update the last request time
        return chat_response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"
