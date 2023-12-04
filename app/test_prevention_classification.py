from example_preventions import correct_prevention_examples_list
from example_mitigations import correct_mitigation_examples_list

from ExamplesGenerator import InputAndExpectedOutputGenerator
from TestModelAccuracy import TestModelAccuracy
from PromptInputs import PreventionClassification
from LLMCaller import OpenAILLM

class GeneratePreventionClassificationExamples:
    def generate_correct_example(self, prevention_object):
        return PreventionClassification(
            prevention=prevention_object.prevention,
            activity=prevention_object.activity,
            hazard=prevention_object.hazard,
            how_it_harms=prevention_object.how_it_harms,
            who_it_harms=prevention_object.who_it_harms
        )
    
    def generate_incorrect_example(self, mitigation_object):
        return PreventionClassification(
            prevention=mitigation_object.mitigation,
            activity=mitigation_object.activity,
            hazard=mitigation_object.hazard,
            how_it_harms=mitigation_object.how_it_harms,
            who_it_harms=mitigation_object.who_it_harms
        )
    
    def generate_correct_examples_from_prevention_list(self, correct_prevention_examples_list):
        return [self.generate_correct_example(prevention_object) for prevention_object in correct_prevention_examples_list]
    
    def generate_incorrect_examples_from_mitigation_list(self, correct_mitigation_examples_list):
        return [self.generate_incorrect_example(mitigation_object) for mitigation_object in correct_mitigation_examples_list]

if __name__ == '__main__':
    prevention_classification_examples_generator = GeneratePreventionClassificationExamples()
    
    correct_examples_list = prevention_classification_examples_generator.generate_correct_examples_from_prevention_list(correct_prevention_examples_list)
    incorrect_examples_list = prevention_classification_examples_generator.generate_incorrect_examples_from_mitigation_list(correct_mitigation_examples_list)

    examples_generator = InputAndExpectedOutputGenerator(correct_examples_list=correct_examples_list, incorrect_examples_list=incorrect_examples_list)
    examples = examples_generator.get_input_and_expected_output_list()
    test_accuracy = TestModelAccuracy(
        LLM=OpenAILLM(),
        LLM_name='gpt-3.5-turbo',
        list_of_input_and_expected_outputs=examples,
        sheet_name='Prevention Classification')
    test_accuracy.run_test()
