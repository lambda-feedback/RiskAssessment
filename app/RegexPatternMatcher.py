import re

class RegexPatternMatcher:
    def __init__(self):
        pass
    
    def check_string_for_true_or_false(self, string):
        pattern = re.compile(r"(true|false)", re.IGNORECASE)
        match = re.search(pattern, string)
        if match:
            return match.group(1).lower() == "true"
        else:
            raise Exception("Pattern not found in output prompt")
        
    def check_string_for_prevention_mitigation_or_neither(self, string):
        pattern = re.compile(r"(prevention|mitigation|neither)", re.IGNORECASE)
        match = re.search(pattern, string)
        if match:
            return match.group(1).lower()
        else:
            raise Exception("Pattern not found in output prompt")