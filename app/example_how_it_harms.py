from PromptInputs import HowItHarms
from InputAndExpectedOutput import InputAndExpectedOutput
from LLMCaller import OpenAILLM

class HowItHarmsLists:

    def __init__(self):
        self.correct_hazard_list = [
            HowItHarms(
                hazard="Handling corrosive chemicals without protective gear",
                how_it_harms="Chemical burns",
                activity="Chemical handling"
            ),
            HowItHarms(
                hazard="Presence of combustible materials near an open flame",
                how_it_harms="Fires",
                activity="Fire safety demonstration"),
            HowItHarms(
                hazard="Frayed electrical cords or exposed wiring",
                how_it_harms="Electric shocks",
                activity="Electrical equipment maintenance"
            ),
            HowItHarms(
                hazard="Improperly stored cutting tools with exposed blades",
                how_it_harms="Cuts",
                activity="Tool maintenance"
            ),
            HowItHarms(
                hazard="Exposure to pathogens in a laboratory or healthcare setting",
                how_it_harms="Infections",
                activity="Laboratory work"
            ),
            HowItHarms(
                hazard="Operating heavy machinery without hearing protection",
                how_it_harms="Hearing loss or auditory issues over time",
                activity="Heavy machinery operation"
            ),
            HowItHarms(
                hazard="Working at heights without proper fall protection",
                how_it_harms="Falls",
                activity="Working at heights"
            ),
            HowItHarms(
                hazard="Operating industrial machinery without proper training or safety features",
                how_it_harms="Crushing injuries",
                activity="Industrial machinery operation"
            ),
            HowItHarms(
                hazard="Lack of shielding in an environment with radioactive materials",
                how_it_harms="Radiation exposure",
                activity="Working with radioactive materials"
            ),
            HowItHarms(
                hazard="Entering confined spaces without proper ventilation or rescue procedures",
                how_it_harms="Asphyxiation",
                activity="Working in confined spaces"
            )
        ]
        self.incorrect_hazard_list = self.generate_incorrect_hazard_list()

    def generate_incorrect_hazard_list(self):
        incorrect_hazard_list = []

        for i in range(len(self.correct_hazard_list)):
            activity_and_hazard_index = i
            how_it_harms_index = (i+1) % len(self.correct_hazard_list)
            incorrect_hazard_list.append(HowItHarms(
                activity=self.correct_hazard_list[activity_and_hazard_index].activity, 
                hazard=self.correct_hazard_list[activity_and_hazard_index].hazard, 
                how_it_harms=self.correct_hazard_list[how_it_harms_index].how_it_harms))
            
        return incorrect_hazard_list
    
    def get_input_and_expected_output(self, how_it_harms: HowItHarms, expected_output: bool):
        return InputAndExpectedOutput(input=how_it_harms, expected_output=expected_output)
    
    def get_input_and_expected_output_list(self):
        input_and_expected_output_list = []
        
        for correct_hazard in self.correct_hazard_list:
            input_and_expected_output_list.append(self.get_input_and_expected_output(how_it_harms=correct_hazard, expected_output=True))
        
        for incorrect_hazard in self.incorrect_hazard_list:
            input_and_expected_output_list.append(self.get_input_and_expected_output(how_it_harms=incorrect_hazard, expected_output=False))
        
        return input_and_expected_output_list
