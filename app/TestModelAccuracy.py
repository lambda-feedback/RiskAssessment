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

class TestModelcorrectness_Accuracy:
    def __init__(self, 
                LLM: LLMCaller,
                list_of_input_and_expected_outputs: list[InputAndExpectedOutputForSinglePrompt],
                sheet_name: str,
                examples_gathered_or_generated_message: str,
                domain: str = None,
                is_first_test: bool = False):
        
        self.LLM = LLM
        self.list_of_input_and_expected_outputs = list_of_input_and_expected_outputs
        self.sheet_name = sheet_name
        self.examples_gathered_or_generated_message = examples_gathered_or_generated_message
        self.domain = domain
        self.is_first_test = is_first_test

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

        if pattern_matched == 'No pattern found':
            return confusion_matrix # Don't change confusion matrix if no pattern found
        
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
    
    def update_prompt_output_strings(self, prompt_output, expected_output, pattern_matched, prompt_outputs_for_correct_responses, prompt_outputs_for_incorrect_responses, prompt_outputs_where_pattern_was_not_matched, example_index, count_correct, number_of_examples_where_pattern_in_prompt_output):
        if pattern_matched == 'No pattern found':
            prompt_outputs_where_pattern_was_not_matched += f'{example_index + 1}: {prompt_output}\nExpected output: {expected_output}\n\n'
        
        else:
            number_of_examples_where_pattern_in_prompt_output += 1

            if pattern_matched == expected_output:
                count_correct += 1

                prompt_outputs_for_correct_responses += f'{example_index + 1}: {prompt_output}\nExpected output: {expected_output}\n\n'
            
            else:
                prompt_outputs_for_incorrect_responses += f'{example_index + 1}: {prompt_output}\nExpected output: {expected_output}\n\n'

        return prompt_outputs_for_correct_responses, prompt_outputs_for_incorrect_responses, prompt_outputs_where_pattern_was_not_matched, count_correct, number_of_examples_where_pattern_in_prompt_output

    def convert_list_of_lists_to_string(self, list_of_lists):
        # Convert each sublist to a string with newline
        sublist_strings = ['[' + ', '.join(map(str, sublist)) + ']' for sublist in list_of_lists]

        # Join the sublist strings with a newline and add outer brackets
        return '[' + ',\n'.join(sublist_strings) + ']'

    def get_model_correctness_accuracy_and_model_outputs(self):
        if self.is_first_test == True:
            purpose_of_test = input('Please enter the purpose of the test: ')
        else:
            purpose_of_test = ''

        print('Counting correct responses...')
        count_correct = 0
        number_of_examples_where_pattern_in_prompt_output = 0
        
        output_string = ''
        prompt_outputs_for_correct_responses = ''
        prompt_outputs_for_incorrect_responses = ''
        prompt_outputs_where_pattern_was_not_matched = ''

        classes = self.get_classes()
        n_classes = len(classes)

        confusion_matrix = np.zeros((n_classes, n_classes))

        n_examples = self.get_number_of_examples()

        for example_index in range(n_examples):

            expected_output, pattern_matched, prompt_output = self.get_expected_output_and_pattern_matched_and_prompt_output(example_index)

            confusion_matrix = self.update_confusion_matrix(confusion_matrix, classes, pattern_matched, expected_output)

            output_string = self.update_output_string(output_string, example_index, pattern_matched, expected_output)

            prompt_outputs_for_correct_responses, prompt_outputs_for_incorrect_responses, prompt_outputs_where_pattern_was_not_matched, count_correct, number_of_examples_where_pattern_in_prompt_output = self.update_prompt_output_strings(
                                                                                                                            prompt_output=prompt_output, 
                                                                                                                            expected_output=expected_output, 
                                                                                                                            pattern_matched=pattern_matched, 
                                                                                                                            prompt_outputs_for_correct_responses=prompt_outputs_for_correct_responses, 
                                                                                                                            prompt_outputs_for_incorrect_responses=prompt_outputs_for_incorrect_responses, 
                                                                                                                            prompt_outputs_where_pattern_was_not_matched=prompt_outputs_where_pattern_was_not_matched,
                                                                                                                            example_index=example_index, 
                                                                                                                            count_correct=count_correct,
                                                                                                                            number_of_examples_where_pattern_in_prompt_output=number_of_examples_where_pattern_in_prompt_output)
            
            print(count_correct)
            time.sleep(self.LLM.delay_between_requests)

        correctness_accuracy = round(count_correct / n_examples * 100, 2)
        faithfulness_accuracy = round(number_of_examples_where_pattern_in_prompt_output / n_examples * 100, 2)

        confusion_matrix_string = self.generate_confusion_matrix_string(confusion_matrix, classes)
        
        return purpose_of_test, correctness_accuracy, faithfulness_accuracy, confusion_matrix_string, output_string, prompt_outputs_for_correct_responses, prompt_outputs_for_incorrect_responses, prompt_outputs_where_pattern_was_not_matched
    
    def get_first_prompt_input(self):
        first_input = self.list_of_input_and_expected_outputs[0].input
        first_prompt_input = first_input.generate_prompt()

        return first_prompt_input
    
    def save_test_results(self, 
                          purpose_of_test,
                          correctness_accuracy,
                          faithfulness_accuracy,
                          confusion_matrix,
                          output_string, 
                          prompt_outputs_for_correct_responses,
                          prompt_outputs_for_incorrect_responses,
                          prompt_outputs_where_pattern_was_not_matched,
                          first_prompt_input):

        datetime_now = datetime.now().strftime("%d-%m_%H-%M")

        model_parameters = f'Temp: {self.LLM.temperature}, Max tokens: {self.LLM.max_tokens}'
        
        num_examples = self.get_number_of_examples()

        new_line_data = [purpose_of_test, 
                        self.domain,
                         datetime_now, 
                         self.LLM.name, 
                        model_parameters, 
                        self.examples_gathered_or_generated_message,
                        correctness_accuracy, 
                        faithfulness_accuracy,
                        num_examples,
                        confusion_matrix,
                        output_string[:45000], # Google Sheets has a 50,000 character limit
                        first_prompt_input,
                        prompt_outputs_for_correct_responses[:45000],
                        prompt_outputs_for_incorrect_responses[:45000],
                        prompt_outputs_where_pattern_was_not_matched[:45000]]
        
        sheets_writer = GoogleSheetsWriter(sheet_name=self.sheet_name)
        sheets_writer.write_to_sheets(new_line_data)

    # TODO: Refactoring: As below, remove positional arguments and only use keyword arguments
    def run_test(self):
        purpose_of_test, correctness_accuracy, faithfulness_accuracy, confusion_matrix, output_string, prompt_outputs_for_correct_responses, prompt_outputs_for_incorrect_responses, prompt_outputs_where_pattern_was_not_matched = self.get_model_correctness_accuracy_and_model_outputs()

        first_prompt_input = self.get_first_prompt_input()
        self.save_test_results(purpose_of_test=purpose_of_test,
                               correctness_accuracy=correctness_accuracy,
                               faithfulness_accuracy=faithfulness_accuracy,
                               confusion_matrix=confusion_matrix,
                               output_string=output_string, 
                               first_prompt_input=first_prompt_input,
                               prompt_outputs_for_correct_responses=prompt_outputs_for_correct_responses,
                               prompt_outputs_for_incorrect_responses=prompt_outputs_for_incorrect_responses,
                               prompt_outputs_where_pattern_was_not_matched=prompt_outputs_where_pattern_was_not_matched)

