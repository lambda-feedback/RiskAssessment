from typing import Type
import csv


try:
    from .PromptInputs import *
    from .LLMCaller import *
    from .RegexPatternMatcher import RegexPatternMatcher
except ImportError:
    from PromptInputs import *
    from LLMCaller import *
    from RegexPatternMatcher import RegexPatternMatcher

class RiskAssessment:
    def __init__(self, activity, hazard, who_it_harms, how_it_harms,
                  uncontrolled_likelihood, uncontrolled_severity, uncontrolled_risk,
                 prevention, mitigation, controlled_likelihood, controlled_severity, controlled_risk):
        self.activity = activity
        self.hazard = hazard
        self.who_it_harms = who_it_harms
        self.how_it_harms = how_it_harms
        self.uncontrolled_likelihood = uncontrolled_likelihood
        self.uncontrolled_severity = uncontrolled_severity
        self.uncontrolled_risk = uncontrolled_risk
        self.prevention = prevention
        self.mitigation = mitigation
        self.controlled_likelihood = controlled_likelihood
        self.controlled_severity = controlled_severity
        self.controlled_risk = controlled_risk

    def convert_RiskAssessment_object_into_lambda_response_list(self):
        return list(vars(self).values())
    
    def get_activity_input(self):
        return Activity(activity=self.activity)
    
    def get_how_it_harms_input(self):
        return HowItHarms(how_it_harms=self.how_it_harms)
    
    def get_how_it_harms_in_context_input(self):
        return HowItHarmsInContext(how_it_harms=self.how_it_harms,
                          activity=self.activity,
                          hazard = self.hazard)

    def get_who_it_harms_input(self):
        return WhoItHarms(who_it_harms=self.who_it_harms)
    
    def get_who_it_harms_in_context_input(self):
        return WhoItHarmsInContext(who_it_harms=self.who_it_harms,
                            how_it_harms=self.how_it_harms,
                            activity=self.activity,
                            hazard=self.hazard)
    
    def get_prevention_input(self):
        return Prevention(prevention=self.prevention,
                          activity=self.activity,
                          hazard=self.hazard,
                          how_it_harms=self.how_it_harms,
                          who_it_harms=self.who_it_harms)
    
    def get_mitigation_input(self):
        return Mitigation(mitigation=self.mitigation,
                          activity=self.activity,
                          hazard=self.hazard,
                          how_it_harms=self.how_it_harms,
                          who_it_harms=self.who_it_harms)
    
    def get_prevention_classification_input(self):
        return PreventionClassification(
                        prevention=self.prevention,
                        activity=self.activity,
                        hazard=self.hazard,
                        how_it_harms=self.how_it_harms,
                        who_it_harms=self.who_it_harms)
    
    def get_mitigation_classification_input(self):
        return MitigationClassification(
                        mitigation=self.mitigation,
                        activity=self.activity,
                        hazard=self.hazard,
                        how_it_harms=self.how_it_harms,
                        who_it_harms=self.who_it_harms)
    
    # TODO: Add ability to see prompt output percentages

    # TODO: Put a function in each of the PromptInputs which gets the prompt output. Each PromptInput class
    # should inherit this method. That way, you would no longer need a PromptAndPromptOutput class.
    
    def get_list_of_prompts(self, LLM_caller: Type[LLMCaller]):
        return [self.get_activity_input().generate_prompt(),
                self.get_how_it_harms_input().generate_prompt(),
                self.get_how_it_harms_in_context_input().generate_prompt(),
                self.get_who_it_harms_input().generate_prompt(),
                self.get_who_it_harms_in_context_input().generate_prompt(),
                self.get_prevention_input().generate_prompt(),
                self.get_mitigation_input().generate_prompt(),
                self.get_prevention_classification_input().generate_prompt(),
                self.get_mitigation_classification_input().generate_prompt()]
    
    def get_list_of_prompt_outputs(self, LLM_caller: Type[LLMCaller]):
        return [LLM_caller.get_model_output(self.get_activity_input()),
                LLM_caller.get_model_output(self.get_how_it_harms_input()),
                LLM_caller.get_model_output(self.get_how_it_harms_in_context_input()),
                LLM_caller.get_model_output(self.get_who_it_harms_input()),
                LLM_caller.get_model_output(self.get_who_it_harms_in_context_input()),
                LLM_caller.get_model_output(self.get_prevention_input()),
                LLM_caller.get_model_output(self.get_mitigation_input()),
                LLM_caller.get_model_output(self.get_prevention_classification_input()),
                LLM_caller.get_model_output(self.get_mitigation_classification_input())]
    
    def get_list_of_regex_matches_for_prompt_outputs(self, prompt_outputs):
        regex_pattern_matcher = RegexPatternMatcher()

        regex_matches = []

        for prompt_output in prompt_outputs:
            regex_matches.append(regex_pattern_matcher.check_string_against_pattern(prompt_output))
        
        return regex_matches