try:
    from RegexPatternMatcher import RegexPatternMatcher
except:
    from .RegexPatternMatcher import RegexPatternMatcher

class PromptInput:
    def __init__(self):
        self.activity_definition = """an action or process that involves physical or mental effort."""

        self.hazard_definition = """a dangerous phenomenon, object, human activity or condition. 
        It may cause loss of life, injury or other health impacts, property damage, loss of livelihoods 
        and services, social and economic disruption, or environmental damage."""

        self.how_it_harms_entry_definition = """
        the potential negative consequences of a hazard. It can outline the specific impacts on
        human health, property, environment, economics, social structures, livelihoods, essential 
        services, and the risk of loss of life. It must be specific, clear and precise."""

        self.who_it_harms_entry_definition = """
        specific individuals, groups, environmental components or infrastructure
        likely to be negatively affected by identified risks, 
        excluding abstract concepts, generic terms or vague terms."""

        self.prevention_definition = f'an action which directly reduces the probability that the hazard occurs.'

        # TODO: I changed the definition of mitigation. See if this has an effect.
        self.mitigation_definition = f'''an action which directly reduces the harm caused by a hazard occurring
        or reduces the harm caused by the hazard after it has occurred.''' 

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
        
class NoInformationProvided(PromptInput):
    def __init__(self, input: str):
        super().__init__()
        self.pattern_matching_method = 'check_string_for_no_information_provided'
        self.candidate_labels = ['control measure', 'no information provided']
        self.input = input
    
    def generate_prompt(self):
        return f'''
        <s> [INST]

        Follow these instructions:
        1. Classify the following input as either "No information provided" or "Control measure"

        <EXAMPLES>
        Input: "N/A" 
        Answer: No information provided

        Input: "Not Applicable" 
        Answer: No information provided

        Input: "Unknown" 
        Answer: No information provided

        Input: "None" 
        Answer: No information provided

        Input: "TBD" 
        Answer: No information provided

        Input: "To Be Determined" 
        Answer: No information provided

        Input: "Unspecified" 
        Answer: No information provided

        Input: "No Information Available" 
        Answer: No information provided

        Input: "Do Not Know" 
        Answer: No information provided

        Input: "Not specified" 
        Answer: No information provided

        Input: "Unavailable" 
        Answer: No information provided

        Input: "Not applicable" 
        Answer: No information provided

        Input: "Not known" 
        Answer: No information provided

        Input: "Wear helmet"
        Answer: Control measure

        Input: "Take care"
        Answer: Control measure

        Input: "Apply ice"
        Answer: Control measure
        </EXAMPLES>

        <OUTPUT FORMAT>
        Use the following output format:
        Answer: <your answer>
        </OUTPUT FORMAT>

        [/INST]
 
        Input: "{self.input}"'''

class Activity(PromptInput):
    def __init__(self, activity: str):
        super().__init__()
        self.activity = activity

    def get_field_checked(self):
        return 'Activity'
    
        # If "Golf" is an example of an activity, answer True, else answer False.

        # Use the following output format:
        # Overall Answer: <your answer>
    
    def generate_prompt(self):
        return f'''
        If the input is an example of an activity, answer True, else answer False.

        If "{self.activity}" is an example of an activity, answer True, else answer False.

        Use the following output format:
        Overall Answer: <your answer>'''
    
    def get_shortform_feedback(self, feedback_type):
        if feedback_type == 'positive':
            return f"Correct! '{self.activity}' is an activity."
        if feedback_type == 'negative':
            return f"Incorrect. '{self.activity}' is not an activity."
    
    def get_longform_feedback(self, prompt_output=''):
        regex_pattern_matcher = RegexPatternMatcher()
        return ''

    def get_recommendation(self):
        return f'Enter an activity that aligns with the definition: {self.activity_definition}'

