    # TODO: Make it easier to add new prompts. At the moment it is too difficult. 
    # Have to change code in 2 places.

class PromptInput:
    def __init__(self):
        self.activity_definition = """an action or process that involves
        physical or mental effort."""

        self.hazard_definition = """a dangerous phenomenon, substance, human activity or condition. 
        It may cause loss of life, injury or other health impacts, property damage, loss of livelihoods 
        and services, social and economic disruption, or environmental damage."""

        self.who_it_harms_entry_definition = """
        specific individuals, groups, environmental components or infrastructure
        likely to be negatively affected by identified risks, 
        excluding abstract concepts, generic terms or vague terms."""

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

        return f'''
        An 'activity' is defined as {self.activity_definition}
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
        return f'''If a 'hazard' is defined as '{self.hazard_definition}', is the following: '{self.hazard}', 
        during the activity: '{self.activity}', an example of a 'hazard'?'''

class HowItHarms(PromptInput):
    def __init__(self, how_it_harms):
        super().__init__()
        self.how_it_harms = how_it_harms
    
    def generate_prompt(self):
        how_it_harms_entry_definition = f"""
            the potential negative consequences of a hazard. It can outline the specific impacts on
            human health, property, environment, economics, social structures, livelihoods, essential 
            services, and the risk of loss of life. It must be specific, clear and precise."""
        
        return f'''An "appropriate entry for the how it harms field" in a Risk Assessment is 
        defined as: "{how_it_harms_entry_definition}". 
        Firstly, comparing the entry: "{self.how_it_harms}"
        with the definition of an "appropriate entry for the how it harms field", 
        explain whether "{self.how_it_harms}" is an appropriate entry. Secondly, 
        answer True if "{self.how_it_harms} is an appropriate entry, or False if it is not.
        
        The output should be in the format:
        Comparison and Explanation: your_explanation
        Answer: your_answer'''

class HowItHarmsInContext(PromptInput):
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

        return f'''The "expected entry" for the "who it harms" field in a Risk Assessment is 
        defined as: "{self.who_it_harms_entry_definition}".
        Firstly, describe "{self.who_it_harms}" in one sentence. Secondly, comparing this description
        with the definition of the "expected entry" for the "who it harms" field, 
        explain whether "{self.who_it_harms}" is an appropriate entry.
        Thirdly, answer True if "{self.who_it_harms} is an appropriate entry, or False if it is not.
        
        The output should be in the format:
        Comparison: your_comparison
        Explanation: your_explanation
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

# TODO: Could also do a test to see if a model can correctly classify between Prevention and mitigation.
class Prevention(PromptInput):
    def __init__(self, prevention, activity, hazard, how_it_harms, who_it_harms):
        super().__init__()
        self.prevention = prevention
        self.activity = activity
        self.hazard = hazard
        self.how_it_harms = how_it_harms
        self.who_it_harms = who_it_harms

    def generate_prompt(self):
        prevention_definition = f'an action which directly reduces the probability that the hazard occurs.'
        return f'''A 'prevention measure' is defined as '{prevention_definition}'. Given this definition,
        explain in one sentence whether '{self.prevention}' is a prevention measure for the following hazard: '{self.hazard}' 
        during the activity: '{self.activity}', given how the hazard harms: '{self.how_it_harms}' 
        and who/what the hazard harms: '{self.who_it_harms}'. If it is a 'prevention measure', answer True, 
        else answer False. The prompt output should be in the format:
        Explanation: your_explanation_in_one_sentence
        Answer: your_answer'''

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
        mitigation_definition = f'an action which directly reduces the severity of a hazard. Severity in this context is {severity_definition}'

        return f'''A 'mitigation measure' is defined as '{mitigation_definition}'. Given this definition,
        explain in one sentence whether '{self.mitigation}' is a mitigation measure for the following hazard: 
        '{self.hazard}' during the activity: '{self.activity}', given how the hazard harms: '{self.how_it_harms}' 
        and who/what the hazard harms: '{self.who_it_harms}'. If it is a 'mitigation measure', answer True, 
        else answer False. The prompt output should be in the format:
        Explanation: your_explanation_in_one_sentence
        Answer: your_answer'''

class PreventionClassification(PromptInput):
    def __init__(self, prevention, activity, hazard, how_it_harms, who_it_harms):
        super().__init__()
        self.prevention = prevention
        self.activity = activity
        self.hazard = hazard
        self.how_it_harms = how_it_harms
        self.who_it_harms = who_it_harms

    # TODO: Change to it either outputting Prevention or Mitigation (not true or false)
    def generate_prompt(self):

        prevention_definition = f'an action which directly reduces the probability that the hazard occurs.'

        severity_definition = """a measure of the seriousness of adverse consequences that could occur if the hazard 
        leads to an accident."""
        mitigation_definition = f'an action which directly reduces the severity of a hazard. Severity in this context is {severity_definition}'

        return f'''Given that a 'prevention measure' is defined as {prevention_definition} and a 'mitigation measure' 
        is defined as {mitigation_definition}, explain in one sentence whether the following:
        '{self.prevention}' is a 'prevention measure' or a 'mitigation measure' for the following hazard: 
        '{self.hazard}' during the activity: '{self.activity}', given how the hazard harms: '{self.how_it_harms}'
        and who/what the hazard harms: '{self.who_it_harms}'. Then answer True if it is a prevention measure
        and False if it is a mitigation measure. The output should be in the format:
        Explanation: your_explanation_in_one_sentence
        Answer: your_answer'''