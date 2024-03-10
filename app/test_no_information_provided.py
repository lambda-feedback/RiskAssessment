from InputAndExpectedOutput import InputAndExpectedOutputForSinglePrompt
from LLMCaller import *
from PromptInputs import NoInformationProvided
from TestModelAccuracy import TestModelAccuracy

from example_risk_assessments import unique_activities, unique_hazards, unique_how_it_harms, unique_who_it_harms, unique_control_measures

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
    # # Hazard
    # "Bike collides with car",
    # "Fall during climbing ascent",
    
    # # How it harms
    # "Impact injuries from bike collision",
    # "Injuries sustained in climbing fall",
    
    # # Who it harms
    # "Biker and car occupants",
    # "Climber and belayer",

    # Prevention
    "Using safe climbing techniques",
    "Maintaining safe distance in traffic",
    
    # Mitigation
    "Using proper climbing gear",
    "Wearing a helmet while biking",
]

examples_dict = {
    'No information provided': no_information_provided_examples,
    'Information provided about physical risks': information_provided_examples
}

number_of_examples_in_each_domain = {key: len(value) for key, value in examples_dict.items()}

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

for example in unique_examples:
    examples.append(InputAndExpectedOutputForSinglePrompt(input=NoInformationProvided(input=example), expected_output='control measure'))

if __name__ == "__main__":

    test_accuracy = TestModelAccuracy(
        LLM=OpenAILLM(),
        # LLM=AnthropicLLM(name='claude-3-sonnet-20240229', system_message='You are capable of following instructions and learning patterns from examples. '),
        # LLM=MixtralLLM(),
        list_of_input_and_expected_outputs=examples,
        number_of_examples_in_each_domain=number_of_examples_in_each_domain,
        sheet_name='No Information Provided',
        examples_gathered_or_generated_message='"No information" examples generated using Chat GPT.\n\n "Information provided" examples gathered from student risk assessments.'
        )
    test_accuracy.run_test()