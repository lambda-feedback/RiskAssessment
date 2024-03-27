try:
    from .PromptInputs import PromptInput
    from .RiskAssessment import RiskAssessment
except:
    from PromptInputs import PromptInput
    from RiskAssessment import RiskAssessment

class InputAndExpectedOutputForSinglePrompt:
    def __init__(self, prompt_input_object: PromptInput, expected_output):
        self.prompt_input_object = prompt_input_object
        self.expected_output = expected_output

class InputAndExpectedOutputForCombinedPrompts:
    def __init__(self, risk_assessment: RiskAssessment, expected_output):
        self.risk_assessment = risk_assessment
        self.expected_output = expected_output