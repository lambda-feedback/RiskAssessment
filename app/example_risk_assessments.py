# Learnings:
# 1. Keeping a safe distance away from a possible projectile is a prevention measure.
# The hazard event is therefore the projectile hitting someone, not the projectile being released.

try:
    from .RiskAssessment import RiskAssessmentWithoutNumberInputs, RiskAssessment
except ImportError:
    from RiskAssessment import RiskAssessmentWithoutNumberInputs, RiskAssessment

RA_empty_input = RiskAssessmentWithoutNumberInputs(
    activity="",
    hazard="Loud noise",
    who_it_harms="Everyone present",
    how_it_harms="Loud noise from instrument can cause hearing damage.",
    prevention="Play quietly, at a volume suitable for the room",
    mitigation="1",
    prevention_prompt_expected_output='prevention',
    mitigation_prompt_expected_output='',
)

RA_controlled_likelihood_wrong_type = RiskAssessment(
    activity="Using a trombone as a demonstration for a TPS presentation",
    hazard="Loud noise",
    who_it_harms="Everyone present",
    how_it_harms="Loud noise from instrument can cause hearing damage.",
    prevention="Play quietly, at a volume suitable for the room",
    mitigation="",
    prevention_prompt_expected_output='prevention',
    mitigation_prompt_expected_output='',
    uncontrolled_likelihood='1',
    uncontrolled_severity='1',
    uncontrolled_risk='1',
    controlled_likelihood='One',
    controlled_severity='1',
    controlled_risk='1'
)

RA_mitigation_wrong_type = RiskAssessmentWithoutNumberInputs(
    activity="Using a trombone as a demonstration for a TPS presentation",
    hazard="Loud noise",
    who_it_harms="Everyone present",
    how_it_harms="Loud noise from instrument can cause hearing damage.",
    prevention="Play quietly, at a volume suitable for the room",
    mitigation="1",
    prevention_prompt_expected_output='prevention',
    mitigation_prompt_expected_output='',
)

RA_incorrect_prevention_and_mitigation = RiskAssessmentWithoutNumberInputs(
    activity="Welding metal structures",
    hazard="Exposure to toxic welding fumes",
    how_it_harms="Inhaling welding fumes can lead to respiratory problems, lung damage, and long-term health issues.",
    who_it_harms="Welders and individuals in the vicinity of the welding area.",
    prevention="Using the welding equipment in an enclosed space without proper ventilation.",
    mitigation='',
    prevention_prompt_expected_output='neither',
    mitigation_prompt_expected_output='',

)

RA_trombone_impact = RiskAssessmentWithoutNumberInputs(
    activity="Using a trombone as a demonstration for a TPS presentation",
    hazard="Impact from instrument",
    who_it_harms="Audience",
    how_it_harms="Slide could hit audience member, causing impact injury.",
    prevention="Keep safe distance between the player and audience",
    mitigation="",
    prevention_prompt_expected_output='prevention',
    mitigation_prompt_expected_output='',
)

RA_hearing_damage = RiskAssessmentWithoutNumberInputs(
    activity="Using a trombone as a demonstration for a TPS presentation",
    hazard="Loud noise",
    who_it_harms="Everyone present",
    how_it_harms="Loud noise from instrument can cause hearing damage.",
    prevention="Play quietly, at a volume suitable for the room", # reduces likelihood of loud noise
    mitigation="Keep a space between the player and audience", # reduces severity of loud noise
    prevention_prompt_expected_output='prevention', 
    mitigation_prompt_expected_output='mitigation',
)

RA_hearing_damage_mitigation_prevention_switched = RiskAssessmentWithoutNumberInputs(
    activity="Using a trombone as a demonstration for a TPS presentation",
    hazard="Loud noise",
    who_it_harms="Everyone present",
    how_it_harms="Loud noise from instrument can cause hearing damage.",
    mitigation="Play quietly, at a volume suitable for the room", # reduces likelihood of loud noise
    prevention="Keep a space between the player and audience", # reduces severity of loud noise
    prevention_prompt_expected_output='mitigation', 
    mitigation_prompt_expected_output='prevention',
)


