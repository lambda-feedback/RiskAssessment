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
    risk_domain="physical risk to individuals"
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
    risk_domain="physical risk to individuals",
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
    risk_domain="physical risk to individuals"
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
    risk_domain="physical risk to individuals"
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
    risk_domain="physical risk to individuals"
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
    risk_domain="physical risk to individuals"
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
    risk_domain="physical risk to individuals"
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
#   risk_domain="physical risk to individuals"
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
    risk_domain="physical risk to individuals"
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
    risk_domain="physical risk to individuals"
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
    risk_domain="physical risk to individuals"
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
    risk_domain="physical risk to individuals"
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
    risk_domain="physical risk to individuals"
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
    risk_domain="physical risk to individuals"
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
    risk_domain="physical risk to individuals"
)

RA_syringe_needle = RiskAssessmentWithoutNumberInputs(
    activity="Fluids laboratory",
    hazard="Syringes with sharp needles",
    who_it_harms="Students",
    how_it_harms="Sharp needles can pierce the skin and cause bleeding",
    prevention="Point needle away from yourself and others",
    mitigation="Wear lab coat and PPE", # This is both prevention and mitigation
    prevention_prompt_expected_output='prevention',
    mitigation_prompt_expected_output='both',
    risk_domain="physical risk to individuals"
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
    risk_domain="physical risk to individuals"
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
    risk_domain="physical risk to individuals"
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
    risk_domain="physical risk to individuals"
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
    risk_domain="physical risk to individuals"
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
    risk_domain="physical risk to individuals"
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
    risk_domain="physical risk to individuals"
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
    risk_domain="physical risk to individuals"
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
    risk_domain="physical risk to individuals"
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
    risk_domain="physical risk to individuals"
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
    risk_domain="physical risk to individuals"
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
    risk_domain="physical risk to individuals"
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
    risk_domain="physical risk to individuals"
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
    risk_domain="physical risk to individuals"
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
    risk_domain="physical risk to individuals"
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
    risk_domain="physical risk to individuals"
)

RA_crossing_road = RiskAssessmentWithoutNumberInputs(
    activity="Crossing Exhibition Road",
    hazard="A car crashing into you",
    who_it_harms="The person crossing the road",
    how_it_harms="Could cause potentially life threatening injury",
    prevention="Look left and right before crossing the road",
    mitigation="One person at back and one at front",
    prevention_prompt_expected_output="prevention",
    mitigation_prompt_expected_output="prevention",
    risk_domain="physical risk to individuals"
)

RA_cycling = RiskAssessmentWithoutNumberInputs(
    activity="Cycle commuting",
    hazard="Head injury",
    who_it_harms="Cyclist",
    how_it_harms="Mistakes by cyclists or motorists leading to crash",
    prevention="Helmet wearing",
    mitigation="",
    prevention_prompt_expected_output="mitigation",
    mitigation_prompt_expected_output="",
    risk_domain="physical risk to individuals"
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
    risk_domain="physical risk to individuals"
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
    risk_domain="physical risk to individuals"
)   

RA_mop_up_spill = RiskAssessmentWithoutNumberInputs(
    activity = "Fluid lab",
    hazard = "Water spills",
    how_it_harms = "Slip",
    who_it_harms = "Users",
    prevention = "Be careful",
    mitigation = "Mop up",
    prevention_prompt_expected_output = "neither", # Not specific enough
    mitigation_prompt_expected_output = "prevention",
    risk_domain="physical risk to individuals"
)

RA_syringe_with_cover = RiskAssessmentWithoutNumberInputs(
    activity = "Using syringe for injecting fuel",
    hazard = "Stabbing yourself",
    how_it_harms = "Sharp blade cuts skin and causes bleeding",
    who_it_harms = "The user",
    prevention = "Use a cover over the syringe when not in use",
    mitigation = "Wear gloves",
    prevention_prompt_expected_output = "prevention",
    mitigation_prompt_expected_output = "mitigation",
    risk_domain="physical risk to individuals"
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
    risk_domain="physical risk to individuals"
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
    risk_domain="physical risk to individuals"
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
    risk_domain="physical risk to individuals"
)

