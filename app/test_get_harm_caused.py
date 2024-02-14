
from TestModelAccuracy import TestIllnessAndInjuryPrompts
from LLMCaller import OpenAILLM
from example_risk_assessments import example_risk_assessments

from ExamplesGenerator import RiskAssessmentExamplesGeneratorForMultiplePrompts

if __name__ == '__main__':
    # examples_generator = PreventionExamplesGenerator(correct_examples_list=correct_prevention_examples_list)
    examples_generator = RiskAssessmentExamplesGeneratorForMultiplePrompts(risk_assessments=example_risk_assessments,
                                                         ground_truth_parameter='prevention_protected_clothing_expected_output',
                                                        method_to_get_prompt_input='get_injury_input')

    examples = examples_generator.get_risk_assessment_and_expected_output_list()

    test_accuracy = TestIllnessAndInjuryPrompts(test_description="""Testing ability of LLM to produce hazard event and harm caused from hazard and how it harms inputs 
                                      Testing with examples from student Fluids Lab and TPS presentation Risk Assessment examples.
                                       """,
                                      LLM=OpenAILLM(),
                                                LLM_name='gpt-3.5-turbo',
                                                list_of_risk_assessment_and_expected_outputs=examples,
                                                sheet_name='Get Harm Caused')
    test_accuracy.run_test()