# RA_3_water_from_instrument = RiskAssessmentWithoutNumberInputs(
#     activity="Using a trombone as a demonstration for a TPS presentation",
#     hazard="Water from instrument",
#     who_it_harms="Audience",
#     how_it_harms="Condensation formed in instrument could spread germs if released",
#     prevention="Ensure water is not released during presentation", # Not very specific.
#     # Should include feedback stating: "How would you ensure water is not released during presentation?"
#     mitigation="Keep a space between the player and audience", # Reduces severity of water being released
#     prevention_prompt_expected_output='prevention',
#     mitigation_prompt_expected_output='prevention', # reduces likelihood that someone becomes ill
# )

# RA_3_water_from_instrument_mitiagation_prevention_switched = RiskAssessmentWithoutNumberInputs(
#     activity="Using a trombone as a demonstration for a TPS presentation",
#     hazard="Water from instrument",
#     who_it_harms="Audience",
#     how_it_harms="Condensation formed in instrument could spread germs if released",
#     mitigation="Ensure water is not released during presentation", # Not very specific.
#     # Should include feedback stating: "How would you ensure water is not released during presentation?"
#     prevention="Keep a space between the player and audience", # Reduces severity of water being released
#     prevention_prompt_expected_output='mitigation',
#     mitigation_prompt_expected_output='prevention',
# )

RA_ink_spill_in_eye = RiskAssessmentWithoutNumberInputs(
    activity="Fluids laboratory",
    hazard="Ink spillage",
    who_it_harms="Students",
    how_it_harms="Serious eye damage",
    prevention="Wear safety glasses", # If ink gets on face, wearing safety glasses reduces severity
    mitigation="Wash your eyes with clean water", # reduces severity after hazard has occurred
    prevention_prompt_expected_output='mitigation',
    mitigation_prompt_expected_output='mitigation',
)

# RA_ink_spill_in_eye_with_first_aid = RiskAssessmentWithoutNumberInputs(
#     activity="Fluids laboratory",
#     hazard="Ink spillage",
#     who_it_harms="Students",
#     how_it_harms="Serious eye damage",
#     prevention="Wear safety glasses", # reduces likelihood of hazard occurring
#     mitigation="First aid", # reduces severity after hazard has occurred
#     prevention_prompt_expected_output='mitigation',
#     mitigation_prompt_expected_output='mitigation',
# )


RA_ink_spill_in_eye_with_incorrect_how_it_harms = RiskAssessmentWithoutNumberInputs(
    activity="Fluids laboratory",
    hazard="Ink spillage",
    who_it_harms="Students",
    how_it_harms="Radiation exposure",
    prevention="Wear safety glasses", # reduces likelihood of hazard occurring
    mitigation="Wash your eyes with clean water", # reduces severity after hazard has occurred
    prevention_prompt_expected_output='mitigation',
    mitigation_prompt_expected_output='mitigation',
)

RA_wet_hands_electric_shock = RiskAssessmentWithoutNumberInputs(
    activity="Fluids laboratory",
    hazard="Wet hands",
    who_it_harms="Students",
    how_it_harms="Electric shock of students when touching electronics (pump power supply) with wet hands",
    prevention="Students should make sure they touch electronics only with dry hands", # reduces likelihood of hazard occurring
    mitigation="Call for urgent medical assistance", # reduces severity after hazard has occurred
    prevention_prompt_expected_output='prevention',
    mitigation_prompt_expected_output='mitigation',
)

RA_wet_hands_electric_shock_mitigation_prevention_switched = RiskAssessmentWithoutNumberInputs(
    activity="Fluids laboratory",
    hazard="Wet hands",
    who_it_harms="Students",
    how_it_harms="Electric shock of students when touching electronics (pump power supply) with wet hands",
    mitigation="Students should make sure they touch electronics only with dry hands", # reduces likelihood of hazard occurring
    prevention="Unplug the pump and call for urgent medical assistance", # reduces severity after hazard has occurred
    prevention_prompt_expected_output='mitigation',
    mitigation_prompt_expected_output='prevention',
)

