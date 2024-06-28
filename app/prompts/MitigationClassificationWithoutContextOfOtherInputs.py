from ..prompts.BasePromptInput import BasePromptInput

class MitigationClassificationWithoutContextOfOtherInputs(BasePromptInput):
    def __init__(self, mitigation):
        self.mitigation = mitigation

        self.candidate_labels = [True, False]
        self.pattern_matching_method = 'check_string_for_true_or_false'
        self.max_tokens = 300
    
    def return_few_shot_examples(self):
        return f'''
        <EXAMPLE INSTRUCTIONS>
        1. Assuming an event has led to harm, explain whether "Wearing a helmet" reduces the severity of the harm caused by the event.
        2. Answer True if it does and False if it does not.
        </EXAMPLE INSTRUCTIONS>

        <EXAMPLE OUTPUT>
        1. Mitigation Explanation: Assuming that an event involving a head injury has occurred, "wearing a helmet" is a preparatory measure that reduces the severity of harm caused.
        2. Answer: True
        </EXAMPLE OUTPUT>

        <EXAMPLE INSTRUCTIONS>
        1. Assuming an event has led to harm, explain whether "Apply first aid" reduces the harm caused by this event.
        2. Answer True if it does and False if it does not.
        </EXAMPLE INSTRUCTIONS>

        <EXAMPLE OUTPUT>
        1. Mitigation Explanation: Assuming an event like a burn has occurred, "apply first aid" is a measure in response to the event that reduces the harm caused by the event.
        2. Answer: True
        </EXAMPLE OUTPUT>

        <EXAMPLE INSTRUCTIONS>
        1. Assuming an event has led to harm, explain whether "Point needle away from yourself and others" reduces the harm caused by this event.
        2. Answer True if it does and False if it does not.
        </EXAMPLE INSTRUCTIONS>

        <EXAMPLE OUTPUT>
        1. Mitigation Explanation: Assuming that an event like a needle-stick injury has occurred, "Point needle away from yourself and others" would not reduce the harm caused; this is a preventative measure to reduce the likelihood of the event.
        2. Answer: False
        </EXAMPLE OUTPUT>
        
        <EXAMPLE INSTRUCTIONS>
        1. Assuming an event has led to harm, explain whether "Landing on one foot" reduces the harm caused by this event.
        2. Answer True if it does and False if it does not.
        </EXAMPLE INSTRUCTIONS>

        <EXAMPLE OUTPUT>
        1. Mitigation Explanation: Assuming an event such as a fall has occurred, "Landing on one foot" does not reduce the harm caused by the event; it instead exacerbates the harm caused.
        2. Answer: False
        '''

    def generate_prompt(self):
        return f'''
        {self.return_few_shot_examples()}

        <INSTRUCTIONS>
        1. Assuming an event has led to harm, explain whether "{self.mitigation}" reduces the harm caused by this event.
        2. Answer True if it does and False if it does not.
        </INSTRUCTIONS>

        <OUTPUT FORMAT>
        Use the following output format:
        Mitigation Explanation: <your explanation>
        Overall Answer: <True OR False>
        </OUTPUT FORMAT>

        <OUTPUT>
        1. Mitigation Explanation: '''