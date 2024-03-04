import openai
import requests

from typing import Type

import os
from dotenv import load_dotenv

try:
    from .PromptInputs import *
except ImportError:
    from PromptInputs import *

class LLMCaller:
    def __init__(self, name:str):
        pass

    def update_api_key_from_env_file(self):
        pass
    
    def get_JSON_output_from_API_call(self, prompt_input: Type[PromptInput]):
        pass

    def get_model_output(self):
        pass

class HuggingfaceLLMCaller(LLMCaller):
    def __init__(self, name, LLM_API_ENDPOINT):
        self.name = name
        self.LLM_API_ENDPOINT = LLM_API_ENDPOINT
        self.update_api_key_from_env_file()
    
    def update_api_key_from_env_file(self):
        load_dotenv()
        self.HUGGINGFACE_API_KEY = os.environ.get("HUGGINGFACE_API_KEY")

class LLMWithGeneratedText(HuggingfaceLLMCaller):
    def __init__(self, name, LLM_API_ENDPOINT):
        super().__init__(name, LLM_API_ENDPOINT)
    
    def get_JSON_output_from_API_call(self, prompt):
        headers = {"Authorization": f"Bearer {self.HUGGINGFACE_API_KEY}"}
        payload = {"inputs": prompt,
                   "options": {"wait_for_model": True},
                   "parameters": {"return_full_text": False,
                                  "max_new_tokens": 250
                   }}
        return requests.post(self.LLM_API_ENDPOINT, 
                             headers=headers, 
                             json=payload).json()
    
    def get_model_output(self, prompt_input: Type[PromptInput]):
        LLM_output = self.get_JSON_output_from_API_call(prompt_input)
        return LLM_output[0]['generated_text']
    
class MixtralLLM(LLMWithGeneratedText):
    def __init__(self):
        name = 'Mixtral-8x7B-Instruct-v0.1'
        LLM_API_ENDPOINT = 'https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1'
        
        super().__init__(name, LLM_API_ENDPOINT)
    
    def get_JSON_output_from_API_call(self, prompt):
        headers = {"Authorization": f"Bearer {self.HUGGINGFACE_API_KEY}"}
        payload = {"inputs": prompt,
                   "options": {"wait_for_model": True},
                   "parameters": {"return_full_text": False,
                                  "max_new_tokens": 250
                   }}
        return requests.post(self.LLM_API_ENDPOINT, 
                             headers=headers, 
                             json=payload).json()
    
    def get_model_output(self, prompt_input: Type[PromptInput]):
        LLM_output = self.get_JSON_output_from_API_call(prompt_input)
        return LLM_output[0]['generated_text']
    
# class LLMWithCandidateLabels(HuggingfaceLLMCaller):
#     def __init__(self, LLM_API_ENDPOINT):
#         super().__init__(LLM_API_ENDPOINT)
    
#     def get_JSON_output_from_API_call(self, prompt_input: Type[PromptInput]):
#         headers = {"Authorization": f"Bearer {self.HUGGINGFACE_API_KEY}"}
#         prompt = prompt_input.generate_prompt()
#         payload = {"inputs": prompt,
#                 "parameters": {"candidate_labels": prompt_input.candidate_labels},
#                 "options": {"wait_for_model": True}}
#         return requests.post(self.LLM_API_ENDPOINT, 
#                              headers=headers, 
#                              json=payload).json()

#     def get_model_output(self, prompt_input: Type[PromptInput]):
#         LLM_output = self.get_JSON_output_from_API_call(prompt_input)
#         max_score_index = LLM_output['scores'].index(max(LLM_output['scores']))
#         predicted_label = LLM_output['labels'][max_score_index]

#         return predicted_label

class OpenAILLM(LLMCaller):
    def __init__(self):
        self.name = 'gpt-3.5-turbo'
        self.update_api_key_from_env_file()
        self.temperature = 0.1
        self.max_tokens = 300

    def update_api_key_from_env_file(self):
        load_dotenv()
        openai.api_key = os.environ.get("OPENAI_API_KEY")

    def get_JSON_output_from_API_call(self, prompt):
        messages = [{"role": "user", "content": prompt}]

        # TODO: Vary max_tokens based on prompt and test different temperatures.
        # NOTE: Lower temperature means more deterministic output.
        LLM_output = openai.ChatCompletion.create(model="gpt-3.5-turbo", 
                                            messages=messages, 
                                            temperature=self.temperature, 
                                            max_tokens=self.max_tokens)
        return LLM_output
    
    def get_model_output(self, prompt):
        LLM_output = self.get_JSON_output_from_API_call(prompt)
        return LLM_output.choices[0].message["content"]