RA_tripping_on_belongings = RiskAssessmentWithoutNumberInputs(
    activity="Fluids laboratory",
    hazard="Tripping over personal belongings",
    who_it_harms="Students",
    how_it_harms="Tripping can cause physical harm.",
    prevention="Put all belongings away from footpaths", # This reduces likelihood of hazard occurring and is therefore a prevention measure
    mitigation="Take care when walking around", # This reduces likelihood of hazard occurring and is therefore a prevention measure 
    prevention_prompt_expected_output='prevention',
    mitigation_prompt_expected_output='prevention',
)

RA_water_tank = RiskAssessmentWithoutNumberInputs(
    activity="Fluids laboratory",
    hazard="Water being spilt on the floor",
    who_it_harms="Students",
    how_it_harms="Injuries caused by possible slipping on wet floor",
    prevention="Do not move the water tank when it is full",
    mitigation="""If someone gets injured due to slipping, apply an ice pack to the injured area and 
    seek medical advice without delay.""",
    prevention_prompt_expected_output='prevention',
    mitigation_prompt_expected_output='mitigation',
)

RA_water_tank_mitigation_prevention_switched = RiskAssessmentWithoutNumberInputs(
    activity="Fluids laboratory",
    hazard="Water being spilt on the floor",
    who_it_harms="Students",
    how_it_harms="Injuries caused by possible slipping on wet floor",
    mitigation="Do not move the water tank when it is full",
    prevention="""If someone gets injured due to slipping, apply an ice pack to the injured area and 
    seek medical advice without delay.""",
    prevention_prompt_expected_output='mitigation',
    mitigation_prompt_expected_output='prevention',
)

RA_syringe_needle = RiskAssessmentWithoutNumberInputs(
    activity="Fluids laboratory",
    hazard="Syringes with sharp needles",
    who_it_harms="Students",
    how_it_harms="Sharp needles can pierce the skin and cause bleeding",
    prevention="Point needle away from yourself and others",
    mitigation="Wear lab coat and PPE", # This is both prevention and mitigation
    prevention_prompt_expected_output='prevention',
    mitigation_prompt_expected_output='mitigation',
)

RA_syringe_needle_mitigation_prevention_switched = RiskAssessmentWithoutNumberInputs(
    activity="Fluids laboratory",
    hazard="Syringes with sharp needles",
    who_it_harms="Students",
    how_it_harms="Sharp needles can pierce the skin and cause bleeding",
    mitigation="Point needle away from yourself and others",
    prevention="Wear lab coat and PPE", # This is both prevention and mitigation
    prevention_prompt_expected_output='mitigation',
    mitigation_prompt_expected_output='prevention',
)

# RA_9 = RiskAssessmentWithoutNumberInputs(
#     activity="Fluids laboratory",
#     hazard="Electrocution",
#     who_it_harms="Students",
#     how_it_harms="Electrocuted by mains voltage", # This is a description of the process not the harm on the students
#     prevention="Pump plug stays away from water",
#     mitigation="First aid on site", # There needs to be a description of how this will be used in the event of an electrocution.
#     prevention_prompt_expected_output='prevention',
#     mitigation_prompt_expected_output='mitigation',
# )

# RA_9_mitigation_prevention_switched = RiskAssessmentWithoutNumberInputs(
#     activity="Fluids laboratory",
#     hazard="Electrocution",
#     who_it_harms="Students",
#     how_it_harms="Electrocuted by mains voltage", # This is a description of the process not the harm on the students
#     mitigation="Pump plug stays away from water",
#     prevention="First aid on site", # There needs to be a description of how this will be used in the event of an electrocution.
#     prevention_prompt_expected_output='mitigation',
#     mitigation_prompt_expected_output='prevention',
# )

# RA_13 = RiskAssessmentWithoutNumberInputs(
#     activity='Presentation Demonstration',
#     hazard='Demonstration with ruler, styrofoam and bbq sticks. I will be flicking the ruler while clamping it to a table. The bbq sticks will be stuck in the styrofoam and I will shake to show resonance',
#     who_it_harms='Me and audience',
#     how_it_harms='Could hit someone or the demonstration falls apart',
#     prevention='Do the demonstration with care',
#     mitigation='',
#     prevention_prompt_expected_output='prevention',
#     mitigation_prompt_expected_output='',
# )