class TestModelcorrectness_AccuracyForCombinationOfPrompts(TestModelcorrectness_Accuracy):
    def __init__(self, 
                    LLM: LLMCaller,
                    list_of_risk_assessment_and_expected_outputs: list[InputAndExpectedOutputForCombinedPrompts],
                    sheet_name: str,
                    examples_gathered_or_generated_message: str,
                    candidate_labels: list,
                    domain: str = None,
                    is_first_test: bool = False):
        
        self.LLM = LLM
        self.list_of_risk_assessment_and_expected_outputs = list_of_risk_assessment_and_expected_outputs
        self.sheet_name = sheet_name
        self.examples_gathered_or_generated_message = examples_gathered_or_generated_message
        self.candidate_labels = candidate_labels
        self.domain = domain
        self.is_first_test = is_first_test

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

class TestHarmCausedAndHazardEventPrompt(TestModelcorrectness_AccuracyForCombinationOfPrompts):
    def __init__(self, 
                    LLM: LLMCaller,
                    list_of_risk_assessment_and_expected_outputs: list[InputAndExpectedOutputForCombinedPrompts],
                    sheet_name: str,
                    examples_gathered_or_generated_message: str,
                    candidate_labels: list,
                    domain: str = None,
                    is_first_test: bool = False):
        
        super().__init__(LLM, list_of_risk_assessment_and_expected_outputs, sheet_name, examples_gathered_or_generated_message, candidate_labels, domain=domain, is_first_test=is_first_test)

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

