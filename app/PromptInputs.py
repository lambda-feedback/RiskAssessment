    # TODO: Make it easier to add new prompts. At the moment it is too difficult. 
    # Have to change code in 2 places.

class ShortformFeedback:
    def __init__(self, positive_feedback, negative_feedback):
        self.positive_feedback = positive_feedback
        self.negative_feedback = negative_feedback

class PromptInput:
    def __init__(self):
        self.activity_definition = """an action or process that involves
        physical or mental effort."""

        self.hazard_definition = """a dangerous phenomenon, substance, human activity or condition. 
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

        severity_definition = """a measure of the seriousness of adverse consequences that could occur if the hazard 
        leads to an accident."""
        
        self.mitigation_definition = f'''an action which directly reduces the severity of a hazard or the consequences of the hazard. 
        Severity in this context is {severity_definition}'''

    def get_question(self):
        pass

    def get_question_title(self):
        pass

    def generate_prompt(self):
        pass

    def get_shortform_feedback(self):
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

    def get_question_title(self):
        return 'Activity'

    def get_question(self):
        return f'''Is the 'activity': '{self.activity}' correct?'''

    def generate_prompt(self):
        return f'''
        An 'activity' is defined as {self.activity_definition}
        Firstly, in one sentence, provide a description of "{self.activity}". Secondly, in one sentence, 
        compare this description with the provided definition of an activity. Then if "{self.activity}",
        answer True, else answer False. 
        
        The output should be in the format:
        Description: your_description
        Comparison: your_comparison
        Answer: your_answer'''
    
    def get_shortform_feedback(self):
        return ShortformFeedback(positive_feedback=f"Correct! '{self.activity}' is an activity.",
                                 negative_feedback=f"Incorrect. '{self.activity}' is not an activity.")

class HowItHarms(PromptInput):
    def __init__(self, how_it_harms):
        super().__init__()
        self.how_it_harms = how_it_harms

    def get_question_title(self):
        return 'How It Harms'

    def get_question(self):
        return f'''Is 'how it harms': '{self.how_it_harms}' correct?'''
    
    def generate_prompt(self):
        return f'''An "appropriate entry for the how it harms field" in a Risk Assessment is 
        defined as: "{self.how_it_harms_entry_definition}". 
        Firstly, comparing the entry: "{self.how_it_harms}"
        with the definition of an "appropriate entry for the how it harms field", 
        explain whether "{self.how_it_harms}" is an appropriate entry. Secondly, 
        answer True if "{self.how_it_harms} is an appropriate entry, or False if it is not.
        
        The output should be in the format:
        Comparison and Explanation: your_explanation
        Answer: your_answer'''
    
    def get_shortform_feedback(self):
        return ShortformFeedback(positive_feedback=f"Correct! '{self.how_it_harms}' is an appropriate entry for the how it harms field.",
                                    negative_feedback=f"Incorrect. '{self.how_it_harms}' is not an appropriate entry for the how it harms field.")

class HowItHarmsInContext(PromptInput):
    def __init__(self, how_it_harms, activity, hazard):
        super().__init__()
        self.how_it_harms = how_it_harms
        self.activity = activity
        self.hazard = hazard

    def get_question_title(self):
        return 'How It Harms In Context'

    def get_question(self):
        return f'''Is 'how it harms': '{self.how_it_harms}' a way that the 'hazard': '{self.hazard}' 
        during the 'activity': '{self.activity}' causes harm?'''
    
    def generate_prompt(self):
        return f'''Firstly, in one sentence, describe the hazard: '{self.hazard}' during the 
        activity: '{self.activity}'. Secondly, in one sentence, explain whether or not 
        '{self.how_it_harms}' is a way that this hazard causes harm. 
        If it does cause harm, answer True, else, answer False.

        The output should be in the format:
        Description: your_description
        Comparison: your_comparison
        Answer: your_answer'''
    
    def get_shortform_feedback(self):
        return ShortformFeedback(positive_feedback=f"Correct! '{self.how_it_harms}' is a way that the hazard causes harm.",
                                    negative_feedback=f"Incorrect. '{self.how_it_harms}' is not a way that the hazard causes harm.")
    
class WhoItHarms(PromptInput):
    def __init__(self, who_it_harms):
        super().__init__()
        self.who_it_harms = who_it_harms

    def get_question_title(self):
        return 'Who It Harms'

    def get_question(self):
        return f'''Is 'who it harms': '{self.who_it_harms}' correct?'''

    def generate_prompt(self):

        return f'''The "expected entry" for the "who it harms" field in a Risk Assessment is 
        defined as: "{self.who_it_harms_entry_definition}".
        Firstly, describe "{self.who_it_harms}" in one sentence. Secondly, comparing this description
        with the definition of the "expected entry" for the "who it harms" field, 
        explain whether "{self.who_it_harms}" is an appropriate entry.
        Thirdly, answer True if "{self.who_it_harms} is an appropriate entry, or False if it is not.
        
        The output should be in the format:
        Description: your_description
        Comparison: your_comparison
        Explanation: your_explanation
        Answer: your_answer'''
    
    def get_shortform_feedback(self):
        return ShortformFeedback(positive_feedback=f"Correct! '{self.who_it_harms}' is an appropriate entry for the who it harms field.",
                                    negative_feedback=f"Incorrect. '{self.who_it_harms}' is not an appropriate entry for the who it harms field.")

class WhoItHarmsInContext(PromptInput):
    def __init__(self, who_it_harms, how_it_harms, activity, hazard):
        super().__init__()
        self.who_it_harms = who_it_harms
        self.how_it_harms = how_it_harms
        self.activity = activity
        self.hazard = hazard

    def get_question_title(self):
        return 'Who It Harms In Context'

    def get_question(self):
        return f'''Could 'who it harms': '{self.who_it_harms}' 
        be harmed by the 'hazard': '{self.hazard}' during 'activity': '{self.activity}'
        given how the hazard harms: '{self.how_it_harms}'?'''

    def generate_prompt(self):
        
        return f'''In one sentence, describe the hazard: '{self.hazard}' during the 
        activity: '{self.activity}' and how it harms: '{self.how_it_harms}'. Then in one sentence,
        explain whether or not 'who it harms': '{self.who_it_harms}' is harmed by this hazard. 
        If 'who it harms' is harmed by this hazard, is_correct = True. 
        Then write the final sentence of your answer in the format: dict(is_correct=True/False).

        Your answer should be in the format:
        Description: your_description
        Explanation: your_explanation
        Answer: your_answer'''
    
    def get_shortform_feedback(self):
        return ShortformFeedback(positive_feedback=f"Correct! '{self.who_it_harms}' could be harmed by the hazard.",
                                    negative_feedback=f"Incorrect. '{self.who_it_harms}' could not be harmed by the hazard.")
    
class Prevention(PromptInput):
    def __init__(self, prevention, activity, hazard, how_it_harms, who_it_harms):
        super().__init__()
        self.prevention = prevention
        self.activity = activity
        self.hazard = hazard
        self.how_it_harms = how_it_harms
        self.who_it_harms = who_it_harms

    def get_question_title(self):
        return 'Prevention In Context'
    
    def get_question(self):
        return f'''Will the prevention measure: '{self.prevention}' reduce the likelihood of the
        'hazard': '{self.hazard}' occurring during the 'activity': {self.activity}, given
        given how the hazard harms: '{self.how_it_harms}' and who/what the hazard harms: '{self.who_it_harms}?'''

    def generate_prompt(self):
        return f'''A 'prevention measure' is defined as '{self.prevention_definition}'. Given this definition,
        explain in one sentence whether '{self.prevention}' is a prevention measure for the following hazard: '{self.hazard}' 
        during the activity: '{self.activity}', given how the hazard harms: '{self.how_it_harms}' 
        and who/what the hazard harms: '{self.who_it_harms}'. If it is a 'prevention measure', answer True, 
        else answer False. The prompt output should be in the format:
        Explanation: your_explanation_in_one_sentence
        Answer: your_answer'''
    
    def get_shortform_feedback(self):
        return ShortformFeedback(positive_feedback=f"Correct! '{self.prevention}' is a prevention measure.",
                                    negative_feedback=f"Incorrect. '{self.prevention}' is not a prevention measure.")

class Mitigation(PromptInput):
    def __init__(self, mitigation, activity, hazard, how_it_harms, who_it_harms):
        super().__init__()
        self.mitigation = mitigation
        self.activity = activity
        self.hazard = hazard
        self.how_it_harms = how_it_harms
        self.who_it_harms = who_it_harms

    def get_question_title(self):
        return 'Mitigation In Context'

    def get_question(self):
        return f'''Will the mitigation measure: '{self.mitigation}' reduce the severity of the
        'hazard': '{self.hazard}' occurring during the 'activity': {self.activity}, given
        given how the hazard harms: '{self.how_it_harms}' and who/what the hazard harms: '{self.who_it_harms}?'''

    def generate_prompt(self):
        return f'''
        Example Input: For the hazard: "Electrocution" during the activity: "Fluids laboratory", 
        given the consequences of the hazard: "Electrocuted by mains voltage" and who/what the hazard harms: 
        "Students", is the following: "First aid on site" a mitigation measure?
        
        Output: 'First aid on site' is not a mitigation meausure for the hazard: 'Electrocution'
        since having the first aid on site alone does not reduce the severity of the hazard
        and additional measures such as 'applying the first aid and seeking medical assistance' is required.
        Answer: False' 

        Example Input: For the hazard: "Ink spillage" during the activity: "Fluids laboratory",
        given how the hazard harms: "Serious eye damage" and who/what the hazard harms: "Students",
        is the following: "Wash your eyes with clean water" a mitigation measure?

        Output: 'Wash your eyes with clean water' is a mitigation measure for the hazard: 'Ink spillage'
        since it reduces the severity of the consequences of the hazard: "Serious eye damage" as
        the water will help wash the ink out of the eye. Answer: True.
        
        A 'mitigation measure' is defined as '{self.mitigation_definition}'. Given this definition,
        explain in one sentence whether '{self.mitigation}' is a mitigation measure for the following hazard: 
        '{self.hazard}' during the activity: '{self.activity}', given the potential consequences of the hazard:
        '{self.how_it_harms}' and who/what the hazard harms: '{self.who_it_harms}'. If it is a 'mitigation measure', answer True, 
        else answer False. The prompt output should be in the format:
        Explanation: your_explanation_in_one_sentence
        Answer: your_answer'''
    
    def get_shortform_feedback(self):
        return ShortformFeedback(positive_feedback=f"Correct! '{self.mitigation}' is a mitigation measure.",
                                    negative_feedback=f"Incorrect. '{self.mitigation}' is not a mitigation measure.")

class PreventionClassification(PromptInput):
    def __init__(self, prevention, activity, hazard, how_it_harms, who_it_harms):
        super().__init__()
        self.prevention = prevention
        self.activity = activity
        self.hazard = hazard
        self.how_it_harms = how_it_harms
        self.who_it_harms = who_it_harms

    def get_question_title(self):
        return 'Prevention Classification'
    
    def get_question(self):
        return f'''Given that a 'prevention' measure reduces the likelihood of a hazard
        and a 'mitigation' measure reduces the severity of a hazard, is the 'prevention': 
        '{self.prevention}' an example of a 'prevention' or 'mitigation'''

    # TODO: Change to it either outputting Prevention or Mitigation (not true or false)
    def generate_prompt(self):
        return f'''Given that a 'prevention measure' is defined as {self.prevention_definition} and a 'mitigation measure' 
        is defined as {self.mitigation_definition}, explain in one sentence whether the following:
        '{self.prevention}' is a 'prevention measure' or a 'mitigation measure' for the following hazard: 
        '{self.hazard}' during the activity: '{self.activity}', given how the hazard harms: '{self.how_it_harms}'
        and who/what the hazard harms: '{self.who_it_harms}'. Then answer True if it is a prevention measure
        and False if it is a mitigation measure. The output should be in the format:
        Explanation: your_explanation_in_one_sentence
        Answer: your_answer'''
    
    def get_shortform_feedback(self):
        return ShortformFeedback(positive_feedback=f"Correct! '{self.prevention}' is a prevention measure.",
                                    negative_feedback=f"Incorrect. '{self.prevention}' is actually a mitigation measure.")
    
class MitigationClassification(PromptInput):
    def __init__(self, mitigation, activity, hazard, how_it_harms, who_it_harms):
        super().__init__()
        self.mitigation = mitigation
        self.activity = activity
        self.hazard = hazard
        self.how_it_harms = how_it_harms
        self.who_it_harms = who_it_harms

    def get_question_title(self):
        return 'Mitigation Classification'

    def get_question(self):
        return f'''Given that a 'prevention' measure reduces the likelihood of a hazard
        and a 'mitigation' measure reduces the severity of a hazard, is the 'mitigation': 
        '{self.mitigation}' an example of a 'prevention' or 'mitigation'''
    
        # TODO: Change to it either outputting Prevention or Mitigation (not true or false)
    def generate_prompt(self):
        return f'''Given that a 'prevention measure' is defined as {self.prevention_definition} and a 'mitigation measure' 
        is defined as {self.mitigation_definition}, explain in one sentence whether the following:
        '{self.mitigation}' is a 'prevention measure' or a 'mitigation measure' for the following hazard: 
        '{self.hazard}' during the activity: '{self.activity}', given how the hazard harms: '{self.how_it_harms}'
        and who/what the hazard harms: '{self.who_it_harms}'. Then answer True if it is a mitigation measure
        and False if it is a prvention measure. The output should be in the format:
        Explanation: your_explanation_in_one_sentence
        Answer: your_answer'''
    
    def get_shortform_feedback(self):
        return ShortformFeedback(positive_feedback=f"Correct! '{self.mitigation}' is a mitigation measure.",
                                    negative_feedback=f"Incorrect. '{self.mitigation}' is actually a prevention measure.")