RA_cycling_safer_routes = RiskAssessmentWithoutNumberInputs(
    activity = "Riding a Bike",
    hazard = "Getting hit",
    how_it_harms = "Could injure",
    who_it_harms = "The cyclist",
    prevention = "Take safer routes",
    mitigation = "",
    prevention_prompt_expected_output = "prevention",
    mitigation_prompt_expected_output = "",
    risk_domain="physical risk to individuals"
)

RA_credit_risk = RiskAssessmentWithoutNumberInputs(
    activity='Extending credit to customers',
    hazard='Default or non-payment',
    who_it_harms='Lender or creditor',
    how_it_harms='Loss of interest income',
    prevention='Conduct thorough credit checks and set appropriate credit limits',
    mitigation='Diversify credit exposure and establish collateral or guarantees',
    prevention_prompt_expected_output = "prevention",
    mitigation_prompt_expected_output = "mitigation",
    risk_domain="financial risk"
)

RA_interest_rate_risk = RiskAssessmentWithoutNumberInputs(
    activity='Issuing or investing in fixed-rate securities',
    hazard='Changes in interest rates',
    who_it_harms='Borrower or investor',
    how_it_harms='Decreased asset value or income',
    prevention='Analyze interest rate trends and duration of securities',
    mitigation='Utilize interest rate hedging instruments',
    prevention_prompt_expected_output = "prevention",
    mitigation_prompt_expected_output = "mitigation",
    risk_domain="financial risk"
)

RA_liquidity_risk = RiskAssessmentWithoutNumberInputs(
    activity='Holding illiquid assets',
    hazard='Inability to convert assets into cash',
    who_it_harms='Investor or institution',
    how_it_harms='Inability to meet financial obligations or fund withdrawals',
    prevention='Maintain sufficient cash reserves',
    mitigation='Establish lines of credit or',
    prevention_prompt_expected_output = "prevention",
    mitigation_prompt_expected_output = "mitigation",
    risk_domain="financial risk"

)

RA_operational_risk = RiskAssessmentWithoutNumberInputs(
    activity='Conducting daily operations',
    hazard='System failures',
    who_it_harms='Organization or financial institution',
    how_it_harms='Financial loss',
    prevention='Implement regular audits',
    mitigation='Invest in technology infrastructure',
    prevention_prompt_expected_output = "prevention",
    mitigation_prompt_expected_output = "prevention",
    risk_domain="financial risk"
)

RA_market_risk = RiskAssessmentWithoutNumberInputs(
    activity='Trading securities or commodities',
    hazard='Fluctuations in market prices',
    who_it_harms='Trader or investor',
    how_it_harms='Losses due to market movements',
    prevention='Analyze market trends',
    mitigation='Implement hedging strategies',
    prevention_prompt_expected_output = "prevention",
    mitigation_prompt_expected_output = "mitigation",
    risk_domain="financial risk"
)

### ENVIRONMENTAL
RA_wildfire_early_detection = RiskAssessmentWithoutNumberInputs(
    activity="Wildfire",
    hazard="Wildfire",
    who_it_harms="Residents, wildlife, and the environment",
    how_it_harms="Wildfires can cause extensive damage to homes and the environment.",
    prevention="Use fire-resistant plants",
    mitigation="Early detection systems",
    prevention_prompt_expected_output="prevention",
    mitigation_prompt_expected_output="mitigation",
    risk_domain="environmental risk"
)

RA_wildfire_fire_resistant_infrastructure = RiskAssessmentWithoutNumberInputs(
    activity="Wildfire",
    hazard="Wildfire",
    who_it_harms="Residents, wildlife, and the environment",
    how_it_harms="Wildfires can cause extensive damage to homes and the environment.",
    prevention="",
    mitigation="Retrofit buildings with fire-resistant materials",
    prevention_prompt_expected_output="",
    mitigation_prompt_expected_output="mitigation",
    risk_domain="environmental risk"
)

RA_wildfire_community_preparedness = RiskAssessmentWithoutNumberInputs(
    activity="Wildfire",
    hazard="Wildfire",
    who_it_harms="Residents, wildlife, and the environment",
    how_it_harms="Wildfires can cause extensive damage to homes and the environment.",
    prevention="",
    mitigation="Community wildfire protection plans",
    prevention_prompt_expected_output="",
    mitigation_prompt_expected_output="mitigation",
    risk_domain="environmental risk"
)