class HowItHarmsInContext(PromptInput):
    def __init__(self, how_it_harms, activity, hazard):
        super().__init__()
        self.how_it_harms = how_it_harms
        self.activity = activity
        self.hazard = hazard

    def get_field_checked(self):
        return 'Hazard & How It Harms'
    
    # TODO: Scope for adding a few shot example with an 'Add more detail' output.

    def generate_prompt_without_few_shot_examples(self):
        return f'''
        Follow these instructions:
        1. In one sentence, describe the hazard: '{self.hazard}' during the 
        activity: '{self.activity}'.
        2. In one sentence, explain whether or not '{self.how_it_harms}' is a way that this hazard causes harm. 
        3. If '{self.how_it_harms}' is a way that this hazard causes harm, answer True, else answer False.
        '''
    
    def generate_prompt(self):
        example_of_correct_how_it_harms = f'''
        Example Input:
        Follow these instructions:
        1. In one sentence, describe the hazard: 'Electrocution' during the 
        activity: 'Fluids laboratory'.
        2. In one sentence, explain whether or not 'Electrocuted by mains voltage' is a way that this hazard causes harm. 
        3. If 'Electrocuted by mains voltage' is a way that this hazard causes harm, answer True, else answer False.

        Output:
        Description: It is argued that wet hands during a fluids laboratory can cause harm through electrocution.
        Explanation: As water is a conductor of electricity, touching electronics with wet hands can cause electrocution as
        the water provides a path for electrical current to flow through the body.
        Overall Answer: True
        '''

        example_of_incorrect_how_it_harms = f'''
        Example Input:
        Follow these instructions:
        1. In one sentence, describe the hazard: 'Ink spillage' during the
        activity: 'Fluids laboratory'.
        2. In one sentence, explain whether or not 'Radiation exposure' is a way that this hazard causes harm.
        3. If 'Radiation exposure' is a way that this hazard causes harm, answer True, else answer False.

        Output:
        Description: It is argued that an ink spillage during a fluids laboratory can cause radiation exposure.
        Explanation: Radiation exposure is not a way that ink spillage during the fluids laboratory causes harm, 
        as the hazard primarily involves physical contamination rather than radiation.
        Overall Answer: False.
        '''
        return f'''
        {example_of_correct_how_it_harms}

        {example_of_incorrect_how_it_harms}

        {self.generate_prompt_without_few_shot_examples()}

        Use the following output format:
        Description: <your description>
        Explanation: <your Explanation>
        Overall Answer: <your answer>'''
    
    def get_shortform_feedback(self, feedback_type):
        if feedback_type == 'positive':
            return f"Correct! '{self.how_it_harms}' is a way that the hazard: '{self.hazard}' causes harm."
        if feedback_type == 'negative':
            return f"Incorrect. '{self.how_it_harms}' is not a way that the hazard: '{self.hazard}' causes harm."
    
    def get_longform_feedback(self, prompt_output=''):
        regex_pattern_matcher = RegexPatternMatcher()
        return regex_pattern_matcher.extract_section_of_prompt_until_new_line_or_end_of_string(prompt_output, 'Explanation')

    def get_recommendation(self):
        return f'For the "How it harms" input, enter how the hazard leads to harm, and the specific harm caused, e.g. an injury or illness.'

class WhoItHarmsInContext(PromptInput):
    def __init__(self, who_it_harms, activity):
        super().__init__()
        self.who_it_harms = who_it_harms
        self.activity = activity

    def get_field_checked(self):
        return 'Who It Harms'
    
    def generate_prompt(self):
        
        example_of_correct_who_it_harms = f'''
        Example Input:
        Follow these instructions:
        1. In one sentence, describe the activity: 'Mucking out stable'.
        2. In one sentence, explain whether it is possible that a 'Stable hand' take part in this activity. 
        3. If it is possible, answer True, else answer False.

        Output:
        Description: "Mucking out a stable" involves the process of cleaning and removing waste, such as manure and soiled bedding, from a horse's stall or stable.
        Explanation: It is highly likely that a "Stable hand" would take part in this activity as it is a core responsibility associated with their role in maintaining the stable environment.
        Overall Answer: True
        '''

        example_of_incorrect_who_it_harms = f'''
        Example Input:
        1. In one sentence, describe the activity: 'Fluids laboratory'.
        2. In one sentence, explain whether it is possible that a 'Stable hand' take part in this activity.
        3. If it is possible, answer True, else answer False.

        Output:
        Description: A "Fluids laboratory" is a facility where controlled experiments and analyses are conducted to study the properties and behaviors of various fluids, including liquids and gases.
        Explanation: It is highly unlikely that a "Stable hand" would take part in this activity, as their expertise typically lies in the care and maintenance of horses within a stable environment rather than laboratory work with fluids.
        Overall Answer: False
        '''
        return f'''
        {example_of_correct_who_it_harms}

        {example_of_incorrect_who_it_harms}

        Follow these instructions:
        1. In one sentence, describe the activity: '{self.activity}'.
        2. In one sentence, explain whether it is possible that {self.who_it_harms} take part in this activity.
        3. If it is possible, answer True, else answer False.

        Your answer should be in the format:
        Description: <your description>
        Explanation: your_explanation
        Overall Answer: <your answer>'''
    
    def get_shortform_feedback(self, feedback_type):
        if feedback_type == 'positive':
            return f"Correct! '{self.who_it_harms}' could take part in the activity: '{self.activity}'."
        if feedback_type == 'negative':
            return f"Incorrect. '{self.who_it_harms}' could not take part in the activity: '{self.activity}'."

    def get_longform_feedback(self, prompt_output=''):
        regex_pattern_matcher = RegexPatternMatcher()
        return regex_pattern_matcher.extract_section_of_prompt_until_new_line_or_end_of_string(prompt_output, 'Explanation')
    
    def get_recommendation(self):
        return f"For the 'Who it harms' field, please enter the individuals or group at risk of harm from the hazard"  

