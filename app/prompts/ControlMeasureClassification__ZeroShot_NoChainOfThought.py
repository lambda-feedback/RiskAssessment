from ..prompts.BasePromptInput import BasePromptInput

class ControlMeasureClassification__ZeroShot_NoChainOfThought(BasePromptInput):
    def __init__(self, control_measure, activity, hazard, how_it_harms, who_it_harms):
        super().__init__()
        self.control_measure = control_measure
        self.activity = activity
        self.hazard = hazard
        self.how_it_harms = how_it_harms
        self.who_it_harms = who_it_harms
        self.max_tokens = 400

        self.pattern_matching_method = 'check_string_for_prevention_mitigation_or_neither'
        self.candidate_labels = ['prevention', 'mitigation', 'neither', 'both']
        self.labels_indicating_correct_input = ['prevention', 'both']
    
    def generate_prompt(self, hazard_event, harm_caused):

        # TODO: Should alter the mitigation explanations - sometimes a mitigation measure is done to prepare for 
        # the hazard event, not just to reduce the harm caused by the hazard event.

        return f'''
        <CONTEXT>
        You are a Risk Assessment expert responsible for giving feedback on Risk Assessment inputs.
        </CONTEXT>

        <STYLE>
        Follow the writing style of a secondary school teacher.
        </STYLE>

        <TONE>
        Use a formal tone in your outputs.
        </TONE>

        <AUDIENCE>
        Your audience is a student who is learning how to write a risk assessment.
        </AUDIENCE>

        <EXAMPLE OUTPUT>
        Hazard Description: <description>

        Hazard Event: <hazard event>

        Harm Caused: <harm caused>

        Prevention Explanation: <explanation>

        Mitigation Explanation: <explanation>

        Answer: Mitigation
        </EXAMPLE OUTPUT>

        <EXAMPLE OUTPUT>
        Hazard Description: <description>

        Hazard Event: <hazard event>

        Harm Caused: <harm caused>

        Prevention Explanation: <explanation>

        Mitigation Explanation: <explanation>

        Answer: Prevention
        </EXAMPLE OUTPUT>

        <EXAMPLE OUTPUT>
        Hazard Description: <description>

        Hazard Event: <hazard event>

        Harm Caused: <harm caused>

        Prevention Explanation: <explanation>

        Mitigation Explanation: <explanation>

        Answer: Both
        </EXAMPLE OUTPUT>

        <EXAMPLE OUTPUT>
        Hazard Description: <description>

        Hazard Event: <hazard event>

        Harm Caused: <harm caused>

        Prevention Explanation: <explanation>

        Mitigation Explanation: <explanation>

        Answer: Neither
        </EXAMPLE OUTPUT>

        <INSTRUCTIONS>
        Follow these instructions:
        1. In one sentence, describe the hazard given the hazard event: "{hazard_event}" during the
        activity: "{self.activity}" given the harm caused: "{harm_caused}" for {self.who_it_harms}.
        2. Write the hazard event: "{hazard_event}"
        3. Write the harm caused: "{harm_caused}"
        4. State whether "{self.control_measure}" reduces the likelihood that the hazard event: "{hazard_event}" occurs.
        If so, it is a prevention measure.
        5. State whether or not "{self.control_measure}" removes or reduces the harm caused: "{harm_caused}" for the "{self.who_it_harms}".
        If so, it is a mitigation measure.
        6. If it is a prevention measure, answer 'Prevention'. If it is a mitigation meausure, answer 'Mitigation'.
        If it is neither a prevention measure nor a mitigation measure, answer 'Neither'. If it is both a
        prevention measure and a mitigation measure, answer 'Both'.
        </INSTRUCTIONS>

        <OUTPUT FORMAT>
        Use the following output format:
        Hazard Description: <your hazard event description>
        Hazard Event: <hazard event>
        Harm Caused: <harm caused>
        Prevention Explanation: <your prevention explanation>
        Mitigation Explanation: <your mitigation explanation>
        Answer: <your_answer>
        </OUTPUT FORMAT>
        
        <OUTPUT>
        Hazard Description: '''