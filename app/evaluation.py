

# Add option in RiskAssessment to specify whether prevention is misclassified as mitigation, 
# is not a suitable prevention, or mitigation is misclassified as prevention, or is not a suitable mitigation

# TODO: Functions can make this code shorter.
 
from typing import Any, TypedDict
import numpy as np

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

class Result(TypedDict):
    is_correct: bool
    feedback: str

class Params(TypedDict):
    is_feedback_text: bool
    is_risk_matrix: bool
    is_risk_assessment: bool

def provide_feedback_on_risk_matrix(response):
        risk_matrix = np.array(response)

        risk_matrix_flattened = np.array(response).flatten()
        for value in risk_matrix_flattened:
            if value == '':
                return Result(is_correct=False, feedback="Please fill in all the fields")
            else:
                try:
                    int_value = int(value)
                except ValueError:
                    return Result(is_correct=False, feedback="Please enter an integer for all fields.")

        risk_matrix_dict = {'uncontrolled likelihood': int(risk_matrix[0, 0]),
                    'uncontrolled severity': int(risk_matrix[0, 1]),
                    'controlled likelihood': int(risk_matrix[1, 0]), 
                    'controlled severity': int(risk_matrix[1, 1])}

        is_correct = True
        feedback = f''''''

        for key in risk_matrix_dict.keys():
            if risk_matrix_dict[key] > 4 or risk_matrix_dict[key] < 1:
                is_correct = False
                feedback += f'''\n\n\n\n\n##### The {key} is incorrect. As per the likelihood and severity conventions above, the likelihood and severity should be between 1 and 4.\n\n\n\n'''

        uncontrolled_likelihood = risk_matrix_dict['uncontrolled likelihood']
        uncontrolled_severity = risk_matrix_dict['uncontrolled severity']
        uncontrolled_risk = int(risk_matrix[0, 2])
        controlled_likelihood = risk_matrix_dict['controlled likelihood']
        controlled_severity = risk_matrix_dict['controlled severity']
        controlled_risk = int(risk_matrix[1, 2])

        feedback += '\n'

        # Comparing Uncontrolled and Controlled Rows
                
        # Likelihoods
        if is_correct == True: # Only write feedback if all previous checks have passed
            if uncontrolled_likelihood <= controlled_likelihood:
                feedback += f'''\n\n\n\n\n##### Likelihood values are incorrect. Since an effective prevention measure has been implemented ("taking care when cross the road"), the controlled likelihood should be less than the uncontrolled likelihood.\n\n\n\n'''
                is_correct = False

        # Severities
        if is_correct == True: # Only write feedback if all previous checks have passed
            if uncontrolled_severity != controlled_severity:
                feedback += f'''\n\n\n\n\n##### Severity values are incorrect. The uncontrolled and controlled severity should be the same since no mitigation measure has been implemented.\n\n\n\n''' 
                is_correct = False

        # --- Checking Uncontrolled Row ---
        
        # Likelihoods
        if is_correct == True: # Only write feedback if all previous checks have passed
            if uncontrolled_likelihood != 4:
                feedback += f'''\n\n\n\n\n##### An uncontrolled likelihood of {uncontrolled_likelihood} is incorrect. The convention is that all uncontrolled risks have a likelihood of 4. If you didn't look or listen when crossing the road, you would almost certainly be harmed.\n\n\n\n'''
                is_correct = False

        # Severities
        if is_correct == True:
            if uncontrolled_severity == 1:
                feedback += f'''\n\n\n\n\n##### An uncontrolled severity of 1 is incorrect. As by the above severity convention, a severity of 1 indicates that a car crashing into a pedestrian causes "minor injury or property damage". The harm will be greater than this.\n\n\n\n''' 
                is_correct = False

        # Multiplications
        if is_correct == True: # Only write feedback if all previous checks have passed
            if uncontrolled_likelihood * uncontrolled_severity != uncontrolled_risk:
                feedback += f'''\n\n\n\n\n##### Uncontrolled risk multiplication is incorrect. Make sure the risk is the likelihood multiplied by the severity.\n\n\n\n'''
                is_correct = False

        # --- Checking Controlled Row ---
                
        # Likelihoods
        if is_correct == True: # Only write feedback if all previous checks have passed
            if controlled_likelihood == 1:
                feedback += f'''\n\n\n\n\n##### A controlled likelihood of 1 is incorrect. A controlled likelihood of 1 indicates that the control measure is implemented passively whereas you have to activily pay attention when cross the road.\n\n\n\n'''
                is_correct = False

            if controlled_likelihood == 2:
                feedback += f'''\n\n\n\n\n##### Correct controlled likelihood. A controlled likelihood of 2 indicates that the control measure of "taking care when crossing the road" is implemented actively.\n\n\n\n''' 
            
            if controlled_likelihood == 3:
                feedback += f'''\n\n\n\n\n##### A controlled likelihood of 3 is incorrect. A controlled likelihood of 3 indicates that the control measure is not effective and the likelihood is "possible".\n\n\n\n''' 
                is_correct = False
            
            if controlled_likelihood == 4:
                feedback += f'''\n\n\n\n\n##### A controlled likelihood of 4 is incorrect. A controlled likelihood of 4 indicates that the control measure is effective and the likelihood is "likely".\n\n\n\n''' 
                is_correct = False

        # Severities
        if is_correct == True: # Only write feedback if all previous checks have passed
            if controlled_severity == 1:
                feedback += f'''\n\n\n\n\n##### A controlled severity of 1 is incorrect. As by the above severity convention, a severity of 1 indicates that a car crashing into a pedestrian causes "minor injury or property damage". The harm will be greater than this.\n\n\n\n''' 
                is_correct = False

        # Multiplications
        if is_correct == True: # Only write feedback if all previous checks have passed
            if controlled_likelihood * controlled_severity != controlled_risk:
                feedback += f'''\n\n\n\n\n##### Controlled risk multiplication is incorrect. Make sure the risk is the likelihood multiplied by the severity.\n\n\n\n'''
                is_correct = False

        return Result(is_correct=is_correct, feedback=feedback)

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

    if params["is_feedback_text"] == True:
        return Result(is_correct=True, feedback="Thank you for your feedback")
    
    if params["is_risk_matrix"] == True:
        return provide_feedback_on_risk_matrix(response)
    
    if params["is_risk_assessment"] == True:
        activity, hazard, how_it_harms, who_it_harms, uncontrolled_likelihood, uncontrolled_severity, uncontrolled_risk, prevention, mitigation, controlled_likelihood, controlled_severity, controlled_risk = np.array(response).flatten()

        RA = RiskAssessment(activity=activity, hazard=hazard, who_it_harms=who_it_harms, how_it_harms=how_it_harms,
                            uncontrolled_likelihood=uncontrolled_likelihood, uncontrolled_severity=uncontrolled_severity,
                            uncontrolled_risk=uncontrolled_risk, prevention=prevention, mitigation=mitigation,
                            controlled_likelihood=controlled_likelihood, controlled_severity=controlled_severity, controlled_risk=controlled_risk,
                            prevention_prompt_expected_output='prevention', mitigation_prompt_expected_output='mitigation',
                            prevention_clothing=False,
                            mitigation_clothing=False,
                            prevention_protected_clothing_expected_output=False,
                            mitigation_protected_clothing_expected_output=False,
                            prevention_first_aid_expected_output=False,
                            mitigation_first_aid_expected_output=False,
                            harm_caused_in_how_it_harms='',
                            hazard_event="",
                            )

        input_check_feedback_message = RA.get_input_check_feedback_message()

        if input_check_feedback_message != '':
            return Result(is_correct=False,
                        feedback=f'Feedback: \n\n {input_check_feedback_message}')

        uncontrolled_values_check = RA.check_that_uncontrolled_likelihood_and_severity_values_are_between_1_and_4()
        controlled_values_check = RA.check_that_controlled_likelihood_and_severity_values_are_between_1_and_4()

        if input_check_feedback_message == '' and uncontrolled_values_check != 'correct' or controlled_values_check != 'correct':
            return Result(is_correct=False,
                        feedback=f'Feedback: \n\n {uncontrolled_values_check}\n\n{controlled_values_check}')

        controlled_risk_multiplication_check = RA.check_controlled_risk_multiplication()
        uncontrolled_risk_multiplication_check = RA.check_uncontrolled_risk_multiplication()

        if input_check_feedback_message == '' and controlled_risk_multiplication_check != 'correct' or uncontrolled_risk_multiplication_check != 'correct':
            return Result(is_correct=False,
                        feedback=f'Feedback: \n\n {controlled_risk_multiplication_check}\n\nUncontrolled risk is {uncontrolled_risk_multiplication_check}')
        
        likelihood_comparison_check = RA.compare_controlled_and_uncontrolled_likelihood()
        severity_comparison_check = RA.compare_controlled_and_uncontrolled_severity()

        if input_check_feedback_message == '' and likelihood_comparison_check != 'correct' and severity_comparison_check != 'correct':
            return Result(is_correct=False,
                        feedback=f'Feedback: \n\n {likelihood_comparison_check}\n\n{severity_comparison_check}')
        
        else:
            LLM = OpenAILLM()

            feedback_for_incorrect_answers = '\n\n\n\n# Feedback for Incorrect Answers\n\n\n\n'
            feedback_for_correct_answers = '\n\n\n\n# Feedback for Correct Answers\n\n\n\n'
            answers_for_which_feedback_cannot_be_given_message = '\n\n\n\n# Feedback for the following answers cannot be given\n\n\n\n'
            no_information_provided_message = '\n\n\n\n# No information provided for the following fields:\n\n\n\n'

            is_everything_correct = True
            is_complete_feedback_given = True

            first_3_prompt_input_objects = RA.get_list_of_prompt_input_objects_for_first_3_prompts()
            
            for prompt_input_object in first_3_prompt_input_objects:
                if is_everything_correct == True:
                    prompt_output, pattern = RA.get_prompt_output_and_pattern_matched(prompt_input_object, LLM)
                    shortform_feedback = RA.get_shortform_feedback_from_regex_match(prompt_input_object, pattern)

                    field = prompt_input_object.get_field_checked()
                    
                    feedback_header_to_add = f''' 
                    \n\n\n## Feedback for Input: {field}\n\n\n
                    '''

                    feedback_to_add = f'''
                    \n\n\n\n#### Feedback: {shortform_feedback}\n\n\n\n'''
                    
                    if pattern in prompt_input_object.labels_indicating_correct_input:
                        feedback_for_correct_answers += feedback_header_to_add
                        feedback_for_correct_answers += feedback_to_add + '\n\n'
                    
                    else:

                        longform_feedback = prompt_input_object.get_longform_feedback(prompt_output=prompt_output)
                        
                        if longform_feedback != '':
                            feedback_to_add += f'''\n\n\n\n#### Explanation: {longform_feedback}\n\n\n\n'''
                        
                        is_everything_correct = False
                        recommendation = prompt_input_object.get_recommendation()

                        feedback_to_add += f'''\n\n\n\n#### Recommendation: {recommendation}'''

                        feedback_for_incorrect_answers += feedback_header_to_add
                        feedback_for_incorrect_answers += feedback_to_add

           
            if is_everything_correct == True:
                # PREVENTION CHECKS

                no_information_provided_for_prevention_prompt_input = RA.get_no_information_provided_for_prevention_input()
                no_information_provided_for_prevention_prompt_output, no_information_provided_for_prevention_pattern = RA.get_prompt_output_and_pattern_matched(no_information_provided_for_prevention_prompt_input, LLM)

                if no_information_provided_for_prevention_pattern == 'no information provided':
                    no_information_provided_message += f'''\n\n\n\n#### Prevention\n\n\n\n'''
                else:
                    feedback_header = f'''\n\n\n## Feedback for Input: Prevention\n\n\n'''

                    prevention_protective_barrier_prompt_input = RA.get_prevention_protective_barrier_input()
                    prevention_protective_barrier_prompt_output, prevention_protective_barrier_pattern = RA.get_prompt_output_and_pattern_matched(prevention_protective_barrier_prompt_input, LLM)
                    
                    # Indicating that the prevention is a protective clothing so is actually a mitigation
                    if prevention_protective_barrier_pattern == True:
                        shortform_feedback = prevention_protective_barrier_prompt_input.get_shortform_feedback('negative')
                        longform_feedback = prevention_protective_barrier_prompt_input.get_longform_feedback()
                        recommendation = prevention_protective_barrier_prompt_input.get_recommendation()

                        feedback_for_incorrect_answers += f'''
                        {feedback_header}
                        \n\n\n\n#### Feedback: {shortform_feedback}\n\n\n\n
                        \n\n\n\n#### Explanation: {longform_feedback}\n\n\n\n
                        \n\n\n\n#### Recommendation: {recommendation}\n\n\n\n'''

                        is_everything_correct = False
                    
                    # Indicating that the prevention is not a protective clothing
                    else:
                        prevention_first_aid_prompt_input = RA.get_prevention_first_aid_input()
                        prevention_first_aid_prompt_output, prevention_first_aid_pattern = RA.get_prompt_output_and_pattern_matched(prevention_first_aid_prompt_input, LLM)

                        # Indicating that the prevention is an example of first aid so is a mitigation
                        if prevention_first_aid_pattern == True:
                            shortform_feedback = prevention_first_aid_prompt_input.get_shortform_feedback('negative')
                            longform_feedback = prevention_first_aid_prompt_input.get_longform_feedback()
                            recommendation = prevention_first_aid_prompt_input.get_recommendation()

                            feedback_for_incorrect_answers += f'''
                            {feedback_header}
                            \n\n\n\n#### Feedback: {shortform_feedback}\n\n\n\n
                            \n\n\n\n#### Explanation: {longform_feedback}\n\n\n\n
                            \n\n\n\n#### Recommendation: {recommendation}\n\n\n\n'''

                            is_everything_correct = False
                        
                        # Indicating that the prevention is neither a protective clothing nor an example of first aid
                        # This checks whether the inputted prevention is a prevention or a mitigation 
                        else:
                            prevention_prompt_input = RA.get_prevention_input()
                            prevention_prompt_output, prevention_pattern = RA.get_prompt_output_and_pattern_matched(prevention_prompt_input, LLM)

                            longform_feedback = prevention_prompt_input.get_longform_feedback(prompt_output=prevention_prompt_output)

                            if prevention_pattern == 'both':
                                recommendation = prevention_prompt_input.get_recommendation(recommendation_type='both')
                                answers_for_which_feedback_cannot_be_given_message += f'''
                                \n\n\n\n#### {prevention_prompt_input.get_shortform_feedback('both')}\n\n\n\n
                                \n\n\n\n#### Recommendation: {recommendation}\n\n\n\n'''

                                is_complete_feedback_given = False
                            
                            if prevention_pattern == 'prevention':
                                feedback_for_correct_answers += f'''
                                {feedback_header}
                                \n\n\n\n#### Feedback: {prevention_prompt_input.get_shortform_feedback('positive')}\n\n\n\n
                                \n\n\n\n#### Explanation: {longform_feedback}\n\n\n\n'''

                            if prevention_pattern == 'neither':
                                recommendation = prevention_prompt_input.get_recommendation(recommendation_type='neither')
                                feedback_for_incorrect_answers += f'''
                                {feedback_header}
                                \n\n\n\n#### Feedback: {prevention_prompt_input.get_shortform_feedback('neither')}\n\n\n\n
                                \n\n\n\n#### Explanation: {longform_feedback}\n\n\n\n
                                \n\n\n\n#### Recommendation: {recommendation}\n\n\n\n'''

                                is_everything_correct = False

                            if prevention_pattern == 'mitigation':
                                longform_feedback = prevention_prompt_input.get_longform_feedback(prompt_output=prompt_output, pattern_to_search_for='Mitigation Explanation')
                                recommendation = prevention_prompt_input.get_recommendation(recommendation_type='misclassification')

                                feedback_for_incorrect_answers += f'''
                                {feedback_header}
                                \n\n\n\n#### Feedback: {prevention_prompt_input.get_shortform_feedback('misclassification')}\n\n\n\n
                                \n\n\n\n#### Explanation: {longform_feedback}\n\n\n\n
                                \n\n\n\n#### Recommendation: {recommendation}\n\n\n\n'''

                                is_everything_correct = False


                # MITIGATION CHECKS
                no_information_provided_for_mitigation_prompt_input = RA.get_no_information_provided_for_mitigation_input()
                no_information_provided_for_mitigation_prompt_output, no_information_provided_for_mitigation_pattern = RA.get_prompt_output_and_pattern_matched(no_information_provided_for_mitigation_prompt_input, LLM)

                if no_information_provided_for_mitigation_pattern == 'no information provided':
                    no_information_provided_message += f'''\n\n\n\n#### Mitigation\n\n\n\n'''
                else:
                    feedback_header = f'''\n\n\n## Feedback for Input: Mitigation\n\n\n'''

                    mitigation_protective_barrier_prompt_input = RA.get_mitigation_protective_barrier_input()
                    mitigation_protective_barrier_prompt_output, mitigation_protective_barrier_pattern = RA.get_prompt_output_and_pattern_matched(mitigation_protective_barrier_prompt_input, LLM)

                    shortform_feedback = mitigation_protective_barrier_prompt_input.get_shortform_feedback('positive')
                    longform_feedback = mitigation_protective_barrier_prompt_input.get_longform_feedback()

                    # Indicating that the mitigation is a protective clothing
                    if mitigation_protective_barrier_pattern == True:
                        feedback_for_correct_answers += f'''
                        {feedback_header}
                        \n\n\n\n#### Feedback: {shortform_feedback}\n\n\n\n
                        \n\n\n\n#### Explanation: {longform_feedback}\n\n\n\n'''
                    
                    # Indicating that the mitigation is not a protective clothing
                    else:
                        mitigation_first_aid_prompt_input = RA.get_mitigation_first_aid_input()
                        mitigation_first_aid_prompt_output, mitigation_first_aid_pattern = RA.get_prompt_output_and_pattern_matched(mitigation_first_aid_prompt_input, LLM)

                        shortform_feedback = mitigation_first_aid_prompt_input.get_shortform_feedback('positive')
                        longform_feedback = mitigation_first_aid_prompt_input.get_longform_feedback()

                        # Indicating that the mitigation is an example of first aid
                        if mitigation_first_aid_pattern == True:
                                
                            feedback_for_correct_answers += f'''
                            {feedback_header}
                            \n\n\n\n#### Feedback: {shortform_feedback}\n\n\n\n
                            \n\n\n\n#### Explanation: {longform_feedback}\n\n\n\n'''

                        # Indicating that the mitigation is neither a protective clothing or an example of first aid
                        # This checks whether the inputted mitigation is a prevention or a mitigation 
                        else:
                            mitigation_prompt_input = RA.get_mitigation_input()
                            mitigation_prompt_output, mitigation_pattern = RA.get_prompt_output_and_pattern_matched(mitigation_prompt_input, LLM)

                            longform_feedback = mitigation_prompt_input.get_longform_feedback(prompt_output=mitigation_prompt_output)

                            if mitigation_pattern == 'both':
                                recommendation = mitigation_prompt_input.get_recommendation(recommendation_type='both')
                                answers_for_which_feedback_cannot_be_given_message += f'''
                                \n\n\n\n#### {mitigation_prompt_input.get_shortform_feedback('both')}\n\n\n\n
                                \n\n\n\n#### Recommendation: {recommendation}\n\n\n\n'''

                                is_complete_feedback_given = False

                            if mitigation_pattern == 'mitigation' or mitigation_pattern == 'both':
                                feedback_for_correct_answers += f'''
                                {feedback_header}
                                \n\n\n\n#### Feedback: {mitigation_prompt_input.get_shortform_feedback('positive')}\n\n\n\n
                                \n\n\n\n#### Explanation: {longform_feedback}\n\n\n\n'''
                            
                            if mitigation_pattern == 'neither':
                                recommendation = mitigation_prompt_input.get_recommendation(recommendation_type='neither')

                                feedback_for_incorrect_answers += f'''
                                {feedback_header}
                                \n\n\n\n#### Feedback: {mitigation_prompt_input.get_shortform_feedback('neither')}\n\n\n\n
                                \n\n\n\n#### Explanation: {longform_feedback}\n\n\n\n
                                \n\n\n\n#### Recommendation: {recommendation}\n\n\n\n'''

                                is_everything_correct = False

                            if mitigation_pattern == 'prevention':
                                longform_feedback = mitigation_prompt_input.get_longform_feedback(prompt_output=mitigation_prompt_output, pattern_to_search_for='Prevention Explanation')
                                recommendation = mitigation_prompt_input.get_recommendation(recommendation_type='misclassification')

                                feedback_for_incorrect_answers += f'''
                                {feedback_header}
                                \n\n\n\n#### Feedback: {mitigation_prompt_input.get_shortform_feedback('misclassification')}\n\n\n\n
                                \n\n\n\n#### Explanation: {longform_feedback}\n\n\n\n
                                \n\n\n\n#### Recommendation: {recommendation}\n\n\n\n'''
                                
                                is_everything_correct = False

            if is_everything_correct == True:

                if is_complete_feedback_given == True:
                    feedback_for_incorrect_answers = '# Congratulations! All your answers are correct!'
                else:
                    feedback_for_incorrect_answers = ''

            if is_complete_feedback_given == True:
                answers_for_which_feedback_cannot_be_given_message = ''
            
            if no_information_provided_for_prevention_pattern == False and no_information_provided_for_mitigation_pattern == False:
                no_information_provided_message = ''

            feedback_for_correct_answers += f'''
            \n\n\n## Feedback for Risk Multiplications\n\n\n\n
            \n\n\n\n#### Uncontrolled risk multiplication is: {uncontrolled_risk_multiplication_check}\n\n\n\n
            \n\n\n\n#### Controlled risk multiplication is: {controlled_risk_multiplication_check}\n\n\n\n'''

            return Result(is_correct=is_everything_correct, feedback=feedback_for_incorrect_answers + '\n\n\n\n\n' + answers_for_which_feedback_cannot_be_given_message + '\n\n\n\n\n' + feedback_for_correct_answers + '\n\n\n\n\n' + no_information_provided_message)