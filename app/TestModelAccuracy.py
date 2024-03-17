import re
from datetime import datetime
import numpy as np
import pandas as pd
from tabulate import tabulate
import time

from LLMCaller import LLMCaller
from InputAndExpectedOutput import InputAndExpectedOutputForSinglePrompt, InputAndExpectedOutputForCombinedPrompts
from GoogleSheetsWriter import GoogleSheetsWriter
from RegexPatternMatcher import RegexPatternMatcher

class TestModelAccuracy:
    def __init__(self, 
                LLM: LLMCaller,
                list_of_input_and_expected_outputs: list[InputAndExpectedOutputForSinglePrompt],
                number_of_examples_in_each_domain: dict,
                sheet_name: str,
                examples_gathered_or_generated_message: str):
        
        self.LLM = LLM
        self.list_of_input_and_expected_outputs = list_of_input_and_expected_outputs
        self.number_of_examples_in_each_domain = number_of_examples_in_each_domain
        self.sheet_name = sheet_name
        self.examples_gathered_or_generated_message = examples_gathered_or_generated_message

    def get_number_of_examples(self):
        return len(self.list_of_input_and_expected_outputs)

    def get_first_prompt_input(self):
        first_prompt_input_object = self.list_of_input_and_expected_outputs[0].input
        first_prompt_input = first_prompt_input_object.generate_prompt()
        return first_prompt_input
    
    def get_classes(self):
        first_prompt_input_object = self.list_of_input_and_expected_outputs[0].input

        classes = first_prompt_input_object.candidate_labels
        return classes
    
    def update_confusion_matrix(self, confusion_matrix, classes, pattern_matched, expected_output):
        pattern_matched_index_in_class_list = classes.index(pattern_matched)
        expected_output_index_in_class_list = classes.index(expected_output)
        confusion_matrix[pattern_matched_index_in_class_list, expected_output_index_in_class_list] += 1

        return confusion_matrix
    
    def generate_confusion_matrix_string(self, confusion_matrix, classes):
        classes_as_strings = [str(e) for e in classes]
        confusion_matrix_df = pd.DataFrame(confusion_matrix, index=classes_as_strings, columns=classes_as_strings)

        confusion_matrix_df_values = confusion_matrix_df.values

        confusion_matrix_df_column_titles = confusion_matrix_df.columns
        column_titles_with_blank_space = confusion_matrix_df_column_titles.insert(0, "")

        confusion_matrix_with_column_titles = np.vstack((confusion_matrix_df_column_titles, confusion_matrix_df_values)).tolist()

        for i in range(len(confusion_matrix_with_column_titles)):
            confusion_matrix_with_column_titles[i].insert(0, column_titles_with_blank_space[i])

        confusion_matrix_string = tabulate(confusion_matrix_with_column_titles, headers='firstrow', tablefmt='grid')

        return confusion_matrix_string

    def update_output_string(self, output_string, example_index, pattern_matched, expected_output):
        result_dict = {'input': self.list_of_input_and_expected_outputs[example_index].input.to_string(),
                'pattern_matched': pattern_matched, 
                'expected_output': expected_output}

        output_string += f'{example_index + 1}: {str(result_dict)}\n\n'

        return output_string

    def get_expected_output_and_pattern_matched_and_prompt_output(self, example_index):
        expected_output = self.list_of_input_and_expected_outputs[example_index].expected_output
        input = self.list_of_input_and_expected_outputs[example_index].input

        pattern_matching_method_string = input.pattern_matching_method
        regex_pattern_matcher = RegexPatternMatcher()
        pattern_matching_method = getattr(regex_pattern_matcher, pattern_matching_method_string)
    
        prompt_output = self.LLM.get_model_output(input.generate_prompt())
        print(prompt_output)

        pattern_matched = pattern_matching_method(prompt_output)
        
        return expected_output, pattern_matched, prompt_output
    
    def update_prompt_output_strings(self, prompt_output, expected_output, pattern_matched, binary_correct_list, prompt_outputs_for_correct_responses, prompt_outputs_for_incorrect_responses, example_index, count_correct):
        if pattern_matched == expected_output:
            count_correct += 1

            binary_correct_list.append(1)

            prompt_outputs_for_correct_responses += f'{example_index + 1}: {prompt_output}\nExpected output: {expected_output}\n\n'

        else:
            binary_correct_list.append(0)
            prompt_outputs_for_incorrect_responses += f'{example_index + 1}: {prompt_output}\nExpected output: {expected_output}\n\n'

        return binary_correct_list, prompt_outputs_for_correct_responses, prompt_outputs_for_incorrect_responses, count_correct

    def convert_list_of_lists_to_string(self, list_of_lists):
        # Convert each sublist to a string with newline
        sublist_strings = ['[' + ', '.join(map(str, sublist)) + ']' for sublist in list_of_lists]

        # Join the sublist strings with a newline and add outer brackets
        return '[' + ',\n'.join(sublist_strings) + ']'

    def get_model_accuracy_and_model_outputs(self):
        purpose_of_test_input = input('Please enter the purpose of the test: ')

        print('Counting correct responses...')
        count_correct = 0
        
        output_string = ''
        prompt_outputs_for_correct_responses = ''
        prompt_outputs_for_incorrect_responses = ''

        classes = self.get_classes()
        n_classes = len(classes)

        confusion_matrix = np.zeros((n_classes, n_classes))

        n_examples = self.get_number_of_examples()

        binary_correct_list = []

        for example_index in range(n_examples):

            expected_output, pattern_matched, prompt_output = self.get_expected_output_and_pattern_matched_and_prompt_output(example_index)

            confusion_matrix = self.update_confusion_matrix(confusion_matrix, classes, pattern_matched, expected_output)

            output_string = self.update_output_string(output_string, example_index, pattern_matched, expected_output)

            prompt_outputs_for_correct_responses, 
            prompt_outputs_for_incorrect_responses, 
            binary_correct_list, prompt_outputs_for_correct_responses, prompt_outputs_for_incorrect_responses, count_correct = self.update_prompt_output_strings(
                                                                                                                            prompt_output=prompt_output, 
                                                                                                                            expected_output=expected_output, 
                                                                                                                            pattern_matched=pattern_matched, 
                                                                                                                            binary_correct_list=binary_correct_list,
                                                                                                                            prompt_outputs_for_correct_responses=prompt_outputs_for_correct_responses, 
                                                                                                                            prompt_outputs_for_incorrect_responses=prompt_outputs_for_incorrect_responses, 
                                                                                                                            example_index=example_index, 
                                                                                                                            count_correct=count_correct)
            
            print(count_correct)
            time.sleep(self.LLM.delay_between_requests)

        accuracy = round(count_correct / n_examples * 100, 2)

        confusion_matrix_string = self.generate_confusion_matrix_string(confusion_matrix, classes)
        
        return purpose_of_test_input, binary_correct_list, accuracy, confusion_matrix_string, output_string, prompt_outputs_for_correct_responses, prompt_outputs_for_incorrect_responses
    
    def get_first_prompt_input(self):
        first_input = self.list_of_input_and_expected_outputs[0].input
        first_prompt_input = first_input.generate_prompt()

        return first_prompt_input

    def get_accuracy_in_different_domains(self, binary_correct_list):
        domains = self.number_of_examples_in_each_domain.keys()
        domain_accuracy_string = ''

        starting_index_of_current_domain_in_binary_correct_list = 0
        for domain in domains:
            number_of_risk_assessments_in_domain = self.number_of_examples_in_each_domain[domain]

            ending_index_of_current_domain_in_binary_correct_list = starting_index_of_current_domain_in_binary_correct_list + number_of_risk_assessments_in_domain
            
            number_of_risk_assessments_correctly_classified_in_domain = sum(binary_correct_list[starting_index_of_current_domain_in_binary_correct_list:ending_index_of_current_domain_in_binary_correct_list])

            domain_accuracy_string += f'{domain}: {number_of_risk_assessments_correctly_classified_in_domain}/{number_of_risk_assessments_in_domain}\n\n'

            starting_index_of_current_domain_in_binary_correct_list = ending_index_of_current_domain_in_binary_correct_list

        return domain_accuracy_string
    
    def save_test_results(self, 
                          purpose_of_test_input,
                          accuracy, 
                          accuracy_in_different_domains_string,
                          confusion_matrix,
                          output_string, 
                          prompt_outputs_for_correct_responses,
                          prompt_outputs_for_incorrect_responses,
                          first_prompt_input):

        datetime_now = datetime.now().strftime("%d-%m_%H-%M")

        if self.LLM.name.split('-')[0] in ['gpt', 'claude']:
            model_parameters = f'Temp: {self.LLM.temperature}, Max tokens: {self.LLM.max_tokens}'
        else:
            model_parameters = ''
        
        num_examples = self.get_number_of_examples()

        new_line_data = [purpose_of_test_input, 
                         datetime_now, 
                         self.LLM.name, 
                        model_parameters, 
                        self.examples_gathered_or_generated_message,
                        accuracy, 
                        accuracy_in_different_domains_string,
                        num_examples,
                        confusion_matrix,
                        output_string[:45000], # Google Sheets has a 50,000 character limit
                        first_prompt_input,
                        prompt_outputs_for_correct_responses[:45000],
                        prompt_outputs_for_incorrect_responses[:45000]]
        
        sheets_writer = GoogleSheetsWriter(sheet_name=self.sheet_name)
        sheets_writer.write_to_sheets(new_line_data)

    # TODO: Refactoring: As below, remove positional arguments and only use keyword arguments
    def run_test(self):
        purpose_of_test_input, binary_correct_list, accuracy, confusion_matrix, output_string, prompt_outputs_for_correct_responses, prompt_outputs_for_incorrect_responses = self.get_model_accuracy_and_model_outputs()

        accuracy_in_different_domains_string = self.get_accuracy_in_different_domains(binary_correct_list)

        first_prompt_input = self.get_first_prompt_input()
        self.save_test_results(purpose_of_test_input=purpose_of_test_input,
                               accuracy=accuracy, 
                               accuracy_in_different_domains_string=accuracy_in_different_domains_string,
                               confusion_matrix=confusion_matrix,
                               output_string=output_string, 
                               first_prompt_input=first_prompt_input,
                               prompt_outputs_for_correct_responses=prompt_outputs_for_correct_responses,
                               prompt_outputs_for_incorrect_responses=prompt_outputs_for_incorrect_responses)

