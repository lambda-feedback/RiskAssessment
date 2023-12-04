from TestModelAccuracy import TestModelAccuracy
from LLMCaller import OpenAILLM
from ExamplesGenerator import ExamplesGenerator
from PromptInputs import HowItHarms

class HowItHarmsExamplesGenerator(ExamplesGenerator):
    def generate_incorrect_example(self, correct_index, incorrect_index):
        return HowItHarms(
                activity=self.correct_examples_list[correct_index].activity, 
                hazard=self.correct_examples_list[correct_index].hazard, 
                how_it_harms=self.correct_examples_list[incorrect_index].how_it_harms)

correct_examples_list = [
        HowItHarms(
            hazard="Handling corrosive chemicals without protective gear",
            how_it_harms="Chemical burns",
            activity="Chemical handling"
        ),
        HowItHarms(
            hazard="Presence of combustible materials near an open flame",
            how_it_harms="Fires",
            activity="Fire safety demonstration")
        # HowItHarms(
        #     hazard="Frayed electrical cords or exposed wiring",
        #     how_it_harms="Electric shocks",
        #     activity="Electrical equipment maintenance"
        # ),
        # HowItHarms(
        #     hazard="Improperly stored cutting tools with exposed blades",
        #     how_it_harms="Cuts",
        #     activity="Tool maintenance"
        # ),
        # HowItHarms(
        #     hazard="Operating heavy machinery without hearing protection",
        #     how_it_harms="Hearing loss or auditory issues over time",
        #     activity="Heavy machinery operation"
        # ),
        # HowItHarms(
        #     hazard="Exposure to pathogens in a laboratory or healthcare setting",
        #     how_it_harms="Infections",
        #     activity="Laboratory work"
        # ),
        # HowItHarms(
        #     hazard="Operating industrial machinery without proper training or safety features",
        #     how_it_harms="Crushing injuries",
        #     activity="Industrial machinery operation"
        # ),
        # HowItHarms(
        #     hazard="Lack of shielding in an environment with radioactive materials",
        #     how_it_harms="Radiation exposure",
        #     activity="Working with radioactive materials"
        # ),
        # HowItHarms(
        #     hazard="Working at heights without proper fall protection",
        #     how_it_harms="Falls",
        #     activity="Working at heights"
        # ),
        # HowItHarms(
        #     hazard="Entering confined spaces without proper ventilation or rescue procedures",
        #     how_it_harms="Asphyxiation",
        #     activity="Working in confined spaces"
        # )
    ]

if __name__ == "__main__":
    how_it_harms_examples_generator = HowItHarmsExamplesGenerator(correct_examples_list=correct_examples_list)
    how_it_harms_examples = how_it_harms_examples_generator.get_input_and_expected_output_list()
    test_accuracy = TestModelAccuracy(LLM=OpenAILLM(),
                                                LLM_name='gpt-3.5-turbo',
                                                list_of_input_and_expected_outputs=how_it_harms_examples,
                                                sheet_name='How It Harms In Context')
    test_accuracy.run_test()