class HarmCausedAndHazardEvent(PromptInput):
    def __init__(self, activity, hazard, how_it_harms, prevention):
        super().__init__()
        self.activity = activity
        self.hazard = hazard
        self.how_it_harms = how_it_harms
        self.pattern_matching_method = 'extract_harm_caused_and_hazard_event'

    def generate_prompt_without_few_shot_examples(self):
        return f'''
        1. Describe the harm caused: '{self.how_it_harms}' by the hazard: '{self.hazard}' during the activity: '{self.activity}'.
        The harm caused by a hazard refers to the negative consequences resulting from the hazard event.
        2. From the above description, extract the harm caused.
        3. Describe the events which lead to the harm caused. Don't refer to the harm caused.
        '''

    def generate_prompt(self):

        return f'''

        <EXAMPLE INSTRUCTIONS>
        1. Describe the harm caused: 'Could injure' by the hazard: 'Getting hit' during the activity: 'Riding a Bike'.
        The harm caused by a hazard refers to the negative consequences resulting from the hazard event.
        2. From the above description, extract the harm caused.
        3. Describe the events which lead to the harm caused. Don't refer to the harm caused.
        </EXAMPLE INSTRUCTIONS>

        <EXAMPLE OUTPUT>
        Description: Riding a bike can lead to getting hit by a car, which could lead to an impact injury.
        Harm caused: Impact injury
        Event that leads to harm: Getting hit by a car while riding a bike
        </EXAMPLE OUTPUT>

        <EXAMPLE INSTRUCTIONS>
        1. Describe the harm caused: 'Mistakes by cyclists or motorists leading to crash' by the hazard: 'Head injury' during the activity: 'Cycle commuting'.
        The harm caused by a hazard refers to the negative consequences resulting from the events which leads to the harm caused.
        2. From the above description, extract the harm caused.
        3. Describe the events which leads to the harm caused. Don't refer to the harm caused.

        <EXAMPLE OUTPUT>
        Description: Cycle commuting can lead to mistakes by cyclists or motorists leading to a crash, which can cause a head injury.
        Harm caused: Head injury
        Event that leads to harm: Mistakes by cyclists or motorists leading to a crash
        </EXAMPLE OUTPUT>

        <INSTRUCTIONS>
        1. Describe the harm caused: '{self.how_it_harms}' by the hazard: '{self.hazard}' during the activity: '{self.activity}'.
        The harm caused by a hazard refers to the negative consequences resulting from the events which leads to the harm caused.
        2. From the above description, extract the harm caused.
        3. Describe the events which leads to the harm caused. Don't refer to the harm caused.
        </INSTRUCTIONS>

        <OUTPUT>'''
    
