from PromptInputs import InputFieldClassification
from InputAndExpectedOutput import InputAndExpectedOutputForSinglePrompt
from TestModelAccuracy import TestModelAccuracy
from LLMCaller import OpenAILLM

# Define categories
categories = {
    "activity": [
        "Construction Site Work",
        "Cooking in a Restaurant Kitchen",
        "Operating Heavy Machinery",
        # "Swimming in a Pool",
        # "Driving on a Highway",
        # "Playing Sports",
        # "Working in an Office",
        # "Using Power Tools",
        # "Hiking in the Mountains",
        # "Playing at a Playground"
    ],
    "hazard": [
        "Unsecured scaffolding",
        "Hot surfaces",
        "Mechanical malfunction",
        # "Lack of lifeguard supervision",
        # "Reckless drivers",
        # "Lack of protective gear",
        # "Improperly stored cables",
        # "Electrical malfunction",
        # "Unstable terrain",
        # "Broken equipment"
    ],
    "event_that_leads_to_harm": [
        "Worker falling from scaffolding",
        "Chef burning hand on stove",
        "Operator caught in machinery",
        # "Swimmer drowning",
        # "Car collision",
        # "Athlete getting hit in the head",
        # "Employee tripping on cables",
        # "Worker receiving electric shock",
        # "Hiker slipping and falling",
        # "Child falling off monkey bars"
    ],
    "how_it_harms": [
        "Impact injury",
        "Burn injury",
        "Crushing injury",
        # "Drowning",
        # "Whiplash injury",
        # "Concussion",
        # "Fall injury",
        # "Electric shock injury",
        # "Sprained ankle or broken bone",
        # "Fractured arm"
    ],
    "who_it_harms": [
        "Construction workers",
        "Kitchen staff",
        "Machine operators",
        # "Swimmers",
        # "Drivers and passengers",
        # "Athletes",
        # "Office workers",
        # "Construction workers, technicians",
        # "Hikers",
        # "Children"
    ]
}

# Generate examples with expected outputs
examples_with_expected_outputs = [
    InputAndExpectedOutputForSinglePrompt(
        input=InputFieldClassification(input=item),
        expected_output=category
    )
    for category, items in categories.items()
    for item in items
]

if __name__ == "__main__":
    
    test_accuracy = TestModelAccuracy(
        LLM=OpenAILLM(),
        LLM_name='gpt-3.5-turbo',
        list_of_input_and_expected_outputs=examples_with_expected_outputs,
        sheet_name='Input Field Classification',
        test_description='First Input Field Classification Test'
        )
    test_accuracy.run_test()

