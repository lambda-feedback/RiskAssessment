from TestModelAccuracy import TestModelAccuracy
from LLMCaller import OpenAILLM
from ExamplesGenerator import ExamplesGeneratorFromCorrectExamples
from PromptInputs import HowItHarmsInContext
from example_risk_assessments import physical_risks_to_individuals__original_student_data, natural_disaster_risks, cybersecurity_risks, terrorism_risks, biohazard_risks
from LLMCaller import LLMCaller

class HowItHarmsInContextExamplesGenerator(ExamplesGeneratorFromCorrectExamples):
    def generate_incorrect_example(self, correct_index, incorrect_index):
        return HowItHarmsInContext(
                activity=self.correct_examples_list[correct_index].activity, 
                hazard=self.correct_examples_list[correct_index].hazard, 
                how_it_harms=self.correct_examples_list[incorrect_index].how_it_harms)

risk_assessments_list = []

for i in range(10):
    # TODO: Some of the correct volcano/earthquake examples are duplicates 
    # because the activity, hazard and how it harms are all the same.
     
    # NOTE: For the incorrect examples, even numbers have "how it harms" belonging to first_risk_assessment_example
    # and "hazard" and "activity" corresponding to second_risk_assessment_example
    
    # Also for incorrect examples, odd numbers have "how it harms" belonging to second_risk_assessment_example
    # and "hazard" and "activity" corresponding to first_risk_assessment_example
    first_risk_assessment_example = physical_risks_to_individuals__original_student_data['risk_assessments'][i]
    second_risk_assessment_example = natural_disaster_risks['risk_assessments'][i]
    risk_assessments_list.append(first_risk_assessment_example)
    risk_assessments_list.append(second_risk_assessment_example)

    # risk_assessments_list.append(cybersecurity_risks[i])
    # risk_assessments_list.append(terrorism_risks[i])
    # risk_assessments_list.append(biohazard_risks[i])

correct_examples_list = []

for risk_assessment in risk_assessments_list:
    correct_examples_list.append(risk_assessment.get_how_it_harms_in_context_input())

def test_how_it_harms_in_context(correct_examples_list, LLM, is_first_test: bool = False):
    how_it_harms_examples_generator = HowItHarmsInContextExamplesGenerator(correct_examples_list=correct_examples_list)
    how_it_harms_examples = how_it_harms_examples_generator.get_input_and_expected_output_list()

    test_accuracy = TestModelAccuracy(
                        LLM=LLM,
                        is_first_test=is_first_test,
                        domain='Physical Risks and Natural Disasters',       
                        list_of_input_and_expected_outputs=how_it_harms_examples,
                        examples_gathered_or_generated_message='Risk assessments gathered and not AI-generated',
                        sheet_name='How It Harms In Context')
    
    test_accuracy.run_test()

if __name__ == "__main__":
    LLM = OpenAILLM()

    test_how_it_harms_in_context(correct_examples_list=correct_examples_list, 
                                 LLM=LLM, 
                                 is_first_test=True)