RA_earthquake_building_retrofit = RiskAssessmentWithoutNumberInputs(
    activity="Earthquake",
    hazard="Earthquake",
    who_it_harms="Residents, infrastructure, and the environment",
    how_it_harms="Earthquakes can cause extensive damage to buildings, roads, and the environment.",
    prevention="",
    mitigation="Retrofit buildings and infrastructure to withstand seismic activity.",
    prevention_prompt_expected_output="",
    mitigation_prompt_expected_output="mitigation",
    risk_domain="environmental risk"
)

RA_earthquake_public_education = RiskAssessmentWithoutNumberInputs(
    activity="Earthquake",
    hazard="Earthquake",
    who_it_harms="Residents, infrastructure, and the environment",
    how_it_harms="Earthquakes can cause extensive damage to buildings, roads, and the environment.",
    prevention="",
    mitigation="Educate the public about earthquake preparedness and response.",
    prevention_prompt_expected_output="",
    mitigation_prompt_expected_output="mitigation",
    risk_domain="environmental risk"
)

RA_earthquake_early_warning_systems = RiskAssessmentWithoutNumberInputs(
    activity="Earthquake",
    hazard="Earthquake",
    who_it_harms="Residents, infrastructure, and the environment",
    how_it_harms="Earthquakes can cause extensive damage to buildings, roads, and the environment.",
    prevention="",
    mitigation="Invest in early warning systems to detect seismic activity",
    prevention_prompt_expected_output="",
    mitigation_prompt_expected_output="mitigation",
    risk_domain="environmental risk"
)

RA_volcano_early_warning_systems = RiskAssessmentWithoutNumberInputs(
    activity="Volcano",
    hazard="Volcanic Eruption",
    who_it_harms="Residents, infrastructure, and the environment",
    how_it_harms="Volcanic eruptions can cause destruction of property, infrastructure, loss of life, and disruption of ecosystems",
    prevention="",
    mitigation="Invest in early warning systems to detect volcanic activity",
    prevention_prompt_expected_output="",
    mitigation_prompt_expected_output="mitigation",
    risk_domain="environmental risk"
)

RA_volcano_causing_ash_cloud = RiskAssessmentWithoutNumberInputs(
    activity="Volcano",
    hazard="Volcanic Eruption",
    who_it_harms="Airline passengers",
    how_it_harms="Flight delays and cancellations due to ash clouds from volcanic eruptions",
    prevention="",
    mitigation="Use volcanic ash data to assist in flight diversions",
    prevention_prompt_expected_output="",
    mitigation_prompt_expected_output="mitigation",
    risk_domain="environmental risk"
)

RA_volcano_zoning = RiskAssessmentWithoutNumberInputs(
    activity="Volcano",
    hazard="Volcanic Eruption",
    who_it_harms="Residents, infrastructure, and the environment",
    how_it_harms="Volcanic eruptions can cause destruction of property and loss of life",
    prevention="",
    mitigation="Zoning regulations to restrict development in high-risk areas.",
    prevention_prompt_expected_output="",
    mitigation_prompt_expected_output="mitigation",
    risk_domain="environmental risk"
)

RA_volcano_emergency_response = RiskAssessmentWithoutNumberInputs(
    activity="Volcano",
    hazard="Volcanic Eruption",
    who_it_harms="Residents, infrastructure, and the environment",
    how_it_harms="Volcanic eruptions can cause destruction of property and loss of life",
    prevention="",
    mitigation="Develop emergency response plans",
    prevention_prompt_expected_output="",
    mitigation_prompt_expected_output="mitigation",
    risk_domain="environmental risk"
)

RA_volcano_post_disaster_recovery = RiskAssessmentWithoutNumberInputs(
    activity="Volcano",
    hazard="Volcanic Eruption",
    who_it_harms="Residents, infrastructure, and the environment",
    how_it_harms="Volcanic eruptions can cause destruction of property and loss of life",
    prevention="",
    mitigation="Support affected communities",
    prevention_prompt_expected_output="",
    mitigation_prompt_expected_output="mitigation",
    risk_domain="environmental risk"
)

