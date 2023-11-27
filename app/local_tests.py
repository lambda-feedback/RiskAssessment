# pytest -v -s local_tests.py

# The -s option above is so you can see printouts even if the test fails

import unittest
import re
import pathlib
from datetime import datetime
import csv

try:
    from .example_activities import activities
    from .LLMCaller import LLMCaller, LLMWithCandidateLabels, LLMWithGeneratedText, OpenAILLM
    from .PromptInputs import Activity
    from .GPTCostCalculator import GPTCostCalculator
except ImportError:
    from example_activities import activities
    from LLMCaller import LLMCaller, LLMWithCandidateLabels, LLMWithGeneratedText, OpenAILLM
    from PromptInputs import Activity
    from GPTCostCalculator import GPTCostCalculator

def test_get_model_accuracy_activities(LLM_name: str):
        if LLM_name == 'gpt':
            LLM = OpenAILLM()
        if LLM_name == 'llama':
            LLM = LLMWithGeneratedText(LLM_API_ENDPOINT="https://api-inference.huggingface.co/models/meta-llama/Llama-2-70b-chat-hf")

        count_correct = 0

        if LLM_name == 'gpt':
            total_cost_of_calling_LLM_API = 0
            GPT_cost_calculator = GPTCostCalculator()

        output_string = ''
        prompt_outputs_for_incorrect_responses = ''

        for activity in activities:
            activity_input = Activity(activity=activity.input)
            prompt_input = LLM.get_prompt_input(prompt_input=activity_input)
            prompt_output = LLM.get_model_output(prompt_input=activity_input)

            pattern = r'dict\(\'input\': "({})", is_an_activity: (True|False)\)'.format(re.escape(activity.input))
            match = re.search(pattern, prompt_output)

            if match:
                input_description = match.group(1)
                is_an_activity = match.group(2) == "True"
                result_dict = {'input': input_description,
                               'is_an_activity': is_an_activity, 
                               'expected_output': activity.expected_output}
                
                output_string += f'{str(result_dict)}\n'

                if is_an_activity == activity.expected_output:
                    count_correct += 1
                else:
                    prompt_outputs_for_incorrect_responses += f'{prompt_output}\n\n'

                if LLM_name == 'gpt':
                    total_cost_of_calling_LLM_API = total_cost_of_calling_LLM_API + GPT_cost_calculator.calculate_cost(prompt_input=prompt_input, prompt_output=prompt_output)
                
            else:
                print('Pattern not found in output prompt')
                prompt_outputs_for_incorrect_responses += f'{prompt_output}\n\n'

            print(count_correct)
        
        if LLM_name == 'gpt':
            path_to_folder = pathlib.Path('test_results/activities/GPT')
        
        if LLM_name == 'llama':
            path_to_folder = pathlib.Path('test_results/activities/LLAMA')

        accuracy = count_correct / len(activities) * 100
        file_name = f'{len(activities)}_{accuracy}_{datetime.now().strftime("%d-%m_%H-%M")}'

        path_to_file = path_to_folder / file_name

        first_activity_input = Activity(activity=activities[0].input)
        first_prompt_input = LLM.get_prompt_input(prompt_input=first_activity_input)
        first_prompt_output = LLM.get_model_output(prompt_input=first_activity_input)

        with open(path_to_file, 'w') as file:
            file.write(f'Example prompt input:\n{first_prompt_input}\n\n')
            file.write(f'Example prompt output:\n{first_prompt_output}\n\n')
            file.write(f'All model outputs and expected outputs:\n{output_string}\n\n')
            if len(prompt_outputs_for_incorrect_responses) > 0:
                file.write(f'The following are the prompt outputs for incorrect responses: \n {prompt_outputs_for_incorrect_responses}')
            file.write(f'Accuracy = {accuracy} %')
        
        if LLM_name == 'gpt':
            path_to_folder = pathlib.Path('LLM_costs')
            file_name = 'gpt_costs.csv'
            path_to_file = path_to_folder / file_name

            with open(path_to_file, 'a', newline='\n') as csv_file:
                new_line_data = [datetime.now().strftime("%Y-%m-%d_%H-%M-%S"), total_cost_of_calling_LLM_API]
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(new_line_data)

class TestEvaluationFunction(unittest.TestCase):
    """
    TestCase Class used to test the algorithm.
    ---
    Tests are used here to check that the algorithm written
    is working as it should.

    It's best practise to write these tests first to get a
    kind of 'specification' for how your algorithm should
    work, and you should run these tests before committing
    your code to AWS.

    Read the docs on how to use unittest here:
    https://docs.python.org/3/library/unittest.html

    Use evaluation_function() to check your algorithm works
    as it should.
    """

    # def test_get_model_accuracy_activities_LLAMA(self):
    #     test_get_model_accuracy_activities(LLM_name='llama')

    def test_get_model_accuracy_activities_GPT(self):
        test_get_model_accuracy_activities(LLM_name='gpt')

if __name__ == "__main__":
    unittest.main()
