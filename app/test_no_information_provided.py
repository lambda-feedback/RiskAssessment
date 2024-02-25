from InputAndExpectedOutput import InputAndExpectedOutputForSinglePrompt
from LLMCaller import *
from PromptInputs import NoInformationProvided
from TestModelAccuracy import TestModelAccuracy

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
    "No content"
]

information_provided_examples = [
    # Hazard
    "Bike collides with car",
    "Fall during climbing ascent",
    
    # How it harms
    "Impact injuries from bike collision",
    "Injuries sustained in climbing fall",
    
    # Who it harms
    "Biker and car occupants",
    "Climber and belayer",

    # Prevention
    "Using safe climbing techniques",
    "Maintaining safe distance in traffic",
    
    # Mitigation
    "Using proper climbing gear",
    "Wearing a helmet while biking",
]

examples = []

for example in no_information_provided_examples:
    examples.append(InputAndExpectedOutputForSinglePrompt(input=NoInformationProvided(input=example), expected_output=True))

for example in information_provided_examples:
    examples.append(InputAndExpectedOutputForSinglePrompt(input=NoInformationProvided(input=example), expected_output=False))

if __name__ == "__main__":
    
    test_accuracy = TestModelAccuracy(
        LLM=OpenAILLM(),
        LLM_name='gpt-3.5-turbo',
        list_of_input_and_expected_outputs=examples,
        sheet_name='No Information Provided',
        test_description='Evaluating prompt on Chat GPT generated data which has examples of no information provided and information provided.'
        )
    test_accuracy.run_test()