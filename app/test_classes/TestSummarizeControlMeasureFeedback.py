from ..test_classes.TestControlMeasureClassificationPrompt import TestControlMeasureClassificationPrompt
from ..LLMCaller import LLMCaller

class TestSummarizeControlMeasureFeedback(TestControlMeasureClassificationPrompt):
    def __init__(self, 
                    LLM: LLMCaller,
                    list_of_risk_assessment_and_expected_outputs: list,
                    sheet_name: str,
                    examples_gathered_or_generated_message: str,
                    candidate_labels: list,
                    domain: str = None,
                    is_first_test: bool = False):
        super().__init__(LLM, list_of_risk_assessment_and_expected_outputs, sheet_name, examples_gathered_or_generated_message, candidate_labels, domain=domain, is_first_test=is_first_test)

    def get_classes(self):
        return [True, False]
    
    def get_pattern_matched_and_prompt_output_with_risk_assessment_method(self, input_object, risk_assessment_method_name, control_measure_name):

        hazard_event, harm_caused, _, hazard_event_and_harm_caused_prompt_output  = self.get_hazard_event_and_harm_caused_and_prompt(RA=input_object)

        if hazard_event == 'No pattern found' or harm_caused == 'No pattern found':
            return 'No pattern found', hazard_event_and_harm_caused_prompt_output

        control_measure_prompt_input = getattr(input_object, risk_assessment_method_name)()
        control_measure_prompt_output, control_measure_pattern = input_object.get_prompt_output_and_pattern_matched(prompt_input_object=control_measure_prompt_input, LLM_caller=self.LLM, harm_caused=harm_caused, hazard_event=hazard_event)

        control_measure_feedback = control_measure_prompt_input.get_longform_feedback(prompt_output=control_measure_prompt_output)

        prompt_input_for_summarizing_control_measure_prompt_feedback = input_object.get_feedback_summary_input()

        prompt = prompt_input_for_summarizing_control_measure_prompt_feedback.generate_prompt(control_measure_type=control_measure_name, feedback=control_measure_feedback)

        summary_of_control_measure_prompt_feedback, _ = input_object.get_prompt_output_and_pattern_matched(prompt_input_object=prompt_input_for_summarizing_control_measure_prompt_feedback, LLM_caller=self.LLM, control_measure_type=control_measure_name, feedback=control_measure_feedback)

        return True, summary_of_control_measure_prompt_feedback

    def get_first_prompt_input_with_risk_assessment_method(self, risk_assessment_method_name):
        return ''
    
class TestSummarizePreventionFeedback(TestSummarizeControlMeasureFeedback):
    def __init__(self, 
                    LLM: LLMCaller,
                    list_of_risk_assessment_and_expected_outputs: list,
                    sheet_name: str,
                    examples_gathered_or_generated_message: str,
                    candidate_labels: list,
                    domain: str = None,
                    is_first_test: bool = False):
        super().__init__(LLM, list_of_risk_assessment_and_expected_outputs, sheet_name, examples_gathered_or_generated_message, candidate_labels, domain=domain, is_first_test=is_first_test)
    
    def get_first_prompt_input(self):
        return self.get_first_prompt_input_with_risk_assessment_method(risk_assessment_method_name='get_control_measure_prompt_with_prevention_input')
    
    def get_pattern_matched_and_prompt_output(self, input_object):
        return self.get_pattern_matched_and_prompt_output_with_risk_assessment_method(input_object=input_object, risk_assessment_method_name='get_control_measure_prompt_with_prevention_input', control_measure_name='prevention')
    
class TestSummarizeMitigationFeedback(TestSummarizeControlMeasureFeedback):
    def __init__(self, 
                    LLM: LLMCaller,
                    list_of_risk_assessment_and_expected_outputs: list,
                    sheet_name: str,
                    examples_gathered_or_generated_message: str,
                    candidate_labels: list,
                    domain: str = None,
                    is_first_test: bool = False):
        super().__init__(LLM, list_of_risk_assessment_and_expected_outputs, sheet_name, examples_gathered_or_generated_message, candidate_labels, domain=domain, is_first_test=is_first_test)
    
    def get_first_prompt_input(self):
        return self.get_first_prompt_input_with_risk_assessment_method(risk_assessment_method_name='get_control_measure_prompt_with_mitigation_input')
    
    def get_pattern_matched_and_prompt_output(self, input_object):
        return self.get_pattern_matched_and_prompt_output_with_risk_assessment_method(input_object=input_object, risk_assessment_method_name='get_control_measure_prompt_with_mitigation_input', control_measure_name='mitigation')