RA_ransomware_NHS_isolation = RiskAssessmentWithoutNumberInputs(
    activity="Providing healthcare services",
    hazard="Ransomware",
    who_it_harms="Patients and healthcare providers",
    how_it_harms="Disruption of healthcare services and potential data loss",
    prevention="Regularly update and patch software.",
    mitigation="Isolate infected system from the rest of the network",
    prevention_prompt_expected_output="prevention",
    mitigation_prompt_expected_output="mitigation",
    risk_domain="cybersecurity risk"
)

RA_ransomware_NHS_MFA = RiskAssessmentWithoutNumberInputs(
    activity="Providing healthcare services",
    hazard="Ransomware attack",
    who_it_harms="Patients and healthcare providers",
    how_it_harms="Disruption of healthcare services and potential data loss",
    prevention="Multi-factor authentication",
    mitigation="Use decryption tools for the specific ransomware variant",
    prevention_prompt_expected_output="prevention",
    mitigation_prompt_expected_output="mitigation",
    risk_domain="cybersecurity risk"
)

RA_ransomware_NHS_data_backup = RiskAssessmentWithoutNumberInputs(
    activity="Providing healthcare services",
    hazard="Ransomware",
    who_it_harms="Patients and healthcare providers",
    how_it_harms="Disruption of healthcare services and potential data loss",
    prevention="Train employees on how to recognize phishing emails",
    mitigation="Implement a robust data backup strategy",
    prevention_prompt_expected_output="prevention",
    mitigation_prompt_expected_output="mitigation",
    risk_domain="cybersecurity risk"
)

RA_bank_cybersecurity_attack = RiskAssessmentWithoutNumberInputs(
    activity="Providing banking services",
    hazard="Phishing Attack",
    who_it_harms="Customers",
    how_it_harms="Unauthorized access to sensitive financial information",
    prevention="Train customers and employees on how to recognize phishing emails",
    mitigation="Implement email filtering solutions to detect and block phishing attempts",
    prevention_prompt_expected_output="prevention",
    mitigation_prompt_expected_output="prevention",
    risk_domain="cybersecurity risk"
)

RA_transport_cyber_attack_specific = RiskAssessmentWithoutNumberInputs(
    activity="Managing transportation systems",
    hazard="Ransomware Attack on Traffic Control Systems",
    who_it_harms="Passengers",
    how_it_harms="Disruption of traffic flow",
    prevention="Regularly update and patch traffic control system software",
    mitigation="Implement robust data backup strategies",
    prevention_prompt_expected_output="prevention",
    mitigation_prompt_expected_output="mitigation",
    risk_domain="cybersecurity risk"
)

RA_telecoms_cyber_attack = RiskAssessmentWithoutNumberInputs(
    activity="Managing telecommunications networks",
    hazard="Disruptive Cyber Attack on Major UK Telecoms Network Provider",
    who_it_harms="Telecommunications customers",
    how_it_harms="Disruption of internet and voice calls for millions of customers",
    prevention="Conduct regular security assessments",
    mitigation="Develop and test incident response plans",
    prevention_prompt_expected_output="prevention",
    mitigation_prompt_expected_output="mitigation",
    risk_domain="cybersecurity risk",
)

RA_civil_nuclear_cyber_attack = RiskAssessmentWithoutNumberInputs(
    activity="Operating civil nuclear generating sites",
    hazard="Cyber Attack on Civil Nuclear Generating Site",
    who_it_harms="Energy consumers",
    how_it_harms="Temporary loss of power supply",
    prevention="Foster sector-wide collaboration against cyber-threats",
    mitigation="Develop incident response plans",
    prevention_prompt_expected_output="prevention",
    mitigation_prompt_expected_output="mitigation",
    risk_domain="cybersecurity risk"
)

RA_electricity_infrastructure_cyber_attack = RiskAssessmentWithoutNumberInputs(
    activity="Operating the National Electicity Transmission System (NETS)",
    hazard="Cyber Attack on NETS",
    who_it_harms="Energy consumers",
    how_it_harms="Instantaneous loss of mains electricity supply",
    prevention="Empower employees to recognize and respond effectively to suspicious activities.",
    mitigation="Divide the NETS infrastructure into distinct segments", # to limit the spread of a cybersecurity attack
    prevention_prompt_expected_output="prevention",
    mitigation_prompt_expected_output="mitigation",
    risk_domain="cybersecurity risk"
)

