    # TODO: Make it easier to add new prompts. At the moment it is too difficult. 
    # Have to change code in 2 places.

class PromptInput:
    def __init__(self):
        pass

    def generate_prompt(self):
        pass

    def to_string(self):
        class_name = self.__class__.__name__
        if hasattr(self, '__dict__'):
            attributes = ', '.join([f"{key}={value}" for key, value in self.__dict__.items()])
            return f"{class_name}({attributes})"
        else:
            return f"{class_name}()"

class Activity(PromptInput):
    # TODO: Adjust prompt so there is few shot prompting with an example of what the output should look like.
    def __init__(self, activity: str):
        super().__init__()
        self.activity = activity

    def generate_prompt(self):
        common_noun_definition = """a noun denoting a class of objects or a concept as opposed 
        to a particular individual."""

        activity_definition = """a specific action or process that involves 
        physical or mental effort."""

        return f'''
        An 'activity' is defined as 'a specific action or process that involves 
        physical or mental effort'. 
        Firstly, in one sentence, provide a description of "{self.activity}". Secondly, in one sentence, 
        compare this description with the provided definition of an activity. Then decide if "{self.activity}" 
        is an activity. Thirdly, write the sentence in the format: 
        dict(input="{self.activity}", is_activity=True/False)'''
        
        # return f'''
        # The definition of activity is: "{activity_definition}". 
        # In one sentence, provide a description of "{self.activity}".
        # Then in one sentence compare this description of "{self.activity}" 
        # with the provided definition of an activity. 
        # If "{self.activity}" is an activity, is_correct = True. 
        # Then write one sentence in the format: \ndict(is_correct=True/False)'''

        # dict\(\'input\'=({}), is_correct=(True|False)\)''.format(re.escape(input))

class Hazard(PromptInput):
    def __init__(self, activity: str, hazard: str):
        super().__init__()
        self.activity = activity
        self.hazard = hazard

    def generate_prompt(self):
        hazard_definition = """a dangerous phenomenon, substance, human activity or condition. 
        It may cause loss of life, injury or other health impacts, property damage, loss of livelihoods 
        and services, social and economic disruption, or environmental damage."""
        return f'''If a 'hazard' is defined as '{hazard_definition}', is the following: '{self.hazard}', 
        during the activity: '{self.activity}', an example of a 'hazard'?'''

class HowItHarms(PromptInput):
    def __init__(self, how_it_harms, activity, hazard):
        super().__init__()
        self.how_it_harms = how_it_harms
        self.activity = activity
        self.hazard = hazard
    
    def generate_prompt(self):
        return f'''In one sentence, describe the hazard: '{self.hazard}' during the 
        activity: '{self.activity}'. Then in one sentence, explain whether or not 
        '{self.how_it_harms}' is a way that this hazard causes harm. 
        If it does cause harm, is_correct = True. Then write the final sentence of your answer 
        in the format: dict(is_correct=True/False).'''
    
class WhoItHarms(PromptInput):
    def __init__(self, who_it_harms):
        super().__init__()
        self.who_it_harms = who_it_harms

    def generate_prompt(self):

        who_it_harms_entry_definition = """
            specific individuals, groups, environmental components or infrastructure
            likely to be negatively affected by identified risks, 
            excluding abstract concepts, generic terms or vague terms."""

        return f'''The "expected entry" for the "who it harms" field in a Risk Assessment is 
        defined as: "{who_it_harms_entry_definition}".
        Firstly, describe "{self.who_it_harms}" in one sentence. Secondly, comparing this description
        with the definition of the "expected entry" for the "who it harms" field, 
        explain whether "{self.who_it_harms}" is an appropriate entry.
        Thirdly, answer True if "{self.who_it_harms} is an appropriate entry, or False if it is not.
        
        The output should be in the format:
        Description: your_description
        Comparison: your_explanation
        Answer: your_answer'''

class WhoItHarmsInContext(PromptInput):
    def __init__(self, who_it_harms, how_it_harms, activity, hazard):
        super().__init__()
        self.who_it_harms = who_it_harms
        self.how_it_harms = how_it_harms
        self.activity = activity
        self.hazard = hazard

    def generate_prompt(self):

        # TOOD: Try avoid getting just {'is_correct': True} as the output.
        
        return f'''In one sentence, describe the hazard: '{self.hazard}' during the 
        activity: '{self.activity}' and how it harms: '{self.how_it_harms}'. Then in one sentence,
        explain whether or not 'who it harms': '{self.who_it_harms}' is harmed by this hazard. 
        If 'who it harms' is harmed by this hazard, is_correct = True. 
        Then write the final sentence of your answer in the format: dict(is_correct=True/False).

        Your answer should be in the format:
        Description: your_description
        Explanation: your_explanation
        Answer: your_answer
        '''
    
        # noun_definition = "a word (other than a pronoun) used to identify any of a class of people, places, or things"

        # return f'''Given that a noun is defined as: '{noun_definition}', is '{self.who_it_harms}' an example of a noun?
        # If not, is '{self.who_it_harms}' likely to be harmed by hazard: '{self.hazard}' during the activity: '{self.activity}' 
        # because of how the hazard causes harm: '{self.how_it_harms}'?'''

class Prevention(PromptInput):
    def __init__(self, prevention, activity, hazard, how_it_harms, who_it_harms):
        super().__init__()
        self.prevention = prevention
        self.activity = activity
        self.hazard = hazard
        self.how_it_harms = how_it_harms
        self.who_it_harms = who_it_harms

    def generate_prompt(self):
        prevention_definition = f'an action which reduces the probability that the hazard occurs.'
        return f'''If a 'prevention measure' is defined as '{prevention_definition}', is the following: '{self.prevention}' 
        an example of a 'prevention measure' for the following hazard: '{self.hazard}' during the activity: '{self.activity}' 
        given how it harms: '{self.how_it_harms}' and who it harms: '{self.who_it_harms}'?'''

class Mitigation(PromptInput):
    def __init__(self, mitigation, activity, hazard, how_it_harms, who_it_harms):
        super().__init__()
        self.mitigation = mitigation
        self.activity = activity
        self.hazard = hazard
        self.how_it_harms = how_it_harms
        self.who_it_harms = who_it_harms

    def generate_prompt(self):
        severity_definition = """a measure of the seriousness of adverse consequences that could occur if the hazard 
        leads to an accident."""
        mitigation_definition = f'an action which reduces the severity of a hazard. Severity in this context is {severity_definition}'

        return f'''If a 'mitigation measure' is defined as '{mitigation_definition}', is the following: '{self.mitigation}' 
        an example of a 'mitigation measure' for the following hazard: '{self.hazard}' during the activity '{self.activity}' 
        given how it harms: '{self.how_it_harms}' and who it harms: '{self.who_it_harms}'?'''