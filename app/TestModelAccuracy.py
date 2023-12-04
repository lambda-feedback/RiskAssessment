import re
import csv
import pathlib
from datetime import datetime

try:
    from .LLMCaller import LLMCaller, LLMWithCandidateLabels, LLMWithGeneratedText, OpenAILLM
    from .GPTCostCalculator import GPTCostCalculator
    from .InputAndExpectedOutput import InputAndExpectedOutput
    from .GoogleSheetsWriter import GoogleSheetsWriter
except:
    from LLMCaller import LLMCaller, LLMWithCandidateLabels, LLMWithGeneratedText, OpenAILLM
    from GPTCostCalculator import GPTCostCalculator
    from InputAndExpectedOutput import InputAndExpectedOutput
    from GoogleSheetsWriter import GoogleSheetsWriter

class TestModelAccuracy:
    def __init__(self, 
                LLM: LLMCaller,
                LLM_name: str,
                list_of_input_and_expected_outputs: list[InputAndExpectedOutput],
                sheet_name: str):
        
        self.LLM = LLM
        self.LLM_name = LLM_name
        self.list_of_input_and_expected_outputs = list_of_input_and_expected_outputs
        self.sheet_name = sheet_name

    def get_prompt_input_and_output(self, input_and_expected_output):
        input = input_and_expected_output.input

        prompt_input = self.LLM.get_prompt_input(prompt_input=input)
        prompt_output = self.LLM.get_model_output(prompt_input=input)
        
        return prompt_input, prompt_output
    
    def get_regex_pattern(self, input_and_expected_output):
        return re.compile(r"(true|false)", re.IGNORECASE)
    
    def check_prompt_output_against_regex_pattern(self, pattern, prompt_output):
        
        try:
            match = re.search(pattern, prompt_output)
            if match:
                return match.group(1).lower() == "true"
            else:
                raise Exception("Pattern not found in output prompt")
            
        except Exception as e:
            print(f'Caught an exception: {e}')

    def get_model_accuracy_and_model_outputs(self):
        print('Counting correct responses...')
        count_correct = 0
        output_string = ''
        prompt_outputs_for_correct_responses = ''
        prompt_outputs_for_incorrect_responses = ''

        for i in range(len(self.list_of_input_and_expected_outputs)):
            prompt_input, prompt_output = self.get_prompt_input_and_output(self.list_of_input_and_expected_outputs[i])
            pattern = self.get_regex_pattern(self.list_of_input_and_expected_outputs[i])

            is_correct = self.check_prompt_output_against_regex_pattern(pattern, prompt_output)

            result_dict = {'input': self.list_of_input_and_expected_outputs[i].input.to_string(),
                            'is_correct': is_correct, 
                            'expected_output': self.list_of_input_and_expected_outputs[i].expected_output}
            
            output_string += f'{i + 1}: {str(result_dict)}\n\n'

            if is_correct == self.list_of_input_and_expected_outputs[i].expected_output:
                count_correct += 1
                prompt_outputs_for_correct_responses += f'{i + 1}: {prompt_output}\n\n'
                print(count_correct)
            else:
                prompt_outputs_for_incorrect_responses += f'{i + 1}: {prompt_output}\n\n'
        
        accuracy = round(count_correct / len(self.list_of_input_and_expected_outputs) * 100, 2)

        return accuracy, output_string, prompt_outputs_for_correct_responses, prompt_outputs_for_incorrect_responses
    
    def get_first_prompt_input_and_output(self):
        first_input = self.list_of_input_and_expected_outputs[0].input
        first_prompt_input = self.LLM.get_prompt_input(prompt_input=first_input)
        first_prompt_output = self.LLM.get_model_output(prompt_input=first_input)

        return first_prompt_input, first_prompt_output
    
    def total_cost_of_calling_LLM_API(self):
        GPT_cost_calculator = GPTCostCalculator()
        
        if self.LLM_name == 'gpt-3.5-turbo':
            total_cost_of_calling_LLM_API = 0

            for input_and_expected_output in self.list_of_input_and_expected_outputs:
                prompt_input, prompt_output = self.get_prompt_input_and_output(input_and_expected_output)
                total_cost_of_calling_LLM_API = total_cost_of_calling_LLM_API + GPT_cost_calculator.calculate_cost(prompt_input=prompt_input, prompt_output=prompt_output)
            
            return total_cost_of_calling_LLM_API
        else:
            return 0
    
    def save_test_results(self, 
                          accuracy, 
                          output_string, 
                          prompt_outputs_for_correct_responses,
                          prompt_outputs_for_incorrect_responses,
                          first_prompt_input,
                          first_prompt_output):

        datetime_now = datetime.now().strftime("%d-%m_%H-%M")

        if self.LLM_name == 'gpt-3.5-turbo':
            model_parameters = f'Temp: {self.LLM.temperature}, Max tokens: {self.LLM.max_tokens}'
        else:
            model_parameters = ''
        
        num_examples = len(self.list_of_input_and_expected_outputs)

        total_cost_of_calling_LLM_API = self.total_cost_of_calling_LLM_API()

        new_line_data = ['', 
                         self.LLM_name, 
                            datetime_now, 
                            total_cost_of_calling_LLM_API,
                            model_parameters, 
                            accuracy, 
                            num_examples,
                            output_string,
                            first_prompt_input,
                            first_prompt_output,
                            prompt_outputs_for_correct_responses,
                            prompt_outputs_for_incorrect_responses]
        
        sheets_writer = GoogleSheetsWriter(sheet_name=self.sheet_name)
        sheets_writer.write_to_sheets(new_line_data)
        
    # TODO: As below, remove positional arguments and only use keyword arguments
    def run_test(self):
        accuracy, output_string, prompt_outputs_for_correct_responses, prompt_outputs_for_incorrect_responses = self.get_model_accuracy_and_model_outputs()
        first_prompt_input, first_prompt_output = self.get_first_prompt_input_and_output()
        self.save_test_results(accuracy=accuracy, 
                               output_string=output_string, 
                               first_prompt_input=first_prompt_input,
                               first_prompt_output=first_prompt_output,
                               prompt_outputs_for_correct_responses=prompt_outputs_for_correct_responses,
                               prompt_outputs_for_incorrect_responses=prompt_outputs_for_incorrect_responses,)

class TestModelAccuracyForActivitiesWithLLAMA(TestModelAccuracy):
    def get_regex_pattern(self, input_and_expected_output):
        input = input_and_expected_output.input
        activity = input.activity
        return re.compile(r"Output: dict(input\s*=\s*\"{}\", is_activity\s*=\s*(true|false))".format(re.escape(activity)), re.IGNORECASE)