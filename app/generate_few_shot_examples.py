from PromptInputs import PromptInput, Prevention, Mitigation

from example_risk_assessments import RA_4, RA_5, RA_incorrect_prevention_and_mitigation

def get_prevention_prompt(risk_assessment):
    prevention = risk_assessment.get_prevention_input()

    return prevention.generate_prompt()

def get_mitigation_prompt(risk_assessment):
    mitigation = risk_assessment.get_mitigation_input()

    return mitigation.generate_prompt()

if __name__ == "__main__":
    # print(get_mitigation_prompt(RA_4))
    # print(get_prevention_prompt(RA_5))
    print(get_prevention_prompt(RA_incorrect_prevention_and_mitigation))