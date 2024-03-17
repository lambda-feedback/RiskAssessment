from PromptInputs import PromptInput

class OldMitigation(PromptInput):
    def __init__(self, mitigation, activity, hazard, how_it_harms, who_it_harms):
        super().__init__()
        self.mitigation = mitigation
        self.activity = activity
        self.hazard = hazard
        self.how_it_harms = how_it_harms
        self.who_it_harms = who_it_harms

        self.pattern_matching_method = 'check_string_for_prevention_mitigation_or_neither'
        self.candidate_labels = ['prevention', 'mitigation', 'neither', 'both']
        self.labels_indicating_correct_input = ['mitigation', 'both']

    def get_field_checked(self):
        return 'Mitigation'

    def get_question(self):
        return f'''Will the mitigation measure: '{self.mitigation}' reduce the severity of the
        'hazard': '{self.hazard}' occurring during the 'activity': {self.activity}, given
        given how the hazard harms: '{self.how_it_harms}' and who/what the hazard harms: '{self.who_it_harms}?'''
    
    def generate_prompt_without_few_shot_examples(self):
        
        return f'''Follow these instructions:
        1. In one sentence, describe the hazard: '{self.hazard}' during the 
        activity: '{self.activity}' given how the hazard harms: '{self.how_it_harms}'
        and who the hazard harms: '{self.who_it_harms}'.
        2. In one sentence, explain why {self.how_it_harms} is a way that this hazard can cause harm.
        3. Thinking step by step, explain whether or not '{self.mitigation}' reduces the likelihood that the hazard event occurs.
        If so, it is a prevention measure.
        4. Assuming the hazard event occurs, explain whether or not '{self.mitigation}' removes or reduces the harm caused by the event.
        If so, it is a mitigation measure.
        5. If it is a prevention measure, answer 'Prevention'. If it is a migitation meausure, answer 'Mitigation'. 
        If it is neither a prevention measure nor a mitigation measure, answer 'Neither'. If it is both a 
        prevention measure and a mitigation measure, answer 'Both'.'''
    
    def generate_prompt(self):

        example_of_correct_mitigation_where_mitigation_reduces_harm_after_hazard_event_has_occurred = f'''
        Example Input:
        Follow these instructions:
        1. In one sentence, describe the hazard: 'Ink spillage' during the
        activity: 'Fluids laboratory' given how the hazard harms: 'Serious eye damage'
        and who the hazard harms: 'Students'.
        2. In one sentence, explain why "Serious eye damage" is a way that this hazard can cause harm.
        3. Explain whether or not 'First aid' reduces the likelihood that the hazard causes harm.
        If so, it is a prevention measure.
        4. Assuming the hazard described above does harm someone, explain whether or not 'First aid' reduces the harm. 
        If so, it is a mitigation measure.
        5. If it is a prevention measure, answer 'Prevention'. If it is a migitation meausure, answer 'Mitigation'.
        If it is neither a prevention measure nor a mitigation measure, answer 'Neither'. If it is both a        
        prevention measure and a mitigation measure, answer 'Both'.

        Output: 
        Description: The hazard of 'Ink spillage' during the activity 'Fluids laboratory' can lead to serious eye damage to students.
        How it Harms Explanation: 'Serious eye damage' is a way that this hazard causes harm because if ink comes into contact with the eyes, it can cause serious damage.
        Prevention Explanation: First aid will not reduce the likelihood of an ink spillage causing harm and it is a reactive step taken after the ink spillage; it therefore does not reduce the likelihood that the hazard causes harm and is not a prevention measure.
        Mitigation Explanation: If an ink spillage has led to serious eye damagen, first aid will help to wash the ink out of the eyes and reduce eye damage; as it reduces the harm, it is therefore a mitigation measure.
        Answer: Mitigation.'''

        example_of_mitigation_which_reduces_harm_when_hazard_event_is_occurring = '''
        Example Input:
        Follow these instructions:
        1. In one sentence, describe the hazard: 'Horse kicks out' during the
        activity: 'Mucking out a horse' given how the hazard harms: 'Impact injury'
        and who the hazard harms: 'Horse rider'.
        2. In one sentence, explain why "Impact injury" is a way that this hazard can cause harm.
        3. Explain whether or not 'Wear a helmet and body protector' reduces the likelihood that the hazard causes harm.
        If so, it is a prevention measure.
        4. Assuming the hazard described above does harm someone, explain whether or not 'Wear a helmet and body protector' reduces the harm.
        If so, it is a mitigation measure.
        5. If it is a prevention measure, answer 'Prevention'. If it is a migitation meausure, answer 'Mitigation'.
        If it is neither a prevention measure nor a mitigation measure, answer 'Neither'. If it is both a        
        prevention measure and a mitigation measure, answer 'Both'.
        
        Output:
        Description: The hazard of 'Horse kicks out' during the activity 'Mucking out a horse' can lead to impact injury to the horse rider.
        How it Harms Explanation: When a horse kicks out during mucking out, it can cause harm through impact injury, as the force of the kick can lead to bruises, fractures, or other injuries.
        Prevention Explanation: Wearing a helmet and body protector does not reduce the likelihood that the horse will kick and is therefore not a prevention measure.
        Mitigation Explanation: If a horse kicks the horse rider, wearing a helmet and body protector provides a protective barrier between the horse's kick and the person, hence reducing the impact injury caused by the horse's kick; as it reduces the harm, it is therefore a mitigation measure.
        Answer: Mitigation.
        '''
        example_of_prevention = f'''
        Example Input:
        Follow these instructions:
        1. In one sentence, describe the hazard: 'Tripping over personal belongings' during the
        activity: 'Fluids laboratory' given how the hazard harms: 'Tripping can cause physical harm.'
        and who the hazard harms: 'Students'.
        2. In one sentence, explain why "Tripping can cause physical harm." is a way that this hazard can cause harm.
        3. Explain whether or not 'Take care when walking around' reduces the likelihood that the hazard causes harm.
        If so, it is a prevention measure.
        4. Assuming the hazard described above does harm someone, explain whether or not 'Take care when walking around' reduces the harm.
        If so, it is a mitigation measure.
        5. If it is a prevention measure, answer 'Prevention'. If it is a migitation meausure, answer 'Mitigation'.
        If it is neither a prevention measure nor a mitigation measure, answer 'Neither'. If it is both a        
        prevention measure and a mitigation measure, answer 'Both'.

        Output:
        Description: The hazard of 'Tripping over personal belongings' during the activity 'Fluids laboratory' can lead to physical harm to students.
        How it Harms Explanation: Tripping can cause physical harm because it can result in falls, which can lead to injuries such as bruises, sprains, or fractures.
        Prevention Explanation: 'Take care when walking around' encourages students to be cautions and aware of their surroundings, making it less likely they will trip so it is a prevention measure.
        Mitigation Explanation: If a student has tripped over personal belongings, whether or not they were taking care when walking around will not affect how much harm the trip; as it does not reduce harm, it is therefore not a mitigation measure.
        Answer: Prevention.'''

        return f'''
        {example_of_correct_mitigation_where_mitigation_reduces_harm_after_hazard_event_has_occurred}

        {example_of_mitigation_which_reduces_harm_when_hazard_event_is_occurring}

        {example_of_prevention}
        
        {self.generate_prompt_without_few_shot_examples()}

        Use the following output format:
        Description: <your description>
        How it Harms Explanation: <your how it harms explanation>
        Prevention Explanation: <your prevention explanation>
        Mitigation Explanation: <your mitigation explanation>
        Answer: <your answer>'''

