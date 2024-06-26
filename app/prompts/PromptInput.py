try:
    from utils.RegexPatternMatcher import RegexPatternMatcher
except:
    from ..utils.RegexPatternMatcher import RegexPatternMatcher

class PromptInput:
    def __init__(self):
        self.pattern_matching_method = 'check_string_for_true_or_false'
        self.candidate_labels = [True, False]
        self.labels_indicating_correct_input = [True]

    def get_field_checked(self):
        pass

    def generate_prompt(self):
        pass

    def get_shortform_feedback(self):
        pass

    # Using regular expressions, extracts the relevant information from the prompt output.
    def get_longform_feedback(self, prompt_output):
        pass

    def to_string(self):
        class_name = self.__class__.__name__
        if hasattr(self, '__dict__'):
            attributes = ', '.join([f"{key}={value}" for key, value in self.__dict__.items()])
            return f"{class_name}({attributes})"
        else:
            return f"{class_name}()"


class ControlMeasureClassification__ZeroShot_ChainOfThought(PromptInput):
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
        4. Thinking step by step, explain whether or not "{self.control_measure}" reduces the likelihood that the hazard event: "{hazard_event}" occurs.
        If so, it is a prevention measure.
        5. Thinking step by step, explain whether or not "{self.control_measure}" removes or reduces the harm caused: "{harm_caused}" for the "{self.who_it_harms}".
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
        Answer: <Prevention OR Mitigation OR Both OR Neither>
        </OUTPUT FORMAT>
        
        <OUTPUT>
        Hazard Description: '''
    
class ControlMeasureClassification__ZeroShot_NoChainOfThought(PromptInput):
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
    
class ControlMeasureClassification__FewShot_NoChainOfThought(PromptInput):
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

        all_few_shot_examples = """
        <EXAMPLE INSTRUCTIONS>
        1. In one sentence, describe the hazard given the hazard event: "Ink spillage" during the
        activity: 'Fluids laboratory' given the harm caused: "Serious eye damage" for Students.
        2. Write the Hazard Event: "Ink spillage"
        3. Write the Harm Caused: "Serious eye damage".
        4. State whether or not 'Cleaning the eyes out with water' reduces the likelihood that the hazard event: "Ink spillage" occurs.
        If so, it is a prevention measure.
        5. State whether or not 'Cleaning the eyes out with water' removes or reduces the harm caused: "Serious eye damage" for the 'Students'.
        If so, it is a mitigation measure.
        6. If it is a prevention measure, answer 'Prevention'. If it is a mitigation meausure, answer 'Mitigation'.
        If it is neither a prevention measure nor a mitigation measure, answer 'Neither'. If it is both a
        prevention measure and a mitigation measure, answer 'Both'.
        </EXAMPLE INSTRUCTIONS>

        <EXAMPLE OUTPUT>
        Hazard Description: During a fluids laboratory, ink spillage on a student's face causes serious eye damage.

        Prevention Statement:
        - Cleaning the eyes with water does not reduce the likelihood of ink spillage on a student's face.
        - Therefore, cleaning the eyes with water is not a prevention measure.

        Mitigation Statement:
        - Cleaning the eyes with water can reduce the severity of the eye damage caused by an ink spillage on a student's face.
        - Therefore, cleaning the eyes with water is a mitigation measure.

        Answer: Mitigation
        </EXAMPLE OUTPUT>

        <EXAMPLE INSTRUCTIONS>
        1. In one sentence, describe the hazard given the hazard event: "Student slips on water" during the
        activity: 'Fluids laboratory' given the harm caused: "Injury caused by students slipping" for Students.
        2. Write the Hazard Event: "Student slips on water"
        3. Write the Harm Caused: "Injury caused by students slipping".
        4. State whether or not 'Keeping the water tank stationary when it's full' reduces the likelihood that hazard event: "Student slips on water" occurs.
        If so, it is a prevention measure.
        5. State whether or not 'Keeping the water tank stationary when it's full' removes or reduces the harm caused: "Injury caused by students slipping" for the 'Students'.
        If so, it is a mitigation measure.
        6. If it is a prevention measure, answer 'Prevention'. If it is a mitigation meausure, answer 'Mitigation'.
        If it is neither a prevention measure nor a mitigation measure, answer 'Neither'. If it is both a
        prevention measure and a mitigation measure, answer 'Both'.
        </EXAMPLE INSTRUCTIONS>

        <EXAMPLE OUTPUT>
        Hazard Description: During a fluids laboratory, water spills on the floor, causing students to slip and suffer injuries
        Hazard Event: Student slips on water
        Harm Caused: Injury caused by students slipping

        Prevention Explanation:
        - Keeping the water tank stationary when it's full reduces the likelihood of students slipping on the wet floor.
        - Therefore, keeping the water tank stationary when it's full is a prevention measure.

        Mitigation Explanation:
        - Keeping the water tank stationary when it's full does not remove or reduce the harm caused by the "Injury caused by students slipping". 
        - Therefore, keeping the water tank stationary when it's full is not a mitigation measure.

        Answer: Prevention
        </EXAMPLE OUTPUT>

        <EXAMPLE INSTRUCTIONS>
        1. In one sentence, describe the hazard given the hazard event: "Car crashes into the cyclist" during the
        activity: 'Cycle commuting' given the harm caused: "Head injury" for Cyclist.
        2. Write the Hazard Event: "Car crashes into the cyclist"
        3. Write the Harm Caused: "Head injury".
        4. State whether or not 'Wear a helmet' reduces the likelihood that hazard event: "Car crashes into the cyclist" occurs.
        If so, it is a prevention measure.
        5. State whether or not 'Wear a helmet' removes or reduces the harm caused: "Head injury" for the 'Cyclist'.
        If so, it is a mitigation measure.
        6. If it is a prevention measure, answer 'Prevention'. If it is a mitigation meausure, answer 'Mitigation'.   
        If it is neither a prevention measure nor a mitigation measure, answer 'Neither'. If it is both a
        prevention measure and a mitigation measure, answer 'Both'.
        </EXAMPLE INSTRUCTIONS>

        <EXAMPLE OUTPUT>
        Hazard Description: A cyclist commuting to work gets hit by a car, resulting in a head injury.
        Hazard Event: Car crashes into the cyclist
        Harm Caused: Head injury

        Prevention Explanation: 
        - Wearing a helmet does not reduce likelihood of a cyclist getting hit by a car.
        - Therefore, wearing a helmet is not a prevention measure.
        
        Mitigation Explanation: 
        - Wearing a helmet can lessen the severity of a head injury caused by a cyclist getting hit by a car.
        - Therefore, wearing a helmet is a mitigation measure.
        
        Answer: Mitigation
        </EXAMPLE OUTPUT>

        <EXAMPLE INSTRUCTIONS>
        1. In one sentence, describe the hazard given the hazard event: "Zip tie projectile hits audience member" during the
        activity: 'Fluids laboratory' given the harm caused: "Impact injury" for Students.
        2. Write the Hazard Event: "Zip tie projectile hits audience member"
        3. Write the Harm Caused: "Impact injury".
        4. State whether or not 'Keeping hand around zip tie when cutting to stop it from flying' reduces the likelihood that hazard event: "Zip tie projectile hits audience member" occurs.
        If so, it is a prevention measure.
        5. State whether or not 'Keeping hand around zip tie when cutting to stop it from flying' removes or reduces the harm caused: "Impact injury" for the 'Students'.
        If so, it is a mitigation measure.
        6. If it is a prevention measure, answer 'Prevention'. If it is a mitigation meausure, answer 'Mitigation'.
        If it is neither a prevention measure nor a mitigation measure, answer 'Neither'. If it is both a
        prevention measure and a mitigation measure, answer 'Both'.
        </EXAMPLE INSTRUCTIONS>

        <EXAMPLE OUTPUT>
        Hazard Description: During a fluids laboratory, a cut zip tie flies and hits a student audience member, causing an impact injury.
        Hazard Event: Zip tie projectile hits audience member
        Harm Caused: Impact injury

        Prevention Explanation: 
        - Keeping a hand around the zip tie while cutting it can reduce the likelihood of the zip tie flying and hitting an audience member.
        - Therefore, keeping a hand around the zip tie when cutting it is a prevention measure.
        
        Mitigation Explanation: 
        - If a cut zip tie were to fly and hit a student, keeping a hand around it during cutting would not reduce the severity of the "Impact injury".
        - Therefore, keeping a hand around the zip tie when cutting is not a mitigation measure.
        
        Answer: Prevention
        </EXAMPLE OUTPUT>
        """

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

        {all_few_shot_examples}

        <INSTRUCTIONS>
        Follow these instructions:
        1. In one sentence, describe the hazard given the hazard event: "{hazard_event}" during the
        activity: "{self.activity}" given the harm caused: "{harm_caused}" for {self.who_it_harms}.
        2. Write the hazard event: "{hazard_event}"
        3. Write the harm caused: "{harm_caused}"
        4. State whether or not "{self.control_measure}" reduces the likelihood that the hazard event: "{hazard_event}" occurs.
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
        Prevention Statement: <your prevention statement>
        Mitigation Statement: <your mitigation statement>
        Answer: <your answer>
        </OUTPUT FORMAT>
        
        <OUTPUT>
        Hazard Description: '''

