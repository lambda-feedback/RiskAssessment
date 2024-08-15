from typing import Type

from ..utils.LLMCaller import *
from ..utils.RegexPatternMatcher import RegexPatternMatcher

from ..prompts.NoInformationProvided import NoInformationProvided
from ..prompts.HowItHarmsInContext import HowItHarmsInContext
from ..prompts.WhoItHarmsInContext import WhoItHarmsInContext
from ..prompts.HarmCausedAndHazardEvent import HarmCausedAndHazardEvent
from ..prompts.PreventionInput__ControlMeasureClassificationPrompt import PreventionInput__ControlMeasureClassificationPrompt
from ..prompts.MitigationInput__ControlMeasureClassificationPrompt import MitigationInput__ControlMeasureClassificationPrompt
from ..prompts.ControlMeasureClassification__ZeroShot_ChainOfThought import ControlMeasureClassification__ZeroShot_ChainOfThought
from ..prompts.ControlMeasureClassification__FewShot_NoChainOfThought import ControlMeasureClassification__FewShot_NoChainOfThought
from ..prompts.ControlMeasureClassification__ZeroShot_NoChainOfThought import ControlMeasureClassification__ZeroShot_NoChainOfThought
from ..prompts.SummarizeControlMeasureFeedback import SummarizeControlMeasureFeedback
from ..prompts.PreventionClassificationWithoutContextOfOtherInputs import PreventionClassificationWithoutContextOfOtherInputs
from ..prompts.MitigationClassificationWithoutContextOfOtherInputs import MitigationClassificationWithoutContextOfOtherInputs

