try:
    from InputAndExpectedOutput import InputAndExpectedOutput
    from LLMCaller import *
    from PromptInputs import Activity
except ImportError:
    from .InputAndExpectedOutput import InputAndExpectedOutput
    from .LLMCaller import *
    from .PromptInputs import Activity

activities = [
    InputAndExpectedOutput(input=Activity(activity='dog'), expected_output=False),
    InputAndExpectedOutput(input=Activity(activity='Butterfly spotting'), expected_output=True),
    InputAndExpectedOutput(input=Activity(activity='Climbing a mountain'), expected_output=True),
    InputAndExpectedOutput(input=Activity(activity='Paris'), expected_output=False),
    InputAndExpectedOutput(input=Activity(activity='table'), expected_output=False),
    InputAndExpectedOutput(input=Activity(activity='cat'), expected_output=False),
    InputAndExpectedOutput(input=Activity(activity='water'), expected_output=False),
    InputAndExpectedOutput(input=Activity(activity='team'), expected_output=False),
    InputAndExpectedOutput(input=Activity(activity='toothpaste'), expected_output=False),
    InputAndExpectedOutput(input=Activity(activity='John\'s car'), expected_output=False),
    InputAndExpectedOutput(input=Activity(activity='he'), expected_output=False),
    InputAndExpectedOutput(input=Activity(activity='swimming'), expected_output=True),
    InputAndExpectedOutput(input=Activity(activity='Cooking a meal'), expected_output=True),
    InputAndExpectedOutput(input=Activity(activity='Painting a picture'), expected_output=True),
    InputAndExpectedOutput(input=Activity(activity='Swimming in a pool'), expected_output=True),
    InputAndExpectedOutput(input=Activity(activity='Writing a letter'), expected_output=True),
    InputAndExpectedOutput(input=Activity(activity='Riding a bike'), expected_output=True),
    InputAndExpectedOutput(input=Activity(activity='Singing a song'), expected_output=True),
    InputAndExpectedOutput(input=Activity(activity='Building a sandcastle'), expected_output=True),
    InputAndExpectedOutput(input=Activity(activity='Planting flowers'), expected_output=True),
    InputAndExpectedOutput(input=Activity(activity='Chess'), expected_output=True),
    InputAndExpectedOutput(input=Activity(activity='Marathon'), expected_output=True),
    InputAndExpectedOutput(input=Activity(activity='Puzzle'), expected_output=True),
    InputAndExpectedOutput(input=Activity(activity='Party'), expected_output=True),
    InputAndExpectedOutput(input=Activity(activity='Movie'), expected_output=True)]