class TestControlMeasureClassificationPrompt(TestModelcorrectness_AccuracyForCombinationOfPrompts):
    def __init__(self, 
                    LLM: LLMCaller,
                    list_of_risk_assessment_and_expected_outputs: list[InputAndExpectedOutputForCombinedPrompts],
                    sheet_name: str,
                    examples_gathered_or_generated_message: str,
                    candidate_labels: list,
                    domain: str = None,
                    is_first_test: bool = False):
        
        super().__init__(LLM, list_of_risk_assessment_and_expected_outputs, sheet_name, examples_gathered_or_generated_message, candidate_labels, domain=domain, is_first_test=is_first_test)
    
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

        if hazard_event == 'No pattern found' or harm_caused == 'No pattern found':
            return f'''Hazard Event/Harm Caused:\n{hazard_event_and_harm_caused_prompt}\n\n No pattern found for hazard event or harm caused in prompt output.'''
        
        else:
            control_measure_prompt_input = getattr(first_RA, risk_assessment_method_name)()
            control_measure_prompt = control_measure_prompt_input.generate_prompt(hazard_event=hazard_event, harm_caused=harm_caused)

            return f'''Hazard Event/Harm Caused:\n{hazard_event_and_harm_caused_prompt}\n\Control Measure:\n{control_measure_prompt}'''
    
    def get_expected_output_and_pattern_matched_and_prompt_output_with_risk_assessment_method(self, i, risk_assessment_method_name):
        RA = self.list_of_risk_assessment_and_expected_outputs[i].risk_assessment

        expected_output = self.list_of_risk_assessment_and_expected_outputs[i].expected_output

        hazard_event, harm_caused, _, hazard_event_and_harm_caused_prompt_output  = self.get_hazard_event_and_harm_caused_and_prompt(RA)

        if hazard_event == 'No pattern found' or harm_caused == 'No pattern found':
            return expected_output, 'No pattern found', hazard_event_and_harm_caused_prompt_output

        control_measure_prompt_input = getattr(RA, risk_assessment_method_name)()
        control_measure_prompt_output, control_measure_pattern = RA.get_prompt_output_and_pattern_matched(control_measure_prompt_input, self.LLM, harm_caused=harm_caused, hazard_event=hazard_event)

        if control_measure_pattern == 'No pattern found':
            return expected_output, 'No pattern found', hazard_event_and_harm_caused_prompt_output

        prompt_output = f'''Hazard Event/Harm Caused:\n{hazard_event_and_harm_caused_prompt_output}\n\nControl Measure:\n{control_measure_prompt_output}'''

        return expected_output, control_measure_pattern, prompt_output

class TestPreventionPromptInput(TestControlMeasureClassificationPrompt):
    def __init__(self, 
                    LLM: LLMCaller,
                    list_of_risk_assessment_and_expected_outputs: list[InputAndExpectedOutputForCombinedPrompts],
                    
                    sheet_name: str,
                    examples_gathered_or_generated_message: str,
                    candidate_labels: list,
                    domain: str = None,
                    is_first_test: bool = False):
        
        super().__init__(LLM, list_of_risk_assessment_and_expected_outputs, sheet_name, examples_gathered_or_generated_message, candidate_labels, domain=domain, is_first_test=is_first_test)
    
    def get_first_prompt_input(self):
        return self.get_first_prompt_input_with_risk_assessment_method('get_prevention_prompt_input')
    
    def get_expected_output_and_pattern_matched_and_prompt_output(self, i):
        return self.get_expected_output_and_pattern_matched_and_prompt_output_with_risk_assessment_method(i, 'get_prevention_prompt_input')
    
class TestMitigationPromptInput(TestControlMeasureClassificationPrompt):
    def __init__(self, 
                    LLM: LLMCaller,
                    list_of_risk_assessment_and_expected_outputs: list[InputAndExpectedOutputForCombinedPrompts],
                    sheet_name: str,
                    examples_gathered_or_generated_message: str,
                    candidate_labels: list,
                    domain: str = None,
                    is_first_test: bool = False):
        
        super().__init__(LLM, list_of_risk_assessment_and_expected_outputs, sheet_name, examples_gathered_or_generated_message, candidate_labels, domain=domain, is_first_test=is_first_test)
    
    def get_first_prompt_input(self):
        return self.get_first_prompt_input_with_risk_assessment_method('get_mitigation_prompt_input')
    
    def get_expected_output_and_pattern_matched_and_prompt_output(self, i):
        return self.get_expected_output_and_pattern_matched_and_prompt_output_with_risk_assessment_method(i, 'get_mitigation_prompt_input')