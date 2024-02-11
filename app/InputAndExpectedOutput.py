from PromptInputs import PromptInput
from RiskAssessment import RiskAssessment

class InputAndExpectedOutputForSinglePrompt:
    def __init__(self, input: PromptInput, expected_output):
        self.input = input
        self.expected_output = expected_output

class InputAndExpectedOutputForCombinedPrompts:
    def __init__(self, risk_assessment: RiskAssessment, final_prompt_input: PromptInput, expected_output):
        self.risk_assessment = risk_assessment
        self.final_prompt_input = final_prompt_input
        self.expected_output = expected_output