class TestModelAccuracyForCombinationOfPrompts(TestModelAccuracy):
    def __init__(self, 
                    LLM: LLMCaller,
                    list_of_risk_assessment_and_expected_outputs: list[InputAndExpectedOutputForCombinedPrompts],
                    number_of_examples_in_each_domain: dict,
                    sheet_name: str,
                    examples_gathered_or_generated_message: str,
                    candidate_labels: list):
        self.LLM = LLM
        self.list_of_risk_assessment_and_expected_outputs = list_of_risk_assessment_and_expected_outputs
        self.number_of_examples_in_each_domain = number_of_examples_in_each_domain
        self.sheet_name = sheet_name
        self.examples_gathered_or_generated_message = examples_gathered_or_generated_message
        self.candidate_labels = candidate_labels

    # Defined in children classes below
    def get_expected_output_and_pattern_matched_and_prompt_output(self, i):
        pass

    # Defined in children classes below
    def get_first_prompt_input(self):
        pass

    def get_classes(self):
        return self.candidate_labels

    def get_number_of_examples(self):
        return len(self.list_of_risk_assessment_and_expected_outputs)
    
    def update_output_string(self, output_string, i, pattern_matched, expected_output):
        result_dict = {'risk_assessment': self.list_of_risk_assessment_and_expected_outputs[i].risk_assessment.to_string(),
                'pattern_matched': pattern_matched, 
                'expected_output': expected_output}

        output_string += f'{i + 1}: {str(result_dict)}\n\n'

        return output_string

