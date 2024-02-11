from PromptInputs import PromptInput, HowItHarmsInContext, WhoItHarmsInContext
from InputAndExpectedOutput import InputAndExpectedOutputForSinglePrompt, InputAndExpectedOutputForCombinedPrompts

class ExamplesGenerator:
    def __init__(self):
        pass
    
    def get_input_and_expected_output_list(self):
        input_and_expected_output_list = []
        
        for correct_example in self.correct_examples_list:
            input_and_expected_output = InputAndExpectedOutputForSinglePrompt(input=correct_example, expected_output=True)
            input_and_expected_output_list.append(input_and_expected_output)
        
        for incorrext_example in self.incorrect_examples_list:
            input_and_expected_output = InputAndExpectedOutputForSinglePrompt(input=incorrext_example, expected_output=False)
            input_and_expected_output_list.append(input_and_expected_output)
        
        return input_and_expected_output_list

class RiskAssessmentExamplesGeneratorForSinglePrompt:
    def __init__(self, risk_assessments, ground_truth_parameter, method_to_get_prompt_input):
        self.risk_assessments = risk_assessments
        self.ground_truth_parameter = ground_truth_parameter
        self.method_to_get_prompt_input = method_to_get_prompt_input

    def get_input_and_expected_output_list(self):
        input_and_expected_output_list = []
        
        for risk_assessment in self.risk_assessments:
            prompt_input = getattr(risk_assessment, self.method_to_get_prompt_input)()
            expected_output = getattr(risk_assessment, self.ground_truth_parameter)

            if expected_output == '':
                continue
            else:
                input_and_expected_output_list.append(InputAndExpectedOutputForSinglePrompt(input=prompt_input, expected_output=expected_output))

        return input_and_expected_output_list
    
class RiskAssessmentExamplesGeneratorForMultiplePrompts:
    def __init__(self, risk_assessments, ground_truth_parameter, method_to_get_prompt_input):
        self.risk_assessments = risk_assessments
        self.ground_truth_parameter = ground_truth_parameter
        self.method_to_get_prompt_input = method_to_get_prompt_input
    
    def get_risk_assessment_and_expected_output_list(self):
        risk_assessment_and_expected_output_list = []
        
        for risk_assessment in self.risk_assessments:
            final_prompt_input = getattr(risk_assessment, self.method_to_get_prompt_input)()
            expected_output = getattr(risk_assessment, self.ground_truth_parameter)
            if expected_output == '':
                continue
            else:
                risk_assessment_and_expected_output_list.append(
                    InputAndExpectedOutputForCombinedPrompts(risk_assessment=risk_assessment, 
                                                             final_prompt_input=final_prompt_input, 
                                                             expected_output=expected_output))
        
        return risk_assessment_and_expected_output_list

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
    
class InputAndExpectedOutputForSinglePromptGenerator(ExamplesGenerator):
    def __init__(self, correct_examples_list, incorrect_examples_list):
        self.correct_examples_list = correct_examples_list
        self.incorrect_examples_list = incorrect_examples_list