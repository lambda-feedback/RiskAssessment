from InputAndExpectedOutput import InputAndExpectedOutputForSinglePrompt
from LLMCaller import *
from PromptInputs import NoInformationProvided
from TestModelAccuracy import TestModelAccuracy

from example_risk_assessments import unique_activities, unique_hazards, unique_how_it_harms, unique_who_it_harms, unique_control_measures

no_information_provided_examples = [
    # "Leave blank",
    # "No data",
    # "Not provided",
    "Not applicable at this time",
    "Not applicable to me",
    "Not applicable in this context",
    # "Nil",
    # "Blank",
    # "Unspecified",
    # "No content"
]

information_provided_examples = [
    # Hazard
    "Bike collides with car",
    "Fall during climbing ascent",
    
    # # How it harms
    # "Impact injuries from bike collision",
    # "Injuries sustained in climbing fall",
    
    # # Who it harms
    # "Biker and car occupants",
    # "Climber and belayer",

    # # Prevention
    # "Using safe climbing techniques",
    # "Maintaining safe distance in traffic",
    
    # # Mitigation
    # "Using proper climbing gear",
    # "Wearing a helmet while biking",
]

unique_examples = []
# unique_examples.extend(unique_activities)
# unique_examples.extend(unique_hazards)
# unique_examples.extend(unique_how_it_harms)
# unique_examples.extend(unique_who_it_harms)
unique_examples.extend(unique_control_measures)

examples = []

for example in no_information_provided_examples:
    examples.append(InputAndExpectedOutputForSinglePrompt(input=NoInformationProvided(input=example), expected_output='no information provided'))

for example in information_provided_examples:
    examples.append(InputAndExpectedOutputForSinglePrompt(input=NoInformationProvided(input=example), expected_output='control measure'))

# for example in unique_examples:
#     examples.append(InputAndExpectedOutputForSinglePrompt(input=NoInformationProvided(input=example), expected_output='control measure'))

if __name__ == "__main__":
    
    LLM = MixtralLLM()

    test_accuracy = TestModelAccuracy(
        LLM=LLM,
        LLM_name=LLM.name,
        list_of_input_and_expected_outputs=examples,
        sheet_name='No Information Provided',
        test_description='Evaluating Mixtral LLM with same prompt as above on Chat GPT generated data which has examples of no information provided and information provided.'
        )
    test_accuracy.run_test()