# python -m app.test_scripts.test_control_measure_classification_prompts_without_context_of_other_inputs

from ..test_classes.TestModelAccuracy import TestModelAccuracy
from ..utils.LLMCaller import *
from ..test_utils.ExamplesGenerator import RiskAssessmentExamplesGeneratorForSinglePrompt
from ..data.example_risk_assessments import *

def test_control_measure_classification_prompt(risk_assessments_dict, 
                                               LLM, 
                                               ground_truth_parameter,
                                               method_to_get_prompt_input,
                                               sheet_name,
                                               is_first_test=False):
    
    examples = RiskAssessmentExamplesGeneratorForSinglePrompt(
        risk_assessments=risk_assessments_dict['risk_assessments'],
        ground_truth_parameter=ground_truth_parameter,
        method_to_get_prompt_input=method_to_get_prompt_input
    )

    test = TestModelAccuracy(
        LLM=LLM,
        list_of_input_and_expected_outputs=examples.get_input_and_expected_output_list(),
        sheet_name=sheet_name,
        examples_gathered_or_generated_message='Risk Assessments gathered from students',
        domain=risk_assessments_dict['risk_domain'],
        is_first_test=is_first_test
    )

    test.run_test()

def test_prevention_classification_prompt(risk_assessments_dict, LLM, is_first_test=False):

    test_control_measure_classification_prompt(
        risk_assessments_dict=risk_assessments_dict,
        LLM=LLM,
        ground_truth_parameter='prevention_classification_prompt_ground_truth',
        method_to_get_prompt_input='get_prevention_classification_prompt_input',
        sheet_name='Prevention Classification 2',
        is_first_test=is_first_test
    )

def test_mitigation_classification_prompt(risk_assessments_dict, LLM, is_first_test=False):

    test_control_measure_classification_prompt(
        risk_assessments_dict=risk_assessments_dict,
        LLM=LLM,
        ground_truth_parameter='mitigation_classification_prompt_ground_truth',
        method_to_get_prompt_input='get_mitigation_classification_prompt_input',
        sheet_name='Mitigation Classification',
        is_first_test=is_first_test
    )

if __name__ == '__main__':
    # test_prevention_classification_prompt(
    #     risk_assessments_dict=physical_risks_to_individuals__data_gathered_from_version_1_deployment,
    #     LLM=MistralLarge(temperature=0.1),
    #     is_first_test=True
    # )

    # test_prevention_classification_prompt(
    #     risk_assessments_dict=natural_disaster_risks,
    #     LLM=MistralLarge(temperature=0.1),
    #     is_first_test=False
    # )

    # test_prevention_classification_prompt(
    #     risk_assessments_dict=cybersecurity_risks,
    #     LLM=MistralLarge(temperature=0.1),
    #     is_first_test=False
    # )

    # test_prevention_classification_prompt(
    #     risk_assessments_dict=terrorism_risks,
    #     LLM=MistralLarge(temperature=0.1),
    #     is_first_test=False
    # )

    # test_prevention_classification_prompt(
    #     risk_assessments_dict=biohazard_risks,
    #     LLM=MistralLarge(temperature=0.1),
    #     is_first_test=False
    # )

    # test_mitigation_classification_prompt(
    #     risk_assessments_dict=physical_risks_to_individuals__data_gathered_from_version_1_deployment,
    #     LLM=MistralLarge(temperature=0.1),
    #     is_first_test=False
    # )

    test_mitigation_classification_prompt(
        risk_assessments_dict=natural_disaster_risks,
        LLM=MistralLarge(temperature=0.1),
        is_first_test=False
    )

    # test_mitigation_classification_prompt(
    #     risk_assessments_dict=cybersecurity_risks,
    #     LLM=MistralLarge(temperature=0.1),
    #     is_first_test=False
    # )

    # test_mitigation_classification_prompt(
    #     risk_assessments_dict=terrorism_risks,
    #     LLM=MistralLarge(temperature=0.1),
    #     is_first_test=False
    # )

    # test_mitigation_classification_prompt(
    #     risk_assessments_dict=biohazard_risks,
    #     LLM=MistralLarge(temperature=0.1),
    #     is_first_test=False
    # )