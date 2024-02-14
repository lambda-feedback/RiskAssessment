
from TestModelAccuracy import TestModelAccuracy
from LLMCaller import OpenAILLM
from example_risk_assessments import example_risk_assessments

from ExamplesGenerator import RiskAssessmentExamplesGeneratorForSinglePrompt

if __name__ == '__main__':
    # examples_generator = PreventionExamplesGenerator(correct_examples_list=correct_prevention_examples_list)
    examples_generator = RiskAssessmentExamplesGeneratorForSinglePrompt(risk_assessments=example_risk_assessments,
                                                         ground_truth_parameter='prevention_protected_clothing_expected_output',
                                                        method_to_get_prompt_input='get_hazard_event_input')
    
    examples = examples_generator.get_input_and_expected_output_list()

    test_accuracy = TestModelAccuracy(test_description="""Testing ability of LLM to produce hazard event and harm caused from hazard and how it harms inputs 
                                      Testing with examples from student Fluids Lab and TPS presentation Risk Assessment examples.
                                       """,
                                      LLM=OpenAILLM(),
                                                LLM_name='gpt-3.5-turbo',
                                                list_of_input_and_expected_outputs=examples,
                                                sheet_name='Get Hazard Event')
    test_accuracy.run_test()