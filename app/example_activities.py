try:
    from InputAndExpectedOutput import InputAndExpectedOutput
    from LLMCaller import *
    from PromptInputs import Activity
except ImportError:
    from .InputAndExpectedOutput import InputAndExpectedOutput
    from .LLMCaller import *
    from .PromptInputs import Activity

activities = [
    InputAndExpectedOutput(input='dog', expected_output=False),
    InputAndExpectedOutput(input='Butterfly spotting', expected_output=True),
    InputAndExpectedOutput(input='Climbing a mountain', expected_output=True),
    InputAndExpectedOutput(input='Paris', expected_output=False),
    InputAndExpectedOutput(input='table', expected_output=False),
    InputAndExpectedOutput(input='cat', expected_output=False),
    InputAndExpectedOutput(input='water', expected_output=False),
    InputAndExpectedOutput(input='team', expected_output=False),
    InputAndExpectedOutput(input='toothpaste', expected_output=False),
    InputAndExpectedOutput(input='John\'s car', expected_output=False),
    InputAndExpectedOutput(input='he', expected_output=False),
    InputAndExpectedOutput(input='swimming', expected_output=True),
    InputAndExpectedOutput(input='Cooking a meal', expected_output=True),
    InputAndExpectedOutput(input='Painting a picture', expected_output=True),
    InputAndExpectedOutput(input='Swimming in a pool', expected_output=True),
    InputAndExpectedOutput(input='Writing a letter', expected_output=True),
    InputAndExpectedOutput(input='Riding a bike', expected_output=True),
    InputAndExpectedOutput(input='Singing a song', expected_output=True),
    InputAndExpectedOutput(input='Building a sandcastle', expected_output=True),
    InputAndExpectedOutput(input='Planting flowers', expected_output=True),
    InputAndExpectedOutput(input='Chess', expected_output=True),
    InputAndExpectedOutput(input='Marathon', expected_output=True),
    InputAndExpectedOutput(input='Puzzle', expected_output=True),
    InputAndExpectedOutput(input='Party', expected_output=True),
    InputAndExpectedOutput(input='Movie', expected_output=True)]