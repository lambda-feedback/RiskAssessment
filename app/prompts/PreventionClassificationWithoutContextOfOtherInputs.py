from ..prompts.BasePromptInput import BasePromptInput

class PreventionClassificationWithoutContextOfOtherInputs(BasePromptInput):
    def __init__(self, prevention):
        self.prevention = prevention

        self.candidate_labels = [True, False]
        self.pattern_matching_method = 'check_string_for_true_or_false'
        self.max_tokens = 300
    
    def return_few_shot_examples(self):
        return f'''
        <EXAMPLE INSTRUCTIONS>
        1. Explain whether "Wearing a helmet" reduces the likelihood of an event that leads to harm.
        2. Answer True if it does and False if it does not.
        </EXAMPLE INSTRUCTIONS>

        <EXAMPLE OUTPUT>
        1. Prevention Explanation: "Wearing a helmet" does not significantly reduce the likelihood of an event that leads to harm (such as an accident).
        2. Answer: False
        </EXAMPLE OUTPUT>

        <EXAMPLE INSTRUCTIONS>
        1. Explain whether "Point needle away from yourself and others" reduces the likelihood of an event that leads to harm.
        2. Answer True if it does and False if it does not.
        </EXAMPLE INSTRUCTIONS>

        <EXAMPLE OUTPUT>
        1. Prevention Explanation: "Point needle away from yourself and others" reduces the likelihood of an event that leads to harm (such as needle-stick injury).
        2. Answer: True
        </EXAMPLE OUTPUT>'''

    def generate_prompt(self):
        return f'''
        {self.return_few_shot_examples()}

        <INSTRUCTIONS>
        1. Explain whether "{self.prevention}" reduces the likelihood of an event that leads to harm.
        2. Answer True if it does and False if it does not.
        </INSTRUCTIONS>

        <OUTPUT FORMAT>
        Use the following output format:
        Prevention Explanation: <your explanation>
        Overall Answer: <True OR False>
        </OUTPUT FORMAT>

        <OUTPUT>
        1. Prevention Explanation: '''