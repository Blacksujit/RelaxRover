# from huggingface_hub import InferenceClient
# from dotenv import load_dotenv
# import os

# load_dotenv()



# # Initialize the client
# client = InferenceClient(
#     "meta-llama/Meta-Llama-3.1-8B-Instruct",
    # token=os.getenv('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'),
# )

# def get_llama_response(user_message):
#     """
#     Get a response from the LLaMA model for a given user message.
#     """
#     prompt = [{"role": "user", "content": user_message}]
    
#     response = ""
#     try:
#         # Fetch response from model
#         for message in client.chat_completion(
#             messages=prompt,
#             max_tokens=500,
#             stream=False  # Set to True if you want streaming responses
#         ):
#             response += message.choices[0].content  # Adjust based on actual response structure
        
#         # Add additional features based on response
#         if "anxiety" in user_message.lower():
#             additional_message = "Here are some breathing exercises you can try..."
#             response += "\n" + additional_message
        
#         if "motivation" in user_message.lower():
#             motivational_quote = "Believe in yourself! Every day is a new opportunity."
#             response += "\n" + motivational_quote

#     except Exception as e:
#         print(f"Error fetching response: {e}")
#         response = "Sorry, I encountered an error processing your request."

#     return response