class OnlyPrevention(PromptInput):
    def __init__(self, control_measure, activity, hazard, how_it_harms, who_it_harms):
        super().__init__()
        self.control_measure = control_measure
        self.activity = activity
        self.hazard = hazard
        self.how_it_harms = how_it_harms
        self.who_it_harms = who_it_harms

    def generate_prompt_without_few_shot_examples(self):
        return f'''Follow these instructions:
        1. In one sentence, describe the event that leads to harm: <hazard event> during the
        activity: '{self.activity}' given the harm caused: <harm caused> for {self.who_it_harms}.
        2. Thinking step by step, explain whether or not '{self.control_measure}' reduces the likelihood that <hazard event> occurs.
        If so, answer True'''
    
    def generate_prompt(self, hazard_event, harm_caused):
        few_shot_examples = """
        <EXAMPLE INSTRUCTIONS>
        Follow these instructions:
        1. In one sentence, describe the event that leads to harm: "Water being spilt on the floor causing students to slip' during the
        activity: 'Fluids laboratory' given the harm caused: 'Impact injuries' for Students.
        2. Thinking step by step, explain whether or not 'Do not move the water tank when it is full' reduces the likelihood that the event: "Water being spilt on the floor causing students to slip' occurs.
        If so, answer True
        </EXAMPLE INSTRUCTIONS>

        <EXAMPLE OUTPUT>
        Hazard Description: The hazard of 'Water being spilt on the floor causing students to slip' during the activity 'Fluids laboratory' can lead to impact injuries.
        Prevention Explanation: 'Keeping the water tank stationary when it's full' means water cannot be spilled on to the floor by moving the water tank; no water on the floor reduces the likelihood of the student slipping; since it reduces the likelihood of the hazard, it is a prevention measure.
        Answer: True
        </EXAMPLE OUTPUT>

        <EXAMPLE INSTRUCTIONS>
        Follow these instructions:
        1. In one sentence, describe the event that leads to harm: 'Cut Zip tie flies and hits audience member' during the
        activity: 'Using a spring contraption as a demonstration for a TPS presentation' given the harm caused: 'Impact injuries' for Audience.   
        2. Thinking step by step, explain whether or not 'Keep hand around zip tie when cutting to stop it from flying' reduces the likelihood that the event: 'Cut Zip tie flies and hits audience member' occurs.
        If so, answer True
        </EXAMPLE INSTRUCTIONS>

        <EXAMPLE OUTPUT>
        Hazard Description: The hazard of 'Cut Zip tie flies and hits audience member' during the activity 'Using a spring contraption as a demonstration for a TPS presentation' can lead to impact injuries.
        Prevention Explanation: 'Keeping hand around zip tie when cutting to stop it from flying' will stop the zip tie from flying and therefore stop the hazard from occurring. Therefore, the likelihood of the hazard occurring has been reduced to zero; since the likelihood has been reduced, it is therefore a prevention measure.
        Answer: True
        </EXAMPLE OUTPUT>

        <EXAMPLE INSTRUCTIONS>
        Follow these instructions:
        1. In one sentence, describe the event that leads to harm: 'Ink spillage on student's face' during the
        activity: 'Fluids laboratory' given the harm caused: 'Series eye damage' for Students.
        2. Thinking step by step, explain whether or not 'Wash your eyes with clean water' reduces the likelihood that the event: 'Ink spillage on student's face' occurs. 
        If so, answer True
        </EXAMPLE INSTRUCTIONS>

        <EXAMPLE OUTPUT>
        Hazard Description: The hazard of 'Ink spillage on student's face' during the activity 'Fluids laboratory' can lead to serious eye damage to students.
        Prevention Explanation: 'First aid' is a reactive measure applied after the hazard of 'Ink spillage on student's face'; it therefore does not reduce the likelihood of the hazard and is not a prevention measure.
        Answer: False
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
        Use a formal tone.
        </TONE>

        <AUDIENCE>
        Your audience is a student who is learning how to write a risk assessment.
        </AUDIENCE>

        <EXAMPLES>
        {few_shot_examples}
        </EXAMPLES>

        <INSTRUCTIONS>
        Follow these instructions:
        1. In one sentence, describe the event that leads to harm: '{hazard_event}' during the
        activity: '{self.activity}' given the harm caused: '{harm_caused}' for {self.who_it_harms}.
        2. Thinking step by step, explain whether or not '{self.control_measure}' reduces the likelihood that '{hazard_event}' occurs.
        If so, answer True
        </INSTRUCTIONS>

        <OUTPUT FORMAT>
        Use the following output format:
        Hazard Description: <your hazard description>
        Prevention Explanation: <your explanation>
        Overall Answer: <your answer>
        </OUTPUT FORMAT>
        
        <OUTPUT>
        Hazard Description: '''
    
class OnlyMitigation(PromptInput):
    def __init__(self, control_measure, activity, hazard, how_it_harms, who_it_harms):
        super().__init__()
        self.control_measure = control_measure
        self.activity = activity
        self.hazard = hazard
        self.how_it_harms = how_it_harms
        self.who_it_harms = who_it_harms

    def generate_prompt_without_few_shot_examples(self):
        return f'''Follow these instructions:
        1. In one sentence, describe the event that leads to harm: <hazard event> during the
        activity: '{self.activity}' given the harm caused: <harm caused> for {self.who_it_harms}.
        2. Thinking step by step, assuming the event: '{hazard_event}' has occurred, explain whether or not '{self.control_measure}' removes or reduces the harm caused by <harm caused> for the '{self.who_it_harms}'.
        If so, answer True'''
    
    def generate_prompt(self, hazard_event, harm_caused):
        few_shot_examples = """
        <EXAMPLE INSTRUCTIONS>
        Follow these instructions:
        1. In one sentence, describe the event that leads to harm: "Water being spilt on the floor causing students to slip' during the
        activity: 'Fluids laboratory' given the harm caused: 'Impact injuries' for Students.
        2. Thinking step by step, assuming the event: '{hazard_event}' has occurred, explain whether or not 'Do not move the water tank when it is full' removes or reduces the harm caused by 'Impact injuries' for the 'Students'.
        If so, answer True
        </EXAMPLE INSTRUCTIONS>

        <EXAMPLE OUTPUT>
        Hazard Description: The hazard of 'Ink spillage on student's face' during the activity 'Fluids laboratory' can lead to serious eye damage to students.
        Mitigation Explanation: If water has been spilled on the floor, 'not moving the water tank when it is full' does not remove or reduce the harm caused by the hazard, as the water is already spilled to pose a slipping hazard; as it does not reduce the harm caused by the hazard, it is not a mitigation measure.
        Answer: False
        </EXAMPLE OUTPUT>

        <EXAMPLE INSTRUCTIONS>
        Follow these instructions:
        1. In one sentence, describe the event that leads to harm: 'Cut Zip tie flies and hits audience member' during the
        activity: 'Using a spring contraption as a demonstration for a TPS presentation' given the harm caused: 'Impact injuries' for Audience.   
        2. Thinking step by step, assuming the event: '{hazard_event}' has occurred, explain whether or not 'Keep hand around zip tie when cutting to stop it from flying' removes or reduces the harm caused by 'Impact injuries' for the 'Audience'.
        If so, answer True
        </EXAMPLE INSTRUCTIONS>

        <EXAMPLE OUTPUT>
        Hazard Description: The hazard of 'Cut Zip tie flies and hits audience member' during the activity 'Using a spring contraption as a demonstration for a TPS presentation' can lead to impact injuries.
        Mitigation Explanation: If the hazard occurs and the zip tie flies and hits an audience member, 'keeping hand around zip tie when cutting to stop it from flying' does not remove or reduce the impact injury caused by the hazard, as the zip tie has already flown and caused harm; it is therefore not a mitigation measure.
        Answer: False
        </EXAMPLE OUTPUT>

        <EXAMPLE INSTRUCTIONS>
        Follow these instructions:
        1. In one sentence, describe the event that leads to harm: 'Ink spillage on student's face' during the
        activity: 'Fluids laboratory' given the harm caused: 'Series eye damage' for Students.
        2. Thinking step by step, assuming the event: '{hazard_event}' has occurred, explain whether or not 'Wash your eyes with clean water' removes or reduces the harm caused by 'Serious eye damage' for the 'Students'.
        If so, answer True
        </EXAMPLE INSTRUCTIONS>

        <EXAMPLE OUTPUT>
        Hazard Description: The hazard of 'Ink spillage on student's face' during the activity 'Fluids laboratory' can lead to serious eye damage to students.
        Mitigation Explanation: If ink has been spilled onto a student's face, 'first aid' will help to wash the ink out of the eyes and reduce eye damage after the hazard has occurred; as it reduces the harm caused by the hazard, it is therefore a mitigation measure.
        Answer: True
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
        Use a formal tone.
        </TONE>

        <AUDIENCE>
        Your audience is a student who is learning how to write a risk assessment.
        </AUDIENCE>

        <EXAMPLES>
        {few_shot_examples}
        </EXAMPLES>

        <INSTRUCTIONS>
        Follow these instructions:
        1. In one sentence, describe the event that leads to harm: '{hazard_event}' during the
        activity: '{self.activity}' given the harm caused: '{harm_caused}' for {self.who_it_harms}.
        2. Thinking step by step, assuming the event: '{hazard_event}' has occurred, explain whether or not '{self.control_measure}' removes or reduces the harm caused by {harm_caused} for the '{self.who_it_harms}'.
        If so, answer True
        </INSTRUCTIONS>

        <OUTPUT FORMAT>
        Use the following output format:
        Hazard Description: <your hazard description>
        Mitigation Explanation: <your explanation>
        Overall Answer: <your answer>
        </OUTPUT FORMAT>
        
        <OUTPUT>
        Hazard Description: '''