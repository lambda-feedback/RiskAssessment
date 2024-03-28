from TestModelAccuracy import TestPreventionPromptInput
from LLMCaller import OpenAILLM, AnthropicLLM, MistralLLM
from example_risk_assessments import cybersecurity_risks

from ExamplesGenerator import RiskAssessmentExamplesGeneratorForMultiplePrompts

def test_prevention_combined_prompts(risk_assessments_dict, LLM, is_first_test: bool = False):
    risk_assessments = risk_assessments_dict['risk_assessments']
    examples_generator = RiskAssessmentExamplesGeneratorForMultiplePrompts(risk_assessments=risk_assessments,
                                                          ground_truth_parameter='prevention_prompt_expected_output')
    
    examples = examples_generator.get_risk_assessment_and_expected_output_list()

    test_accuracy = TestPreventionPromptInput(
                                    LLM=LLM,
                                    is_first_test=is_first_test,
                                    domain=risk_assessments_dict['risk_domain'],       
                                    list_of_risk_assessment_and_expected_outputs=examples,
                                    examples_gathered_or_generated_message='Risk assessments gathered and not AI-generated',
                                    candidate_labels=['prevention', 'mitigation', 'neither', 'both'],
                                    sheet_name='Combined Prevention Prompts')

    test_accuracy.run_test()

if __name__ == '__main__':
    test_prevention_combined_prompts(
        risk_assessments_dict=cybersecurity_risks,
        LLM=MistralLLM(model='open-mixtral-8x7b', temperature=0.1, max_tokens=300),
        is_first_test=True
    )