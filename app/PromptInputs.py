    # TODO: Add requirement to have a generate_prompt function

class PromptInput:
    def __init__(self):
        pass

    def generate_prompt(self):
        pass

class Activity(PromptInput): # TODO so inherits expected_output from PromptInput
    def __init__(self, activity: str):
        super().__init__()
        self.activity = activity
        self.candidate_labels = ['Yes', 'No']

    def generate_prompt(self):
        activity_definition = """An activity is generally defined as a specific action or process that involves 
        physical or mental effort, often undertaken for enjoyment, recreation, or as a part of a routine."""
        
        return f'''If an 'activity' is defined as '{activity_definition}', 
        First provide a description of "{self.activity}" then compare this description 
        with the provided definition, then decide if "{self.activity}" is "an activity" 
        or "not an activity". End your answer in the format: \ndict('input': "{self.activity}", is_an_activity: True/False)'''

class Hazard(PromptInput):
    def __init__(self, activity: str, hazard: str):
        super().__init__()
        self.activity = activity
        self.hazard = hazard
        self.candidate_labels = ['Yes', 'No, it is not a hazard', 'No, it is a hazard but the activity is not related to the hazard']

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
        self.candidate_labels = ['Yes', 'No']
    
    def generate_prompt(self):
        # TODO: Do knowledge generation prompt for this
        return f''''Is '{self.how_it_harms}' a way that the hazard: '{self.hazard}', during the activity: '{self.activity}', 
        may cause harm?'''

class WhoItHarms(PromptInput):
    def __init__(self, who_it_harms, how_it_harms, activity, hazard):
        super().__init__()
        self.who_it_harms = who_it_harms
        self.how_it_harms = how_it_harms
        self.activity = activity
        self.hazard = hazard
        self.candidate_labels = ['Who it harms is a noun and they are likely to be harmed by the hazard',
                                 'Who it harms is a noun, but they are unlikely to be harmed by the hazard',
                                 'Who it harms is not a noun']

    def generate_prompt(self):
        noun_definition = "a word (other than a pronoun) used to identify any of a class of people, places, or things"

        return f'''Given that a noun is defined as: '{noun_definition}', is '{self.who_it_harms}' an example of a noun?
        If not, is '{self.who_it_harms}' likely to be harmed by hazard: '{self.hazard}' during the activity: '{self.activity}' 
        because of how the hazard causes harm: '{self.how_it_harms}'?'''

class Prevention(PromptInput):
    def __init__(self, prevention, activity, hazard, how_it_harms, who_it_harms):
        super().__init__()
        self.prevention = prevention
        self.activity = activity
        self.hazard = hazard
        self.how_it_harms = how_it_harms
        self.who_it_harms = who_it_harms
        self.candidate_labels = ['Yes', 'No']

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
        self.candidate_labels = ['Yes', 'No']

    def generate_prompt(self):
        severity_definition = """a measure of the seriousness of adverse consequences that could occur if the hazard 
        leads to an accident."""
        mitigation_definition = f'an action which reduces the severity of a hazard. Severity in this context is {severity_definition}'

        return f'''If a 'mitigation measure' is defined as '{mitigation_definition}', is the following: '{self.mitigation}' 
        an example of a 'mitigation measure' for the following hazard: '{self.hazard}' during the activity '{self.activity}' 
        given how it harms: '{self.how_it_harms}' and who it harms: '{self.who_it_harms}'?'''