from PromptInputs import Prevention
from ExamplesGenerator import ExamplesGenerator
from TestModelAccuracy import TestModelAccuracy
from LLMCaller import GPT_3_point_5_turbo
from example_risk_assessments import example_risk_assessments

from example_preventions import correct_prevention_examples_list, PreventionExamplesGenerator
from ExamplesGenerator import RiskAssessmentExamplesGeneratorForSinglePrompt

if __name__ == '__main__':
    # examples_generator = PreventionExamplesGenerator(correct_examples_list=correct_prevention_examples_list)
    examples_generator = RiskAssessmentExamplesGeneratorForSinglePrompt(risk_assessments=example_risk_assessments,
                                                         ground_truth_parameter='prevention_prompt_expected_class',
                                                        method_to_get_prompt_input='get_prevention_input')
    
    examples = examples_generator.get_input_and_expected_output_list()

    test_accuracy = TestModelAccuracy(test_description="""Testing prevention input in student Fluids Lab and TPS presentation Risk Assessment examples.
                                      Removed definitions from prompt. Made it more clear that a mitigation reduces severity assuming hazard has led to harm.
                                       """,
                                      LLM=GPT_3_point_5_turbo(temperature=0.1, max_tokens=400),
                                                LLM_name='gpt-3.5-turbo',
                                                list_of_input_and_expected_outputs=examples,
                                                sheet_name='Prevention In Context')
    test_accuracy.run_test()