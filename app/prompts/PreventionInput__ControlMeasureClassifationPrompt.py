from ..prompts.ControlMeasureClassification import ControlMeasureClassification
from ..utils.RegexPatternMatcher import RegexPatternMatcher

class PreventionInput__ControlMeasureClassifationPrompt(ControlMeasureClassification):
    def __init__(self, control_measure, activity, hazard, how_it_harms, who_it_harms):
        super().__init__(control_measure, activity, hazard, how_it_harms, who_it_harms)
    
    def get_field_checked(self):
        return 'Prevention'
    
    def get_shortform_feedback(self, feedback_type):
        if feedback_type == 'positive':
            return f"Correct! '{self.control_measure}' is a prevention measure for the hazard: '{self.hazard}'"
        if feedback_type == 'both':
            return f"The prevention you entered is both a mitigation and a prevention measure"
        if feedback_type == 'neither':
            return f"Incorrect. '{self.control_measure}' is not a prevention measure for the hazard: '{self.hazard}'."
        if feedback_type == 'misclassification':
            return f"Incorrect. You entered a mitigation measure in the prevention field."
    
    def get_longform_feedback(self, prompt_output, start_string='Prevention Explanation', end_string='Mitigation Explanation'):
        regex_pattern_matcher = RegexPatternMatcher()
        return regex_pattern_matcher.extract_section_of_prompt_between_two_strings(prompt_output=prompt_output, start_string=start_string, end_string=end_string)

    # TODO: When you have hazard event input, can include in feedback.
    def get_recommendation(self, recommendation_type):
        if recommendation_type == 'both' or recommendation_type == 'misclassification':
            return f"""A mitigation measure reduces the harm caused by the "event that leads to harm". On the other hand, a prevention measure reduces the likelihood of the "event that leads to harm". Please use the above definitions to ammend your prevention input."""

        if recommendation_type == 'neither':
            return """For the prevention field, enter a control measure which reduces the likelihood of the "event that leads to harm"."""
    
