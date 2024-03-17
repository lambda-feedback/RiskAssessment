from TestModelAccuracy import TestPreventionPromptInput
from LLMCaller import OpenAILLM, AnthropicLLM
from example_risk_assessments import example_risk_assessments_dict, example_risk_assessments, number_of_risk_assessments_in_each_domain

from ExamplesGenerator import RiskAssessmentExamplesGeneratorForMultiplePrompts

if __name__ == '__main__':
    
    examples_generator = RiskAssessmentExamplesGeneratorForMultiplePrompts(risk_assessments=example_risk_assessments,
                                                          ground_truth_parameter='prevention_prompt_expected_output')
    
    examples = examples_generator.get_risk_assessment_and_expected_output_list()

    test_accuracy = TestPreventionPromptInput(
                                      LLM=AnthropicLLM(name='claude-3-sonnet-20240229', system_message=''),                    
                                    list_of_risk_assessment_and_expected_outputs=examples,
                                    number_of_examples_in_each_domain=number_of_risk_assessments_in_each_domain,
                                    examples_gathered_or_generated_message='Risk assessments gathered and not AI-generated',
                                    candidate_labels=['prevention', 'mitigation', 'neither', 'both'],
                                    sheet_name='Combined Prevention Prompts')

    test_accuracy.run_test()