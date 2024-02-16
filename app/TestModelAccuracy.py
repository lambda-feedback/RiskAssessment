import re
from datetime import datetime
import numpy as np
import pandas as pd
from tabulate import tabulate

from LLMCaller import LLMCaller
from InputAndExpectedOutput import InputAndExpectedOutputForSinglePrompt, InputAndExpectedOutputForCombinedPrompts
from GoogleSheetsWriter import GoogleSheetsWriter
from RegexPatternMatcher import RegexPatternMatcher

class TestModelAccuracy:
    def __init__(self, 
                LLM: LLMCaller,
                LLM_name: str,
                list_of_input_and_expected_outputs: list[InputAndExpectedOutputForSinglePrompt],
                sheet_name: str,
                test_description: str):
        
        self.LLM = LLM
        self.LLM_name = LLM_name
        self.list_of_input_and_expected_outputs = list_of_input_and_expected_outputs
        self.sheet_name = sheet_name
        self.test_description = test_description

    def get_number_of_examples(self):
        return len(self.list_of_input_and_expected_outputs)
    
    def get_first_prompt_input_object(self):
        
        return self.list_of_input_and_expected_outputs[0].input

    def get_first_prompt_input(self):
        first_prompt_input_object = self.get_first_prompt_input_object()
        first_prompt_input = first_prompt_input_object.generate_prompt()
        return first_prompt_input
    
    def get_classes(self):
        first_prompt_input_object = self.get_first_prompt_input_object()

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

    def update_output_string(self, output_string, i, pattern_matched, expected_output):
        result_dict = {'input': self.list_of_input_and_expected_outputs[i].input.to_string(),
                'pattern_matched': pattern_matched, 
                'expected_output': expected_output}

        output_string += f'{i + 1}: {str(result_dict)}\n\n'

        return output_string

    def get_expected_output_and_pattern_matched_and_prompt_output(self, i):
        expected_output = self.list_of_input_and_expected_outputs[i].expected_output
        input = self.list_of_input_and_expected_outputs[i].input

        pattern_matching_method_string = input.pattern_matching_method
        regex_pattern_matcher = RegexPatternMatcher()
        pattern_matching_method = getattr(regex_pattern_matcher, pattern_matching_method_string)
    
        prompt_output = self.LLM.get_model_output(input.generate_prompt())

        pattern_matched = pattern_matching_method(prompt_output)
        
        return expected_output, pattern_matched, prompt_output
    
    def update_prompt_output_strings(self, prompt_output, expected_output, pattern_matched, prompt_outputs_for_correct_responses, prompt_outputs_for_incorrect_responses, i, count_correct):
        if pattern_matched == expected_output:
            count_correct += 1

            prompt_outputs_for_correct_responses += f'{i + 1}: {prompt_output}\nExpected output: {expected_output}\n\n'

        else:
            prompt_outputs_for_incorrect_responses += f'{i + 1}: {prompt_output}\nExpected output: {expected_output}\n\n'

        return prompt_outputs_for_correct_responses, prompt_outputs_for_incorrect_responses, count_correct

    def convert_list_of_lists_to_string(self, list_of_lists):
        # Convert each sublist to a string with newline
        sublist_strings = ['[' + ', '.join(map(str, sublist)) + ']' for sublist in list_of_lists]

        # Join the sublist strings with a newline and add outer brackets
        return '[' + ',\n'.join(sublist_strings) + ']'

    def get_model_accuracy_and_model_outputs(self):
        print('Counting correct responses...')
        count_correct = 0
        
        output_string = ''
        prompt_outputs_for_correct_responses = ''
        prompt_outputs_for_incorrect_responses = ''

        classes = self.get_classes()
        n_classes = len(classes)

        confusion_matrix = np.zeros((n_classes, n_classes))

        n_examples = self.get_number_of_examples()

        for i in range(n_examples):

            expected_output, pattern_matched, prompt_output = self.get_expected_output_and_pattern_matched_and_prompt_output(i)

            confusion_matrix = self.update_confusion_matrix(confusion_matrix, classes, pattern_matched, expected_output)

            output_string = self.update_output_string(output_string, i, pattern_matched, expected_output)

            prompt_outputs_for_correct_responses, 
            prompt_outputs_for_incorrect_responses, 
            prompt_outputs_for_correct_responses, prompt_outputs_for_incorrect_responses, count_correct = self.update_prompt_output_strings(prompt_output, 
                                                                expected_output, 
                                                                pattern_matched, 
                                                                prompt_outputs_for_correct_responses, 
                                                                prompt_outputs_for_incorrect_responses, 
                                                                i, 
                                                                count_correct)
            
            print(count_correct)

        accuracy = round(count_correct / n_examples * 100, 2)

        confusion_matrix_string = self.generate_confusion_matrix_string(confusion_matrix, classes)
        
        return accuracy, confusion_matrix_string, output_string, prompt_outputs_for_correct_responses, prompt_outputs_for_incorrect_responses
    
    def get_first_prompt_input(self):
        first_input = self.list_of_input_and_expected_outputs[0].input
        first_prompt_input = first_input.generate_prompt()

        return first_prompt_input
    
    def save_test_results(self, 
                          accuracy, 
                          confusion_matrix,
                          output_string, 
                          prompt_outputs_for_correct_responses,
                          prompt_outputs_for_incorrect_responses,
                          first_prompt_input):

        datetime_now = datetime.now().strftime("%d-%m_%H-%M")

        if self.LLM_name == 'gpt-3.5-turbo':
            model_parameters = f'Temp: {self.LLM.temperature}, Max tokens: {self.LLM.max_tokens}'
        else:
            model_parameters = ''
        
        num_examples = self.get_number_of_examples()

        new_line_data = [self.test_description, 
                         self.LLM_name, 
                            datetime_now, 
                            0,
                            model_parameters, 
                            accuracy, 
                            num_examples,
                            confusion_matrix,
                            output_string[:45000],
                            first_prompt_input,
                            prompt_outputs_for_correct_responses[:45000],
                            prompt_outputs_for_incorrect_responses[:45000]]
        
        sheets_writer = GoogleSheetsWriter(sheet_name=self.sheet_name)
        sheets_writer.write_to_sheets(new_line_data)
        
    # TODO: Refactoring: As below, remove positional arguments and only use keyword arguments
    def run_test(self):
        accuracy, confusion_matrix, output_string, prompt_outputs_for_correct_responses, prompt_outputs_for_incorrect_responses = self.get_model_accuracy_and_model_outputs()
        first_prompt_input = self.get_first_prompt_input()
        self.save_test_results(accuracy=accuracy, 
                               confusion_matrix=confusion_matrix,
                               output_string=output_string, 
                               first_prompt_input=first_prompt_input,
                               prompt_outputs_for_correct_responses=prompt_outputs_for_correct_responses,
                               prompt_outputs_for_incorrect_responses=prompt_outputs_for_incorrect_responses,)