RA_gas_infrastructure_cyber_attack = RiskAssessmentWithoutNumberInputs(
    activity="Operating gas transmission and distribution networks",
    hazard="Encrypting of data upon which critical Gas Infrastructure systems depend",
    who_it_harms="Energy consumers",
    how_it_harms="Disruption of gas supply",
    prevention="Implement multi-factor authentication", # and access controls to protect critical systems and data
    mitigation="Develop and test incident response plans", #  to enable rapid detection, containment, and recovery from cyber attacks
    prevention_prompt_expected_output="prevention",
    mitigation_prompt_expected_output="mitigation",
    risk_domain="cybersecurity risk"
)

RA_fuel_supply_cyber_attack = RiskAssessmentWithoutNumberInputs(
    activity="Operating fuel supply infrastructure",
    hazard="Cyber Attack on system critical to UK fuel distribution and supply",
    who_it_harms="Energy consumers",
    how_it_harms="Disruption of fuel supply",
    prevention="Conduct penetration tests to identify and address vulnerabilities", #  in fuel supply infrastructure
    mitigation="Hire cybersecurity experts to manage emergency responses", # to cyber attacks
    prevention_prompt_expected_output="prevention",
    mitigation_prompt_expected_output="mitigation",
    risk_domain="cybersecurity risk"
)

RA_explosive_devices_sniffer_dogs = RiskAssessmentWithoutNumberInputs(
    activity="Public gatherings or events",
    hazard="Explosive terrorist attack",
    who_it_harms="Attendees, bystanders, emergency responders",
    how_it_harms="Multiple fatalities and casualties",
    prevention="Enhancing explosive detection capabilities", # e.g. with sniffer dogs
    mitigation="Providing victim support structures",
    prevention_prompt_expected_output="prevention",
    mitigation_prompt_expected_output="mitigation",
    risk_domain="terrorism risk"
)

RA_explosive_devices_security = RiskAssessmentWithoutNumberInputs(
    activity="Public gatherings or events",
    hazard="Explosive terrorist attack",
    who_it_harms="Attendees, bystanders, emergency responders",
    how_it_harms="Multiple fatalities and casualties",
    prevention="Implementing security measures at public events", # (e.g., bag checks, surveillance)
    mitigation="Leveraging Forensic Explosives Laboratory for investigation and prosecution",
    prevention_prompt_expected_output="prevention",
    mitigation_prompt_expected_output="mitigation",
    risk_domain="terrorism risk"
)

RA_terrorism_aviation_background_checks = RiskAssessmentWithoutNumberInputs(
    activity="Air travel operations",
    hazard="Terrorist attack targeting aircraft",
    who_it_harms="Passengers, crew members",
    how_it_harms="Significant loss of life",
    prevention="Conducting thorough background checks on airport staff.",
    mitigation="Providing psychological support for affected individuals",
    prevention_prompt_expected_output="prevention",
    mitigation_prompt_expected_output="mitigation",
    risk_domain="terrorism risk"
)

RA_terrorism_aviation_improving_standards = RiskAssessmentWithoutNumberInputs(
    activity="Air travel operations",
    hazard="Terrorist attack targeting aircraft",
    who_it_harms="Passengers, crew members",
    how_it_harms="Significant loss of life",
    prevention="Improve global aviation security standards",
    mitigation="Deploy search and rescue teams",
    prevention_prompt_expected_output="prevention",
    mitigation_prompt_expected_output="mitigation",
    risk_domain="terrorism risk"
)

RA_hostage_negotiation_teams = RiskAssessmentWithoutNumberInputs(
    activity="Public gatherings or high-profile events",
    hazard="Strategic hostage taking",
    who_it_harms="Hostages",
    how_it_harms="Risk of fatalities and casualties, psychological trauma",
    prevention="Implementing security measures",
    mitigation="Utilizing hostage negotiation teams",
    prevention_prompt_expected_output="prevention",
    mitigation_prompt_expected_output="mitigation",
    risk_domain="terrorism risk"
)