class RiskAssessment:
    def __init__(self, activity, hazard, how_it_harms, who_it_harms,
                  uncontrolled_likelihood, uncontrolled_severity, uncontrolled_risk,
                 prevention, mitigation, controlled_likelihood, controlled_severity, controlled_risk,
                 risk_domain, prevention_prompt_expected_class, mitigation_prompt_expected_class):
        self.activity = activity
        self.hazard = hazard
        self.how_it_harms = how_it_harms
        self.who_it_harms = who_it_harms
        self.uncontrolled_likelihood = uncontrolled_likelihood
        self.uncontrolled_severity = uncontrolled_severity
        self.uncontrolled_risk = uncontrolled_risk
        self.prevention = prevention
        self.mitigation = mitigation
        self.controlled_likelihood = controlled_likelihood
        self.controlled_severity = controlled_severity
        self.controlled_risk = controlled_risk

        self.prevention_prompt_expected_class = prevention_prompt_expected_class
        self.mitigation_prompt_expected_class = mitigation_prompt_expected_class
        self.prevention_and_mitigation_expected_class_combined = f'{prevention_prompt_expected_class}, {mitigation_prompt_expected_class}'
        self.risk_domain = risk_domain

        # TODO: Remove these parameters
        self.always_true = True
        self.always_false = False

        self.prevention_classification_prompt_ground_truth = self.set_prevention_classification_prompt_ground_truth()
        self.mitigation_classification_prompt_ground_truth = self.set_mitigation_classification_prompt_ground_truth()
        
        self.set_mitigation_classification_prompt_ground_truth()

    def to_string(self):
        class_name = self.__class__.__name__
        if hasattr(self, '__dict__'):
            attributes = ', '.join([f"{key}={value}" for key, value in self.__dict__.items()])
            return f"{class_name}({attributes})"
        else:
            return f"{class_name}()"

    def set_prevention_classification_prompt_ground_truth(self):
        if self.prevention_prompt_expected_class == 'prevention':
            return True
        if self.prevention_prompt_expected_class in ['mitigation', 'both', 'neither']:
            return False

    def set_mitigation_classification_prompt_ground_truth(self):
        if self.mitigation_prompt_expected_class == 'mitigation':
            return True
        if self.mitigation_prompt_expected_class in ['prevention', 'both', 'neither']:
            return False
    
    def get_no_information_provided_for_prevention_input(self):
        return NoInformationProvided(input=self.prevention)
    
    def get_no_information_provided_for_mitigation_input(self):
        return NoInformationProvided(input=self.mitigation)

    def get_how_it_harms_in_context_input(self):
        return HowItHarmsInContext(how_it_harms=self.how_it_harms,
                          activity=self.activity,
                          hazard = self.hazard)
    
    def get_who_it_harms_in_context_input(self):
        return WhoItHarmsInContext(who_it_harms=self.who_it_harms,
                            activity=self.activity,
                            hazard=self.hazard,
                            how_it_harms=self.how_it_harms)
    
    def get_harm_caused_and_hazard_event_input(self):
        return HarmCausedAndHazardEvent(
                            activity=self.activity,
                            hazard=self.hazard,
                          how_it_harms=self.how_it_harms,
                            who_it_harms=self.who_it_harms)
    
    def get_control_measure_prompt_with_prevention_input(self):
        return PreventionInput__ControlMeasureClassificationPrompt(
            activity=self.activity,
            who_it_harms=self.who_it_harms,
            how_it_harms=self.how_it_harms,
            hazard=self.hazard,
            control_measure=self.prevention)
    
    def get_control_measure_prompt_with_mitigation_input(self):
        return MitigationInput__ControlMeasureClassificationPrompt(
            activity=self.activity,
            who_it_harms=self.who_it_harms,
            how_it_harms=self.how_it_harms,
            hazard=self.hazard,
            control_measure=self.mitigation)
    
    def get_zero_shot_chain_of_thought_control_measure_prompt_with_prevention_input(self):
        return ControlMeasureClassification__ZeroShot_ChainOfThought(
            activity=self.activity,
            who_it_harms=self.who_it_harms,
            how_it_harms=self.how_it_harms,
            hazard=self.hazard,
            control_measure=self.prevention)
    
    def get_zero_shot_chain_of_thought_control_measure_prompt_with_mitigation_input(self):
        return ControlMeasureClassification__ZeroShot_ChainOfThought(
            activity=self.activity,
            who_it_harms=self.who_it_harms,
            how_it_harms=self.how_it_harms,
            hazard=self.hazard,
            control_measure=self.mitigation)
    
    def get_few_shot_no_chain_of_thought_control_measure_prompt_with_prevention_input(self):
        return ControlMeasureClassification__FewShot_NoChainOfThought(
            activity=self.activity,
            who_it_harms=self.who_it_harms,
            how_it_harms=self.how_it_harms,
            hazard=self.hazard,
            control_measure=self.prevention)
    
    def get_few_shot_no_chain_of_thought_control_measure_prompt_with_mitigation_input(self):
        return ControlMeasureClassification__FewShot_NoChainOfThought(
            activity=self.activity,
            who_it_harms=self.who_it_harms,
            how_it_harms=self.how_it_harms,
            hazard=self.hazard,
            control_measure=self.mitigation)
    
    def get_zero_shot_no_chain_of_thought_control_measure_prompt_with_prevention_input(self):
        return ControlMeasureClassification__ZeroShot_NoChainOfThought(
            activity=self.activity,
            who_it_harms=self.who_it_harms,
            how_it_harms=self.how_it_harms,
            hazard=self.hazard,
            control_measure=self.prevention)
    
    def get_zero_shot_no_chain_of_thought_control_measure_prompt_with_mitigation_input(self):
        return ControlMeasureClassification__ZeroShot_NoChainOfThought(
            activity=self.activity,
            who_it_harms=self.who_it_harms,
            how_it_harms=self.how_it_harms,
            hazard=self.hazard,
            control_measure=self.mitigation)
    
    def get_feedback_summary_input(self):
        return SummarizeControlMeasureFeedback()
    
    def get_prevention_classification_prompt_input(self):
        return PreventionClassificationWithoutContextOfOtherInputs(
            prevention=self.prevention)
    
    def get_mitigation_classification_prompt_input(self):
        return MitigationClassificationWithoutContextOfOtherInputs(
            mitigation=self.mitigation)
    
    def get_word_fields(self):
        return ['activity',
                'hazard',
                'who_it_harms',
                'how_it_harms',
                'prevention',
                'mitigation']
    
    def get_word_fields_which_cannot_be_empty(self):
        return ['activity',
                'hazard',
                'how_it_harms',
                'who_it_harms']
    
    def get_integer_fields(self):
        return ['uncontrolled_likelihood',
                'uncontrolled_severity',
                'uncontrolled_risk',
                'controlled_likelihood',
                'controlled_severity',
                'controlled_risk']
    
    # TODO: It should be OK if either prevention or mitigation field is empty, but not both.
    def get_empty_fields(self):
        empty_fields = []

        for field_name in self.get_word_fields_which_cannot_be_empty() + self.get_integer_fields():
            if getattr(self, field_name) == '':
                formatted_field_name = field_name.replace('_', ' ').title()
                empty_fields.append(formatted_field_name)
        
        return empty_fields
        
    def does_string_represent_an_integer(self, string:str):
        try:
            int(string)
            return True
        except ValueError:
            return False
        
    def does_string_represent_words(self, string:str):
        if len(string.split(' ')) > 1: # If there are multiple words, unlikely to represent a number
            return True
        else:
            return string.isalpha() # If there is only one word, check if it is a word and not a number
        
    def get_word_fields_incorrect(self):
        word_fields_incorrect = []

        for word_field_name in self.get_word_fields():
            if not self.does_string_represent_words(getattr(self, word_field_name)):
                formatted_word_field_name = word_field_name.replace('_', ' ').title()
                word_fields_incorrect.append(formatted_word_field_name)
        
        return word_fields_incorrect
    
    def get_integer_fields_incorrect(self):
        integer_fields_incorrect = []

        for integer_field_name in self.get_integer_fields():
            if not self.does_string_represent_an_integer(getattr(self, integer_field_name)):
                formatted_integer_field_name = integer_field_name.replace('_', ' ').title()
                integer_fields_incorrect.append(formatted_integer_field_name)
        
        return integer_fields_incorrect
    
    def check_that_likelihood_and_severity_and_risk_are_all_integers(self, likelihood, severity, risk):
        try:
            likelihood = int(likelihood)
            severity = int(severity)
            risk = int(risk)

            return True
        except ValueError:
            return False
    
    def uncontrolled_values_are_all_integers(self):
        return self.check_that_likelihood_and_severity_and_risk_are_all_integers(likelihood=self.uncontrolled_likelihood, 
                                                                                 severity=self.uncontrolled_severity, 
                                                                                 risk=self.uncontrolled_risk)
    
    def controlled_values_are_all_integers(self):
        return self.check_that_likelihood_and_severity_and_risk_are_all_integers(likelihood=self.controlled_likelihood, 
                                                                                 severity=self.controlled_severity, 
                                                                                 risk=self.controlled_risk)
    
    def check_that_likelihood_and_severity_values_are_between_1_and_4(self, likelihood, severity):
        likelihood = int(likelihood)
        severity = int(severity)

        if likelihood > 4 or likelihood < 1 or severity > 4 or severity < 1:
            return True
        else:
            return False
        
    def uncontrolled_values_are_between_1_and_4(self):
        return self.check_that_likelihood_and_severity_values_are_between_1_and_4(self.uncontrolled_likelihood, self.uncontrolled_severity)
    
    def controlled_values_are_between_1_and_4(self):
        return self.check_that_likelihood_and_severity_values_are_between_1_and_4(self.controlled_likelihood, self.controlled_severity)
        
    def check_that_risk_equals_likelihood_times_severity(self, likelihood, severity, risk):
        likelihood = int(likelihood)
        severity = int(severity)
        risk = int(risk)

        if likelihood * severity == risk:
            return True
        else:
            return False
    
    def check_that_uncontrolled_likelihood_and_severity_and_risk_are_all_integers(self):
        return self.check_that_likelihood_and_severity_and_risk_are_all_integers(likelihood=self.uncontrolled_likelihood, 
                                                                                 severity=self.uncontrolled_severity, 
                                                                                 risk=self.uncontrolled_risk)

    def check_that_uncontrolled_likelihood_and_severity_and_risk_are_all_integers(self):
        return self.check_that_likelihood_and_severity_and_risk_are_all_integers(likelihood=self.controlled_likelihood, 
                                                                                 severity=self.controlled_severity, 
                                                                                 risk=self.controlled_risk)
    
    def uncontrolled_risk_multiplication(self):
        return self.check_that_risk_equals_likelihood_times_severity(likelihood=self.uncontrolled_likelihood,
                                                                severity=self.uncontrolled_severity,
                                                                risk=self.uncontrolled_risk)
    
    def controlled_risk_multiplication(self):
        return self.check_that_risk_equals_likelihood_times_severity(likelihood=self.controlled_likelihood,
                                                                severity=self.controlled_severity,
                                                                risk=self.controlled_risk)
    
    def check_controlled_values_are_less_than_or_equal_to_uncontrolled_values(self, controlled_value, uncontrolled_value, value_name):
        controlled_value = int(controlled_value)
        uncontrolled_value = int(uncontrolled_value)

        if controlled_value <= uncontrolled_value:
            return True
        else:
            return False
    
    def compare_controlled_and_uncontrolled_likelihood(self):
        return self.check_controlled_values_are_less_than_or_equal_to_uncontrolled_values(controlled_value=self.controlled_likelihood,
                                                                                           uncontrolled_value=self.uncontrolled_likelihood,
                                                                                           value_name='likelihood')

    def compare_controlled_and_uncontrolled_severity(self):
        return self.check_controlled_values_are_less_than_or_equal_to_uncontrolled_values(controlled_value=self.controlled_severity,
                                                                                           uncontrolled_value=self.uncontrolled_severity,
                                                                                           value_name='severity')
    
    def get_input_check_feedback_message(self):
        empty_fields = self.get_empty_fields()
        word_fields_incorrect = self.get_word_fields_incorrect()
        integer_fields_incorrect = self.get_integer_fields_incorrect()

        # TODO: Should make it non-compulsory to enter anything for the mitigation field
        if len(empty_fields) > 0:
            return f'Please fill in the following fields: {str(empty_fields)[1:-1]}.\n\n'
        
        if len(word_fields_incorrect) > 0:
            return f'Please make sure that the following fields only contain words: {str(word_fields_incorrect)[1:-1]}.\n\n'
        
        if len(integer_fields_incorrect) > 0:
            return f'Please make sure that the following fields are a single integer: {str(integer_fields_incorrect)[1:-1]}.\n\n'
        
        return True
    
    def get_likelihood_severity_risk_feedback_message(self):

        if self.uncontrolled_values_are_all_integers() == True and self.controlled_values_are_all_integers() == True:
            if self.uncontrolled_values_are_between_1_and_4() or self.controlled_values_are_between_1_and_4():
                return 'Please make sure that the likelihood and severity values are between 1 and 4.'
            
            if self.uncontrolled_risk_multiplication() == False or self.controlled_risk_multiplication() == False:
                return 'One or both of the risk values are incorrect. The risk value should be the product of their respective likelihood and severity values.'
            
            if self.compare_controlled_and_uncontrolled_likelihood() == False:
                return 'The controlled likelihood value should be less than or equal to the uncontrolled likelihood value.'
            
            if self.compare_controlled_and_uncontrolled_severity() == False:
                return 'The controlled severity value should be less than or equal to the uncontrolled severity value.'
            
            return True
        

    # TODO: Add ability to see prompt output percentages - might be possible for LLMs other than GPT-3

    def get_prompt_output_and_pattern_matched(self, prompt_input_object: Type[BasePromptInput], LLM_caller: Type[LLMCaller], **kwargs):
        regex_pattern_matcher = RegexPatternMatcher()
        
        prompt_output = LLM_caller.get_model_output(prompt=prompt_input_object.generate_prompt(**kwargs), max_tokens=prompt_input_object.max_tokens)
        print(prompt_output)
        
        pattern_matching_method = getattr(regex_pattern_matcher, prompt_input_object.pattern_matching_method)
        
        pattern_matched = pattern_matching_method(prompt_output)

        return prompt_output, pattern_matched
    
    def get_shortform_feedback_from_regex_match(self, prompt_input_object: Type[BasePromptInput], pattern_matched):
        
        if pattern_matched in prompt_input_object.labels_indicating_correct_input:
            return prompt_input_object.get_shortform_feedback(feedback_type='positive')
        else:
            return prompt_input_object.get_shortform_feedback(feedback_type='negative')
    
    def are_all_multiplications_correct(self)->bool:
        return self.check_uncontrolled_risk() == 'correct' and self.check_controlled_risk() == 'correct'
    
    def are_all_prompt_outputs_correct(self, prompt_outputs) -> bool:
        regex_matches = self.get_list_of_regex_matches(prompt_outputs)
        prompt_inputs = self.get_list_of_prompt_input_objects()

        for i in range(len(regex_matches)):
            if regex_matches[i] != prompt_inputs[i].labels_indicating_correct_input:
                return False
        
        return True

    def convert_risk_assessment_to_evaluation_function_list_input(self):
        return [self.activity, 
                self.hazard, 
                self.how_it_harms, 
                self.who_it_harms, 
                self.uncontrolled_likelihood, 
                self.uncontrolled_severity, 
                self.uncontrolled_risk, 
                self.prevention, 
                self.mitigation, 
                self.controlled_likelihood, 
                self.controlled_severity, 
                self.controlled_risk]

class RiskAssessmentWithoutNumberInputs(RiskAssessment):
    def __init__(self, activity, hazard, how_it_harms, who_it_harms,
                 prevention, mitigation, 
                 risk_domain,
                 prevention_prompt_expected_class, 
                 mitigation_prompt_expected_class):
        super().__init__(activity=activity,
                         hazard=hazard,
                         how_it_harms=how_it_harms,
                         who_it_harms=who_it_harms,
                         uncontrolled_likelihood='1',
                         uncontrolled_severity='1',
                         uncontrolled_risk='1',
                         prevention=prevention,
                         mitigation=mitigation,
                         controlled_likelihood='1',
                         controlled_severity='1',
                         controlled_risk='1',
                         risk_domain=risk_domain,
                         prevention_prompt_expected_class=prevention_prompt_expected_class,
                         mitigation_prompt_expected_class=mitigation_prompt_expected_class)