class TestModelAccuracyForCombinationOfPrompts(TestModelAccuracy):
    def __init__(self, 
                LLM: LLMCaller,
                LLM_name: str,
                list_of_risk_assessment_and_expected_outputs: list[InputAndExpectedOutputForCombinedPrompts],
                sheet_name: str,
                test_description: str):
        
        self.LLM = LLM
        self.LLM_name = LLM_name
        self.list_of_risk_assessment_and_expected_outputs = list_of_risk_assessment_and_expected_outputs
        self.sheet_name = sheet_name
        self.test_description = test_description

    # Defined in children classes below
    def get_expected_output_and_pattern_matched_and_prompt_output(self, i):
        pass

    # Defined in children classes below
    def get_first_prompt_input(self):
        pass

    def get_number_of_examples(self):
        return len(self.list_of_risk_assessment_and_expected_outputs)

    def get_first_prompt_input_object(self):
        
        return self.list_of_risk_assessment_and_expected_outputs[0].final_prompt_input
    
    def update_output_string(self, output_string, i, pattern_matched, expected_output):
        result_dict = {'risk_assessment': self.list_of_risk_assessment_and_expected_outputs[i].risk_assessment.to_string(),
                'pattern_matched': pattern_matched, 
                'expected_output': expected_output}

        output_string += f'{i + 1}: {str(result_dict)}\n\n'

        return output_string