RA_hostage_psychological_support = RiskAssessmentWithoutNumberInputs(
    activity="Public gatherings or high-profile events",
    hazard="Strategic hostage taking",
    who_it_harms="Hostages, bystanders, law enforcement personnel",
    how_it_harms="Psychological trauma",
    prevention="Enhancing intelligence gathering capabilities",
    mitigation="Providing psychological support",
    prevention_prompt_expected_output="prevention",
    mitigation_prompt_expected_output="mitigation",
    risk_domain="terrorism risk"
)

RA_high_profile_assassination_protection = RiskAssessmentWithoutNumberInputs(
    activity="Public appearances or events involving high-profile figures",
    hazard="Assassination of a high-profile public figure",
    who_it_harms="High-profile public figures",
    how_it_harms="Loss of life",
    prevention="Providing close protection for high-profile figures",
    mitigation="Apprehending perpetrators to prevent further attacks",
    prevention_prompt_expected_output="prevention",
    mitigation_prompt_expected_output="mitigation",
    risk_domain="terrorism risk"
)

RA_high_profile_assassination_security_measures = RiskAssessmentWithoutNumberInputs(
    activity="Public appearances or events involving high-profile figures",
    hazard="Assassination of a high-profile public figure",
    who_it_harms="High-profile public figures",
    how_it_harms="Loss of life",
    prevention="Implementing robust security measures for public appearances",
    mitigation="Managing public communications to prevent escalation of tensions",
    prevention_prompt_expected_output="prevention",
    mitigation_prompt_expected_output="mitigation",
    risk_domain="terrorism risk"
)

RA_CBRN_attack_securing_borders = RiskAssessmentWithoutNumberInputs(
    activity="Public safety and national security",
    hazard="CBRN (Chemical, Biological, Radiological, Nuclear) attack",
    who_it_harms="General public, emergency responders, environmental ecosystems",
    how_it_harms="Contamination of food and water supplies",
    prevention="Securing borders to limit access to hazardous materials",
    mitigation="Rapid response and decontamination procedures",
    prevention_prompt_expected_output="prevention",
    mitigation_prompt_expected_output="mitigation",
    risk_domain="terrorism risk"
)

# TODO: This is a mix between a biohazard and a terrorist attack
# This confirms that you should have multiple different prompts for different risk
# domains and that certain risks can fall into multiple different domains
RA_CBRN_attack_enhance_detection = RiskAssessmentWithoutNumberInputs(
    activity="Public safety and national security",
    hazard="CBRN (Chemical, Biological, Radiological, Nuclear) attack",
    who_it_harms="General public, emergency responders, environmental ecosystems",
    how_it_harms="Potential for large numbers of casualties and fatalities",
    prevention="Enhancing detection methods for CBRN materials",
    mitigation="Providing medical treatment for affected individuals",
    prevention_prompt_expected_output="prevention",
    mitigation_prompt_expected_output="mitigation",
    risk_domain="terrorism risk"
)

RA_pandemic_isolate_cases = RiskAssessmentWithoutNumberInputs(
    activity="Public health and emergency response",
    hazard="Pandemic",
    who_it_harms="General population",
    how_it_harms="Loss of life",
    prevention="Educating the public about disease transmission", # can help reduce the spread of pathogens
    mitigation="Rapid response to identify and isolate suspected cases",
    prevention_prompt_expected_output="prevention",
    mitigation_prompt_expected_output="mitigation",
    risk_domain="biohazard risk"
)


RA_pandemic_scalable_treatment = RiskAssessmentWithoutNumberInputs(
    activity="Public health and emergency response",
    hazard="Pandemic",
    who_it_harms="General population",
    how_it_harms="Loss of life",
    prevention="Addressing factors contributing to the spread of infectious diseases, such as climate change",
    mitigation="Scalable diagnostics and treatment options",
    prevention_prompt_expected_output="prevention",
    mitigation_prompt_expected_output="mitigation",
    risk_domain="biohazard risk"
)

