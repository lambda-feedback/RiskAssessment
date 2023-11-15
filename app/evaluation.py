import os
from dotenv import load_dotenv
import requests

load_dotenv()

from typing import Any, TypedDict

hugging_face_token = os.environ.get("HUGGINGFACEHUB_API_TOKEN")

def get_completion_with_DeBERTa(prompt):
    API_URL = "https://api-inference.huggingface.co/models/MoritzLaurer/DeBERTa-v3-base-mnli-fever-anli"
    headers = {"Authorization": f"Bearer {hugging_face_token}"}
    payload = {
        "inputs": prompt,
        "parameters": {"candidate_labels": ["Yes", "No"]},
        "options": {"wait_for_model": False}}
    output = requests.post(API_URL, headers=headers, json=payload).json()

    # return output
    
    max_score_index = output['scores'].index(max(output['scores']))
    predicted_label = output['labels'][max_score_index]

    return predicted_label

class Params(TypedDict):
    part_of_question: str

class Result(TypedDict):
    is_correct: bool

def evaluation_function(response: Any, answer: Any, params: Params) -> Result:
    """
    Function used to evaluate a student response.
    ---
    The handler function passes three arguments to evaluation_function():

    - `response` which are the answers provided by the student.
    - `answer` which are the correct answers to compare against.
    - `params` which are any extra parameters that may be useful,
        e.g., error tolerances.

    The output of this function is what is returned as the API response
    and therefore must be JSON-encodable. It must also conform to the
    response schema.

    Any standard python library may be used, as well as any package
    available on pip (provided it is added to requirements.txt).

    The way you wish to structure you code (all in this function, or
    split into many) is entirely up to you. All that matters are the
    return types and that evaluation_function() is the main function used
    to output the evaluation response.
    """

    activity, hazard, who_is_harmed, way_it_harms, uncontrolled_likelihood, uncontrolled_severity, uncontrolled_risk, prevention, mitigation, controlled_likelihood, controlled_severity, controlled_risk = response[0]

    model_output = get_completion_with_DeBERTa(prompt=f'Answer yes or no. Is the following an activity: {activity}')

    # return model_output
    if model_output == 'Yes':
        return Result(is_correct=True)
    
    else:
        return Result(is_correct=False)
