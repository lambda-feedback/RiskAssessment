from TestModelAccuracy import TestPreventionPromptInput, TestMitigationPromptInput, TestBothPreventionAndMitigationInput
from LLMCaller import OpenAILLM, ClaudeSonnetLLM, Mixtral8x7B
from example_risk_assessments import *

from ExamplesGenerator import RiskAssessmentExamplesGeneratorForMultiplePrompts

def test_prevention_combined_prompts(risk_assessments_dict, LLM, is_first_test: bool = False):
    risk_assessments = risk_assessments_dict['risk_assessments']
    examples_generator = RiskAssessmentExamplesGeneratorForMultiplePrompts(risk_assessments=risk_assessments,
                                                          ground_truth_parameter='prevention_prompt_expected_class')
    
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

def test_mitigation_combined_prompts(risk_assessments_dict, LLM, is_first_test: bool = False):
    examples_generator = RiskAssessmentExamplesGeneratorForMultiplePrompts(risk_assessments=risk_assessments_dict['risk_assessments'],
                                                          ground_truth_parameter='mitigation_prompt_expected_class')
    
    examples = examples_generator.get_risk_assessment_and_expected_output_list()

    test_accuracy = TestMitigationPromptInput(
                                    LLM=LLM,
                                    is_first_test=is_first_test,
                                    domain=risk_assessments_dict['risk_domain'],
                                    list_of_risk_assessment_and_expected_outputs=examples,
                                    examples_gathered_or_generated_message='Risk assessments gathered and not AI-generated',
                                    candidate_labels=['prevention', 'mitigation', 'neither', 'both'],
                                    sheet_name='Combined Mitigation Prompts')
    
    test_accuracy.run_test()

def test_both_prevention_and_mitigation_inputs(risk_assessments_dict, LLM, is_first_test: bool = False):
    examples_generator = RiskAssessmentExamplesGeneratorForMultiplePrompts(risk_assessments=risk_assessments_dict['risk_assessments'],
                                                          ground_truth_parameter='prevention_and_mitigation_expected_class_combined')
    
    examples = examples_generator.get_risk_assessment_and_expected_output_list()

    test_accuracy = TestBothPreventionAndMitigationInput(
                                    LLM=LLM,
                                    is_first_test=is_first_test,
                                    domain=risk_assessments_dict['risk_domain'],
                                    list_of_risk_assessment_and_expected_outputs=examples,
                                    examples_gathered_or_generated_message='Risk assessments gathered and not AI-generated',
                                    candidate_labels=['prevention, prevention', 'prevention, mitigation', 'prevention, both', 'prevention, neither', 'mitigation, prevention', 'mitigation, mitigation', 'mitigation, both', 'mitigation, neither', 'both, prevention', 'both, mitigation', 'both, both', 'both, neither', 'neither, prevention', 'neither, mitigation', 'neither, both', 'neither, neither'],
                                    sheet_name='Testing Prevention and Mitigation Input')
    
    test_accuracy.run_test()

