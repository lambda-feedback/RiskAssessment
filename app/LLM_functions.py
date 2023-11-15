from environs import Env
import openai
import requests

env = Env()
env.read_env()

openai.api_key = env.str("OPEN_AI_API_KEY")
hugging_face_token = env.str("HUGGINGFACE_API_KEY")

def get_completion_with_open_ai(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]

    response = openai.ChatCompletion.create(model=model, messages=messages, temperature=0)

    return response.choices[0].message["content"]

def get_completion_with_llama(prompt):
    API_URL = "https://api-inference.huggingface.co/models/meta-llama/Llama-2-7b-chat-hf"
    headers = {"Authorization": f"Bearer {hugging_face_token}"}
    payload = {"inputs": prompt}
    output = requests.post(API_URL, headers=headers, json=payload).json()
    return output[0]['generated_text']
    
def get_completion_with_DeBERTa(prompt):
    API_URL = "https://api-inference.huggingface.co/models/MoritzLaurer/DeBERTa-v3-base-mnli-fever-anli"
    headers = {"Authorization": f"Bearer {hugging_face_token}"}
    payload = {
        "inputs": prompt,
        "parameters": {"candidate_labels": ["Yes", "No"]},
        "options": {"wait_for_model": False}}
    output = requests.post(API_URL, headers=headers, json=payload).json()
    
    max_score_index = output['scores'].index(max(output['scores']))
    predicted_label = output['labels'][max_score_index]

    return predicted_label