class TestHarmCausedAndHazardEventPrompt(TestModelAccuracyForCombinationOfPrompts):
    def __init__(self, 
                    LLM: LLMCaller,
                    list_of_risk_assessment_and_expected_outputs: list[InputAndExpectedOutputForCombinedPrompts],
                    number_of_examples_in_each_domain: dict,
                    sheet_name: str,
                    examples_gathered_or_generated_message: str,
                    candidate_labels: list):
        
        super().__init__(LLM, list_of_risk_assessment_and_expected_outputs, number_of_examples_in_each_domain, sheet_name, examples_gathered_or_generated_message, candidate_labels)

    def get_first_prompt_input(self):
        first_RA = self.list_of_risk_assessment_and_expected_outputs[0].risk_assessment

        first_harm_caused_prompt_input = first_RA.get_harm_caused_and_hazard_event_input()

        return first_harm_caused_prompt_input.generate_prompt()
    
    def get_expected_output_and_pattern_matched_and_prompt_output(self, i):
        RA = self.list_of_risk_assessment_and_expected_outputs[i].risk_assessment
        expected_output = self.list_of_risk_assessment_and_expected_outputs[i].expected_output

        harm_caused_prompt_input = RA.get_harm_caused_and_hazard_event_input()
        harm_caused_prompt_output, harm_caused_pattern = RA.get_prompt_output_and_pattern_matched(harm_caused_prompt_input, self.LLM)

        return expected_output, True, harm_caused_prompt_output

