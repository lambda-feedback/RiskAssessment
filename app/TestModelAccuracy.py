import re
import csv
import pathlib
from datetime import datetime

try:
    from .LLMCaller import LLMCaller, LLMWithCandidateLabels, LLMWithGeneratedText, OpenAILLM
    from .GPTCostCalculator import GPTCostCalculator
    from .InputAndExpectedOutput import InputAndExpectedOutput
except:
    from LLMCaller import LLMCaller, LLMWithCandidateLabels, LLMWithGeneratedText, OpenAILLM
    from GPTCostCalculator import GPTCostCalculator
    from InputAndExpectedOutput import InputAndExpectedOutput

class TestModelAccuracy:
    def __init__(self, 
                LLM: LLMCaller,
                LLM_name: str,
                list_of_input_and_expected_outputs: list[InputAndExpectedOutput],
                folder_name: str):
        
        self.LLM = LLM
        self.LLM_name = LLM_name
        self.list_of_input_and_expected_outputs = list_of_input_and_expected_outputs
        self.folder_name = folder_name

    def get_prompt_input_and_output(self, input_and_expected_output):
        input = input_and_expected_output.input
        
        prompt_input = self.LLM.get_prompt_input(prompt_input=input)
        prompt_output = self.LLM.get_model_output(prompt_input=input)
        
        return prompt_input, prompt_output
    
    def check_prompt_output_against_regex_pattern(self, prompt_output):
        
        try:
            pattern = re.compile(r"(true|false)", re.IGNORECASE)
            match = re.search(pattern, prompt_output)
            if match:
                return match.group(1) == "True"
            else:
                raise Exception("Pattern not found in output prompt")
            
        except Exception as e:
            print(f'Caught an exception: {e}')

    def get_model_accuracy_and_model_outputs(self):
        count_correct = 0
        output_string = ''
        prompt_outputs_for_incorrect_responses = ''

        for input_and_expected_output in self.list_of_input_and_expected_outputs:
            prompt_input, prompt_output = self.get_prompt_input_and_output(input_and_expected_output)
            is_correct = self.check_prompt_output_against_regex_pattern(prompt_output)

            result_dict = {'input': input_and_expected_output.input.to_string(),
                            'is_correct': is_correct, 
                            'expected_output': input_and_expected_output.expected_output}
            
            output_string += f'{str(result_dict)}\n'

            if is_correct == input_and_expected_output.expected_output:
                count_correct += 1
                print(count_correct)
            else:
                prompt_outputs_for_incorrect_responses += f'{prompt_output}\n\n'
        
        accuracy = round(count_correct / len(self.list_of_input_and_expected_outputs) * 100, 2)

        return accuracy, output_string, prompt_outputs_for_incorrect_responses
    
    def get_first_prompt_input_and_output(self):
        first_input = self.list_of_input_and_expected_outputs[0].input
        first_prompt_input = self.LLM.get_prompt_input(prompt_input=first_input)
        first_prompt_output = self.LLM.get_model_output(prompt_input=first_input)

        return first_prompt_input, first_prompt_output
    
    def save_test_results(self, 
                          accuracy, 
                          output_string, 
                          prompt_outputs_for_incorrect_responses,
                          first_prompt_input,
                          first_prompt_output):

        path_to_folder = pathlib.Path(f'test_results/{self.folder_name}/{self.LLM_name}')
        file_name = f'{len(self.list_of_input_and_expected_outputs)}_{accuracy}_{datetime.now().strftime("%d-%m_%H-%M")}'

        path_to_file = path_to_folder / file_name

        with open(path_to_file, 'w') as file:
            file.write(f'Example prompt input:\n{first_prompt_input}\n\n')
            file.write(f'Example prompt output:\n{first_prompt_output}\n\n')
            file.write(f'All model outputs and expected outputs:\n{output_string}\n\n')
            if len(prompt_outputs_for_incorrect_responses) > 0:
                file.write(f'The following are the prompt outputs for incorrect responses: \n {prompt_outputs_for_incorrect_responses} \n\n')
            file.write(f'Accuracy = {accuracy} %')
    
    def run_test(self):
        accuracy, output_string, prompt_outputs_for_incorrect_responses = self.get_model_accuracy_and_model_outputs()
        first_prompt_input, first_prompt_output = self.get_first_prompt_input_and_output()
        self.save_test_results(accuracy, 
                               output_string, 
                               prompt_outputs_for_incorrect_responses,
                               first_prompt_input,
                               first_prompt_output)

class TestModelAccuracyWithGPT(TestModelAccuracy):
    def __init__(self, 
                LLM: LLMCaller,
                LLM_name: str,
                list_of_input_and_expected_outputs: list[InputAndExpectedOutput],
                folder_name: str):
        
        super().__init__(LLM, LLM_name, list_of_input_and_expected_outputs, folder_name)
        self.GPT_cost_calculator = GPTCostCalculator()
    
    def total_cost_of_calling_LLM_API(self):
        total_cost_of_calling_LLM_API = 0

        for input_and_expected_output in self.list_of_input_and_expected_outputs:
            prompt_input, prompt_output = self.get_prompt_input_and_output(input_and_expected_output)
            total_cost_of_calling_LLM_API = total_cost_of_calling_LLM_API + self.GPT_cost_calculator.calculate_cost(prompt_input=prompt_input, prompt_output=prompt_output)
        
        return total_cost_of_calling_LLM_API
    
    def save_cost_of_calling_LLM_API(self, total_cost_of_calling_LLM_API):
        path_to_folder = pathlib.Path('LLM_costs')
        file_name = 'gpt_costs.csv'
        path_to_file = path_to_folder / file_name

        with open(path_to_file, 'a', newline='\n') as csv_file:
            new_line_data = [datetime.now().strftime("%Y-%m-%d_%H-%M-%S"), total_cost_of_calling_LLM_API]
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(new_line_data)