RA_paper_plane_impact = RiskAssessmentWithoutNumberInputs(
    activity='Using  paper plane models as a demonstration for a TPS presentation',
    hazard='Plane could hit audience member,',
    who_it_harms='Audience',
    how_it_harms='Impact injury.',
    prevention='Throw the paper plane to a direction without anyone',
    mitigation='',
    prevention_prompt_expected_output='prevention',
    mitigation_prompt_expected_output='',
)

RA_climbing_gear_on_feet = RiskAssessmentWithoutNumberInputs(
    activity='TPS presentation',
    hazard='Climbing Protection Gear (Cams and Hexs)',
    who_it_harms="Students and other individuals who would like to see how they work.",
    how_it_harms="""Some equipment is heavy so could hurt if dropped on feet.""",
    prevention='Inform those who wish to hold the equipment of the risk and demonstrate how they are used correctly.',
    mitigation='First aid if necessary',
    prevention_prompt_expected_output='prevention',
    mitigation_prompt_expected_output='mitigation',
)

RA_climbing_gear_on_feet_mitigation_prevention_switched = RiskAssessmentWithoutNumberInputs(
    activity='TPS presentation',
    hazard='Climbing Protection Gear (Cams and Hexs)',
    who_it_harms="Students and other individuals who would like to see how they work.",
    how_it_harms="""Some equipment is heavy so could hurt if dropped on feet.""",
    mitigation='Inform those who wish to hold the equipment of the risk and demonstrate how they are used correctly.',
    prevention='First aid if necessary',
    prevention_prompt_expected_output='mitigation',
    mitigation_prompt_expected_output='prevention',
)

RA_sharp_drone_propeller_blade = RiskAssessmentWithoutNumberInputs(
    activity='Bringing in a drone and two empty Li-Po batteries',
    hazard='Sharp Edge of propellor blade on drone',
    who_it_harms='Whoever pokes the propellor blade at the tip',
    how_it_harms='Is sharp to the touch to cause pain but not sharp enough to pierce skin',
    prevention='Make them aware the tip is sharp',
    mitigation='',
    prevention_prompt_expected_output='prevention',
    mitigation_prompt_expected_output='',
)

RA_battery_causes_fire = RiskAssessmentWithoutNumberInputs(
    activity='Bringing in a drone and two empty Li-Po batteries',
    hazard='Li-Po battery to handle',
    who_it_harms='Whoever is holding it',
    how_it_harms='It may heat up with an unlikely chance of a fire',
    prevention='Li-Po batteries have been discharged to a safe level',
    mitigation='Don\'t let the audience handle it for too long',
    prevention_prompt_expected_output='prevention',
    mitigation_prompt_expected_output='prevention', # it is both mitigation and prevention
)

RA_heavy_weight_falls_on_demonstrator = RiskAssessmentWithoutNumberInputs(
    activity='Using a spring contraption as a demonstration for a TPS presentation',
    hazard='Slippage of weight for contraption',
    who_it_harms='Demonstrator',
    how_it_harms='Heavy impact when falling onto demonstator, causing injury',
    prevention='Make sure the mass is properly secured to the contraption and the contraption is secured.',
    mitigation='Keep away from below the contraption',
    prevention_prompt_expected_output='prevention',
    mitigation_prompt_expected_output='prevention',
)

RA_zip_tie_hits_audience = RiskAssessmentWithoutNumberInputs(
    activity='Using a spring contraption as a demonstration for a TPS presentation',
    hazard='Cut Zip tie may fly',
    who_it_harms='Audience',
    how_it_harms='When cut the zip tie may hit an audience member',
    prevention='Keep hand around zip tie when cutting to stop it from flying',
    mitigation='Ensure safe distance between contraption and audience.',
    prevention_prompt_expected_output='prevention',
    mitigation_prompt_expected_output='prevention', # Another prevention measure as it reduces the likelihood of the zip tie hitting an audience member
)

RA_pencil_lead_projectile = RiskAssessmentWithoutNumberInputs(
    activity='Using a mechanical pencil and breaking the pencil lead against a surface for demonstration',
    hazard='Pencil lead breaking and becoming a projectile',
    who_it_harms='Anyone present',
    how_it_harms='May enter one\'s eye',
    prevention='Keep safe distance between the audience when demonstrating lead breakage',
    mitigation='',
    prevention_prompt_expected_output='prevention',
    mitigation_prompt_expected_output='',
)

