from ..test_classes.TestControlMeasureClassificationPrompt import TestControlMeasureClassificationPrompt
from ..utils.LLMCaller import LLMCaller

class TestPreventionInput__ControlMeasureClassifiationPrompt(TestControlMeasureClassificationPrompt):
    def __init__(self, 
                    LLM: LLMCaller,
                    list_of_risk_assessment_and_expected_outputs: list,
                    sheet_name: str,
                    examples_gathered_or_generated_message: str,
                    candidate_labels: list,
                    risk_assessment_control_measure_prompt_with_prevention_input_method_name: str,
                    domain: str = None,
                    is_first_test: bool = False):
        
        self.LLM = LLM
        self.list_of_risk_assessment_and_expected_outputs = list_of_risk_assessment_and_expected_outputs
        self.sheet_name = sheet_name
        self.examples_gathered_or_generated_message = examples_gathered_or_generated_message
        self.candidate_labels = candidate_labels
        self.domain = domain
        self.is_first_test = is_first_test
        self.risk_assessment_control_measure_prompt_with_prevention_input_method_name = risk_assessment_control_measure_prompt_with_prevention_input_method_name
        self.domain = domain
        self.is_first_test = is_first_test

    def get_first_prompt_input(self):
        return self.get_first_prompt_input_with_risk_assessment_method(risk_assessment_method_name=self.risk_assessment_control_measure_prompt_with_prevention_input_method_name)
    
    def get_pattern_matched_and_prompt_output(self, input_object):
        return self.get_pattern_matched_and_prompt_output_with_risk_assessment_method(input_object=input_object, risk_assessment_method_name=self.risk_assessment_control_measure_prompt_with_prevention_input_method_name)
    
class TestPreventionPromptOnSingleExample(TestPreventionInput__ControlMeasureClassifiationPrompt):
    def __init__(self,
                 LLM: LLMCaller,
                 expected_output,
                 input_object):
        self.LLM = LLM
        self.expected_output = expected_output
        self.input_object = input_object
    
    def is_pattern_matched_equal_to_expected_output(self):
        pattern_matched, prompt_output = self.get_pattern_matched_and_prompt_output(self.input_object)
        
        return pattern_matched == self.expected_output