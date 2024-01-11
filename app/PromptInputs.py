# TODO: Make it easier to add new prompts. At the moment it is too difficult. 
# Have to change code in 2 places.

# TODO: Decide whether to remove the get_question method from the PromptInput class.

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

        ## TODO: I changed the definition of mitigation. See if this has an effect.
        self.mitigation_definition = f'''an action which directly reduces the harm caused by a hazard occurring
        or reduces the harm caused by the hazard after it has occurred.''' 

        self.pattern_matching_method = 'check_string_for_true_or_false'
        self.correct_matched_pattern = True

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
        compare this description with the provided definition of an activity. Then if "{self.activity}"
        is an activity, answer True, else answer False. 
        
        The output should be in the format:
        Description: your_description
        Comparison: your_comparison
        Answer: your_answer'''
    
    def get_shortform_feedback(self):
        return ShortformFeedback(positive_feedback=f"Correct! '{self.activity}' is an activity.",
                                 negative_feedback=f"Incorrect. '{self.activity}' is not an activity.")
    
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
        return ShortformFeedback(positive_feedback=f"Correct! '{self.how_it_harms}' is a way that the hazard: '{self.hazard}' causes harm.",
        negative_feedback=f"Incorrect. '{self.how_it_harms}' is not a way that the hazard: '{self.hazard}' causes harm.")
    
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
        return ShortformFeedback(positive_feedback=f"Correct! '{self.who_it_harms}' could be harmed by the hazard: '{self.hazard}'.",
        negative_feedback=f"Incorrect. '{self.who_it_harms}' could not be harmed by the hazard: '{self.hazard}'.")
    
class Prevention(PromptInput):
    def __init__(self, prevention, activity, hazard, how_it_harms, who_it_harms):
        super().__init__()
        self.prevention = prevention
        self.activity = activity
        self.hazard = hazard
        self.how_it_harms = how_it_harms
        self.who_it_harms = who_it_harms

        self.pattern_matching_method = 'check_string_for_prevention_mitigation_or_neither'
        self.correct_matched_pattern = 'prevention'

    def get_question_title(self):
        return 'Prevention In Context'
    
    def get_question(self):
        return f'''Will the prevention measure: '{self.prevention}' reduce the likelihood of the
        'hazard': '{self.hazard}' occurring during the 'activity': {self.activity}, given
        given how the hazard harms: '{self.how_it_harms}' and who/what the hazard harms: '{self.who_it_harms}?'''

    def generate_prompt(self):
        example_of_correct_prevention = '''
        Example Input:
        For the hazard: "Slippage of weight for contraption" during the activity: "Using a spring contraption as a demonstration for a TPS presentation",
        given the potential consequences of the hazard: "Heavy impact when falling onto demonstator, causing injury" and who/what the hazard harms: "Demonstrator",
        is the following: "Keep away from below the contraption" a mitigation measure?
        
        Output:
        Explanation: "Keep away from below the contraption" is a prevention meausure for the hazard of
        slippage of weight for contraption since it reduces the likelihood of the consequence of the hazard:
        "Heavy impact when falling onto demonstator, causing injury". This is because
        it is less likely there will be a heavy impact falling onto the demonstrator if they are standing away from 
        below the contraption.
        Answer: prevention'''

        example_of_mitigation = '''
        Example Input: 
        For the hazard: "Ink spillage" during the activity: "Fluids laboratory",
        given the potential consequences of the hazard: "Serious eye damage" and who/what the hazard harms: "Students",
        is the following: "Wash your eyes with clean water" a mitigation measure?

        Output: 
        Explanation: Washing your eyes with clean water is a mitigation measure for the hazard of ink spillage
        since it reduces the harm caused by the serious eye damage. This is because the water will help wash the 
        ink out of the eye. Since, it is a mitigation measure, it is True.
        Answer: mitigation.'''

        example_of_incorrect_prevention = '''
        Example Input:
        For the hazard: "Exposure to toxic welding fumes" during the activity: "Welding metal structures", 
        given the potential consequences of the hazard: "Inhaling welding fumes can lead to respiratory problems, lung damage, and long-term health issues." 
        and who/what the hazard harms: "Welders and individuals in the vicinity of the welding area.",
        is the following: "Using the welding equipment in an enclosed space without proper ventilation." a prevention measure?

        Output:
        Exaplanation: "Using the welding equipment in an enclosed space without proper ventilation" 
        is not a prevention meausure for the hazard of exposure to toxic welding fumes
        since it does not reduce the likelihood of the hazard occurring; 
        an enclosed space without proper ventilation will mean the fumes will become concentrated more quickly. 
        It is also not a mitigation measure since it does not reduce the harm caused by the hazard; 
        the respiratory problems from inhaling the fumes will not be mitigated by using the 
        welding equipment in an enclosed space.
        Answer: neither'''

        return f'''
        {example_of_correct_prevention}

        {example_of_mitigation}

        {example_of_incorrect_prevention}
        
        A 'prevention measure' is defined as '{self.prevention_definition}'.
        A 'mitigation measure' is defined as '{self.mitigation_definition}'. Given these definitions,
        explain why '{self.prevention}' is either a prevention measure, a mitigation measure, 
        or neither a prevention nor a mitigation measure, for the following hazard: 
        '{self.hazard}' during the activity: '{self.activity}', given the potential consequences of the hazard:
        '{self.how_it_harms}' and who/what the hazard harms: '{self.who_it_harms}'.
        If it is a prevention measure, answer prevention. If it is a migitation meausure, answer mitigation. 
        If it is neither a prevention measure nor a mitigation measure, answer neither. 
        The prompt output should be in the format:
        Explanation: your_explanation
        Answer: your_answer'''

        # return f'''A 'prevention measure' is defined as '{self.prevention_definition}'. Given this definition,
        # explain in one sentence whether '{self.prevention}' is a prevention measure for the following hazard: '{self.hazard}' 
        # during the activity: '{self.activity}', given how the hazard harms: '{self.how_it_harms}' 
        # and who/what the hazard harms: '{self.who_it_harms}'. If it is a 'prevention measure', answer True, 
        # else answer False. The prompt output should be in the format:
        # Explanation: your_explanation_in_one_sentence
        # Answer: your_answer'''
    
    def get_shortform_feedback(self):
        return ShortformFeedback(positive_feedback=f"Correct! '{self.prevention}' is a prevention measure for the hazard: '{self.hazard}'",
        negative_feedback=f"Incorrect. '{self.prevention}' is not a prevention measure for the hazard: '{self.hazard}'.")

