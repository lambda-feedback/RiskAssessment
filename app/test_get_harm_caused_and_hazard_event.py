
from TestModelAccuracy import TestHarmCausedAndHazardEventPrompt
from LLMCaller import *
from example_risk_assessments import biohazard_risks, physical_risks_to_individuals__data_gathered_from_version_1_deployment, physical_risks_to_individuals__original_student_data

from ExamplesGenerator import RiskAssessmentExamplesGeneratorForMultiplePrompts

def test_harm_caused_and_hazard_event(risk_assessments_dict, LLM, is_first_test: bool = False):
    risk_assessments = risk_assessments_dict['risk_assessments']
    examples_generator = RiskAssessmentExamplesGeneratorForMultiplePrompts(risk_assessments=risk_assessments,
                                                          ground_truth_parameter='always_true')
    
    examples = examples_generator.get_risk_assessment_and_expected_output_list()

    test_accuracy = TestHarmCausedAndHazardEventPrompt(
                                    LLM=LLM,
                                    is_first_test=is_first_test,
                                    domain=risk_assessments_dict['risk_domain'],       
                                    list_of_risk_assessment_and_expected_outputs=examples,
                                    examples_gathered_or_generated_message='Risk assessments gathered and not AI-generated',
                                    candidate_labels=[True, False],
                                    sheet_name='Harm Caused and Hazard Event')

    test_accuracy.run_test()

if __name__ == '__main__':
    test_harm_caused_and_hazard_event(
        # LLM=ClaudeSonnetLLM(system_message='', temperature=0.1, max_tokens=300),
        LLM=OpenAILLM(),
        risk_assessments_dict=physical_risks_to_individuals__data_gathered_from_version_1_deployment,
        is_first_test=True)