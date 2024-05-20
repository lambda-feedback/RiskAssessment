# pytest -v -s local_tests.py

# The -s option above is so you can see printouts even if the test fails

from TestModelAccuracy import TestModelAccuracy
from LLMCaller import GPT_3_point_5_turbo

import re

try:
    from InputAndExpectedOutput import InputAndExpectedOutputForSinglePrompt
    from LLMCaller import *
    from PromptInputs import Activity
except ImportError:
    from .InputAndExpectedOutput import InputAndExpectedOutputForSinglePrompt
    from .LLMCaller import *
    from .PromptInputs import Activity

activities = [
    # InputAndExpectedOutputForSinglePrompt(input=Activity(activity='dog'), expected_output=False),
    # InputAndExpectedOutputForSinglePrompt(input=Activity(activity='Butterfly spotting'), expected_output=True),
    # InputAndExpectedOutputForSinglePrompt(input=Activity(activity='Climbing a mountain'), expected_output=True),
    # InputAndExpectedOutputForSinglePrompt(input=Activity(activity='Paris'), expected_output=False),
    # InputAndExpectedOutputForSinglePrompt(input=Activity(activity='table'), expected_output=False),
    # InputAndExpectedOutputForSinglePrompt(input=Activity(activity='cat'), expected_output=False),
    # InputAndExpectedOutputForSinglePrompt(input=Activity(activity='water'), expected_output=False),
    # InputAndExpectedOutputForSinglePrompt(input=Activity(activity='team'), expected_output=False),
    # InputAndExpectedOutputForSinglePrompt(input=Activity(activity='toothpaste'), expected_output=False),
    # InputAndExpectedOutputForSinglePrompt(input=Activity(activity='John\'s car'), expected_output=False),
    # InputAndExpectedOutputForSinglePrompt(input=Activity(activity='he'), expected_output=False),
    # InputAndExpectedOutputForSinglePrompt(input=Activity(activity='swimming'), expected_output=True),
    # InputAndExpectedOutputForSinglePrompt(input=Activity(activity='Cooking a meal'), expected_output=True),
    # InputAndExpectedOutputForSinglePrompt(input=Activity(activity='Painting a picture'), expected_output=True),
    # InputAndExpectedOutputForSinglePrompt(input=Activity(activity='Swimming in a pool'), expected_output=True),
    # InputAndExpectedOutputForSinglePrompt(input=Activity(activity='Writing a letter'), expected_output=True),
    # InputAndExpectedOutputForSinglePrompt(input=Activity(activity='Riding a bike'), expected_output=True),
    # InputAndExpectedOutputForSinglePrompt(input=Activity(activity='Singing a song'), expected_output=True),
    # InputAndExpectedOutputForSinglePrompt(input=Activity(activity='Building a sandcastle'), expected_output=True),
    # InputAndExpectedOutputForSinglePrompt(input=Activity(activity='Planting flowers'), expected_output=True),
    # InputAndExpectedOutputForSinglePrompt(input=Activity(activity='Chess'), expected_output=True),
    # InputAndExpectedOutputForSinglePrompt(input=Activity(activity='Marathon'), expected_output=True),
    # InputAndExpectedOutputForSinglePrompt(input=Activity(activity='Puzzle'), expected_output=True),
    # InputAndExpectedOutputForSinglePrompt(input=Activity(activity='Party'), expected_output=True),
    # InputAndExpectedOutputForSinglePrompt(input=Activity(activity='Movie'), expected_output=True),
    # InputAndExpectedOutputForSinglePrompt(input=Activity(activity='Working in a school building'), expected_output=True),
    InputAndExpectedOutputForSinglePrompt(input=Activity(activity='Fluids laboratory'), expected_output=True)
]

if __name__ == "__main__":
    
    test_accuracy = TestModelAccuracy(
        LLM=GPT_3_point_5_turbo(temperature=0.1, max_tokens=400),
        LLM_name='gpt-3.5-turbo',
        list_of_input_and_expected_outputs=activities,
        sheet_name='Activities',
        test_description='Evaluating prompt on Chat GPT generated data for activities'
        )
    test_accuracy.run_test()