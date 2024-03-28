# from PromptInputs import EventCausedByHazard
# from TestModelAccuracy import TestModelAccuracy
# from ExamplesGenerator import ExamplesGeneratorFromCorrectExamples
# from LLMCaller import OpenAILLM

# class EventCausedByHazardExamplesGenerator(ExamplesGeneratorFromCorrectExamples):
#     def generate_incorrect_example(self, correct_index, incorrect_index):
#         return EventCausedByHazard(
#                 hazard=self.correct_examples_list[correct_index].hazard,
#                 hazard_event=self.correct_examples_list[incorrect_index].hazard_event)

# events_caused_by_hazard = [
#     EventCausedByHazard(hazard="Slippery floors", hazard_event="Employee slipping and falling on a wet floor"),
#     EventCausedByHazard(hazard="Sharp objects", hazard_event="Worker cutting hand on a knife blade"),
#     EventCausedByHazard(hazard="Toxic chemicals", hazard_event="Lab technician inhaling toxic fumes"),
#     EventCausedByHazard(hazard="Heavy machinery", hazard_event="Operator caught in a conveyor belt"),
#     EventCausedByHazard(hazard="High voltage equipment", hazard_event="Electrician receiving a shock while working on wiring"),
#     EventCausedByHazard(hazard="Extreme temperatures", hazard_event="Worker suffering from heatstroke in a hot environment"),
#     EventCausedByHazard(hazard="Unstable structures", hazard_event="Construction worker trapped under collapsed scaffolding"),
#     EventCausedByHazard(hazard="Fast-moving vehicles", hazard_event="Pedestrian hit by a speeding car"),
#     EventCausedByHazard(hazard="Uncontrolled fires", hazard_event="Kitchen fire causing burns to restaurant staff"),
#     EventCausedByHazard(hazard="Loose objects", hazard_event="Object falling from height and striking a passerby")
# ]

# examples_generator = EventCausedByHazardExamplesGenerator(correct_examples_list=events_caused_by_hazard)

# examples = examples_generator.get_input_and_expected_output_list()

# test_accuracy = TestModelAccuracy(test_description="""Testing EventCausedByHazard prompt for examples generated using Chat GPT""",
#                                     LLM=OpenAILLM(),
#                                             LLM_name='gpt-3.5-turbo',
#                                             list_of_input_and_expected_outputs=examples,
#                                             sheet_name='Event Caused By Hazard')
# test_accuracy.run_test()