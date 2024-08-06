from models.llama_model import get_llama_response
from models.chatgpt_model import get_chatgpt_response

def handle_query(query):
    # Process the query using both models
    llama_response = get_llama_response(query)
    chatgpt_response = get_chatgpt_response(query)
    
    # Combine responses or choose one
    combined_response = {
        'llama': llama_response,
        'chatgpt': chatgpt_response
    }
    
    return combined_response
