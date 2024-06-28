list_user_inputs = ['thermo lab,hot equipment,skin burn,students,1,3,1,minimise contact time,wear a lab coat,1,2,1',
                    'Crossing road,getting hit,fatal crash,pedestrian,4,3,12,stop lights,cross when light is green only,2,3,6',
                    'Crossing road,getting hit,fatal crash,pedestrian,4,3,12,stop lights,call ambulance,2,3,6',
                    'Lab Experiment,Spilled Chemicals,Irritates Skin,Students,3,3,9,Only let lab techs handle dangerous chemicals,Wear gloves,2,1,2',
                    'Lab Experiment,Spilled Chemicals,Irritates Skin,Students,3,3,9,Do not use dangerous chemicals,Wear gloves,2,1,2',
                    'participating in or conducting the ME2 heat engine lab,burning yourself or other people (different degrees),the surface of the very hot pipes carrying the fluid could come into contact with your skin and burn it,yourself or other people around you,4,2,8,don\'t run in the lab,wear a lab coat,1,1,1',
                    'participating in or conducting the ME2 heat engine lab,burning yourself or other people (different degrees),the surface of the very hot pipes carrying the fluid could come into contact with your skin and burn it,yourself or other people around you,4,2,8,be aware of your surroundings, have a cold water supply available and accessible,1,1,1',
                    'Fluids lab experiment,Water spill out and cause slippery,Spilled water can make floor slippery and people may fall over,Users,3,2,6,Be careful,Mop up using a cloth immediately,3,1,3',
                    'HEAT TRANSFER LAB,Boiling (hot) water,Burns,Students,4,3,12,Do not carry cups around,Cold water tap nearby,2,3,6',
                    'Running pump in fluids lab,Water spilage,Water coming into contact with electronics,Users,4,2,8,Cheeck for leakage before running the pump,Wear a lab coat and PPE,2,1,2',
                    'Fluids laboratory,Water being spilt on the floor,Slipping on the water on the floor causing impact injuries,Students,4,1,4,Do not move the water tank when it is full,If someone gets injured due to slipping apply an ice pack to the injured area and seek medical advice without delay,1,1,1',
                    'Using syringe for injecting fuel,Stabbing yourself,Sharp blade cuts skin and causes bleeding,The user ,3,3,9,Place syringe in the middle of the table,Wear gloves,2,2,4',
                    'dunking in a 3v3 game of basketball,falling,injury of impact,me,3,2,6,stop dunking,wear full body armour,0,1,0']

list_risk_assessment_names = ['thermo_lab_hot_equipment',
                              'crossing_road_getting_hit_green_lights',
                              'crossing_road_getting_hit_call_ambulance',
                              'lab_experiment_spilled_chemicals_lab_techs',
                              'lab_experiment_spilled_chemicals_no_dangerous_chemicals',
                              'heat_engine_lab_burning_yourself_dont_run',
                              'heat_engine_lab_burning_yourself_cold_water',
                            'fluids_lab_water_spill_slippery',
                            'heat_transfer_lab_boiling_water',
                            'running_pump_water_spillage',
                            'fluids_lab_water_spilt_slipping',
                            'syringe_injecting_fuel_place_syringe_in_middle_of_table',
                            'dunking_in_3v3_basketball_stop_dunking']

for i in range(len(list_user_inputs)):
    user_input = list_user_inputs[i]
    risk_assessment_name = list_risk_assessment_names[i]
    activity, hazard, how_it_harms, who_it_harms, _, _, _, prevention, mitigation, _, _, _ = user_input.split(',')
    print(f'''{risk_assessment_name} = RiskAssessmentWithoutNumberInputs(
    activity = "{activity}",
    hazard = "{hazard}",
    who_it_harms = "{who_it_harms}",
    how_it_harms = "{how_it_harms}",
    prevention = "{prevention}",
    mitigation = "{mitigation}",
    prevention_prompt_expected_class = "prevention",
    mitigation_prompt_expected_class = "mitigation",
    risk_domain="physical risk to individuals"
    )\n''')