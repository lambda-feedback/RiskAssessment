from PromptInputs import *
from LLMCaller import GPT_3_point_5_turbo, AnthropicLLM
from InputAndExpectedOutput import InputAndExpectedOutputForSinglePrompt
from TestModelAccuracy import TestModelAccuracy

no_harm_caused = [
    'A cyber attack',
    "A student accidentally spills boiling hot water",
    "The climber is bouldering up a rock face",
    "A fire breaks out on the stove",
    'The person hits the ground',
    'The cigarette ignites a fire',
    'A student accidentally spills boiling hot water',
    'The climber is bouldering up a rock face',
    'The climber lands awkwardly on the ground',
    'The chef accidentally comes into contact with the fire or heat source',
    'The wildfire spreads towards nearby homes',
    'The campfire gets out of control and starts a wildfire',
    'A volcano erupts, releasing ash clouds into the atmosphere',
    'The residents are living near an active volcano',
    'Ash and gases are released into the atmosphere'

]

harm_caused = [
    'The cyclist sustains a head injury',
    'The cyclist is injured in the collision',
    'People below the ladder are impacted by the falling person',
    "The cyclist's head impacts the ground or another hard surface",
    'The awkward landing causes injury to the climber',
    'The chef sustains burns from the contact',
    'The homes are engulfed in the wildfire',
    'The shaking leads to the roads cracking and breaking',
    'Ecosystems are damaged by the lava, ash, and gases'
]

examples = []

for example in no_harm_caused:
    examples.append(InputAndExpectedOutputForSinglePrompt(prompt_input_object=DoesPhraseReferToEventOrHarmCaused(input=example), expected_output=False))

for example in harm_caused:
    examples.append(InputAndExpectedOutputForSinglePrompt(prompt_input_object=DoesPhraseReferToEventOrHarmCaused(input=example), expected_output=True))

def test_event_or_harm_caused_prompt(risk_assessments_dict, examples, LLM, is_first_test: bool):
    test_accuracy = TestModelAccuracy(
                        LLM=LLM,
                        is_first_test=is_first_test,
                        domain="NA",       
                        list_of_input_and_expected_outputs=examples,
                        examples_gathered_or_generated_message='Risk assessments gathered and not AI-generated',
                        sheet_name='Event or Harm Caused')
    
    test_accuracy.run_test()

if __name__ == '__main__':
    test_event_or_harm_caused_prompt(
        LLM=GPT_3_point_5_turbo(temperature=0.1),
        risk_assessments_dict={},
        examples=examples,
        is_first_test=True)