class RiskDomainClassification(PromptInput):
    def __init__(self, hazard, how_it_harms, who_it_harms):
        super().__init__()
        self.hazard = hazard
        self.how_it_harms = how_it_harms
        self.who_it_harms = who_it_harms

        self.pattern_matching_method = 'check_string_for_classification'
        self.candidate_labels = ['physical risk to individuals', 'environmental risk']

    # Other classes
        # - Terrist risk
        # - Accidental risk
        # - Biohazard risk
    
    def generate_prompt(self):
        return f'''
        Follow these instructions:
        1. Classify the following hazard: '{self.hazard}' given how it harms: '{self.how_it_harms}' and who it harms: '{self.who_it_harms}' into one of the following categories:
        - Physical risk to individuals
        - Environmental risk

        <EXAMPLE INSTRUCTIONS>
        Classify the following hazard: "Fire in a building" given how it harms: "Clothes catch on fire and cause a burn" and who it harms: "Building occupants" into one of the following categories:
        - Physical risk to individuals
        - Environmental risk
        </EXAMPLE INSTRUCTIONS>

        <EXAMPLE OUTPUT>
        Classification: Physical risk to individuals
        </EXAMPLE OUTPUT>

        <EXAMPLE INSTRUCTIONS>
        Classify the following hazard: "Volcanic eruption" given how it harms: "Volcanic eruptions can cause destruction of property, infrastructure, loss of life, and disruption of ecosystems" and who it harms: "Residents, infrastructure, and the environment" into one of the following categories:
        - Physical risk to individuals
        - Environmental risk
        </EXAMPLE INSTRUCTIONS>

        <EXAMPLE OUTPUT>
        Classification: Environmental risk
        </EXAMPLE OUTPUT>
        '''

