

# Add option in RiskAssessment to specify whether prevention is misclassified as mitigation, 
# is not a suitable prevention, or mitigation is misclassified as prevention, or is not a suitable mitigation

from typing import Any, TypedDict
import numpy as np

import openai
import requests

from typing import Type

import os
from dotenv import load_dotenv

try:
    from .PromptInputs import *
except:
    from PromptInputs import *

try:
    from RiskAssessment import RiskAssessment
    from LLMCaller import LLMWithCandidateLabels, LLMWithGeneratedText
except:
    from .RiskAssessment import RiskAssessment
    from .LLMCaller import LLMWithCandidateLabels, LLMWithGeneratedText, OpenAILLM

class Params(TypedDict):
    pass

class Result(TypedDict):
    is_correct: bool
    feedback: str

def evaluation_function(response: Any, answer: Any, params: Any) -> Result:
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

    activity, hazard, who_it_harms, how_it_harms, uncontrolled_likelihood, uncontrolled_severity, uncontrolled_risk, prevention, mitigation, controlled_likelihood, controlled_severity, controlled_risk = np.array(response).flatten()

    RA = RiskAssessment(activity=activity, hazard=hazard, who_it_harms=who_it_harms, how_it_harms=how_it_harms,
                        uncontrolled_likelihood=uncontrolled_likelihood, uncontrolled_severity=uncontrolled_severity,
                        uncontrolled_risk=uncontrolled_risk, prevention=prevention, mitigation=mitigation,
                        controlled_likelihood=controlled_likelihood, controlled_severity=controlled_severity, controlled_risk=controlled_risk,
                        prevention_prompt_expected_output='prevention', mitigation_prompt_expected_output='mitigation',
                        prevention_protected_clothing_expected_output=False,
                        mitigation_protected_clothing_expected_output=False,
                        prevention_first_aid_expected_output=False,
                        mitigation_first_aid_expected_output=False,
                        )
    
    input_check_feedback_message = RA.get_input_check_feedback_message()
    controlled_risk = RA.check_controlled_risk()
    uncontrolled_risk = RA.check_uncontrolled_risk()

    if input_check_feedback_message != '':
        return Result(is_correct=False,
                    feedback=f'Feedback: \n\n {input_check_feedback_message}')
    
    if input_check_feedback_message == '' and controlled_risk != 'correct' or uncontrolled_risk != 'correct':
        return Result(is_correct=False,
                      feedback=f'Feedback: \n\n Uncontrolled risk is: {controlled_risk}\n\nUncontrolled risk is {uncontrolled_risk}')
    
    else:
        LLM = OpenAILLM()

        feedback_for_incorrect_answers = '# Feedback for Incorrect Answers\n'
        feedback_for_correct_answers = '# Feedback for Correct Answers\n'

        is_everything_correct = True

        first_3_prompt_input_objects = RA.get_list_of_prompt_input_objects_for_first_3_prompts()

        for prompt_input_object in first_3_prompt_input_objects:
            prompt_output, pattern = RA.get_prompt_output_and_pattern_matched(prompt_input_object, LLM)
            shortform_feedback = RA.get_shortform_feedback_from_regex_match(prompt_input_object, pattern)

            field = prompt_input_object.get_field_checked()

            longform_feedback = prompt_input_object.get_longform_feedback(prompt_output=prompt_output)
            
            feedback_header_to_add = f''' 
            ## Feedback for Input: {field}\n
            '''

            feedback_to_add = f'''
            - **Feedback**: {shortform_feedback}\n
            - **Explanation**: {longform_feedback}\n'''
            
            if pattern in prompt_input_object.labels_indicating_correct_input:
                feedback_for_correct_answers += feedback_header_to_add
                feedback_for_correct_answers += feedback_to_add + '\n\n'
            
            else:
                is_everything_correct = False

                feedback_to_add += f'''- **Recommendation**: Please look at the definition of the {field} input field{'s' if field in ['Hazard & How it harms', 'Prevention and Mitigation'] else ''} and the example risk assessment for assistance.'''

                feedback_for_incorrect_answers += feedback_header_to_add
                feedback_for_incorrect_answers += feedback_to_add

                break
        

        # PREVENTION CHECKS
        feedback_header = f''' ## Feedback for Input: Prevention'''

        if is_everything_correct == True:
            prevention_protective_clothing_prompt_input = RA.get_prevention_protective_clothing_input()
            prevention_protective_clothing_prompt_output, prevention_protective_clothing_pattern = RA.get_prompt_output_and_pattern_matched(prevention_protective_clothing_prompt_input, LLM)
            
            # Indicating that the prevention is a protective clothing so is actually a mitigation
            if prevention_protective_clothing_pattern == True:
                shortform_feedback = prevention_protective_clothing_prompt_input.get_shortform_feedback()
                longform_feedback = prevention_protective_clothing_prompt_input.get_longform_feedback()

                feedback_for_incorrect_answers += f'''
                {feedback_header}
                - **Feedback**: {shortform_feedback}\n
                - **Explanation**: {longform_feedback}\n
                - **Recommendation**: Please look at the definition of a Prevention and Mitigation for assistance.'''

                is_everything_correct = False
            
            # Indicating that the prevention is not a protective clothing
            else:
                prevention_first_aid_prompt_input = RA.get_prevention_first_aid_input()
                prevention_first_aid_prompt_output, prevention_first_aid_pattern = RA.get_prompt_output_and_pattern_matched(prevention_first_aid_prompt_input, LLM)

                # Indicating that the prevention is an example of first aid so is a mitigation
                if prevention_first_aid_pattern == True:
                    shortform_feedback = prevention_first_aid_prompt_input.get_shortform_feedback()
                    longform_feedback = prevention_first_aid_prompt_input.get_longform_feedback()

                    feedback_for_incorrect_answers += f'''
                    {feedback_header}
                    - **Feedback**: {shortform_feedback}\n
                    - **Explanation**: {longform_feedback}\n
                    - **Recommendation**: Please look at the definition of a Prevention and Mitigation for assistance.'''

                    is_everything_correct = False
                
                # Indicating that the prevention is neither a protective clothing nor an example of first aid
                # This checks whether the inputted prevention is a prevention or a mitigation 
                else:
                    prevention_prompt_input = RA.get_prevention_input()
                    prevention_prompt_output, prevention_pattern = RA.get_prompt_output_and_pattern_matched(prevention_prompt_input, LLM)

                    shortform_feedback_object = prevention_prompt_input.get_shortform_feedback()
                    longform_feedback = prevention_prompt_input.get_longform_feedback(prompt_output=prevention_prompt_output)

                    if prevention_pattern == 'mitigation':
                        longform_feedback = prompt_input_object.get_longform_feedback(prompt_output=prompt_output, pattern_to_search_for='Mitigation Explanation',lookahead_assertion='Answer')

                    if prevention_pattern == 'mitigation' or prevention_pattern == 'neither':
                        feedback_for_incorrect_answers += f'''
                        {feedback_header}
                        - **Feedback**: {shortform_feedback_object.negative_feedback}\n
                        - **Explanation**: {longform_feedback}\n
                        - **Recommendation**: Please look at the definition of a Prevention {'and Mitigation' if prevention_pattern == 'mitigation' else ''} for assistance.\n'''

                        is_everything_correct = False
                    
                    if prevention_pattern == 'prevention' or prevention_pattern == 'both':
                        feedback_for_correct_answers += f'''
                        {feedback_header}
                        - **Feedback**: {shortform_feedback_object.positive_feedback}\n
                        - **Explanation**: {longform_feedback}\n'''

        # MITIGATION CHECKS
        feedback_header = f''' ## Feedback for Input: Mitigation'''

        if is_everything_correct == True:
            mitigation_protective_clothing_prompt_input = RA.get_mitigation_protective_clothing_input()
            mitigation_protective_clothing_prompt_output, mitigation_protective_clothing_pattern = RA.get_prompt_output_and_pattern_matched(mitigation_protective_clothing_prompt_input, LLM)

            shortform_feedback = mitigation_protective_clothing_prompt_input.get_shortform_feedback()
            longform_feedback = mitigation_protective_clothing_prompt_input.get_longform_feedback()

            # Indicating that the mitigation is a protective clothing
            if mitigation_protective_clothing_pattern == True:
                feedback_for_correct_answers += f'''
                {feedback_header}
                - **Feedback**: {shortform_feedback.positive_feedback}\n
                - **Explanation**: {longform_feedback}\n'''
            
            # Indicating that the mitigation is not a protective clothing
            else:
                mitigation_first_aid_prompt_input = RA.get_mitigation_first_aid_input()
                mitigation_first_aid_prompt_output, mitigation_first_aid_pattern = RA.get_prompt_output_and_pattern_matched(mitigation_first_aid_prompt_input, LLM)

                shortform_feedback = mitigation_first_aid_prompt_input.get_shortform_feedback()
                longform_feedback = mitigation_first_aid_prompt_input.get_longform_feedback()

                # Indicating that the mitigation is an example of first aid
                if mitigation_first_aid_pattern == True:
                        
                    feedback_for_correct_answers += f'''
                    {feedback_header}
                    - **Feedback**: {shortform_feedback.positive_feedback}\n
                    - **Explanation**: {longform_feedback}\n'''

                # Indicating that the mitigation is neither a protective clothing or an example of first aid
                # This checks whether the inputted mitigation is a prevention or a mitigation 
                else:
                    mitigation_prompt_input = RA.get_mitigation_input()
                    mitigation_prompt_output, mitigation_pattern = RA.get_prompt_output_and_pattern_matched(mitigation_prompt_input, LLM)
                    
                    if mitigation_pattern == 'mitigation' or mitigation_pattern == 'both':
                        feedback_for_correct_answers += f'''
                        {feedback_header}
                        - **Feedback**: {shortform_feedback.positive_feedback}\n
                        - **Explanation**: {longform_feedback}\n'''

                    if mitigation_pattern == 'prevention':
                        longform_feedback = mitigation_prompt_input.get_longform_feedback(prompt_output=mitigation_prompt_output, pattern_to_search_for='Prevention Explanation',lookahead_assertion='Mitigation')
                    
                    if mitigation_pattern == 'prevention' or mitigation_pattern == 'neither':
                        feedback_for_incorrect_answers += f'''
                        {feedback_header}
                        - **Feedback**: {shortform_feedback.negative_feedback}\n
                        - **Explanation**: {longform_feedback}\n
                        - **Recommendation**: Please look at the definition of a Mitigation {'and Prevention' if mitigation_pattern == 'prevention' else ''} for assistance.\n'''

                        is_everything_correct = False

        feedback_for_correct_answers += f'''
        - Uncontrolled risk multiplication is: {uncontrolled_risk}
        - Controlled risk multiplication is: {controlled_risk}'''

        return Result(is_correct=is_everything_correct, feedback=feedback_for_incorrect_answers + '\n\n\n\n\n' + feedback_for_correct_answers)