from TestModelAccuracy import TestModelAccuracy
from LLMCaller import *
from ExamplesGenerator import RiskAssessmentExamplesGeneratorForSinglePrompt
from example_risk_assessments import physical_risks_to_individuals__original_student_data

def test_mitigation_classification_prompt(risk_assessments_dict, LLM, is_first_test=False):

    examples = RiskAssessmentExamplesGeneratorForSinglePrompt(
    risk_assessments=risk_assessments_dict['risk_assessments'],
    ground_truth_parameter='mitigation_classification_prompt_ground_truth',
    method_to_get_prompt_input='get_mitigation_classification_prompt_input'
    )

    test = TestModelAccuracy(
        LLM=LLM,
        list_of_input_and_expected_outputs=examples.get_input_and_expected_output_list(),
        sheet_name='Mitigation Classification',
        examples_gathered_or_generated_message='Risk Assessments gathered from students',
        domain=risk_assessments_dict['domain'],
        is_first_test=is_first_test
    )

    test.run_test()

if __name__ == '__main__':
    test_mitigation_classification_prompt(
        risk_assessments_dict=physical_risks_to_individuals__original_student_data,
        LLM=MistralLarge(temperature=0.1),
        is_first_test=True
    )

    test_mitigation_classification_prompt(
        risk_assessments_dict=physical_risks_to_individuals__original_student_data,
        LLM=MistralLarge(temperature=0.1),
        is_first_test=False
    )