class ControlMeasureClassification(PromptInput):
    def __init__(self, control_measure, activity, hazard, how_it_harms, who_it_harms):
        super().__init__()
        self.control_measure = control_measure
        self.activity = activity
        self.hazard = hazard
        self.how_it_harms = how_it_harms
        self.who_it_harms = who_it_harms

        self.pattern_matching_method = 'check_string_for_prevention_mitigation_or_neither'
        self.candidate_labels = ['prevention', 'mitigation', 'neither', 'both']
        self.labels_indicating_correct_input = ['prevention', 'both']
    
    def generate_prompt_without_few_shot_examples(self):

        return f'''Follow these instructions:
        1. In one sentence, describe the hazard event: "<hazard event>" during the
        activity: '{self.activity}' given the harm caused: "<harm caused>" for {self.who_it_harms}.
        2. Thinking step by stepand thinking through all possible causes of the hazard event: "<hazard_event>", explain whether or not '{self.control_measure}' reduces the likelihood that hazard event: "<hazard event>" occurs.
        If so, it is a prevention measure.
        3. Thinking step by step, explain whether or not '{self.control_measure}' removes or reduces the harm caused: "<harm caused>" for the '{self.who_it_harms}'.
        If so, it is a mitigation measure.
        4. If it is a prevention measure, answer 'Prevention'. If it is a migitation meausure, answer 'Mitigation'.
        If it is neither a prevention measure nor a mitigation measure, answer 'Neither'. If it is both a
        prevention measure and a mitigation measure, answer 'Both'.'''
    
    def generate_prompt(self, hazard_event, harm_caused):

        # TODO: Should alter the mitigation explanations - sometimes a mitigation measure is done to prepare for 
        # the hazard event, not just to reduce the harm caused by the hazard event.

        all_few_shot_examples = """
        <EXAMPLE INSTRUCTIONS>
        1. In one sentence, describe the hazard event: "Ink spillage on students face" during the
        activity: 'Fluids laboratory' given the harm caused: "Serious eye damage" for Students.
        2. Thinking step by step, explain whether or not 'Do not move the water tank when it is full' reduces the likelihood that hazard event: "Ink spillage on students face" occurs.
        If so, it is a prevention measure.
        3. Thinking step by step, explain whether or not 'Do not move the water tank when it is full' removes or reduces the harm caused: "Serious eye damage" for the 'Students'.
        If so, it is a mitigation measure.
        4. If it is a prevention measure, answer 'Prevention'. If it is a migitation meausure, answer 'Mitigation'.
        If it is neither a prevention measure nor a mitigation measure, answer 'Neither'. If it is both a
        prevention measure and a mitigation measure, answer 'Both'.
        </EXAMPLE INSTRUCTIONS>

        <EXAMPLE OUTPUT>
        Hazard Event Description: The hazard event of 'Ink spillage on student's face' during the activity 'Fluids laboratory' can lead to serious eye damage to students.
        Prevention Explanation: 'First aid' is a reactive measure applied after the hazard event of 'Ink spillage on student's face'; it therefore does not reduce the likelihood of the hazard event and is not a prevention measure.
        Mitigation Explanation: If ink has been spilled onto a student's face, 'first aid' will help to wash the ink out of the eyes and reduce eye damage after the hazard event has occurred; as it reduces the harm caused by the hazard event, it is therefore a mitigation measure.
        Answer: Mitigation.
        </EXAMPLE OUTPUT>

        <EXAMPLE INSTRUCTIONS>
        1. In one sentence, describe the hazard event: "Water being spilt on the floor causing students to slip" during the
        activity: 'Using a spring contraption as a demonstration for a TPS presentation' given the harm caused: "Impact injury" for Audience.
        2. Thinking step by step, explain whether or not 'Keep hand around zip tie when cutting to stop it from flying' reduces the likelihood that hazard event: "Water being spilt on the floor causing students to slip" occurs.
        If so, it is a prevention measure.
        3. Thinking step by step, explain whether or not 'Keep hand around zip tie when cutting to stop it from flying' removes or reduces the harm caused: "Impact injury" for the 'Audience'.
        If so, it is a mitigation measure.
        4. If it is a prevention measure, answer 'Prevention'. If it is a migitation meausure, answer 'Mitigation'.
        If it is neither a prevention measure nor a mitigation measure, answer 'Neither'. If it is both a
        prevention measure and a mitigation measure, answer 'Both'.
        </EXAMPLE INSTRUCTIONS>

        <EXAMPLE OUTPUT>
        Hazard Event Description: The hazard event of 'Water being spilt on the floor causing students to slip' during the activity 'Fluids laboratory' can lead to impact injuries.
        Prevention Explanation: 'Keeping the water tank stationary when it's full' means water cannot be spilled on to the floor by moving the water tank; no water on the floor reduces the likelihood of the hazard event of a student slipping; since it reduces the likelihood of the hazard event, it is a prevention measure.
        Mitigation Explanation: If water has been spilled on the floor, 'not moving the water tank when it is full' does not remove or reduce the harm caused by the hazard event, as the water is already spilled to pose a slipping hazard; as it does not reduce the harm caused by the hazard event, it is not a mitigation measure.
        Answer: Prevention.
        </EXAMPLE OUTPUT>

        <EXAMPLE INSTRUCTIONS>
        1. In one sentence, describe the hazard event: "Cut Zip tie flies and hits audience member" during the
        activity: 'Fluids laboratory' given the harm caused: "Impact injury" for Students.
        2. Thinking step by step, explain whether or not 'Wash your eyes with clean water' reduces the likelihood that hazard event: "Cut Zip tie flies and hits audience member" occurs.
        If so, it is a prevention measure.
        3. Thinking step by step, explain whether or not 'Wash your eyes with clean water' removes or reduces the harm caused: "Impact injury" for the 'Students'.
        If so, it is a mitigation measure.
        4. If it is a prevention measure, answer 'Prevention'. If it is a migitation meausure, answer 'Mitigation'.
        If it is neither a prevention measure nor a mitigation measure, answer 'Neither'. If it is both a
        prevention measure and a mitigation measure, answer 'Both'.
        </EXAMPLE INSTRUCTIONS>

        <EXAMPLE OUTPUT>
        Hazard Event Description: The hazard event of 'Cut Zip tie flies and hits audience member' during the activity 'Using a spring contraption as a demonstration for a TPS presentation' can lead to impact injuries.
        Prevention Explanation: 'Keeping hand around zip tie when cutting to stop it from flying' will stop the zip tie from flying and therefore stop the hazard event from occurring. Therefore, the likelihood of the hazard event occurring has been reduced to zero; since the likelihood of the hazard event has been reduced, it is therefore a prevention measure.
        Mitigation Explanation: If the hazard event occurs and the zip tie flies and hits an audience member, 'keeping hand around zip tie when cutting to stop it from flying' does not remove or reduce the impact injury caused by the hazard, as the zip tie has already flown and caused harm; it is therefore not a mitigation measure.
        Answer: Prevention.
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

        {all_few_shot_examples}

        <INSTRUCTIONS>
        Follow these instructions:
        1. In one sentence, describe the hazard event: "{hazard_event}" during the
        activity: "{self.activity}" given the harm caused: "{harm_caused}" for {self.who_it_harms}.
        2. Thinking step by step, explain whether or not "{self.control_measure}" reduces the likelihood that the hazard event: "{hazard_event}" occurs.
        If so, it is a prevention measure.
        3. Thinking step by step, explain whether or not "{self.control_measure}" removes or reduces the harm caused: "{harm_caused}" for the "{self.who_it_harms}".
        If so, it is a mitigation measure.
        4. If it is a prevention measure, answer 'Prevention'. If it is a migitation meausure, answer 'Mitigation'.
        If it is neither a prevention measure nor a mitigation measure, answer 'Neither'. If it is both a
        prevention measure and a mitigation measure, answer 'Both'.

        <OUTPUT FORMAT>
        Use the following output format:
        Hazard Event Description: <your hazard event description>
        Prevention Explanation: <your prevention explanation>
        Mitigation Explanation: <your mitigation explanation>
        Answer: <your answer>
        </OUTPUT FORMAT>
        
        <OUTPUT>
        Hazard Event Description: '''

class PreventionPrompt(ControlMeasureClassification):
    def __init__(self, control_measure, activity, hazard, how_it_harms, who_it_harms):
        super().__init__(control_measure, activity, hazard, how_it_harms, who_it_harms)
    
    def get_field_checked(self):
        return 'Prevention'
    
    def get_shortform_feedback(self, feedback_type):
        if feedback_type == 'positive':
            return f"Correct! '{self.control_measure}' is a prevention measure for the hazard: '{self.hazard}'"
        if feedback_type == 'both':
            return f"Feedback cannot be provided for the prevention: '{self.control_measure}'"
        if feedback_type == 'neither':
            return f"Incorrect. '{self.control_measure}' is not a prevention measure for the hazard: '{self.hazard}'."
        if feedback_type == 'misclassification':
            return f"Incorrect. '{self.control_measure}' is actually a mitigation measure for the hazard: '{self.hazard}'."
    
    def get_longform_feedback(self, prompt_output='', pattern_to_search_for='Prevention Explanation'):
        regex_pattern_matcher = RegexPatternMatcher()
        return regex_pattern_matcher.extract_section_of_prompt_until_new_line_or_end_of_string(prompt_output, pattern_to_search_for)

    # TODO: When you have hazard event input, can include in feedback.
    def get_recommendation(self, recommendation_type):
        if recommendation_type == 'both':
            return f"""A mitigation measure reduces the harm caused by the hazard event either while the hazard event is occurring or after it has occurred. On the other hand, a prevention measure reduces the likelihood of the hazard event occurring in the first place. Please use the above definitions to check your prevention input."""

        if recommendation_type == 'neither':
            return "For the prevention field, enter a control measure which reduces the likelihood of the hazard event."

        if recommendation_type == 'misclassification':
            return f"""A mitigation measure reduces the harm caused by the hazard event either while the hazard event is occurring or after it has occurred. On the other hand, a prevention measure reduces the likelihood of the hazard event occurring in the first place. Please use the above definitions to ammend your prevention input."""
    
class MitigationPrompt(ControlMeasureClassification):
    def __init__(self, control_measure, activity, hazard, how_it_harms, who_it_harms):
        super().__init__(control_measure, activity, hazard, how_it_harms, who_it_harms)

    def get_shortform_feedback(self, feedback_type):
        if feedback_type == 'positive':
            return f"Correct! '{self.mitigation}' is a mitigation measure for the hazard: '{self.hazard}'."
        if feedback_type == 'both':
            return f"Feedback cannot be provided for the prevention: '{self.mitigation}'"
        if feedback_type == 'neither':
            return f"Incorrect. '{self.mitigation}' is not a mitigation measure for the hazard: '{self.hazard}'."
        if feedback_type == 'misclassification':
            return f"Incorrect. '{self.mitigation}' is actually a prevention measure for the hazard: '{self.hazard}'."
    
    def get_longform_feedback(self, prompt_output='', pattern_to_search_for='Mitigation Explanation'):
        regex_pattern_matcher = RegexPatternMatcher()
        return regex_pattern_matcher.extract_section_of_prompt_until_new_line_or_end_of_string(prompt_output, pattern_to_search_for)
    
    # TODO: When you have hazard event input, can include in feedback.
    def get_recommendation(self, recommendation_type):
        if recommendation_type == 'both':
            return f"""A prevention measure reduces the likelihood of the hazard event occurring in the first place. On the other hand, a mitigation measure reduces the harm caused by the hazard event while it is happening or after it has occurred. Please use the above definitions to check your mitigation input."""

        if recommendation_type == 'neither':
            return "For the mitigation field, enter a control measure which reduces the harm caused by the hazard event either while the hazard event is occurring or after it has occurred."
        
        if recommendation_type == 'misclassification':
            return f"""A prevention measure reduces the likelihood of the hazard event occurring in the first place. On the other hand, a mitigation measure reduces the harm caused by the hazard event while it is happening or after it has occurred. Please use the above definitions to ammend your mitigation input."""