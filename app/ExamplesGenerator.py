from PromptInputs import PromptInput, HowItHarmsInContext, WhoItHarmsInContext
from InputAndExpectedOutput import InputAndExpectedOutput

class ExamplesGenerator:
    def __init__(self):
        pass
    
    def get_input_and_expected_output_list(self):
        input_and_expected_output_list = []
        
        for correct_example in self.correct_examples_list:
            input_and_expected_output = InputAndExpectedOutput(input=correct_example, expected_output=True)
            input_and_expected_output_list.append(input_and_expected_output)
        
        for incorrext_example in self.incorrect_examples_list:
            input_and_expected_output = InputAndExpectedOutput(input=incorrext_example, expected_output=False)
            input_and_expected_output_list.append(input_and_expected_output)
        
        return input_and_expected_output_list

class RiskAssessmentExamplesGenerator(ExamplesGenerator):
    def __init__(self, risk_assessments, risk_assessment_parameter_checked, method_to_get_prompt_input):
        self.risk_assessments = risk_assessments
        self.risk_assessment_parameter_checked = risk_assessment_parameter_checked
        self.method_to_get_prompt_input = method_to_get_prompt_input

        self.correct_examples_list, self.incorrect_examples_list = self.generate_correct_and_incorrect_examples_list_from_risk_assessment_examples()
    
    def generate_correct_and_incorrect_examples_list_from_risk_assessment_examples(self):
        correct_examples_list = []
        incorrect_examples_list = []

        for risk_assessment in self.risk_assessments:
            method_to_get_prompt_input = getattr(risk_assessment, self.method_to_get_prompt_input)

            if callable(method_to_get_prompt_input):
                prompt_input = method_to_get_prompt_input()
                if getattr(risk_assessment, self.risk_assessment_parameter_checked) == True:
                    correct_examples_list.append(prompt_input)
                else:
                    incorrect_examples_list.append(prompt_input)

        return correct_examples_list, incorrect_examples_list
    
class ExamplesGeneratorFromCorrectExamples(ExamplesGenerator):
    def __init__(self, correct_examples_list):
        self.correct_examples_list = correct_examples_list
        self.incorrect_examples_list = self.generate_incorrect_examples_list_from_correct_examples_list(self.correct_examples_list)

    def generate_incorrect_example(self):
        pass

    def generate_incorrect_examples_list_from_correct_examples_list(self, correct_examples_list):
        incorrect_examples_list = []

        for i in range(len(self.correct_examples_list)):
            correct_index = i
            incorrect_index = (i+1) % len(self.correct_examples_list)
            incorrect_example = self.generate_incorrect_example(correct_index, incorrect_index)
            incorrect_examples_list.append(incorrect_example)
            
        return incorrect_examples_list
    
class InputAndExpectedOutputGenerator(ExamplesGenerator):
    def __init__(self, correct_examples_list, incorrect_examples_list):
        self.correct_examples_list = correct_examples_list
        self.incorrect_examples_list = incorrect_examples_list