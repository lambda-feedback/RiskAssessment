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
    def __init__(self, hazard, how_it_harms):
        super().__init__()
        self.hazard = hazard
        self.how_it_harms = how_it_harms
        self.pattern_matching_method = 'extract_harm_caused_and_hazard_event'

    def generate_prompt(self):
        return f'''
        Follow these instructions:
        The harm caused by a hazard refers to the negative consequences resulting from the hazard event.
        1. From the hazard and how it harms, extract the harm caused.
        2. Describe the events which lead to the harm caused. Don't refer to the harm caused.

        Hazard: Fire in a building
        How it harms: Clothes catch on fire and cause a burn
        Harm caused: Burn
        Event that leads to harm: Fire in building causes clothes to catch on fire

        Hazard: Unsecured scaffolding
        How it harms: A worker falling from a height causing an impact injury
        Harm caused: Impact injury
        Event that leads to harm: A worker falling from a height
    
        Hazard: Malware infection
        How it harms: Gives hackers remote access to the infected system, allowing them to steal personal data
        Harm caused: Personal data theft
        Event that leads to harm: Malware infects a system giving hackers remote access

        Hazard: Market volatility
        How it harms: If the value of an investor's holdings decreases due to market downturns, they will experience financial losses when selling their assets
        Harm caused: Financial losses
        Event that leads to harm: Market downturn causes a decrease in the value of an investor's holdings

        Use the following output format:
        Hazard: {self.hazard}
        How it harms: {self.how_it_harms}
        Harm caused: <your harm caused>
        Event that leads to harm: <your event>'''
    
# class HazardEvent(PromptInput):
#     def __init__(self, activity, hazard, who_it_harms, how_it_harms):
#         super().__init__()
#         self.activity = activity
#         self.hazard = hazard
#         self.who_it_harms = who_it_harms
#         self.how_it_harms = how_it_harms
#         self.pattern_matching_method = "extract_harm_caused_and_hazard_event"

#     def generate_prompt(self):
#         return f'''
#         Follow these instructions:
#         The harm caused by a hazard refers to the negative consequences resulting from the hazard event.
#         1. Given the activity: "{self.activity}", the hazard: "{self.hazard}", who it harms: {self.who_it_harms}, and how it harms: "{self.how_it_harms}", extract the harm caused.
#         2. Describe the events which lead to the harm caused. Don't refer to the harm caused.

#         Example Output:
#         Activity: Building a house
#         Hazard: Unsecured scaffolding
#         Who it harms: Construction workers
#         How it harms: Impact injuries caused by falling from a height
#         Harm caused: Impact injury
#         Event that leads to harm: A worker falling from a height

#         Example Output:
#         Activity: Fluids Laboratory
#         Hazard: Syringes with sharp needles
#         Who it harms: Students
#         How it harms: Sharp needles can pierce the skin and cause bleeding
#         Harm caused: Puncture wound
#         Event that leads to harm: A student being pricked by the syringe needle

#         Example Output:
#         Activity: Using a computer
#         Hazard: Malware infection
#         Who it harms: Computer users
#         How it harms: Gives hackers remote access to the infected system, allowing them to steal personal data
#         Harm caused: Personal data theft
#         Event that leads to harm: Malware infects a system giving hackers remote access

#         Example Output:
#         Activity: Investing in stocks
#         Hazard: Market volatility
#         Who it harms: Investors
#         How it harms: If the value of an investor's holdings decreases due to market downturns, they will experience financial losses when selling their assets
#         Harm caused: Financial losses
#         Event that leads to harm: Market downturn causes a decrease in the value of an investor's holdings

#         Use the following output format:
#         Activity: {self.activity}
#         Hazard: {self.hazard}
#         Who it harms: {self.who_it_harms}
#         How it harms: {self.how_it_harms}
#         Harm caused: <your harm>
#         Event that leads to harm: <your event>'''

class Prevention(PromptInput):
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
    
class Mitigation(PromptInput):
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