RA_pandemic_vaccines = RiskAssessmentWithoutNumberInputs(
    activity="Public health and emergency response",
    hazard="Pandemic",
    who_it_harms="General population",
    how_it_harms="Loss of life",
    prevention="",
    mitigation="Rapid deployment and distribution of vaccines",
    prevention_prompt_expected_output="",
    mitigation_prompt_expected_output="mitigation",
    risk_domain="biohazard risk"
)

RA_pandemic_resource_allocation = RiskAssessmentWithoutNumberInputs(
    activity="Public health and emergency response",
    hazard="Pandemic",
    who_it_harms="General population",
    how_it_harms="Loss of life",
    prevention="",
    mitigation="Prioritizing allocation of resources",
    prevention_prompt_expected_output="",
    mitigation_prompt_expected_output="mitigation",
    risk_domain="biohazard risk"
)

RA_pandemic_quarantine = RiskAssessmentWithoutNumberInputs(
    activity="Public health and emergency response",
    hazard="Pandemic",
    who_it_harms="General population",
    how_it_harms="Loss of life",
    prevention="",
    mitigation="Contact tracing and quarantine measures",
    prevention_prompt_expected_output="",
    mitigation_prompt_expected_output="mitigation",
    risk_domain="biohazard risk"
)

RA_pandemic_surge_capacity = RiskAssessmentWithoutNumberInputs(
    activity="Public health and emergency response",
    hazard="Pandemic",
    who_it_harms="General population",
    how_it_harms="Loss of life",
    prevention="",
    mitigation="Implementing surge capacity plans in hospitals",
    prevention_prompt_expected_output="",
    mitigation_prompt_expected_output="mitigation",
    risk_domain="biohazard risk"
)

RA_foot_and_mouth_disease_rapid_response = RiskAssessmentWithoutNumberInputs(
    activity="Livestock farming operations",
    hazard="An outbreak of foot and mouth disease",
    who_it_harms="Livestock",
    how_it_harms="Economic losses in agriculture sector",
    prevention="Implementing farm visitor management protocols",
    mitigation="Rapid response to detect and contain outbreaks",
    prevention_prompt_expected_output="prevention",
    mitigation_prompt_expected_output="mitigation",
    risk_domain="biohazard risk"
)

RA_foot_and_mouth_disease_culling = RiskAssessmentWithoutNumberInputs(
    activity="Livestock farming operations",
    hazard="An outbreak of foot and mouth disease",
    who_it_harms="Livestock",
    how_it_harms="Economic losses in agriculture sector",
    prevention="Maintaining high standards of hygiene on the farm",
    mitigation="Conducting mass culling of infected animals",
    prevention_prompt_expected_output="prevention",
    mitigation_prompt_expected_output="mitigation",
    risk_domain="biohazard risk"
)

RA_laboratory_biohazard = RiskAssessmentWithoutNumberInputs(
    activity="Laboratory research involving biohazardous materials",
    hazard="Potential exposure to infectious agents or toxins",
    who_it_harms="Laboratory personnel, researchers, surrounding community",
    how_it_harms="Infections",
    prevention="Providing training on biohazard handling",
    mitigation="Conducting decontamination procedures",
    prevention_prompt_expected_output="prevention",
    mitigation_prompt_expected_output="both",
    risk_domain="biohazard risk"
)

RA_healthcare_biohazard = RiskAssessmentWithoutNumberInputs(
    activity="Healthcare facility operations involving infectious patients",
    hazard="Potential transmission of infectious diseases",
    who_it_harms="Patients, healthcare workers, visitors",
    how_it_harms="Infections",
    prevention="Conducting regular disinfection",
    mitigation="Implementing quarantine measures",
    prevention_prompt_expected_output="prevention",
    mitigation_prompt_expected_output="mitigation",
    risk_domain="biohazard risk"
)

