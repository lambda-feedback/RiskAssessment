try:    
    from .TestModelAccuracy import TestModelAccuracy
    from .ExamplesGenerator import ExamplesGeneratorFromCorrectExamples
    from .PromptInputs import HowItHarmsInContext, WhoItHarmsInContext
    from .example_risk_assessments import *
    from .LLMCaller import *
except:
    from TestModelAccuracy import TestModelAccuracy
    from ExamplesGenerator import ExamplesGeneratorFromCorrectExamples
    from PromptInputs import HowItHarmsInContext, WhoItHarmsInContext
    from example_risk_assessments import *
    from LLMCaller import *

class WhoItHarmsInContextExamplesGeneratorForInputFieldTest(ExamplesGeneratorFromCorrectExamples):
    def generate_incorrect_example(self, correct_index, incorrect_index):
        return WhoItHarmsInContext(
            activity=self.correct_examples_list[correct_index].activity, 
            hazard=self.correct_examples_list[correct_index].hazard, 
            how_it_harms=self.correct_examples_list[correct_index].how_it_harms,
            who_it_harms=self.correct_examples_list[correct_index].how_it_harms)
    
def generate_correct_and_incorrect_examples_lists_for_input_field_test_of_how_it_harms_prompt():
    correct_examples = []

    for risk_assessment_dict in [
        physical_risks_to_individuals__original_student_data, 
                                # physical_risks_to_individuals__data_gathered_from_version_1_deployment,
                                # natural_disaster_risks,
                                # cybersecurity_risks,
                                # terrorism_risks,
                                # biohazard_risks
                                ]:
        
        correct_examples.extend([risk_assessment.get_how_it_harms_in_context_input() for risk_assessment in risk_assessment_dict['risk_assessments']])

    how_it_harms_examples_generator = WhoItHarmsInContextExamplesGeneratorForInputFieldTest(correct_examples_list=correct_examples)
    correct_and_incorrect_examples = how_it_harms_examples_generator.get_input_and_expected_output_list()

    return correct_and_incorrect_examples

def perform_risk_domain_test_for_how_it_harms_in_context_prompt(LLM, 
                                                                is_first_test: bool = False):
    
    how_it_harms_examples = generate_correct_and_incorrect_examples_lists_for_input_field_test_of_how_it_harms_prompt()

    test_accuracy = TestModelAccuracy(
                        LLM=LLM,
                        is_first_test=is_first_test,
                        domain='All risk domains',       
                        list_of_input_and_expected_outputs=how_it_harms_examples,
                        examples_gathered_or_generated_message='Risk assessments gathered and not AI-generated',
                        sheet_name='Input Field Test for Who It Harms') # Should create a new sheet for this test
    
    test_accuracy.run_test()

if __name__ == "__main__":
    # WHO IT HARMS
    # perform_input_field_test_for_how_it_harms_in_context_prompt(
    #     LLM=Mixtral8x7B(temperature=0.1),
    #     is_first_test=True
    # )
    # perform_input_field_test_for_how_it_harms_in_context_prompt(
    #     LLM=Mixtral8x22B(temperature=0.1),
    #     is_first_test=True
    # )
    # perform_input_field_test_for_how_it_harms_in_context_prompt(
    #     LLM=MistralLarge(temperature=0.1),
    #     is_first_test=True
    # )
    perform_risk_domain_test_for_how_it_harms_in_context_prompt(
        LLM=ClaudeSonnetLLM(system_message='', temperature=0.1),
        is_first_test=True
    )
    # perform_input_field_test_for_how_it_harms_in_context_prompt(
    #     LLM=GPT_3_point_5_turbo(temperature=0.1),
    #     is_first_test=True
    # )