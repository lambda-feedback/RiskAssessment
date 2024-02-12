import re

class RegexPatternMatcher:
    def __init__(self):
        pass
    
    def check_string_for_true_or_false(self, string):
        pattern = re.compile(r"Overall Answer: (true|false)", re.IGNORECASE)
        match = re.search(pattern, string)
        if match:
            return match.group(1).lower() == "true"
        else:
            raise Exception("Pattern not found in output prompt")
        
    def check_string_for_prevention_mitigation_or_neither(self, string):
        pattern = re.compile(r"Answer: (prevention|mitigation|neither|both)", re.IGNORECASE)
        match = re.search(pattern, string)
        if match:
            return match.group(1).lower()
        else:
            raise Exception("Pattern not found in output prompt")
    
    def check_string_for_type_of_input_field(self, string):
        pattern = re.compile(r"Answer: (activity|hazard|event_that_leads_to_harm|how_it_harms|who_it_harms)", re.IGNORECASE)
        match = re.search(pattern, string)
        if match:
            return match.group(1).lower()
        else:
            raise Exception("Pattern not found in output prompt")
    
    # def get_match_from_pattern(self, string, pattern):
    #     match = re.search(pattern, string)
    #     if match:
    #         return match.group(1)
    #     else:
    #         raise Exception("Pattern not found in output prompt")
        
    def extract_section_of_prompt_output(self, prompt_output, pattern_to_search_for, lookahead_assertion):
        
        pattern = rf"{pattern_to_search_for}:(.*?)(?={lookahead_assertion})"
        
        match = re.search(pattern, prompt_output, re.DOTALL)
        
        if match:
            explanation = match.group(1).strip()
            return explanation
        else:
            raise Exception("Pattern not found in output prompt")
        
    # def get_predicted_classes_from_input_field_classification_prompt(self, prompt_output):
    #     activity = self.get_match_from_pattern(prompt_output, r"1\. (.+)").lower()
    #     hazard = self.get_match_from_pattern(prompt_output, r"2\. (.+)").lower()
    #     hazard_event = self.get_match_from_pattern(prompt_output, r"3\. (.+)").lower()
    #     how_it_harms = self.get_match_from_pattern(prompt_output, r"4\. (.+)").lower()
    #     who_it_harms = self.get_match_from_pattern(prompt_output, r"5\. (.+)").lower()

    #     return [activity, hazard, hazard_event, how_it_harms, who_it_harms]