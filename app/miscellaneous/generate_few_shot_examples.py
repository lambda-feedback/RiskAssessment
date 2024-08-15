# # Current how it harms examples:
# from example_risk_assessments import RA_4_with_incorrect_how_it_harms

# Current prevention examples:
from data.example_risk_assessments import *

# # Current mitigation examples:
# from example_risk_assessments import RA_6, RA_mucking_out_horse

def get_prevention_prompt(risk_assessment, few_shot=False):
    prevention = risk_assessment.get_control_measure_prompt_with_prevention_input()
    if few_shot:
        return prevention.generate_prompt()
    else:
        return prevention.generate_prompt_without_few_shot_examples()

def get_mitigation_prompt(risk_assessment, few_shot=False):
    mitigation = risk_assessment.get_control_measure_prompt_with_mitigation_input()
    if few_shot:
        return mitigation.generate_prompt()
    else:
        return mitigation.generate_prompt_without_few_shot_examples()

def get_hazard_event_and_harm_caused_prompt(risk_assessment, few_shot=False):
    how_it_harms = risk_assessment.get_harm_caused_and_hazard_event_input()
    if few_shot:
        return how_it_harms.generate_prompt()
    else:
        return how_it_harms.generate_prompt_without_few_shot_examples()
    
def is_future_harm_reduced_prompt_input_with_mitigation(risk_assessment, few_shot=False):
    is_future_harm_reduced = risk_assessment.is_future_harm_reduced_prompt_input_with_mitigation()
    if few_shot:
        return is_future_harm_reduced.generate_prompt()
    else:
        return is_future_harm_reduced.generate_prompt_without_few_shot_examples()

def is_future_harm_reduced_prompt_input_with_prevention(risk_assessment, few_shot=False):
    is_future_harm_reduced = risk_assessment.is_future_harm_reduced_prompt_input_with_prevention()
    if few_shot:
        return is_future_harm_reduced.generate_prompt()
    else:
        return is_future_harm_reduced.generate_prompt_without_few_shot_examples()

if __name__ == "__main__":
    # How it harms
    # print(get_how_it_harms_prompt(RA_9)) # Correct example
    # print(get_how_it_harms_prompt(RA_4_with_incorrect_how_it_harms)) # Incorrect example


    # # Hazard event and how it harms
    # print(get_hazard_event_and_harm_caused_prompt(RA_cycling_high_viz))
    # print(get_hazard_event_and_harm_caused_prompt(RA_cycling))

    # Prevention
    # print(get_prevention_prompt(RA_wildfire_early_detection))

    # print(get_prevention_prompt(RA_water_tank))
    # print('\n\n\n')
    # print(get_prevention_prompt(RA_zip_tie_hits_audience))
    
    # # Mitigation
    # print(get_mitigation_prompt(RA_earthquake_building_retrofit)) # Preparation
    # print('\n\n\n')
    # print(get_mitigation_prompt(RA_volcano_post_disaster_recovery)) # Aftermath

    # print(get_mitigation_prompt(RA_ink_spill_in_eye))
    print(get_prevention_prompt(RA_cycling))

    # Future Mitigation
    # print(is_future_harm_reduced_prompt_input_with_mitigation(RA_foot_and_mouth_disease_rapid_response))
    # print('\n\n\n')
    # print(is_future_harm_reduced_prompt_input_with_mitigation(RA_pandemic_quarantine))
    # print('\n\n\n')
    # print(is_future_harm_reduced_prompt_input_with_prevention(RA_cycling_high_viz))

