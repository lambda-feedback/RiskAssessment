from InputAndExpectedOutput import InputAndExpectedOutputForSinglePrompt
from LLMCaller import GPT_3_point_5_turbo
from PromptInputs import RiskDomainClassification
from TestModelAccuracy import TestModelAccuracy

from example_risk_assessments import example_risk_assessments_dict, example_risk_assessments, number_of_risk_assessments_in_each_domain

from ExamplesGenerator import RiskAssessmentExamplesGeneratorForSinglePrompt


if __name__ == '__main__':

    examples_generator = RiskAssessmentExamplesGeneratorForSinglePrompt(risk_assessments=example_risk_assessments,
                                                         ground_truth_parameter='risk_domain',
                                                         method_to_get_prompt_input='get_risk_domain_classification_input')
  
    examples = examples_generator.get_input_and_expected_output_list()

    test_accuracy = TestModelAccuracy(
                                      LLM=GPT_3_point_5_turbo(temperature=0.1),                      
                                    list_of_input_and_expected_outputs=examples,
                                    number_of_examples_in_each_domain=number_of_risk_assessments_in_each_domain,
                                    examples_gathered_or_generated_message='Risk assessments gathered and not AI-generated',
                                    sheet_name='Risk Domain')

    test_accuracy.run_test()