RA_mucking_out_horse = RiskAssessmentWithoutNumberInputs(
    activity='Mucking out a horse',
    hazard='Horse kicks out',
    who_it_harms='Horse rider',
    how_it_harms='Impact injury',
    prevention='Keep a safe distance from the horse',
    mitigation='Wear a helmet and body protector',
    prevention_prompt_expected_output='prevention',
    mitigation_prompt_expected_output='mitigation',
)

RA_mucking_out_horse_mitigation_prevention_switched = RiskAssessmentWithoutNumberInputs(
    activity='Mucking out a horse',
    hazard='Horse kicks out',
    who_it_harms='Horse rider',
    how_it_harms='Impact injury',
    mitigation='Keep a safe distance from the horse',
    prevention='Wear a helmet and body protector',
    prevention_prompt_expected_output='mitigation',
    mitigation_prompt_expected_output='prevention',
)

RA_slitter_machine = RiskAssessmentWithoutNumberInputs(
    activity="Slitter machine usage",
    hazard="Sharp blade",
    who_it_harms="Operator",
    how_it_harms="Cut hazard",
    prevention="Guard",
    mitigation="Metal gloves for maintenance",
    prevention_prompt_expected_output="prevention",
    mitigation_prompt_expected_output="mitigation",
)

RA_campfire = RiskAssessmentWithoutNumberInputs(
    activity="Building a campfire",
    hazard="Flame",
    who_it_harms="People or property ",
    how_it_harms="Burns or damage",
    prevention="Safe distance from fire to be adhered to",
    mitigation="Flameproof clothing/insulation",
    prevention_prompt_expected_output="prevention",
    mitigation_prompt_expected_output="mitigation",
)

RA_bouldering = RiskAssessmentWithoutNumberInputs(
    activity="Climbing (Bouldering)",
    hazard="Not landing Safely",
    who_it_harms="Climbers",
    how_it_harms="Landing in a awkward way can cause injury",
    prevention="Make sure to climb down before you come off the wall",
    mitigation="Make sure to always land of two feet",
    prevention_prompt_expected_output="prevention",
    mitigation_prompt_expected_output="prevention",
)

RA_hob_burn = RiskAssessmentWithoutNumberInputs(
    activity="Cooking",
    hazard="Fire/ heat",
    who_it_harms="Chef",
    how_it_harms="Burns",
    prevention="Use induction stove,",
    mitigation="wear insulated gloves and use insulated cooking equipment",
    prevention_prompt_expected_output="prevention",
    mitigation_prompt_expected_output="mitigation",
)

RA_crossing_road = RiskAssessmentWithoutNumberInputs(
    activity="Crossing Exhibition Road",
    hazard="A car crashing into you",
    who_it_harms="The person crossing the road",
    how_it_harms="Could cause potentially life threatening injury",
    prevention="Inform participants they should cross on their own terms",
    mitigation="One person at back and one at front",
    prevention_prompt_expected_output="prevention",
    mitigation_prompt_expected_output="prevention",
)

RA_cycling = RiskAssessmentWithoutNumberInputs(
    activity="Cycle commuting",
    hazard="Head injury",
    who_it_harms="Cyclist",
    how_it_harms="Mistakes by cyclists or motorists leading to crash",
    prevention="Helmet wearing",
    mitigation="Reduces risk of head injury ",
    prevention_prompt_expected_output="mitigation",
    mitigation_prompt_expected_output="neither",
)

RA_ladder = RiskAssessmentWithoutNumberInputs(
    activity="Climbing a tall ladder",
    hazard="Falling, slipping",
    who_it_harms="the person on the ladder, people below the ladder",
    how_it_harms="The impact of hitting the ground ",
    prevention="Have someone hold the ladder. Make sure the ladder is locked and the ground in even. ",
    mitigation="Wear helment and padded clothes.",
    prevention_prompt_expected_output="prevention",
    mitigation_prompt_expected_output="mitigation",
)

# RA = RiskAssessmentWithoutNumberInputs(
#     activity = "",
#     hazard = "",
#     how_it_harms = "",
#     who_it_harms = "",
#     prevention = "",
#     mitigation = "",
#     prevention_prompt_expected_output = "",
#     mitigation_prompt_expected_output = "",
# )