class SummarizeControlMeasureFeedback(PromptInput):
    def __init__(self):

        self.candidate_labels = [True, False]
        self.pattern_matching_method = 'always_return_true'
        self.max_tokens = 300

    def get_context_style_tone_audience(self):
        return """<CONTEXT>
        You are a Risk Assessment expert responsible for summarizing feedback on Risk Assessment inputs.
        </CONTEXT>

        <STYLE>
        Follow the writing style of a secondary school teacher.
        </STYLE>

        <TONE>
        Use a formal tone in your outputs.
        </TONE>

        <AUDIENCE>
        Your audience is a student who is learning how to write a risk assessment.
        </AUDIENCE>"""
        
    def get_instructions(self, control_measure_type, feedback):
        return f"""<INSTRUCTIONS>
        Summarize the {control_measure_type} feedback: "{feedback}" in the following format:
        - In 2 sentences, provide an explanation as to why the control measure is or is not a {control_measure_type}. 
        - In one sentence, provide a statement of whether or not control measure is {control_measure_type} measure.
        Start the summary immediately after these instructions.
        </INSTRUCTIONS>"""
    
    def get_example(self, control_measure_type):
        if control_measure_type == 'prevention':
            return f"""<EXAMPLE INPUT>
            Thinking step by step:
            - Enhancing explosive detection capabilities, such as deploying advanced screening equipment or trained explosive detection canine units, increases the chances of identifying and intercepting explosives before they can be detonated.
            - By detecting and preventing explosives from entering the event premises, the likelihood of an explosive terrorist attack occurring is significantly reduced.
            - Therefore, enhancing explosive detection capabilities directly reduces the likelihood of the hazard event "Explosive terrorist attack during public gatherings or events" from occurring. It is a prevention measure.
            </EXAMPLE INPUT>

            <EXAMPLE OUTPUT>
            Enhancing explosive detection capabilities, such as deploying advanced screening equipment or trained explosive detection canine units allows for the detection and prevention of explosives from entering the event premises.
            Thus, the likelihood of an explosive terrorist attack occurring is significantly reduced. Hence, enhancing explosive detection capabilities is a prevention measure.
            </EXAMPLE OUTPUT>"""
        
        if control_measure_type == 'mitigation':
            return '''<EXAMPLE INPUT>
            Thinking step by step:
            - Loud noises can cause hearing damage, especially at close range and with prolonged exposure.
            - By increasing the distance between the trombone player and the audience, the intensity of the sound reaching the audience is reduced.
            - This reduced sound intensity can help reduce hearing damage caused by the loud noise.
            - Therefore, keeping a space between the player and audience removes or reduces the harm caused by "Hearing damage" for everyone present. It is a mitigation measure.
            </EXAMPLE INPUT>

            <EXAMPLE OUTPUT>
            Increasing the distance between the trombone player and the audience reduces the intensity of the sound reaching the audience.
            This helps reduce potential hearing damage from the loud noise. Hence, increasing distance between the trombone player and the audience is a mitigation measure.
            </EXAMPLE OUTPUT>'''

    def generate_prompt(self, control_measure_type, feedback):
        return f'''
        {self.get_context_style_tone_audience()}

        {self.get_example(control_measure_type=control_measure_type)}

        {self.get_instructions(control_measure_type=control_measure_type, feedback=feedback)}'''

class PreventionClassification(PromptInput):
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
    
class MitigationClassification(PromptInput):
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