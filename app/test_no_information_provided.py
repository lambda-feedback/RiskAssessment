try:
    from .InputAndExpectedOutput import InputAndExpectedOutputForSinglePrompt
    from .LLMCaller import *
    from .PromptInputs import NoInformationProvided
    from .TestModelAccuracy import TestModelAccuracy
    from .example_risk_assessments import cybersecurity_risks, create_unique_set_of_control_measures
except:
    from InputAndExpectedOutput import InputAndExpectedOutputForSinglePrompt
    from LLMCaller import *
    from PromptInputs import NoInformationProvided
    from TestModelAccuracy import TestModelAccuracy
    from example_risk_assessments import cybersecurity_risks, create_unique_set_of_control_measures

no_information_provided_examples = [
    "Leave blank",
    "No data",
    "Not provided",
    "Not applicable at this time",
    "Not applicable to me",
    "Not applicable in this context",
    "Nil",
    "Blank",
    "Unspecified",
    "No content",
]

information_provided_examples = [
    # Prevention
    "Using safe climbing techniques",
    "Maintaining safe distance in traffic",
    
    # # Mitigation
    "Using proper climbing gear",
    "Wearing a helmet while biking",
]

examples = []

for example in no_information_provided_examples:
    examples.append(InputAndExpectedOutputForSinglePrompt(prompt_input_object=NoInformationProvided(input=example), expected_output='no information provided'))

for example in information_provided_examples:
    examples.append(InputAndExpectedOutputForSinglePrompt(prompt_input_object=NoInformationProvided(input=example), expected_output='control measure'))

def test_no_information_provided_prompt(risk_assessments_dict, examples, LLM, is_first_test: bool = False):
    risk_assessments = risk_assessments_dict['risk_assessments']

    unique_control_measures_in_risk_domain = create_unique_set_of_control_measures(risk_assessments)
    
    for control_measure in unique_control_measures_in_risk_domain:
        examples.append(InputAndExpectedOutputForSinglePrompt(prompt_input_object=NoInformationProvided(input=control_measure), expected_output='control measure'))

    test_accuracy = TestModelAccuracy(
                        LLM=LLM,
                        is_first_test=is_first_test,
                        domain=risk_assessments_dict['risk_domain'],       
                        list_of_input_and_expected_outputs=examples,
                        examples_gathered_or_generated_message='Risk assessments gathered and not AI-generated',
                        sheet_name='No Information Provided')
    
    test_accuracy.run_test()

if __name__ == "__main__":
    test_no_information_provided_prompt(risk_assessments_dict=cybersecurity_risks
                                    , examples=examples
                                    , LLM=MistralLLM(model='open-mixtral-8x7b', temperature=0.1, max_tokens=300)
                                    , is_first_test=True)

    