class Mitigation(PromptInput):
    def __init__(self, mitigation, activity, hazard, how_it_harms, who_it_harms):
        super().__init__()
        self.mitigation = mitigation
        self.activity = activity
        self.hazard = hazard
        self.how_it_harms = how_it_harms
        self.who_it_harms = who_it_harms

        self.pattern_matching_method = 'check_string_for_prevention_mitigation_or_neither'
        self.correct_matched_pattern = 'mitigation'

    def get_question_title(self):
        return 'Mitigation In Context'

    def get_question(self):
        return f'''Will the mitigation measure: '{self.mitigation}' reduce the severity of the
        'hazard': '{self.hazard}' occurring during the 'activity': {self.activity}, given
        given how the hazard harms: '{self.how_it_harms}' and who/what the hazard harms: '{self.who_it_harms}?'''

    def generate_prompt(self):

        example_of_correct_mitigation = '''
        Example Input: 
        For the hazard: "Ink spillage" during the activity: "Fluids laboratory",
        given the potential consequences of the hazard: "Serious eye damage" and who/what the hazard harms: "Students",
        is the following: "Wash your eyes with clean water" a mitigation measure?

        Output: 
        Explanation: Washing your eyes with clean water is a mitigation measure for the hazard of ink spillage
        since it reduces the harm caused by the serious eye damage. This is because the water will help wash the 
        ink out of the eye.
        Answer: mitigation.'''

        example_of_prevention = '''
        Example Input:
        For the hazard: "Slippage of weight for contraption" during the activity: "Using a spring contraption as a demonstration for a TPS presentation",
        given the potential consequences of the hazard: "Heavy impact when falling onto demonstator, causing injury" and who/what the hazard harms: "Demonstrator",
        is the following: "Keep away from below the contraption" a mitigation measure?
        
        Output:
        Explanation: "Keep away from below the contraption" is a prevention meausure for the hazard of
        slippage of weight for contraption since it reduces the likelihood of the consequence of the hazard:
        "Heavy impact when falling onto demonstator, causing injury". This is because
        it is less likely there will be a heavy impact falling onto the demonstrator if they are standing away from 
        below the contraption.
        Answer: prevention'''

        example_of_incorrect_mitigation = '''
        Example Input:
        For the hazard: "Broken shards of glass" during the activity: "Fluids laboratory", 
        given the potential consequences of the hazard: "Get trapped in soles of shoes" and who/what the hazard harms: "Students",
        is the following: "Vacate area of damage" a mitigation measure?

        Output:
        Exaplanation: "Vacate area of damage" is not a mitigation meausure for the hazard of broken shards of glass
        since it does not reduce the harm caused by the hazard; the broken shards of glass will still
        be on the floor and could still get trapped in the soles of shoes. It is also not a prevention measure since
        it does not reduce the likelihood of the hazard occurring; the hazard of "Broken shards of glass" will still
        occur if students vacate area of damage.
        Answer: neither'''

        return f'''
        {example_of_correct_mitigation}

        {example_of_prevention}

        {example_of_incorrect_mitigation}
        
        A 'mitigation measure' is defined as '{self.mitigation_definition}'.
        A 'prevention measure' is defined as '{self.prevention_definition}'. Given these definitions,
        explain why '{self.mitigation}' is either a mitigation measure, a prevention measure, 
        or neither a mitigation nor a prevention measure, for the following hazard: 
        '{self.hazard}' during the activity: '{self.activity}', given the potential consequences of the hazard:
        '{self.how_it_harms}' and who/what the hazard harms: '{self.who_it_harms}'.
        If it is a mitigation measure, answer mitigation. If it is a prevention meausure, answer prevention. 
        If it is neither a mitigation measure nor a prevention measure, answer neither. 
        The prompt output should be in the format:
        Explanation: your_explanation
        Answer: your_answer'''
    
    def get_shortform_feedback(self):
        return ShortformFeedback(positive_feedback=f"Correct! '{self.mitigation}' is a mitigation measure for the hazard: '{self.hazard}'.",
        negative_feedback=f"Incorrect. '{self.mitigation}' is not a mitigation measure for the hazard: '{self.hazard}'.")