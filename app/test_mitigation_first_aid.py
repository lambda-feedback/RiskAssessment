from PromptInputs import Prevention
from ExamplesGenerator import ExamplesGenerator
from TestModelAccuracy import TestModelAccuracy
from LLMCaller import OpenAILLM
from example_risk_assessments import example_risk_assessments_for_protective_clothing_and_first_aid

from ExamplesGenerator import RiskAssessmentExamplesGeneratorForSinglePrompt

if __name__ == '__main__':
    examples_generator = RiskAssessmentExamplesGeneratorForSinglePrompt(risk_assessments=example_risk_assessments_for_protective_clothing_and_first_aid,
                                                         ground_truth_parameter='mitigation_first_aid_expected_output',
                                                        method_to_get_prompt_input='get_mitigation_first_aid_input')
    
    examples = examples_generator.get_input_and_expected_output_list()

    test_accuracy = TestModelAccuracy(test_description="""Testing mitigation input in the first aid prompt. Use examples from student Fluids Lab and TPS presentation Risk Assessment examples.
                                       """,
                                      LLM=OpenAILLM(),
                                                LLM_name='gpt-3.5-turbo',
                                                list_of_input_and_expected_outputs=examples,
                                                sheet_name='Mitigation First Aid')
    test_accuracy.run_test()