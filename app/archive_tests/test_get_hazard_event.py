
# from TestModelAccuracy import TestHazardEventPrompt
# from LLMCaller import GPT_3_point_5_turbo
# from example_risk_assessments_exemplar import example_risk_assessments

# from ExamplesGenerator import RiskAssessmentExamplesGeneratorForMultiplePrompts

# if __name__ == '__main__':
#     # examples_generator = PreventionExamplesGenerator(correct_examples_list=correct_prevention_examples_list)
#     examples_generator = RiskAssessmentExamplesGeneratorForMultiplePrompts(risk_assessments=example_risk_assessments,
#                                                          ground_truth_parameter='always_true',
#                                                         method_to_get_prompt_input='get_hazard_event_input')

#     examples = examples_generator.get_risk_assessment_and_expected_output_list()

#     test_accuracy = TestHazardEventPrompt(test_description="""Testing ability of LLM to produce hazard harm caused from hazard and how it harms inputs 
#                                       Testing with examples from student Fluids Lab and TPS presentation Risk Assessment examples.
#                                         Testing finance examples.
#                                           """,
#                                       LLM=GPT_3_point_5_turbo(temperature=0.1, max_tokens=400),
#                                                 LLM_name='gpt-3.5-turbo',
#                                                 list_of_risk_assessment_and_expected_outputs=examples,
#                                                 sheet_name='Get Hazard Event')
#     test_accuracy.run_test()