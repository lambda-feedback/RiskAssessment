from PromptInputs import HowItHarms

hazard_list = [
    HowItHarms(
        hazard="Handling corrosive chemicals without protective gear",
        how_it_harms="Chemical burns, respiratory issues, and health problems"
    ),
    HowItHarms(
        hazard="Presence of combustible materials near an open flame",
        how_it_harms="Fires, causing burns, property damage, and potential loss of life"
    ),
    HowItHarms(
        hazard="Frayed electrical cords or exposed wiring",
        how_it_harms="Electric shocks, burns, and the risk of fire"
    ),
    HowItHarms(
        hazard="Improperly stored cutting tools with exposed blades",
        how_it_harms="Cuts, punctures, and injuries"
    ),
    HowItHarms(
        hazard="Exposure to pathogens in a laboratory or healthcare setting",
        how_it_harms="Infections, illnesses, and the spread of diseases"
    ),
    HowItHarms(
        hazard="Operating heavy machinery without hearing protection",
        how_it_harms="Hearing loss or auditory issues over time"
    ),
    HowItHarms(
        hazard="Working at heights without proper fall protection",
        how_it_harms="Falls, resulting in injuries such as fractures or concussions"
    ),
    HowItHarms(
        hazard="Operating industrial machinery without proper training or safety features",
        how_it_harms="Accidents, crushing injuries, or other serious harm"
    ),
    HowItHarms(
        hazard="Lack of shielding in an environment with radioactive materials",
        how_it_harms="Radiation exposure, leading to health problems, including radiation sickness and an increased risk of cancer"
    ),
    HowItHarms(
        hazard="Entering confined spaces without proper ventilation or rescue procedures",
        how_it_harms="Asphyxiation, exposure to harmful substances, or difficulty in rescue operations"
    )
]

incorrect_hazard_list = []

for i in range(len(hazard_list)):
    incorrect_hazard_list.append(HowItHarms(hazard=hazard_list[i].hazard, how_it_harms=hazard_list[i+1]))

print(incorrect_hazard_list)