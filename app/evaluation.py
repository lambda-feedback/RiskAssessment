import os
import openai
from dotenv import load_dotenv

load_dotenv()

from typing import Any, TypedDict

from LLM_functions import get_completion_with_DeBERTa

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

    if model_output == 'Yes':
        return Result(is_correct=True)
    
    else:
        return Result(is_correct=False)