class TestIllnessAndInjuryPrompts(TestModelAccuracyForCombinationOfPrompts):
    def __init__(self, 
                LLM: LLMCaller,
                LLM_name: str,
                list_of_risk_assessment_and_expected_outputs: list[InputAndExpectedOutputForCombinedPrompts],
                sheet_name: str,
                test_description: str):
        
        super().__init__(LLM, LLM_name, list_of_risk_assessment_and_expected_outputs, sheet_name, test_description)
    
    def get_expected_output_and_pattern_matched_and_prompt_output(self, i):
        RA = self.list_of_risk_assessment_and_expected_outputs[i].risk_assessment
        expected_output = self.list_of_risk_assessment_and_expected_outputs[i].expected_output

        injury_prompt_input = RA.get_injury_input()
        injury_prompt_output, injury_pattern = RA.get_prompt_output_and_pattern_matched(injury_prompt_input, self.LLM)

        illness_prompt_input = RA.get_illness_input()
        illness_prompt_output, illness_pattern = RA.get_prompt_output_and_pattern_matched(illness_prompt_input, self.LLM)

        if injury_pattern == False and illness_pattern == False:
            return expected_output, 'neither', f'''Injury prompt: {injury_prompt_output}\n\nIllness prompt: {illness_prompt_output}'''
        else:
            if injury_pattern != False:
                predicted_output = 'injury'
            else:
                predicted_output = 'illness'

            return expected_output, predicted_output, f'''Injury prompt: {injury_prompt_output}\n\nIllness prompt: {illness_prompt_output}'''

class TestHazardEventPrompt(TestModelAccuracyForCombinationOfPrompts):
    def __init__(self, 
                LLM: LLMCaller,
                LLM_name: str,
                list_of_risk_assessment_and_expected_outputs: list[InputAndExpectedOutputForCombinedPrompts],
                sheet_name: str,
                test_description: str):
        
        super().__init__(LLM, LLM_name, list_of_risk_assessment_and_expected_outputs, sheet_name, test_description)
    
    def get_expected_output_and_pattern_matched_and_prompt_output(self, i):
        RA = self.list_of_risk_assessment_and_expected_outputs[i].risk_assessment
        expected_output = self.list_of_risk_assessment_and_expected_outputs[i].expected_output

        injury_prompt_input = RA.get_injury_input()
        injury_prompt_output, injury_pattern = RA.get_prompt_output_and_pattern_matched(injury_prompt_input, self.LLM)

        illness_prompt_input = RA.get_illness_input()
        illness_prompt_output, illness_pattern = RA.get_prompt_output_and_pattern_matched(illness_prompt_input, self.LLM)

        if injury_pattern == False and illness_pattern == False:
            return expected_output, False, f'''Injury prompt: {injury_prompt_output}\n\nIllness prompt: {illness_prompt_output}'''
        
        else:
            if injury_pattern != False:
                harm_caused = injury_pattern
            else:
                harm_caused = illness_pattern
        
            hazard_event_prompt_input = RA.get_hazard_event_input()
            hazard_event_prompt_output, hazard_event_pattern = RA.get_prompt_output_and_pattern_matched(hazard_event_prompt_input, self.LLM)

            return expected_output, True, f'''Injury prompt: {injury_prompt_output}\n\nIllness prompt: {illness_prompt_output}\n\nHazard event prompt: {hazard_event_prompt_output}'''

class TestFirstAidPreventionPrompt(TestModelAccuracyForCombinationOfPrompts):
    def __init__(self, 
                LLM: LLMCaller,
                LLM_name: str,
                list_of_risk_assessment_and_expected_outputs: list[InputAndExpectedOutputForCombinedPrompts],
                sheet_name: str,
                test_description: str):
        
        super().__init__(LLM, LLM_name, list_of_risk_assessment_and_expected_outputs, sheet_name, test_description)

    def get_expected_output_and_pattern_matched_and_prompt_output(self, i):
        RA = self.list_of_risk_assessment_and_expected_outputs[i].risk_assessment
        expected_output = self.list_of_risk_assessment_and_expected_outputs[i].expected_output

        injury_prompt_input = RA.get_injury_input()
        injury_prompt_output, injury_pattern = RA.get_prompt_output_and_pattern_matched(injury_prompt_input, self.LLM)

        illness_prompt_input = RA.get_illness_input()
        illness_prompt_output, illness_pattern = RA.get_prompt_output_and_pattern_matched(illness_prompt_input, self.LLM)

        if injury_pattern == False and illness_pattern == False:
            return expected_output, 'Harm not detected', f'''Injury prompt: {injury_prompt_output}\n\nIllness prompt: {i}'''
        else:
            if injury_pattern != False:
                harm_caused = injury_pattern
            else:
                harm_caused = illness_pattern

            hazard_event_prompt_input = RA.get_hazard_event_input()
            hazard_event_prompt_output, hazard_event_pattern = RA.get_prompt_output_and_pattern_matched(prompt_input_object=hazard_event_prompt_input, 
                                                                                                        LLM_caller=self.LLM, 
                                                                               )
            first_aid_prompt_input = RA.get_prevention_first_aid_input()
            prevention_first_aid_prompt_output, prevention_first_aid_pattern = RA.get_prompt_output_and_pattern_matched(first_aid_prompt_input, self.LLM)

            return expected_output, prevention_first_aid_pattern, prevention_first_aid_prompt_output