class OldPrevention(PromptInput):
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

    def get_field_checked(self):
        return 'Prevention'
    
    def generate_prompt_without_few_shot_examples(self):

        return f'''Follow these instructions:
        1. In one sentence, describe the event that leads to harm: <hazard event> during the
        activity: '{self.activity}' given the harm caused: <harm caused> for {self.who_it_harms}.
        2. Thinking step by step, explain whether or not '{self.control_measure}' reduces the likelihood that <hazard event> occurs.
        If so, it is a prevention measure.
        3. Thinking step by step, explain whether or not '{self.control_measure}' removes or reduces the harm caused by <harm caused> for the '{self.who_it_harms}'.
        If so, it is a mitigation measure.
        4. If it is a prevention measure, answer 'Prevention'. If it is a migitation meausure, answer 'Mitigation'.
        If it is neither a prevention measure nor a mitigation measure, answer 'Neither'. If it is both a
        prevention measure and a mitigation measure, answer 'Both'.'''
    
    def generate_prompt(self, hazard_event, harm_caused):

        all_few_shot_examples = """
        <EXAMPLE INSTRUCTIONS>
        Follow these instructions:
        1. In one sentence, describe the hazard: 'Ink spillage on students face' during the
        activity: 'Fluids laboratory' given how the hazard causes harm: 'Serious eye damage'.
        3. Thinking step by step, explain whether or not 'First aid' reduces the likelihood that the hazard occurs.
        If so, it is a prevention measure.
        4. Thinking step by step, explain whether or not 'First aid' removes or reduces the chance of 'Serious eye damage'.
        If so, it is a mitigation measure.
        5. If it is a prevention measure, answer 'Prevention'. If it is a migitation meausure, answer 'Mitigation'.
        If it is neither a prevention measure nor a mitigation measure, answer 'Neither'. If it is both a        
        prevention measure and a mitigation measure, answer 'Both'.
        </EXAMPLE INSTRUCTIONS>

        <EXAMPLE OUTPUT>
        Hazard Description: The hazard of 'Ink spillage on student's face' during the activity 'Fluids laboratory' can lead to serious eye damage to students.
        Prevention Explanation: 'First aid' is a reactive measure applied after the hazard of 'Ink spillage on student's face'; it therefore does not reduce the likelihood of the hazard and is not a prevention measure.
        Mitigation Explanation: If ink has been spilled onto a student's face, 'first aid' will help to wash the ink out of the eyes and reduce eye damage after the hazard has occurred; as it reduces the harm caused by the hazard, it is therefore a mitigation measure.
        Answer: Mitigation.
        </EXAMPLE OUTPUT>

        <EXAMPLE INSTRUCTIONS>
        Follow these instructions:
        1. In one sentence, describe the hazard: 'Water being spilt on the floor causing students to slip' during the
        activity: 'Fluids laboratory' given how the hazard harms: 'Impact injury'.
        3. Thinking step by step, explain whether or not 'Do not move the water tank when it is full' reduces the likelihood that the hazard occurs.
        If so, it is a prevention measure.
        4. Thinking step by step, explain whether or not 'Do not move the water tank when it is full' removes or reduces the chance of 'Impact injury'.
        If so, it is a mitigation measure.
        5. If it is a prevention measure, answer 'Prevention'. If it is a migitation meausure, answer 'Mitigation'.
        If it is neither a prevention measure nor a mitigation measure, answer 'Neither'. If it is both a        
        prevention measure and a mitigation measure, answer 'Both'.
        </EXAMPLE INSTRUCTIONS>

        <EXAMPLE OUTPUT>
        Hazard Description: The hazard of 'Water being spilt on the floor causing students to slip' during the activity 'Fluids laboratory' can lead to impact injuries.
        Prevention Explanation: 'Keeping the water tank stationary when it's full' means water cannot be spilled on to the floor by moving the water tank; no water on the floor reduces the likelihood of the student slipping; since it reduces the likelihood of the hazard, it is a prevention measure.
        Mitigation Explanation: If water has been spilled on the floor, 'not moving the water tank when it is full' does not remove or reduce the harm caused by the hazard, as the water is already spilled to pose a slipping hazard; as it does not reduce the harm caused by the hazard, it is not a mitigation measure.
        Answer: Prevention.
        </EXAMPLE OUTPUT>

        <EXAMPLE INSTRUCTIONS>
        Follow these instructions:
        1. In one sentence, describe the hazard: 'Cut Zip tie flies and hits audience member' during the
        activity: 'Using a spring contraption as a demonstration for a TPS presentation' given how the hazard harms: 'Impact injury.'.
        3. Thinking step by step, explain whether or not 'Keep hand around zip tie when cutting to stop it from flying' reduces the likelihood that the hazard occurs.
        If so, it is a prevention measure.
        3. Thinking step by step, explain whether or not 'Keep hand around zip tie when cutting to stop it from flying' removes or reduces the chance of Impact injury..
        If so, it is a mitigation measure.
        4. If it is a prevention measure, answer 'Prevention'. If it is a migitation meausure, answer 'Mitigation'.
        If it is neither a prevention measure nor a mitigation measure, answer 'Neither'. If it is both a
        prevention measure and a mitigation measure, answer 'Both'.
        </EXAMPLE INSTRUCTIONS>

        <EXAMPLE OUTPUT>
        Hazard Description: The hazard of 'Cut Zip tie flies and hits audience member' during the activity 'Using a spring contraption as a demonstration for a TPS presentation' can lead to impact injuries.
        Prevention Explanation: 'Keeping hand around zip tie when cutting to stop it from flying' will stop the zip tie from flying and therefore stop the hazard from occurring. Therefore, the likelihood of the hazard occurring has been reduced to zero; since the likelihood has been reduced, it is therefore a prevention measure.
        Mitigation Explanation: If the hazard occurs and the zip tie flies and hits an audience member, 'keeping hand around zip tie when cutting to stop it from flying' does not remove or reduce the impact injury caused by the hazard, as the zip tie has already flown and caused harm; it is therefore not a mitigation measure.
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
        1. In one sentence, describe the event that leads to harm: {hazard_event} during the
        activity: '{self.activity}' given the harm caused: {harm_caused} for {self.who_it_harms}.
        2. Thinking step by step, explain whether or not '{self.control_measure}' reduces the likelihood that {hazard_event} occurs.
        If so, it is a prevention measure.
        3. Thinking step by step, explain whether or not '{self.control_measure}' removes or reduces the harm caused by {harm_caused} for the '{self.who_it_harms}'.
        If so, it is a mitigation measure.
        4. If it is a prevention measure, answer 'Prevention'. If it is a migitation meausure, answer 'Mitigation'.
        If it is neither a prevention measure nor a mitigation measure, answer 'Neither'. If it is both a
        prevention measure and a mitigation measure, answer 'Both'.

        <OUTPUT FORMAT>
        Use the following output format:
        Hazard Description: <your hazard description>
        Prevention Explanation: <your prevention explanation>
        Mitigation Explanation: <your mitigation explanation>
        Answer: <your answer>
        </OUTPUT FORMAT>
        
        <OUTPUT>
        Hazard Description: '''
    
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