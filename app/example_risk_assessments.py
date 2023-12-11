try:
    from .RiskAssessment import RiskAssessment
except ImportError:
    from RiskAssessment import RiskAssessment

# TODO: For incorrect examples, in PromptInputAndExpectedOutput, could include a reason as to why it is incorrect

# RA_1 = RiskAssessment(
#     activity="Using a trombone as a demonstration for a TPS presentation",
#     hazard="Impact from instrument",
#     who_it_harms="Audience",
#     how_it_harms="Slide could hit audience member, causing impact injury.",
#     uncontrolled_likelihood="4",
#     uncontrolled_severity="2",
#     uncontrolled_risk=8,
#     prevention="Keep safe distance between the player and audience; hold instrument securely",
#     mitigation="",
#     controlled_likelihood="1",
#     controlled_severity="2",
#     controlled_risk="2"
# )

# RA_2 = RiskAssessment(
#     activity="Using a trombone as a demonstration for a TPS presentation",
#     hazard="Loud noise",
#     who_it_harms="Everyone present",
#     how_it_harms="Loud noise from instrument can cause hearing damage.",
#     uncontrolled_likelihood="4",
#     uncontrolled_severity="1",
#     uncontrolled_risk="4",
#     prevention="Play quietly, at a volume suitable for the room",
#     mitigation="Keep a space between the player and audience",
#     controlled_likelihood="1",
#     controlled_severity="1",
#     controlled_risk="1"
# )

# RA_3 = RiskAssessment(
#     activity="Using a trombone as a demonstration for a TPS presentation",
#     hazard="Water from instrument",
#     who_it_harms="Audience",
#     how_it_harms="Condensation formed in instrument could spread germs if released",
#     uncontrolled_likelihood="4",
#     uncontrolled_severity="1",
#     uncontrolled_risk="4",
#     prevention="Ensure water is not released during presentation",
#     mitigation="Keep a space between the player and audience",
#     controlled_likelihood="1",
#     controlled_severity="1",
#     controlled_risk="1"
# )

RA_empty_input = RiskAssessment(
    activity="",
    hazard="Loud noise",
    who_it_harms="Everyone present",
    how_it_harms="Loud noise from instrument can cause hearing damage.",
    uncontrolled_likelihood="4",
    uncontrolled_severity="1",
    uncontrolled_risk="4",
    prevention="Play quietly, at a volume suitable for the room",
    mitigation="1",
    controlled_likelihood="1",
    controlled_severity="1",
    controlled_risk="1",
    is_prevention_correct=True,
    is_mitigation_correct=True
)

RA_mitigation_wrong_type = RiskAssessment(
    activity="Using a trombone as a demonstration for a TPS presentation",
    hazard="Loud noise",
    who_it_harms="Everyone present",
    how_it_harms="Loud noise from instrument can cause hearing damage.",
    uncontrolled_likelihood="4",
    uncontrolled_severity="1",
    uncontrolled_risk="4",
    prevention="Play quietly, at a volume suitable for the room",
    mitigation="1",
    controlled_likelihood="1",
    controlled_severity="1",
    controlled_risk="1",
    is_prevention_correct=True,
    is_mitigation_correct=True
)

RA_controlled_likelihood_wrong_type = RiskAssessment(
    activity="Using a trombone as a demonstration for a TPS presentation",
    hazard="Loud noise",
    who_it_harms="Everyone present",
    how_it_harms="Loud noise from instrument can cause hearing damage.",
    uncontrolled_likelihood="4",
    uncontrolled_severity="1",
    uncontrolled_risk="4",
    prevention="Play quietly, at a volume suitable for the room",
    mitigation="Keep a space between the player and audience",
    controlled_likelihood="Keep a space between the player and audience",
    controlled_severity="1",
    controlled_risk="1",
    is_prevention_correct=True,
    is_mitigation_correct=True
)

RA_4 = RiskAssessment(
    activity="Fluids laboratory",
    hazard="Ink spillage",
    who_it_harms="Students",
    how_it_harms="Serious eye damage",
    uncontrolled_likelihood="2",
    uncontrolled_severity="3",
    uncontrolled_risk="6",
    prevention="Wear safety glasses",
    mitigation="Wash your eyes with clean water.",
    controlled_likelihood="1",
    controlled_severity="3",
    controlled_risk="3",
    is_prevention_correct=True,
    is_mitigation_correct=True
)

