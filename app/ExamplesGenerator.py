from PromptInputs import PromptInput, HowItHarms, WhoItHarmsInContext
from InputAndExpectedOutput import InputAndExpectedOutput

class ExamplesGenerator:
    def __init__(self, correct_examples_list):
        self.correct_examples_list = correct_examples_list

        self.incorrect_examples_list = self.generate_incorrect_examples_list()

    def generate_incorrect_example(self, correct_index, incorrect_index):
        pass

    def generate_incorrect_examples_list(self):
        incorrect_examples_list = []

        for i in range(len(self.correct_examples_list)):
            correct_index = i
            incorrect_index = (i+1) % len(self.correct_examples_list)
            incorrect_example = self.generate_incorrect_example(correct_index, incorrect_index)
            incorrect_examples_list.append(incorrect_example)
            
        return incorrect_examples_list
    
    def get_input_and_expected_output(self, input: PromptInput, expected_output: bool):
        return InputAndExpectedOutput(input=input, expected_output=expected_output)
    
    def get_input_and_expected_output_list(self):
        input_and_expected_output_list = []
        
        for correct_example in self.correct_examples_list:
            input_and_expected_output_list.append(self.get_input_and_expected_output(input=correct_example, expected_output=True))
        
        for incorrext_example in self.incorrect_examples_list:
            input_and_expected_output_list.append(self.get_input_and_expected_output(input=incorrext_example, expected_output=False))
        
        return input_and_expected_output_list

class InputAndExpectedOutputGenerator(ExamplesGenerator):
    def __init__(self, correct_examples_list, incorrect_examples_list):
        self.correct_examples_list = correct_examples_list
        self.incorrect_examples_list = incorrect_examples_list
    