if __name__ == '__main__':
    ### Mixtral8x7B TESTS ###
    # test_prevention_combined_prompts(
    #     risk_assessments_dict=physical_risks_to_individuals__original_student_data,
    #     LLM=Mixtral8x7B(temperature=0.1, max_tokens=400),
    #     is_first_test=True
    # )
    # test_prevention_combined_prompts(
    #     risk_assessments_dict=physical_risks_to_individuals__data_gathered_from_version_1_deployment,
    #     LLM=Mixtral8x7B(temperature=0.1, max_tokens=400),
    #     is_first_test=False
    # )
    # test_prevention_combined_prompts(
    #     risk_assessments_dict=natural_disaster_risks,
    #     LLM=Mixtral8x7B(temperature=0.1, max_tokens=400),
    #     is_first_test=False
    # )
    # test_prevention_combined_prompts(
    #     risk_assessments_dict=cybersecurity_risks,
    #     LLM=Mixtral8x7B(temperature=0.1, max_tokens=400),
    #     is_first_test=False
    # )
    # test_prevention_combined_prompts(
    #     risk_assessments_dict=biohazard_risks,
    #     LLM=Mixtral8x7B(temperature=0.1, max_tokens=400),
    #     is_first_test=False
    # )
    # test_prevention_combined_prompts(
    #     risk_assessments_dict=terrorism_risks,
    #     LLM=Mixtral8x7B(temperature=0.1, max_tokens=400),
    #     is_first_test=True
    # )
    # test_mitigation_combined_prompts(
    #     risk_assessments_dict=physical_risks_to_individuals__original_student_data,
    #     LLM=Mixtral8x7B(temperature=0.1, max_tokens=400),
    #     is_first_test=False
    # )
    # test_mitigation_combined_prompts(
    #     risk_assessments_dict=physical_risks_to_individuals__data_gathered_from_version_1_deployment,
    #     LLM=Mixtral8x7B(temperature=0.1, max_tokens=400),
    #     is_first_test=False
    # )
    # test_mitigation_combined_prompts(
    #     risk_assessments_dict=natural_disaster_risks,
    #     LLM=Mixtral8x7B(temperature=0.1, max_tokens=400),
    #     is_first_test=False
    # )
    # test_mitigation_combined_prompts(
    #     risk_assessments_dict=cybersecurity_risks,
    #     LLM=Mixtral8x7B(temperature=0.1, max_tokens=400),
    #     is_first_test=False
    # )
    # test_mitigation_combined_prompts(
    #     risk_assessments_dict=biohazard_risks,
    #     LLM=Mixtral8x7B(temperature=0.1, max_tokens=400),
    #     is_first_test=False
    # )
    # test_mitigation_combined_prompts(
    #     risk_assessments_dict=terrorism_risks,
    #     LLM=Mixtral8x7B(temperature=0.1, max_tokens=400),
    #     is_first_test=False
    # )

    # ### GPT-3.5 TESTS ###
    test_both_prevention_and_mitigation_inputs(
        risk_assessments_dict=physical_risks_to_individuals__data_gathered_from_version_1_deployment,
        LLM=OpenAILLM(temperature=0.1, max_tokens=400),
        is_first_test=True
    )
    # test_prevention_combined_prompts(
    #     risk_assessments_dict=physical_risks_to_individuals__original_student_data,
    #     LLM=OpenAILLM(temperature=0.1, max_tokens=400),
    #     is_first_test=False
    # )
    # test_prevention_combined_prompts(
    #     risk_assessments_dict=physical_risks_to_individuals__data_gathered_from_version_1_deployment,
    #     LLM=OpenAILLM(temperature=0.1, max_tokens=400),
    #     is_first_test=False
    # )
    # test_prevention_combined_prompts(
    #     risk_assessments_dict=natural_disaster_risks,
    #     LLM=OpenAILLM(temperature=0.1, max_tokens=400),
    #     is_first_test=False
    # )
    # test_prevention_combined_prompts(
    #     risk_assessments_dict=cybersecurity_risks,
    #     LLM=OpenAILLM(temperature=0.1, max_tokens=400),
    #     is_first_test=False
    # )
    # test_prevention_combined_prompts(
    #     risk_assessments_dict=biohazard_risks,
    #     LLM=OpenAILLM(temperature=0.1, max_tokens=400),
    #     is_first_test=False
    # )
    # test_prevention_combined_prompts(
    #     risk_assessments_dict=terrorism_risks,
    #     LLM=OpenAILLM(temperature=0.1, max_tokens=400),
    #     is_first_test=False
    # )
    # test_mitigation_combined_prompts(
    #     risk_assessments_dict=physical_risks_to_individuals__original_student_data,
    #     LLM=OpenAILLM(temperature=0.1, max_tokens=400),
    #     is_first_test=False
    # )
    # test_mitigation_combined_prompts(
    #     risk_assessments_dict=physical_risks_to_individuals__data_gathered_from_version_1_deployment,
    #     LLM=OpenAILLM(temperature=0.1, max_tokens=400),
    #     is_first_test=False
    # )
    # test_mitigation_combined_prompts(
    #     risk_assessments_dict=natural_disaster_risks,
    #     LLM=OpenAILLM(temperature=0.1, max_tokens=400),
    #     is_first_test=False
    # )
    # test_mitigation_combined_prompts(
    #     risk_assessments_dict=cybersecurity_risks,
    #     LLM=OpenAILLM(temperature=0.1, max_tokens=400),
    #     is_first_test=False
    # )
    # test_mitigation_combined_prompts(
    #     risk_assessments_dict=biohazard_risks,
    #     LLM=OpenAILLM(temperature=0.1, max_tokens=400),
    #     is_first_test=False
    # )
    # test_mitigation_combined_prompts(
    #     risk_assessments_dict=terrorism_risks,
    #     LLM=OpenAILLM(temperature=0.1, max_tokens=400),
    #     is_first_test=False
    # )

    ### CLAUDE SONNET TESTS
    # test_both_prevention_and_mitigation_inputs(
    #     risk_assessments_dict=physical_risks_to_individuals__data_gathered_from_version_1_deployment,
    #     LLM=ClaudeSonnetLLM(system_message='', temperature=0.1, max_tokens=400),
    #     is_first_test=True
    # )
    # test_prevention_combined_prompts(
    #     risk_assessments_dict=physical_risks_to_individuals__original_student_data,
    #     LLM=ClaudeSonnetLLM(system_message='', temperature=0.1, max_tokens=400),
    #     is_first_test=False
    # )
    # test_prevention_combined_prompts(
    #     risk_assessments_dict=physical_risks_to_individuals__data_gathered_from_version_1_deployment,
    #     LLM=ClaudeSonnetLLM(system_message='', temperature=0.1, max_tokens=400),
    #     is_first_test=True
    # )
    # test_prevention_combined_prompts(
    #     risk_assessments_dict=natural_disaster_risks,
    #     LLM=ClaudeSonnetLLM(system_message='', temperature=0.1, max_tokens=400),
    #     is_first_test=False
    # )
    # test_prevention_combined_prompts(
    #     risk_assessments_dict=cybersecurity_risks,
    #     LLM=ClaudeSonnetLLM(system_message='', temperature=0.1, max_tokens=400),
    #     is_first_test=False
    # )
    # test_prevention_combined_prompts(
    #     risk_assessments_dict=biohazard_risks,
    #     LLM=ClaudeSonnetLLM(system_message='', temperature=0.1, max_tokens=400),
    #     is_first_test=False
    # )
    # test_prevention_combined_prompts(
    #     risk_assessments_dict=terrorism_risks,
    #     LLM=ClaudeSonnetLLM(system_message='', temperature=0.1, max_tokens=400),
    #     is_first_test=False
    # )
    # test_mitigation_combined_prompts(
    #     risk_assessments_dict=physical_risks_to_individuals__original_student_data,
    #     LLM=ClaudeSonnetLLM(system_message='', temperature=0.1, max_tokens=400),
    #     is_first_test=False
    # )
    # test_mitigation_combined_prompts(
    #     risk_assessments_dict=physical_risks_to_individuals__data_gathered_from_version_1_deployment,
    #     LLM=ClaudeSonnetLLM(system_message='', temperature=0.1, max_tokens=400),
    #     is_first_test=False
    # )
    # test_mitigation_combined_prompts(
    #     risk_assessments_dict=natural_disaster_risks,
    #     LLM=ClaudeSonnetLLM(system_message='', temperature=0.1, max_tokens=400),
    #     is_first_test=False
    # )
    # test_mitigation_combined_prompts(
    #     risk_assessments_dict=cybersecurity_risks,
    #     LLM=ClaudeSonnetLLM(system_message='', temperature=0.1, max_tokens=400),
    #     is_first_test=False
    # )
    # test_mitigation_combined_prompts(
    #     risk_assessments_dict=biohazard_risks,
    #     LLM=ClaudeSonnetLLM(system_message='', temperature=0.1, max_tokens=400),
    #     is_first_test=False
    # )
    # test_mitigation_combined_prompts(
    #     risk_assessments_dict=terrorism_risks,
    #     LLM=ClaudeSonnetLLM(system_message='', temperature=0.1, max_tokens=400),
    #     is_first_test=False
    # )