class TestControlMeasurePrompt(TestModelAccuracyForCombinationOfPrompts):
    def __init__(self, 
                    LLM: LLMCaller,
                    list_of_risk_assessment_and_expected_outputs: list[InputAndExpectedOutputForCombinedPrompts],
                    number_of_examples_in_each_domain: dict,
                    sheet_name: str,
                    examples_gathered_or_generated_message: str,
                    candidate_labels: list):
        
        super().__init__(LLM, list_of_risk_assessment_and_expected_outputs, number_of_examples_in_each_domain, sheet_name, examples_gathered_or_generated_message, candidate_labels)
    
    def get_classes(self):
        return ['prevention', 'mitigation', 'neither', 'both']
    
    def get_hazard_event_and_harm_caused_and_prompt(self, RA):
        hazard_event_and_harm_caused_prompt_input = RA.get_harm_caused_and_hazard_event_input()
        hazard_event_and_harm_caused_prompt = hazard_event_and_harm_caused_prompt_input.generate_prompt()
        hazard_event_and_harm_caused_prompt_output, hazard_event_and_harm_caused_pattern = RA.get_prompt_output_and_pattern_matched(hazard_event_and_harm_caused_prompt_input, self.LLM)

        hazard_event = hazard_event_and_harm_caused_pattern.hazard_event
        harm_caused = hazard_event_and_harm_caused_pattern.harm_caused

        return hazard_event, harm_caused, hazard_event_and_harm_caused_prompt, hazard_event_and_harm_caused_prompt_output
    
    def get_first_prompt_input_with_risk_assessment_method(self, risk_assessment_method_name):
        first_RA = self.list_of_risk_assessment_and_expected_outputs[0].risk_assessment

        hazard_event, harm_caused, hazard_event_and_harm_caused_prompt, _  = self.get_hazard_event_and_harm_caused_and_prompt(first_RA)

        control_measure_prompt_input = getattr(first_RA, risk_assessment_method_name)()
        control_measure_prompt = control_measure_prompt_input.generate_prompt(hazard_event=hazard_event, harm_caused=harm_caused)

        return f'''Hazard Event/Harm Caused:\n{hazard_event_and_harm_caused_prompt}\n\Control Measure:\n{control_measure_prompt}'''
    
    def get_expected_output_and_pattern_matched_and_prompt_output_with_risk_assessment_method(self, i, risk_assessment_method_name):
        RA = self.list_of_risk_assessment_and_expected_outputs[i].risk_assessment

        expected_output = self.list_of_risk_assessment_and_expected_outputs[i].expected_output

        hazard_event, harm_caused, _, hazard_event_and_harm_caused_prompt_output  = self.get_hazard_event_and_harm_caused_and_prompt(RA)

        control_measure_prompt_input = getattr(RA, risk_assessment_method_name)()
        control_measure_prompt_output, control_measure_prompt_with_prevention_pattern = RA.get_prompt_output_and_pattern_matched(control_measure_prompt_input, self.LLM, harm_caused=harm_caused, hazard_event=hazard_event)

        prompt_output = f'''Hazard Event/Harm Caused:\n{hazard_event_and_harm_caused_prompt_output}\n\nControl Measure:\n{control_measure_prompt_output}'''

        return expected_output, control_measure_prompt_with_prevention_pattern, prompt_output

class TestPreventionPromptInput(TestControlMeasurePrompt):
    def __init__(self, 
                    LLM: LLMCaller,
                    list_of_risk_assessment_and_expected_outputs: list[InputAndExpectedOutputForCombinedPrompts],
                    number_of_examples_in_each_domain: dict,
                    sheet_name: str,
                    examples_gathered_or_generated_message: str,
                    candidate_labels: list):
        
        super().__init__(LLM, list_of_risk_assessment_and_expected_outputs, number_of_examples_in_each_domain, sheet_name, examples_gathered_or_generated_message, candidate_labels)
    
    def get_first_prompt_input(self):
        return self.get_first_prompt_input_with_risk_assessment_method('get_prevention_prompt_input')
    
    def get_expected_output_and_pattern_matched_and_prompt_output(self, i):
        return self.get_expected_output_and_pattern_matched_and_prompt_output_with_risk_assessment_method(i, 'get_prevention_prompt_input')
    
class TestMitigationPromptInput(TestControlMeasurePrompt):
    def __init__(self, 
                    LLM: LLMCaller,
                    list_of_risk_assessment_and_expected_outputs: list[InputAndExpectedOutputForCombinedPrompts],
                    number_of_examples_in_each_domain: dict,
                    sheet_name: str,
                    examples_gathered_or_generated_message: str,
                    candidate_labels: list):
        
        super().__init__(LLM, list_of_risk_assessment_and_expected_outputs, number_of_examples_in_each_domain, sheet_name, examples_gathered_or_generated_message, candidate_labels)
    
    def get_first_prompt_input(self):
        return self.get_first_prompt_input_with_risk_assessment_method('get_mitigation_prompt_input')
    
    def get_expected_output_and_pattern_matched_and_prompt_output(self, i):
        return self.get_expected_output_and_pattern_matched_and_prompt_output_with_risk_assessment_method(i, 'get_mitigation_prompt_input')