class TestModelAccuracyForCompletePreventionPromptPipeline(TestModelAccuracyForCombinationOfPrompts):
    def __init__(self, 
                LLM: LLMCaller,
                LLM_name: str,
                list_of_risk_assessment_and_expected_outputs: list[InputAndExpectedOutputForCombinedPrompts],
                sheet_name: str,
                test_description: str):
        
        super().__init__(LLM, LLM_name, list_of_risk_assessment_and_expected_outputs, sheet_name, test_description)
    
    def get_expected_output_and_pattern_matched_and_prompt_output(self, i):
        RA = self.list_of_risk_assessment_and_expected_outputs[i].risk_assessment
        expected_output = self.list_of_risk_assessment_and_expected_outputs[i].expected_output

        # injury_prompt_input = RA.get_injury_input()
        # injury_prompt_output, injury_pattern = RA.get_prompt_output_and_pattern_matched(injury_prompt_input, self.LLM)

        # illness_prompt_input = RA.get_illness_input()
        # illness_prompt_output, illness_pattern = RA.get_prompt_output_and_pattern_matched(illness_prompt_input, self.LLM)

        # if injury_pattern == False and illness_pattern == False:
        #     return expected_output, 'neither', f'''Injury prompt: {injury_prompt_output}\n\nIllness prompt: {i}'''
        # else:
        #     if injury_pattern != False:
        #         harm_caused = injury_pattern
        #     else:
        #         harm_caused = illness_pattern

        #     hazard_event_prompt_input = RA.get_hazard_event_input()
        #     hazard_event_prompt_output, hazard_event_pattern = RA.get_prompt_output_and_pattern_matched(prompt_input_object=hazard_event_prompt_input, 
        #                                                                                                 LLM_caller=self.LLM, 
        #                                                                        )

        prevention_protective_clothing_prompt_input = RA.get_prevention_protective_clothing_input()
        prevention_protective_clothing_prompt_output, prevention_protective_clothing_pattern = RA.get_prompt_output_and_pattern_matched(prompt_input_object=prevention_protective_clothing_prompt_input, 
                                                                                                                                        LLM_caller=self.LLM,
                                                                                                                                        
                                                                                                                )
        
        if prevention_protective_clothing_pattern == True:
            prompt_output = f'''{prevention_protective_clothing_prompt_output} 
            
            'First aid prompt not run'
            
            'Prevention prompt not run'''
            
            return expected_output, 'mitigation', prompt_output

        else:
            first_aid_prompt_input = RA.get_prevention_first_aid_input()
            prevention_first_aid_prompt_output, prevention_first_aid_pattern = RA.get_prompt_output_and_pattern_matched(first_aid_prompt_input, self.LLM)

            if prevention_first_aid_pattern == True:
                prompt_output = f'''{prevention_protective_clothing_prompt_output}

                {prevention_first_aid_prompt_output}

                'Prevention prompt not run'''

                return expected_output, 'mitigation', prompt_output
            
            else:
                prevention_prompt_input = RA.get_prevention_input()
                prevention_prompt_output, prevention_pattern = RA.get_prompt_output_and_pattern_matched(prevention_prompt_input, self.LLM)

                prompt_output = f'''{prevention_protective_clothing_prompt_output}

                {prevention_first_aid_prompt_output}
                
                {prevention_prompt_output}'''

                return expected_output, prevention_pattern, prompt_output
    
    def get_first_prompt_input(self):
        RA = self.list_of_risk_assessment_and_expected_outputs[0].risk_assessment

        # injury_prompt_input = RA.get_injury_input()
        # injury_prompt_output, injury_pattern = RA.get_prompt_output_and_pattern_matched(injury_prompt_input, self.LLM)

        # illness_prompt_input = RA.get_illness_input()
        # illness_prompt_output, illness_pattern = RA.get_prompt_output_and_pattern_matched(illness_prompt_input, self.LLM)

        # if injury_pattern == False and illness_pattern == False:
        #     harm_caused = RA.how_it_harms
        # else:
        #     if injury_pattern != False:
        #         harm_caused = injury_pattern
        #     else:
        #         harm_caused = illness_pattern

        # hazard_event_prompt_input = RA.get_hazard_event_input()
        # hazard_event_prompt_output, hazard_event_pattern = RA.get_prompt_output_and_pattern_matched(prompt_input_object=hazard_event_prompt_input, 
        #                                                                                             LLM_caller=self.LLM, 
        #                                                                    )
        
        first_prevention_protective_clothing_prompt_input_object = RA.get_prevention_protective_clothing_input()
        first_prevention_protective_clothing_prompt_input = first_prevention_protective_clothing_prompt_input_object.generate_prompt()

        first_prevention_first_aid_prompt_input_object = RA.get_prevention_first_aid_input()
        first_prevention_first_aid_prompt_input = first_prevention_first_aid_prompt_input_object.generate_prompt()

        first_prevention_prompt_input_object = RA.get_prevention_input()
        first_prevention_prompt_input = first_prevention_prompt_input_object.generate_prompt()

        return f'''{first_prevention_protective_clothing_prompt_input}
                  
                  {first_prevention_first_aid_prompt_input}
                  
                  {first_prevention_prompt_input}'''

