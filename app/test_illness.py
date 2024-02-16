from PromptInputs import Illness
from TestModelAccuracy import TestModelAccuracy
from LLMCaller import OpenAILLM

from InputAndExpectedOutput import InputAndExpectedOutputForSinglePrompt

examples = [
    # InputAndExpectedOutputForSinglePrompt(input=Illness(input="Respiratory illnesses caused by chemical exposure"), expected_output=True),
    # InputAndExpectedOutputForSinglePrompt(input=Illness(input="Heat-related illnesses due to prolonged exposure to high temperatures"), expected_output=True),
    # InputAndExpectedOutputForSinglePrompt(input=Illness(input="Musculoskeletal disorders resulting from improper ergonomic setups"), expected_output=True),
    # InputAndExpectedOutputForSinglePrompt(input=Illness(input="Foodborne illnesses due to improper handling of food items"), expected_output=True),
    # InputAndExpectedOutputForSinglePrompt(input=Illness(input="Infectious disease resulting from lack of proper sanitation practices"), expected_output=True),
    # InputAndExpectedOutputForSinglePrompt(input=Illness(input="Respiratory infections due to exposure to airborne pathogens"), expected_output=True),
    # InputAndExpectedOutputForSinglePrompt(input=Illness(input="Heat exhaustion resulting from extreme heat and dehydration"), expected_output=True),
    # InputAndExpectedOutputForSinglePrompt(input=Illness(input="Food poisoning caused by consuming contaminated food"), expected_output=True),
    # InputAndExpectedOutputForSinglePrompt(input=Illness(input="Gastrointestinal illnesses from consuming contaminated food"), expected_output=True),
    # InputAndExpectedOutputForSinglePrompt(input=Illness(input="Vector-borne diseases transmitted by infected insects"), expected_output=True),

    InputAndExpectedOutputForSinglePrompt(input=Illness(input="Crush injuries caused by inadequate training on machinery operation"), expected_output=False),
    InputAndExpectedOutputForSinglePrompt(input=Illness(input="Serious head injuries or fractures due to absence of fall protection measures"), expected_output=False),
    InputAndExpectedOutputForSinglePrompt(input=Illness(input="Electric shock injuries resulting from faulty wiring and inadequate electrical safety measures"), expected_output=False),
    InputAndExpectedOutputForSinglePrompt(input=Illness(input="Hearing loss caused by high noise levels in the manufacturing plant"), expected_output=False),
    InputAndExpectedOutputForSinglePrompt(input=Illness(input="Back injuries due to improper lifting techniques and heavy lifting tasks"), expected_output=False),
    InputAndExpectedOutputForSinglePrompt(input=Illness(input="Fractured wrist from a fall"), expected_output=False),
    InputAndExpectedOutputForSinglePrompt(input=Illness(input="Lacerations from a knife accident"), expected_output=False),
    InputAndExpectedOutputForSinglePrompt(input=Illness(input="Sprained ankle while playing sports"), expected_output=False),
    InputAndExpectedOutputForSinglePrompt(input=Illness(input="Concussion from a car collision"), expected_output=False),
    InputAndExpectedOutputForSinglePrompt(input=Illness(input="Burns from touching hot surfaces"), expected_output=False),

    # InputAndExpectedOutputForSinglePrompt(input=Illness(input="Chemical exposure resulting from inadequate safety measures"), expected_output=False),
    # InputAndExpectedOutputForSinglePrompt(input=Illness(input="Prolonged exposure to high temperatures without proper precautions"), expected_output=False),
    # InputAndExpectedOutputForSinglePrompt(input=Illness(input="Improper ergonomic setups in the office"), expected_output=False),
    # InputAndExpectedOutputForSinglePrompt(input=Illness(input="Inadequate training on machinery operation"), expected_output=False),
    # InputAndExpectedOutputForSinglePrompt(input=Illness(input="Absence of proper fall protection measures"), expected_output=False),
    # InputAndExpectedOutputForSinglePrompt(input=Illness(input="Faulty wiring and inadequate electrical safety measures"), expected_output=False),
    # InputAndExpectedOutputForSinglePrompt(input=Illness(input="Improper handling of food items"), expected_output=False),
    # InputAndExpectedOutputForSinglePrompt(input=Illness(input="High noise levels in the manufacturing plant"), expected_output=False),
    # InputAndExpectedOutputForSinglePrompt(input=Illness(input="Lack of proper sanitation practices in healthcare facilities"), expected_output=False),
    # InputAndExpectedOutputForSinglePrompt(input=Illness(input="Improper lifting techniques and heavy lifting tasks in the warehouse"), expected_output=False)
]

test_accuracy = TestModelAccuracy(test_description="""Testing Illness prompt for examples generated using Chat GPT""",
                                    LLM=OpenAILLM(),
                                            LLM_name='gpt-3.5-turbo',
                                            list_of_input_and_expected_outputs=examples,
                                            sheet_name='Illness')
test_accuracy.run_test()