RA_fire_alarm = RiskAssessmentWithoutNumberInputs(
    activity = "Lesson in school building",
    hazard = "Smoking causes fire",
    who_it_harms = "Students and teachers",
    how_it_harms = "Burns",
    prevention = "Banning smoking in the school",
    mitigation = "Fire alarm",
    prevention_prompt_expected_output = "prevention",
    mitigation_prompt_expected_output = "mitigation",
)   

RA_mop_up_spill = RiskAssessmentWithoutNumberInputs(
    activity = "Fluid lab",
    hazard = "Water spills",
    how_it_harms = "Slip",
    who_it_harms = "Users",
    prevention = "Be careful",
    mitigation = "Mop up",
    prevention_prompt_expected_output = "prevention",
    mitigation_prompt_expected_output = "prevention",
)

RA_syringe_with_cover = RiskAssessmentWithoutNumberInputs(
    activity = "Using syringe for injecting fuel",
    hazard = "Stabbing yourself",
    how_it_harms = "Sharp blade cuts skin and causes bleeding",
    who_it_harms = "The user",
    prevention = "Use a cover over the syringe when not in use",
    mitigation = "Wear gloves",
    prevention_prompt_expected_output = "mitigation",
    mitigation_prompt_expected_output = "mitigation",
)

RA_hot_water_in_cups = RiskAssessmentWithoutNumberInputs(
    activity = "HEAT TRANSFER LAB",
    hazard = "Boiling (hot) water",
    how_it_harms = "Burns",
    who_it_harms = "Students",
    prevention = "Sealed cups",
    mitigation = "Cold water tap nearby",
    prevention_prompt_expected_output = "prevention",
    mitigation_prompt_expected_output = "mitigation",
)

RA_bigger_beaker = RiskAssessmentWithoutNumberInputs(
    activity = "Filling a beaker with hot water",
    hazard = "Spilling hot water on your hands",
    how_it_harms = "Leaves you with painful burn scars",
    who_it_harms = "Yourself",
    prevention = "Use a bigger beaker",
    mitigation = "Be attentive when filling beaker",
    prevention_prompt_expected_output = "prevention",
    mitigation_prompt_expected_output = "prevention",
)

RA_cycling_high_viz = RiskAssessmentWithoutNumberInputs(
    activity = "Riding a Bike",
    hazard = "Getting hit",
    how_it_harms = "Could injure",
    who_it_harms = "The cyclist",
    prevention = "Wear high vis clothing",
    mitigation = "Wear helmet",
    prevention_prompt_expected_output = "prevention",
    mitigation_prompt_expected_output = "mitigation",
)

RA_cycling_safer_routes = RiskAssessmentWithoutNumberInputs(
    activity = "Riding a Bike",
    hazard = "Getting hit",
    how_it_harms = "Could injure",
    who_it_harms = "The cyclist",
    prevention = "Take safer routes",
    mitigation = "Wear high viz clothing",
    prevention_prompt_expected_output = "prevention",
    mitigation_prompt_expected_output = "prevention",
)

RA_credit_risk = RiskAssessmentWithoutNumberInputs(
    activity='Extending credit to customers',
    hazard='Default or non-payment',
    who_it_harms='Lender or creditor',
    how_it_harms='Loss of interest income',
    prevention='Conduct thorough credit checks and set appropriate credit limits',
    mitigation='Diversify credit exposure and establish collateral or guarantees',
    prevention_prompt_expected_output = "prevention",
    mitigation_prompt_expected_output = "mitigation"
)

RA_interest_rate_risk = RiskAssessmentWithoutNumberInputs(
    activity='Issuing or investing in fixed-rate securities',
    hazard='Changes in interest rates',
    who_it_harms='Borrower or investor',
    how_it_harms='Decreased asset value or income',
    prevention='Analyze interest rate trends and duration of securities',
    mitigation='Utilize interest rate hedging instruments',
    prevention_prompt_expected_output = "prevention",
    mitigation_prompt_expected_output = "mitigation"
)

