from ..prompts.ControlMeasureClassification import ControlMeasureClassification
from ..utils.RegexPatternMatcher import RegexPatternMatcher

class MitigationInput__ControlMeasureClassificationPrompt(ControlMeasureClassification):
    def __init__(self, control_measure, activity, hazard, how_it_harms, who_it_harms):
        super().__init__(control_measure, activity, hazard, how_it_harms, who_it_harms)

    def get_shortform_feedback(self, feedback_type):
        if feedback_type == 'positive':
            return f"Correct! '{self.control_measure}' is a mitigation measure for the hazard: '{self.hazard}'."
        if feedback_type == 'both':
            return f"The mitigation measure you entered is both a prevention and a mitigation."
        if feedback_type == 'neither':
            return f"Incorrect."
        if feedback_type == 'misclassification':
            return f"Incorrect. You entered a prevention measure in the mitigation field."
    
    def get_longform_feedback(self, prompt_output, start_string='Mitigation Explanation', end_string='Answer'):
        regex_pattern_matcher = RegexPatternMatcher()
        return regex_pattern_matcher.extract_section_of_prompt_between_two_strings(prompt_output=prompt_output, start_string=start_string, end_string=end_string)
    
    # TODO: When you have hazard event input, can include in feedback.
    def get_recommendation(self, recommendation_type):
        if recommendation_type == 'both' or recommendation_type == 'misclassification':
            return f"""A prevention measure reduces the likelihood of the "event that leads to harm". On the other hand, a mitigation measure reduces the harm caused by the "event that leads to harm". Please use the above definitions to ammend your mitigation input."""

        if recommendation_type == 'neither':
            return """For the mitigation field, enter a control measure which reduces the harm caused by the "event that leads to harm"."""
