try:
    from .RiskAssessment import RiskAssessment
except ImportError:
    from RiskAssessment import RiskAssessment

RA_1 = RiskAssessment(
    activity="Using a trombone as a demonstration for a TPS presentation",
    hazard="Impact from instrument",
    who_it_harms="Audience",
    how_it_harms="Slide could hit audience member, causing impact injury.",
    uncontrolled_likelihood=4,
    uncontrolled_severity=2,
    uncontrolled_risk=8,
    prevention="Keep safe distance between the player and audience; hold instrument securely",
    mitigation="",
    controlled_likelihood=1,
    controlled_severity=2,
    controlled_risk=2
)

RA_2 = RiskAssessment(
    activity="Using a trombone as a demonstration for a TPS presentation",
    hazard="Loud noise",
    who_it_harms="Everyone present",
    how_it_harms="Loud noise from instrument can cause hearing damage.",
    uncontrolled_likelihood=4,
    uncontrolled_severity=1,
    uncontrolled_risk=4,
    prevention="Play quietly, at a volume suitable for the room",
    mitigation="Keep a space between the player and audience",
    controlled_likelihood=1,
    controlled_severity=1,
    controlled_risk=1
)

RA_3 = RiskAssessment(
    activity="Using a trombone as a demonstration for a TPS presentation",
    hazard="Water from instrument",
    who_it_harms="Audience",
    how_it_harms="Condensation formed in instrument could spread germs if released",
    uncontrolled_likelihood=4,
    uncontrolled_severity=1,
    uncontrolled_risk=4,
    prevention="Ensure water is not released during presentation",
    mitigation="Keep a space between the player and audience",
    controlled_likelihood=1,
    controlled_severity=1,
    controlled_risk=1
)

RA_4 = RiskAssessment(
    activity="Fluids laboratory",
    hazard="Ink spillage",
    who_it_harms="Students",
    how_it_harms="Serious eye damage",
    uncontrolled_likelihood=2,
    uncontrolled_severity=3,
    uncontrolled_risk=6,
    prevention="Wear safety glasses",
    mitigation="Wash your eyes with clean water and seek medical advice without delay.",
    controlled_likelihood=1,
    controlled_severity=3,
    controlled_risk=3
)

RA_5 = RiskAssessment(
    activity="Fluids laboratory",
    hazard="Wet hands",
    who_it_harms="Students",
    how_it_harms="Electric shock of students when touching electronics (pump power supply) with wet hands",
    uncontrolled_likelihood=3,
    uncontrolled_severity=3,
    uncontrolled_risk=9,
    prevention="Students should make sure they touch electronics only with dry hands",
    mitigation="Unplug the pump and call for urgent medical assistance",
    controlled_likelihood=2,
    controlled_severity=3,
    controlled_risk=6
)

RA_6 = RiskAssessment(
    activity="Fluids laboratory",
    hazard="Tripping over personal belongings",
    who_it_harms="Students",
    how_it_harms="Tripping can cause physical harm. It can also cause the equipment to be damaged.",
    uncontrolled_likelihood=5,
    uncontrolled_severity=2,
    uncontrolled_risk=10,
    prevention="Put all belongings away from footpaths",
    mitigation="Take care when walking around",
    controlled_likelihood=1,
    controlled_severity=2,
    controlled_risk=2
)


example_risk_assessments = [RA_1, RA_2, RA_3, RA_4, RA_5, RA_6]