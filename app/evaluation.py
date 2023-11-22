from typing import Any, TypedDict

try:
    from .RiskAssessment import RiskAssessment
    from .HuggingfaceLLMCaller import LLMWithCandidateLabels
except ImportError:
    from RiskAssessment import RiskAssessment
    from HuggingfaceLLMCaller import LLMWithCandidateLabels

class Params(TypedDict):
    pass

class Result(TypedDict):
    is_correct: bool
    feedback: str

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

    activity, hazard, who_it_harms, how_it_harms, uncontrolled_likelihood, uncontrolled_severity, uncontrolled_risk, prevention, mitigation, controlled_likelihood, controlled_severity, controlled_risk = response[0]

    RA = RiskAssessment(activity=activity, hazard=hazard, who_it_harms=who_it_harms, how_it_harms=how_it_harms,
                        uncontrolled_likelihood=uncontrolled_likelihood, uncontrolled_severity=uncontrolled_severity,
                        uncontrolled_risk=uncontrolled_risk, prevention=prevention, mitigation=mitigation,
                        controlled_likelihood=controlled_likelihood, controlled_severity=controlled_severity, controlled_risk=controlled_risk)
    
    deBERTa_LLM = LLMWithCandidateLabels(LLM_API_ENDPOINT="https://api-inference.huggingface.co/models/MoritzLaurer/DeBERTa-v3-base-mnli-fever-anli")
    prompts_and_prompt_outputs = RA.get_list_of_prompt_outputs(deBERTa_LLM)

    feedback = ''

    feedback = f'{activity} {hazard} {who_it_harms}'
    for i in range(len(prompts_and_prompt_outputs)):
        prompt = prompts_and_prompt_outputs[i].prompt
        prompt_output = prompts_and_prompt_outputs[i].prompt_output

        feedback += f'Prompt: {prompt}, Prompt Output: {prompt_output}\n'

    output_from_activity_prompt = prompts_and_prompt_outputs[0].prompt_output
    
    if output_from_activity_prompt == 'Yes':
        return Result(is_correct=True, feedback=feedback)
    else:
        return Result(is_correct=False, feedback=feedback)