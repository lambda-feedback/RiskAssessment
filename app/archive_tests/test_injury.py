# from PromptInputs import Injury
# from TestModelAccuracy import TestModelAccuracy
# from LLMCaller import GPT_3_point_5_turbo

# from InputAndExpectedOutput import InputAndExpectedOutputForSinglePrompt

# examples = [
#     # InputAndExpectedOutputForSinglePrompt(input=Injury(input="Crush injuries caused by inadequate training on machinery operation"), expected_output=True),
#     # InputAndExpectedOutputForSinglePrompt(input=Injury(input="Serious head injuries or fractures due to absence of fall protection measures"), expected_output=True),
#     # InputAndExpectedOutputForSinglePrompt(input=Injury(input="Electric shock injuries resulting from faulty wiring and inadequate electrical safety measures"), expected_output=True),
#     # InputAndExpectedOutputForSinglePrompt(input=Injury(input="Hearing loss caused by high noise levels in the manufacturing plant"), expected_output=True),
#     # InputAndExpectedOutputForSinglePrompt(input=Injury(input="Back injuries due to improper lifting techniques and heavy lifting tasks"), expected_output=True),
#     # InputAndExpectedOutputForSinglePrompt(input=Injury(input="Fractured wrist from a fall"), expected_output=True),
#     # InputAndExpectedOutputForSinglePrompt(input=Injury(input="Lacerations from a knife accident"), expected_output=True),
#     # InputAndExpectedOutputForSinglePrompt(input=Injury(input="Sprained ankle while playing sports"), expected_output=True),
#     # InputAndExpectedOutputForSinglePrompt(input=Injury(input="Concussion from a car collision"), expected_output=True),
#     # InputAndExpectedOutputForSinglePrompt(input=Injury(input="Burns from touching hot surfaces"), expected_output=True),

#     # InputAndExpectedOutputForSinglePrompt(input=Injury(input="Respiratory illnesses caused by chemical exposure"), expected_output=False),
#     # InputAndExpectedOutputForSinglePrompt(input=Injury(input="Heat-related illnesses due to prolonged exposure to high temperatures"), expected_output=False),
#     # InputAndExpectedOutputForSinglePrompt(input=Injury(input="Musculoskeletal disorders resulting from improper ergonomic setups"), expected_output=False),
#     # InputAndExpectedOutputForSinglePrompt(input=Injury(input="Foodborne illnesses due to improper handling of food items"), expected_output=False),
#     # InputAndExpectedOutputForSinglePrompt(input=Injury(input="Infectious disease resulting from lack of proper sanitation practices"), expected_output=False),
#     # InputAndExpectedOutputForSinglePrompt(input=Injury(input="Respiratory infections due to exposure to airborne pathogens"), expected_output=False),
#     # InputAndExpectedOutputForSinglePrompt(input=Injury(input="Heat exhaustion resulting from extreme heat and dehydration"), expected_output=False),
#     # InputAndExpectedOutputForSinglePrompt(input=Injury(input="Food poisoning caused by consuming contaminated food"), expected_output=False),
#     # InputAndExpectedOutputForSinglePrompt(input=Injury(input="Gastrointestinal illnesses from consuming contaminated food"), expected_output=False),
#     # InputAndExpectedOutputForSinglePrompt(input=Injury(input="Vector-borne diseases transmitted by infected insects"), expected_output=False),

#     # InputAndExpectedOutputForSinglePrompt(input=Injury(input="Chemical exposure resulting from inadequate safety measures"), expected_output=False),
#     # InputAndExpectedOutputForSinglePrompt(input=Injury(input="Prolonged exposure to high temperatures without proper precautions"), expected_output=False),
#     # InputAndExpectedOutputForSinglePrompt(input=Injury(input="Improper ergonomic setups in the office"), expected_output=False),
#     # InputAndExpectedOutputForSinglePrompt(input=Injury(input="Inadequate training on machinery operation"), expected_output=False),
#     # InputAndExpectedOutputForSinglePrompt(input=Injury(input="Absence of proper fall protection measures"), expected_output=False),
#     # InputAndExpectedOutputForSinglePrompt(input=Injury(input="Faulty wiring and inadequate electrical safety measures"), expected_output=False),
#     # InputAndExpectedOutputForSinglePrompt(input=Injury(input="Improper handling of food items"), expected_output=False),
#     InputAndExpectedOutputForSinglePrompt(input=Injury(input="High noise levels in the manufacturing plant"), expected_output=False),
# #     InputAndExpectedOutputForSinglePrompt(input=Injury(input="Lack of proper sanitation practices in healthcare facilities"), expected_output=False),
# #     InputAndExpectedOutputForSinglePrompt(input=Injury(input="Improper lifting techniques and heavy lifting tasks in the warehouse"), expected_output=False)
# ]

# test_accuracy = TestModelAccuracy(test_description="""Testing Injury prompt for examples generated using Chat GPT""",
#                                     LLM=GPT_3_point_5_turbo(temperature=0.1, max_tokens=400),
#                                             LLM_name='gpt-3.5-turbo',
#                                             list_of_input_and_expected_outputs=examples,
#                                             sheet_name='Injury')
# test_accuracy.run_test()