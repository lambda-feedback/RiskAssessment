import openai
import requests

from typing import Type

import os
from dotenv import load_dotenv

try:
    from .PromptInputs import *
except ImportError:
    from PromptInputs import *

class ModelOutputAndExpectedOutput:
    def __init__(self, model_output, expected_output):
        self.model_output = model_output
        self.expected_output = expected_output

class HuggingfaceLLMCaller:
    def __init__(self, LLM_API_ENDPOINT):
        self.LLM_API_ENDPOINT = LLM_API_ENDPOINT
         # NOTE: Don't need to pass self as input to calls of methods within a class 
         # as it is automatically passed in, i.e. it is not self.update_api_key_from_env_file(self) but:
        self.update_api_key_from_env_file()

    def update_api_key_from_env_file(self):
            
        load_dotenv()

        self.HUGGINGFACE_API_KEY = os.environ.get("HUGGINGFACE_API_KEY")
    
    def get_JSON_output_from_API_call(self, prompt_input: Type[PromptInput]):
        pass

    def get_model_output(self):
        pass

    def get_both_model_output_and_expected_output(self, expected_output):
        return ModelOutputAndExpectedOutput(
            model_output=self.get_model_output(self),
            expected_output=expected_output)
    
class LLMWithGeneratedText(HuggingfaceLLMCaller):
    def __init__(self, LLM_API_ENDPOINT):
        super().__init__(LLM_API_ENDPOINT)
    
    def get_JSON_output_from_API_call(self, prompt_input: Type[PromptInput]):
        headers = {"Authorization": f"Bearer {self.HUGGINGFACE_API_KEY}"}
        prompt = prompt_input.generate_prompt()
        payload = {"inputs": prompt}
        return requests.post(self.LLM_API_ENDPOINT, 
                             headers=headers, 
                             json=payload).json()
    
    def get_model_output(self, prompt_input: Type[PromptInput]):
        LLM_output = super().get_JSON_output_from_API_call(prompt_input)
        return LLM_output[0]['generated_text']
    
class LLMWithCandidateLabels(HuggingfaceLLMCaller):
    def __init__(self, LLM_API_ENDPOINT):
        super().__init__(LLM_API_ENDPOINT)
    
    def get_JSON_output_from_API_call(self, prompt_input: Type[PromptInput]):
        headers = {"Authorization": f"Bearer {self.HUGGINGFACE_API_KEY}"}
        prompt = prompt_input.generate_prompt()
        payload = {"inputs": prompt,
                "parameters": {"candidate_labels": prompt_input.candidate_labels},
                "options": {"wait_for_model": True}}
        return requests.post(self.LLM_API_ENDPOINT, 
                             headers=headers, 
                             json=payload).json()

    def get_model_output(self, prompt_input: Type[PromptInput]):
        LLM_output = self.get_JSON_output_from_API_call(prompt_input)
        max_score_index = LLM_output['scores'].index(max(LLM_output['scores']))
        predicted_label = LLM_output['labels'][max_score_index]

        return predicted_label