RA_liquidity_risk = RiskAssessmentWithoutNumberInputs(
    activity='Holding illiquid assets',
    hazard='Inability to convert assets into cash',
    who_it_harms='Investor or institution',
    how_it_harms='Inability to meet financial obligations or fund withdrawals',
    prevention='Maintain sufficient cash reserves',
    mitigation='Establish lines of credit or',
    prevention_prompt_expected_output = "prevention",
    mitigation_prompt_expected_output = "mitigation"
)

RA_operational_risk = RiskAssessmentWithoutNumberInputs(
    activity='Conducting daily operations',
    hazard='System failures',
    who_it_harms='Organization or financial institution',
    how_it_harms='Financial loss',
    prevention='Implement regular audits',
    mitigation='Invest in technology infrastructure',
    prevention_prompt_expected_output = "prevention",
    mitigation_prompt_expected_output = "prevention"
)

RA_market_risk = RiskAssessmentWithoutNumberInputs(
    activity='Trading securities or commodities',
    hazard='Fluctuations in market prices',
    who_it_harms='Trader or investor',
    how_it_harms='Losses due to market movements',
    prevention='Analyze market trends',
    mitigation='Implement hedging strategies',
    prevention_prompt_expected_output = "prevention",
    mitigation_prompt_expected_output = "mitigation"
)

example_risk_assessments_dict = {
    'Old Physical Risks': [
        # RA_syringe_needle, 
        # RA_syringe_needle_mitigation_prevention_switched, 
        # RA_trombone_impact, 
        # RA_hearing_damage, 
        # RA_ink_spill_in_eye, 
        # RA_wet_hands_electric_shock, 
        # RA_tripping_on_belongings, 
        # RA_water_tank,
        # RA_paper_plane_impact, 
        # RA_climbing_gear_on_feet, 
        # RA_sharp_drone_propeller_blade, 
        # RA_battery_causes_fire, 
        # RA_heavy_weight_falls_on_demonstrator, 
        # RA_zip_tie_hits_audience,
        # RA_pencil_lead_projectile,
        # RA_incorrect_prevention_and_mitigation, 
        # RA_hearing_damage_mitigation_prevention_switched,
        # RA_wet_hands_electric_shock_mitigation_prevention_switched, 
        # RA_water_tank_mitigation_prevention_switched,
        # RA_climbing_gear_on_feet_mitigation_prevention_switched,
        # RA_mucking_out_horse,
        # RA_slitter_machine
        ],

    'New Physical Risks': [
        RA_fire_alarm,
        RA_mop_up_spill,
        RA_syringe_with_cover,
        # RA_hot_water_in_cups,
        # RA_bigger_beaker,
        # RA_campfire,
        # RA_bouldering,
        # RA_hob_burn,
        # RA_crossing_road,
        # RA_cycling,
        # RA_ladder,
        # RA_cycling_high_viz,
        # RA_cycling_safer_routes
        ],
    
    'Finance Risks': [
        # RA_credit_risk,
        # RA_interest_rate_risk,
        # RA_liquidity_risk,
        # RA_operational_risk,
        # RA_market_risk
    ]
}

example_risk_assessments = []

for risk_assessment_list in example_risk_assessments_dict.values():
    example_risk_assessments.extend(risk_assessment_list)

number_of_risk_assessments_in_each_domain = {key: len(value) for key, value in example_risk_assessments_dict.items()}

# Assuming you have a list of RiskAssessment objects named risk_assessments

# Initialize empty sets to store unique values for each field
unique_activities = set()
unique_hazards = set()
unique_how_it_harms = set()
unique_who_it_harms = set()
unique_control_measures = set()

# Iterate through the list of risk assessments
for risk_assessment in example_risk_assessments:
    # Check and add unique values for each field that is not an empty string
    if risk_assessment.activity != "":
        unique_activities.add(risk_assessment.activity)
    if risk_assessment.hazard != "":
        unique_hazards.add(risk_assessment.hazard)
    if risk_assessment.how_it_harms != "":
        unique_how_it_harms.add(risk_assessment.how_it_harms)
    if risk_assessment.who_it_harms != "":
        unique_who_it_harms.add(risk_assessment.who_it_harms)
    if risk_assessment.prevention != "":
        unique_control_measures.add(risk_assessment.prevention)
    if risk_assessment.mitigation != "":
        unique_control_measures.add(risk_assessment.mitigation)