class TestModelAccuracyForCompleteMitigationPromptPipeline(TestModelAccuracyForCombinationOfPrompts):
    def __init__(self, 
                LLM: LLMCaller,
                LLM_name: str,
                list_of_risk_assessment_and_expected_outputs: list[InputAndExpectedOutputForCombinedPrompts],
                sheet_name: str,
                test_description: str):
        
        super().__init__(LLM, LLM_name, list_of_risk_assessment_and_expected_outputs, sheet_name, test_description)

    def get_expected_output_and_pattern_matched_and_prompt_output(self, i):
        RA = self.list_of_risk_assessment_and_expected_outputs[i].risk_assessment
        expected_output = self.list_of_risk_assessment_and_expected_outputs[i].expected_output

        mitigation_protective_clothing_prompt_input = RA.get_mitigation_protective_clothing_input()
        mitigation_protective_clothing_prompt_output, mitigation_protective_clothing_pattern = RA.get_prompt_output_and_pattern_matched(mitigation_protective_clothing_prompt_input, self.LLM)

        if mitigation_protective_clothing_pattern == True:
            prompt_output = f'''{mitigation_protective_clothing_prompt_output} 
            
            'First aid prompt not run'
            
            'Mitigation prompt not run'''
            
            return expected_output, 'mitigation', prompt_output

        else:
            first_aid_prompt_input = RA.get_mitigation_first_aid_input()
            mitigation_first_aid_prompt_output, mitigation_first_aid_pattern = RA.get_prompt_output_and_pattern_matched(first_aid_prompt_input, self.LLM)

            if mitigation_first_aid_pattern == True:
                prompt_output = f'''{mitigation_protective_clothing_prompt_output}

                {mitigation_first_aid_prompt_output}

                'Mitigation prompt not run'''

                return expected_output, 'mitigation', prompt_output
            
            else:
                mitigation_prompt_input = RA.get_mitigation_input()
                mitigation_prompt_output, mitigation_pattern = RA.get_prompt_output_and_pattern_matched(mitigation_prompt_input, self.LLM)

                prompt_output = f'''{mitigation_protective_clothing_prompt_output}

                {mitigation_first_aid_prompt_output}
                
                {mitigation_prompt_output}'''

                return expected_output, mitigation_pattern, prompt_output
    
    def get_first_prompt_input(self):
        first_risk_assessment = self.list_of_risk_assessment_and_expected_outputs[0].risk_assessment
        
        first_protective_clothing_prompt_input_object = first_risk_assessment.get_mitigation_protective_clothing_input()
        first_protective_clothing_prompt_input = first_protective_clothing_prompt_input_object.generate_prompt()

        first_aid_prompt_input_object = first_risk_assessment.get_mitigation_first_aid_input()
        first_aid_prompt_input = first_aid_prompt_input_object.generate_prompt()

        first_prevention_prompt_input_object = first_risk_assessment.get_mitigation_input()
        first_prevention_prompt_input = first_prevention_prompt_input_object.generate_prompt()

        return f'''{first_protective_clothing_prompt_input}
                  
                  {first_aid_prompt_input}
                  
                  {first_prevention_prompt_input}'''