RA_5 = RiskAssessment(
    activity="Fluids laboratory",
    hazard="Wet hands",
    who_it_harms="Students",
    how_it_harms="Electric shock of students when touching electronics (pump power supply) with wet hands",
    uncontrolled_likelihood="3",
    uncontrolled_severity="3",
    uncontrolled_risk="9",
    prevention="Students should make sure they touch electronics only with dry hands",
    mitigation="Unplug the pump and call for urgent medical assistance",
    controlled_likelihood="2",
    controlled_severity="3",
    controlled_risk="6",
    is_prevention_correct=True,
    is_mitigation_correct=True
)

RA_6 = RiskAssessment(
    activity="Fluids laboratory",
    hazard="Tripping over personal belongings",
    who_it_harms="Students",
    how_it_harms="Tripping can cause physical harm. It can also cause the equipment to be damaged.",
    uncontrolled_likelihood="5",
    uncontrolled_severity="2",
    uncontrolled_risk="10",
    prevention="Put all belongings away from footpaths",
    mitigation="Take care when walking around",
    controlled_likelihood="1",
    controlled_severity="2",
    controlled_risk="2",
    is_prevention_correct=True,
    is_mitigation_correct=True
)

RA_7 = RiskAssessment(
    activity="Fluids laboratory",
    hazard="Spilling water",
    who_it_harms="Students",
    how_it_harms="Injuries caused by possible slipping on wet floor",
    uncontrolled_likelihood="3",
    uncontrolled_severity="2",
    uncontrolled_risk="6",
    prevention="Do not move the water tank when it is full",
    mitigation="""If someone gets injured due to slipping, apply an ice pack to the injured area and 
    seek medical advice without delay.""",
    controlled_likelihood="2",
    controlled_severity="2",
    controlled_risk="4",
    is_prevention_correct=True,
    is_mitigation_correct=True
)

RA_8 = RiskAssessment(
    activity="Fluids laboratory",
    hazard="Syringes with sharp needles",
    who_it_harms="Students",
    how_it_harms="Sharp needles can pierce the skin and cause bleeding",
    uncontrolled_likelihood="3",
    uncontrolled_severity="3",
    uncontrolled_risk="9",
    prevention="Point needle away from yourself and others",
    mitigation="Wear lab coat and PPE", # This is both prevention and mitigation
    controlled_likelihood="2",
    controlled_severity="1",
    controlled_risk="2",
    is_prevention_correct=True,
    is_mitigation_correct=True
)

RA_9 = RiskAssessment(
    activity="Fluids laboratory",
    hazard="Electrocution",
    who_it_harms="Students",
    how_it_harms="Electrocuted by mains voltage", # This is a description of the process not the harm on the students
    uncontrolled_likelihood="2",
    uncontrolled_severity="2",
    uncontrolled_risk="4",
    prevention="Pump plug stays away from water",
    mitigation="First aid on site",
    controlled_likelihood="1",
    controlled_severity="2",
    controlled_risk="2",
    is_prevention_correct=True,
    is_mitigation_correct=False
)

RA_10 = RiskAssessment(
    activity="Fluids laboratory",
    hazard="High speed air in wind tunnels",
    who_it_harms="Students",
    how_it_harms="Impact injury",
    uncontrolled_likelihood="4",
    uncontrolled_severity="3",
    uncontrolled_risk="12",
    prevention="Stay out of flow of wind tunnel",
    mitigation="Wear lab coat and PPE", # This is both prevention and mitigation
    controlled_likelihood="1",
    controlled_severity="2",
    controlled_risk="2",
    is_prevention_correct=True,
    is_mitigation_correct=True
)

RA_11 = RiskAssessment(
    activity="Fluids laboratory",
    hazard="Broken shards of glass",
    who_it_harms="Students",
    how_it_harms="Get trapped in soles of shoes",
    uncontrolled_likelihood="3",
    uncontrolled_severity="3",
    uncontrolled_risk="9",
    prevention="Handle equipment with care",
    mitigation="Vacate area of damage",
    controlled_likelihood="2",
    controlled_severity="1",
    controlled_risk="2",
    is_prevention_correct=True,
    is_mitigation_correct=True
)

RA_12 = RiskAssessment(
    activity="Fluids laboratory",
    hazard="Wires/tubing",
    who_it_harms="Anyone present", # Not specific
    how_it_harms="Trip/entanglement",
    uncontrolled_likelihood="2",
    uncontrolled_severity="4",
    uncontrolled_risk="8",
    prevention="Keep a tidy workspace",
    mitigation="First aid on site",
    controlled_likelihood="1",
    controlled_severity="3",
    controlled_risk="3",
    is_prevention_correct=True,
    is_mitigation_correct=False
)

example_risk_assessments = [RA_4, RA_5, RA_6, RA_7, RA_8, RA_9, RA_10, RA_11, RA_12]