physical_risks_to_individuals__original_student_data = {
    'risk_assessments': [
        RA_syringe_needle, 
        RA_trombone_impact, 
        RA_hearing_damage, 
        RA_ink_spill_in_eye, 
        RA_wet_hands_electric_shock, 
        RA_tripping_on_belongings, 
        RA_water_tank,
        RA_sharp_drone_propeller_blade, 
        RA_battery_causes_fire, 
        RA_heavy_weight_falls_on_demonstrator, 
        RA_zip_tie_hits_audience,
        RA_incorrect_prevention_and_mitigation, 
        RA_mucking_out_horse,
        RA_slitter_machine

        # RA_paper_plane_impact, 
        # RA_pencil_lead_projectile,
        # RA_climbing_gear_on_feet, 
        ],
    'risk_domain': 'Physical risks to individuals (original student data)'
}

physical_risks_to_individuals__data_gathered_from_version_1_deployment = {
    'risk_assessments': [
        RA_fire_alarm,
        RA_mop_up_spill,
        RA_syringe_with_cover,
        RA_hot_water_in_cups,
        RA_bigger_beaker,
        RA_campfire,
        RA_bouldering,
        RA_hob_burn,
        RA_crossing_road,
        RA_cycling,
        RA_ladder,
        RA_cycling_high_viz,
        RA_cycling_safer_routes
    ],
    'risk_domain': 'Physical risks to individuals (data gathered from version 1 deployment)'
}

finance_risks = {
    'risk_assessments': [
        RA_credit_risk,
        RA_interest_rate_risk,
        RA_liquidity_risk,
        RA_operational_risk,
        RA_market_risk
    ],
    'risk_domain': 'Financial risks'
}

natural_disaster_risks = {
    'risk_assessments': [
        # MITIGATION ONLY
        RA_wildfire_fire_resistant_infrastructure,
        RA_wildfire_community_preparedness,
        RA_earthquake_building_retrofit,
        RA_earthquake_public_education,
        RA_earthquake_early_warning_systems,
        RA_volcano_early_warning_systems,
        RA_volcano_causing_ash_cloud,
        RA_volcano_zoning,
        RA_volcano_emergency_response,
        RA_volcano_post_disaster_recovery,

        # PREVENTION AND MITIGATION
        RA_wildfire_early_detection
    ],
    'risk_domain': 'Natural disaster risks'
}

cybersecurity_risks = {
    'risk_assessments': [
        # RA_ransomware_NHS_isolation,
        RA_ransomware_NHS_MFA,
        RA_ransomware_NHS_data_backup,
        RA_bank_cybersecurity_attack,
        RA_transport_cyber_attack_specific,
        RA_telecoms_cyber_attack,
        RA_civil_nuclear_cyber_attack,
        RA_electricity_infrastructure_cyber_attack,
        RA_gas_infrastructure_cyber_attack,
        RA_fuel_supply_cyber_attack,
    ],
    'risk_domain': 'Cybersecurity risks'
}

terrorism_risks = {
    'risk_assessments': [
        RA_explosive_devices_sniffer_dogs,
        RA_explosive_devices_security,
        RA_terrorism_aviation_background_checks,
        RA_terrorism_aviation_improving_standards,
        RA_hostage_negotiation_teams,
        RA_hostage_psychological_support,
        RA_high_profile_assassination_protection,
        RA_high_profile_assassination_security_measures,
        RA_CBRN_attack_enhance_detection,
        RA_CBRN_attack_securing_borders
    ],
    'risk_domain': 'Terrorism_risks'
}

biohazard_risks = {
    'risk_assessments': [
    # MITIGATION ONLY
    # RA_pandemic_resource_allocation,
    RA_pandemic_surge_capacity,
    RA_pandemic_quarantine,
    RA_pandemic_vaccines,

    # PREVENTION AND MITIGATION
    RA_pandemic_isolate_cases,
    RA_pandemic_scalable_treatment,
    # RA_foot_and_mouth_disease_culling,
    # RA_foot_and_mouth_disease_rapid_response,
    RA_laboratory_biohazard,
    RA_healthcare_biohazard
    ],

    'risk_domain': 'biohazard_risks'
}

# Assuming you have a list of RiskAssessment objects named risk_assessments

def create_unique_set_of_control_measures(risk_assessments):
    unique_control_measures = set()

    for risk_assessment in risk_assessments:
        if risk_assessment.prevention != "":
            unique_control_measures.add(risk_assessment.prevention)
        if risk_assessment.mitigation != "":
            unique_control_measures.add(risk_assessment.mitigation)
    
    return unique_control_measures