# python -m app.test_scripts.risk_domain_test_for_how_it_harms_prompt

from ..test_classes.TestModelAccuracy import TestModelAccuracy
from ..test_utils.ExamplesGenerator import ExamplesGeneratorFromCorrectExamples
from ..prompts.HowItHarmsInContext import HowItHarmsInContext
from ..data.example_risk_assessments import *
from ..utils.LLMCaller import *

class HowItHarmsInContextExamplesGeneratorForRiskDomainTest(ExamplesGeneratorFromCorrectExamples):
    def generate_incorrect_example(self, correct_index, incorrect_index):
        return HowItHarmsInContext(
                activity=self.correct_examples_list[correct_index].activity, 
                hazard=self.correct_examples_list[correct_index].hazard, 
                how_it_harms=self.correct_examples_list[incorrect_index].how_it_harms)

def generate_correct_examples_list_for_risk_domain_test_of_how_it_harms_prompt(risk_assessment_dict_from_first_risk_domain,
                                                        risk_assessment_dict_from_second_risk_domain):
    risk_assessments_list = []

    # Number of examples is limited by the second type of risk domain
    # as the first risk domain type is always physical risks and there are many examples
    # of risk assessments in this domain
    number_of_examples_taken_from_each_domain = len(risk_assessment_dict_from_second_risk_domain['risk_assessments'])
    
    for i in range(number_of_examples_taken_from_each_domain):
    # TODO: Some of the correct volcano/earthquake examples are duplicates 
    # because the activity, hazard and how it harms are all the same.
     
    # NOTE: For the incorrect examples, even numbers have "how it harms" belonging to first_risk_assessment_example
    # and "hazard" and "activity" corresponding to second_risk_assessment_example
    
    # Also for incorrect examples, odd numbers have "how it harms" belonging to second_risk_assessment_example
    # and "hazard" and "activity" corresponding to first_risk_assessment_example
        first_risk_assessment_example = risk_assessment_dict_from_first_risk_domain['risk_assessments'][i]
        second_risk_assessment_example = risk_assessment_dict_from_second_risk_domain['risk_assessments'][i]
        risk_assessments_list.append(first_risk_assessment_example)
        risk_assessments_list.append(second_risk_assessment_example)

    correct_examples_list = []

    for risk_assessment in risk_assessments_list:
        correct_examples_list.append(risk_assessment.get_how_it_harms_in_context_input())

    return correct_examples_list

def generate_correct_examples_lists_for_risk_domain_test_of_how_it_harms_prompt():
    correct_examples_for_natural_disasters = generate_correct_examples_list_for_risk_domain_test_of_how_it_harms_prompt(
        risk_assessment_dict_from_first_risk_domain=physical_risks_to_individuals_with_unique_hazard_description_fields,
        risk_assessment_dict_from_second_risk_domain=natural_disaster_risks_with_unique_hazard_description_fields
    )

    correct_examples_for_cybersecurity_risks = generate_correct_examples_list_for_risk_domain_test_of_how_it_harms_prompt(
        risk_assessment_dict_from_first_risk_domain=physical_risks_to_individuals_with_unique_hazard_description_fields,
        risk_assessment_dict_from_second_risk_domain=cybersecurity_risks_with_unique_hazard_description_fields,
    )

    correct_examples_for_terrorism_risks = generate_correct_examples_list_for_risk_domain_test_of_how_it_harms_prompt(
        risk_assessment_dict_from_first_risk_domain=physical_risks_to_individuals_with_unique_hazard_description_fields,
        risk_assessment_dict_from_second_risk_domain=terrorism_risks_with_unique_hazard_description_fields,
    )

    correct_examples_for_biohazard_risks = generate_correct_examples_list_for_risk_domain_test_of_how_it_harms_prompt(
        risk_assessment_dict_from_first_risk_domain=physical_risks_to_individuals_with_unique_hazard_description_fields,
        risk_assessment_dict_from_second_risk_domain=biohazard_risks_with_unique_hazard_description_fields,
    )

    return correct_examples_for_natural_disasters, correct_examples_for_terrorism_risks, correct_examples_for_cybersecurity_risks, correct_examples_for_biohazard_risks


def generate_correct_and_incorrect_examples_list_for_how_it_harms_risk_domain_test():
    correct_examples_for_natural_disasters, correct_examples_for_terrorism_risks, correct_examples_for_cybersecurity_risks, correct_examples_for_biohazard_risks = generate_correct_examples_lists_for_risk_domain_test_of_how_it_harms_prompt()

    how_it_harms_examples_generator = HowItHarmsInContextExamplesGeneratorForRiskDomainTest(correct_examples_list=correct_examples_for_natural_disasters)
    how_it_harms_examples = how_it_harms_examples_generator.get_input_and_expected_output_list()

    for correct_examples_list in [correct_examples_for_terrorism_risks, correct_examples_for_cybersecurity_risks, correct_examples_for_biohazard_risks]:
        how_it_harms_examples_generator = HowItHarmsInContextExamplesGeneratorForRiskDomainTest(correct_examples_list=correct_examples_list)

        input_and_output_list = how_it_harms_examples_generator.get_input_and_expected_output_list()

        indices_to_select = [i for i in range(len(input_and_output_list) // 2) if i % 2 != 0]
        indices_to_select += [i for i in range(len(input_and_output_list) // 2, len(input_and_output_list))]
        how_it_harms_examples.extend([input_and_output_list[i] for i in indices_to_select]) # Remove the first few correct examples from the physical_risks_to_individuals__original_student_data domain so they are not duplicated

    return how_it_harms_examples

def perform_risk_domain_test_for_how_it_harms_in_context_prompt(LLM, 
                                                                is_first_test: bool = False):
    
    how_it_harms_examples = generate_correct_and_incorrect_examples_list_for_how_it_harms_risk_domain_test()

    test_accuracy = TestModelAccuracy(
                        LLM=LLM,
                        is_first_test=is_first_test,
                        domain='All risk domains',       
                        list_of_input_and_expected_outputs=how_it_harms_examples,
                        examples_gathered_or_generated_message='Risk assessments gathered and not AI-generated',
                        sheet_name='Risk Domain Test for How It Harms')
    
    test_accuracy.run_test()

if __name__ == "__main__":
    # WHO IT HARMS
    perform_risk_domain_test_for_how_it_harms_in_context_prompt(
        LLM=Mixtral8x7B(temperature=0.1),
        is_first_test=False
    )
    # perform_risk_domain_test_for_how_it_harms_in_context_prompt(
    #     LLM=Mixtral8x22B(temperature=0.1),
    #     is_first_test=False
    # )
    # perform_risk_domain_test_for_how_it_harms_in_context_prompt(
    #     LLM=MistralLarge(temperature=0.1),
    #     is_first_test=False
    # )
    # perform_risk_domain_test_for_how_it_harms_in_context_prompt(
    #     LLM=ClaudeSonnetLLM(system_message='', temperature=0.1),
    #     is_first_test=False
    # )
    # perform_risk_domain_test_for_how_it_harms_in_context_prompt(
    #     LLM=GPT_3_point_5_turbo(temperature=0.1),
    #     is_first_test=False
    # )
