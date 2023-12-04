import re

class RegexPatternMatcher:
    def __init__(self, pattern):
        self.pattern = re.compile(r"(true|false)", re.IGNORECASE)
    
    def check_string_against_pattern(self, string):
        match = re.search(self.pattern, string)
        if match:
            return match.group(1).lower() == "true"
        else:
            raise Exception("Pattern not found in output prompt")