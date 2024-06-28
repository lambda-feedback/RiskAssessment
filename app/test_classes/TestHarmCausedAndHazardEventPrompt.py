from ..LLMCaller import LLMCaller
from ..test_classes.TestModelAccuracyForCombinationOfPrompts import TestModelAccuracyForCombinationOfPrompts

class TestHarmCausedAndHazardEventPrompt(TestModelAccuracyForCombinationOfPrompts):
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
        first_RA = self.list_of_risk_assessment_and_expected_outputs[0].risk_assessment

        first_harm_caused_prompt_input = first_RA.get_harm_caused_and_hazard_event_input()

        return first_harm_caused_prompt_input.generate_prompt()
    
    def get_pattern_matched_and_prompt_output(self, input_object):

        harm_caused_prompt_input = input_object.get_harm_caused_and_hazard_event_input()
        harm_caused_prompt_output, harm_caused_pattern = input_object.get_prompt_output_and_pattern_matched(prompt_input_object=harm_caused_prompt_input, LLM_caller=self.LLM)

        return True, harm_caused_prompt_output