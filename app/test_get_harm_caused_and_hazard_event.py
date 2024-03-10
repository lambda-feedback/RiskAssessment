
from TestModelAccuracy import TestHarmCausedAndHazardEventPrompt
from LLMCaller import OpenAILLM
from example_risk_assessments import example_risk_assessments, example_risk_assessments_dict, number_of_risk_assessments_in_each_domain

from ExamplesGenerator import RiskAssessmentExamplesGeneratorForMultiplePrompts

if __name__ == '__main__':
    # examples_generator = PreventionExamplesGenerator(correct_examples_list=correct_prevention_examples_list)
    examples_generator = RiskAssessmentExamplesGeneratorForMultiplePrompts(risk_assessments=example_risk_assessments,
                                                         ground_truth_parameter='always_true')

    examples = examples_generator.get_risk_assessment_and_expected_output_list()

    test_accuracy = TestHarmCausedAndHazardEventPrompt(
                                      LLM=OpenAILLM(),
                                    list_of_risk_assessment_and_expected_outputs=examples,
                                    number_of_examples_in_each_domain=number_of_risk_assessments_in_each_domain,
                                    examples_gathered_or_generated_message='Risk assessments gathered and not AI-generated',
                                    candidate_labels=[True, False],
                                    sheet_name='Get Harm Caused')
    
    test_accuracy.run_test()