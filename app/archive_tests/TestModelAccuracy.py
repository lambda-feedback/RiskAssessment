# class TestModelAccuracyForCompletePreventionPromptPipeline(TestModelAccuracyForCombinationOfPrompts):
#     def __init__(self, 
#                     LLM: LLMCaller,
#                     list_of_risk_assessment_and_expected_outputs: list[InputAndExpectedOutputForCombinedPrompts],
#                     number_of_examples_in_each_domain: dict,
#                     sheet_name: str,
#                     examples_gathered_or_generated_message: str,
#                     candidate_labels: list):
        
#         super().__init__(LLM, list_of_risk_assessment_and_expected_outputs, number_of_examples_in_each_domain, sheet_name, examples_gathered_or_generated_message, candidate_labels)

#     def get_classes(self):
#         return ['prevention', 'mitigation', 'neither', 'both']
    
#     def get_first_prompt_input(self):
#         first_RA = self.list_of_risk_assessment_and_expected_outputs[0].risk_assessment

#         first_harm_caused_prompt_input = first_RA.get_harm_caused_and_hazard_event_input()
#         first_harm_caused_prompt = first_harm_caused_prompt_input.generate_prompt()
#         harm_caused_and_hazard_event_prompt_output, harm_caused_and_hazard_event_pattern = first_RA.get_prompt_output_and_pattern_matched(first_harm_caused_prompt_input, self.LLM)

#         hazard_event = harm_caused_and_hazard_event_pattern.hazard_event
#         harm_caused = harm_caused_and_hazard_event_pattern.harm_caused

#         first_prevention_prompt_with_prevention_input = first_RA.get_prevention_prompt_with_prevention_input()
#         first_prevention_prompt_with_prevention_prompt = first_prevention_prompt_with_prevention_input.generate_prompt(hazard_event=hazard_event, harm_caused=harm_caused)

#         first_mitigation_prompt_with_prevention_input = first_RA.get_mitigation_prompt_with_prevention_input()
#         first_mitigation_prompt_with_prevention_prompt = first_mitigation_prompt_with_prevention_input.generate_prompt(hazard_event=hazard_event, harm_caused=harm_caused)

#         return f'''Harm Caused:\n{first_harm_caused_prompt}\n\nPrevention :\n{first_prevention_prompt_with_prevention_prompt}\n\nMitigation: {first_mitigation_prompt_with_prevention_prompt}'''
    
#     def get_pattern_matched_and_prompt_output(self, i):
#         RA = self.list_of_risk_assessment_and_expected_outputs[i].risk_assessment
#         expected_output = self.list_of_risk_assessment_and_expected_outputs[i].expected_output

#         harm_caused_and_hazard_event_prompt_input = RA.get_harm_caused_and_hazard_event_input()
#         harm_caused_and_hazard_event_prompt_output, harm_caused_and_hazard_event_pattern = RA.get_prompt_output_and_pattern_matched(harm_caused_and_hazard_event_prompt_input, self.LLM)

#         hazard_event = harm_caused_and_hazard_event_pattern.hazard_event
#         harm_caused = harm_caused_and_hazard_event_pattern.harm_caused

#         prevention_prompt_with_prevention_input = RA.get_prevention_prompt_with_prevention_input()
#         prevention_prompt_with_prevention_output, prevention_prompt_with_prevention_pattern = RA.get_prompt_output_and_pattern_matched(prevention_prompt_with_prevention_input, self.LLM, harm_caused=harm_caused, hazard_event=hazard_event)

#         mitigation_prompt_with_prevention_input = RA.get_mitigation_prompt_with_prevention_input()
#         mitigation_prompt_with_prevention_output, mitigation_prompt_with_prevention_pattern = RA.get_prompt_output_and_pattern_matched(mitigation_prompt_with_prevention_input, self.LLM, harm_caused=harm_caused, hazard_event=hazard_event)

#         prompt_output = f'''{harm_caused_and_hazard_event_prompt_output}\n\n{prevention_prompt_with_prevention_output}\n\n{mitigation_prompt_with_prevention_output}'''

#         if prevention_prompt_with_prevention_pattern == True and mitigation_prompt_with_prevention_pattern == True:
#             return expected_output, 'both', prompt_output
        
#         if prevention_prompt_with_prevention_pattern == True and mitigation_prompt_with_prevention_pattern == False:
#             return expected_output, 'prevention', prompt_output
        
#         if prevention_prompt_with_prevention_pattern == False and mitigation_prompt_with_prevention_pattern == True:
#             return expected_output, 'mitigation', prompt_output
        
#         if prevention_prompt_with_prevention_pattern == False and mitigation_prompt_with_prevention_pattern == False:
#             return expected_output, 'neither', prompt_output

# class TestIsFutureHarmReducedPromptInputWithPrevention(TestControlMeasureClassificationPrompt):
#     def __init__(self, 
#                     LLM: LLMCaller,
#                     list_of_risk_assessment_and_expected_outputs: list,
#                     sheet_name: str,
#                     examples_gathered_or_generated_message: str,
#                     candidate_labels: list,
#                     domain: str = None,
#                     is_first_test: bool = False):
        
#         super().__init__(LLM, list_of_risk_assessment_and_expected_outputs, sheet_name, examples_gathered_or_generated_message, candidate_labels, domain=domain, is_first_test=is_first_test)

#     def get_classes(self):
#         return [True, False]
    
#     def get_first_prompt_input(self):
#         return self.get_first_prompt_input_with_risk_assessment_method('is_future_harm_reduced_prompt_input_with_prevention')
    
#     def get_pattern_matched_and_prompt_output(self, i):
#         return self.get_pattern_matched_and_prompt_output_with_risk_assessment_method(i, 'is_future_harm_reduced_prompt_input_with_prevention')

# class TestIsFutureHarmReducedPromptInputWithMitigation(TestControlMeasureClassificationPrompt):
#     def __init__(self, 
#                     LLM: LLMCaller,
#                     list_of_risk_assessment_and_expected_outputs: list,
#                     sheet_name: str,
#                     examples_gathered_or_generated_message: str,
#                     candidate_labels: list,
#                     domain: str = None,
#                     is_first_test: bool = False):
        
#         super().__init__(LLM, list_of_risk_assessment_and_expected_outputs, sheet_name, examples_gathered_or_generated_message, candidate_labels, domain=domain, is_first_test=is_first_test)

#     def get_classes(self):
#         return [True, False]
    
#     def get_first_prompt_input(self):
#         return self.get_first_prompt_input_with_risk_assessment_method('is_future_harm_reduced_prompt_input_with_mitigation')
    
#     def get_pattern_matched_and_prompt_output(self, i):
#         return self.get_pattern_matched_and_prompt_output_with_risk_assessment_method(i, 'is_future_harm_reduced_prompt_input_with_mitigation')