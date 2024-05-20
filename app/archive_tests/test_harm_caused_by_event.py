# from PromptInputs import HarmCausedAndHazardEventByEvent
# from TestModelAccuracy import TestModelAccuracy
# from LLMCaller import GPT_3_point_5_turbo

# from ExamplesGenerator import ExamplesGeneratorFromCorrectExamples

# class HarmCausedAndHazardEventByEventExamplesGenerator(ExamplesGeneratorFromCorrectExamples):
#     def generate_incorrect_example(self, correct_index, incorrect_index):
#         return HarmCausedAndHazardEventByEvent(
#                 hazard_event=self.correct_examples_list[correct_index].hazard_event,
#                 how_it_harms=self.correct_examples_list[incorrect_index].how_it_harms)

# correct_examples = [
#     HarmCausedAndHazardEventByEvent(hazard_event="Employee slipping and falling on a wet floor", how_it_harms="Impact injury"),
#     HarmCausedAndHazardEventByEvent(hazard_event="Lab technician inhaling toxic fumes", how_it_harms="Respiratory irritation"),
#     HarmCausedAndHazardEventByEvent(hazard_event="Operator caught in a conveyor belt", how_it_harms="Amputation"),
#     HarmCausedAndHazardEventByEvent(hazard_event="Electrician receiving a shock while working on wiring", how_it_harms="Cardiac arrest"),
#     HarmCausedAndHazardEventByEvent(hazard_event="Worker cutting hand on a knife blade", how_it_harms="Cut injury"),
#     HarmCausedAndHazardEventByEvent(hazard_event="Worker suffering from heatstroke in a hot environment", how_it_harms="Heatstroke"),
#     HarmCausedAndHazardEventByEvent(hazard_event="Pedestrian hit by a speeding car", how_it_harms="Brain injury"),
#     HarmCausedAndHazardEventByEvent(hazard_event="Kitchen fire causing burns to restaurant staff", how_it_harms="Burn injury"),
#     HarmCausedAndHazardEventByEvent(hazard_event="Construction worker trapped under collapsed scaffolding", how_it_harms="Suffocation"),
#     HarmCausedAndHazardEventByEvent(hazard_event="Chemical spill in a laboratory", how_it_harms="Chemical burns")
# ]

# examples_generator = HarmCausedAndHazardEventByEventExamplesGenerator(correct_examples_list=correct_examples)

# examples = examples_generator.get_input_and_expected_output_list()

# test_accuracy = TestModelAccuracy(test_description="""Testing EventCausedByHazard prompt for examples generated using Chat GPT""",
#                                     LLM=GPT_3_point_5_turbo(temperature=0.1, max_tokens=400),
#                                             LLM_name='gpt-3.5-turbo',
#                                             list_of_input_and_expected_outputs=examples,
#                                             sheet_name='Harm Caused By Event')
# test_accuracy.run_test()