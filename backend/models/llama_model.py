from transformers import AutoTokenizer, AutoModelForCausalLM
from huggingface_hub import login
import transformers
import torch
from transformers import pipeline
# Log in to Hugging Face
login(token='LOGIN_KEY')  # Replace with your actual token


 

pipe = pipeline("text-generation", model="meta-llama/Meta-Llama-3.1-8B")
 
# from transformers import AutoTokenizer, AutoModelForCausalLM
model_id = "meta-llama/Meta-Llama-3.1-8B"

pipeline = transformers.pipeline(
    "text-generation", model=model_id, model_kwargs={"torch_dtype": torch.bfloat16}, device_map="auto"
)

pipeline("Hey how are you doing today?")


# Load the LLaMA model and tokenizer
# model_id = "meta-llama/Meta-Llama-3.1-8B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model_id, use_auth_token=True)
model = AutoModelForCausalLM.from_pretrained(model_id, use_auth_token=True)

def get_llama_response(query):
    inputs = tokenizer(query, return_tensors="pt")
    outputs = model.generate(inputs['input_ids'], max_length=100)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response
