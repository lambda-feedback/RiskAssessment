# pytest -v -s evaluation_tests.py

# The -s option above is so you can see printouts even if the test fails

import unittest

try:
    from .utils.LLMCaller import GPT_3_point_5_turbo, ClaudeSonnetLLM
    from .evaluation import Params, evaluation_function
    from .example_risk_assessments import *
    from .utils.RegexPatternMatcher import RegexPatternMatcher
    from .test_modules.TestModelAccuracy import *
    from .prompts.PromptInput import NoInformationProvided, HowItHarmsInContext, WhoItHarmsInContext
    from .test_scripts.test_no_information_provided import no_information_provided_examples, information_provided_examples
    from .test_scripts.risk_domain_test_for_how_it_harms_prompt import HowItHarmsInContextExamplesGeneratorForRiskDomainTest
    from .RiskAssessment import RiskAssessmentWithoutNumberInputs
except:
    from .utils.LLMCaller import GPT_3_point_5_turbo, ClaudeSonnetLLM
    from evaluation import Params, evaluation_function
    from example_risk_assessments import *
    from utils.RegexPatternMatcher import RegexPatternMatcher
    from test_modules.TestModelAccuracy import *
    from prompts.PromptInput import NoInformationProvided, HowItHarmsInContext, WhoItHarmsInContext
    from test_scripts.test_no_information_provided import no_information_provided_examples, information_provided_examples
    from test_scripts.risk_domain_test_for_how_it_harms_prompt import HowItHarmsInContextExamplesGeneratorForRiskDomainTest
    from RiskAssessment import RiskAssessmentWithoutNumberInputs

class TestEvaluationFunction(unittest.TestCase):
    """
    TestCase Class used to test the algorithm.
    ---
    Tests are used here to check that the algorithm written
    is working as it should.

    It's best practise to write these tests first to get a
    kind of 'specification' for how your algorithm should
    work, and you should run these tests before committing
    your code to AWS.

    Read the docs on how to use unittest here:
    https://docs.python.org/3/library/unittest.html

    Use evaluation_function() to check your algorithm works
    as it should.
    """

    ### UNIT TESTS ON PROMPTS ###
    # def test_no_information_provided_prompt(self):
    #     LLM = GPT_3_point_5_turbo(temperature=0.1)
        
    #     tests = []

    #     for example in no_information_provided_examples:
    #         tests.append(TestPromptOnSingleExample(
    #                                         LLM=LLM,
    #                                         input_object=NoInformationProvided(input=example), 
    #                                         expected_output='no information provided'))
            
    #     for example in information_provided_examples:
    #         tests.append(TestPromptOnSingleExample(
    #                                         LLM=LLM,
    #                                         input_object=NoInformationProvided(input=example), 
    #                                         expected_output='control measure'))
            
    #     for test in tests:
    #         self.assertTrue(test.is_pattern_matched_equal_to_expected_output())

    # def test_how_it_harms_in_context_prompt__input_field(self):
    #     # TODO: Should use same LLM for all of them
    #     LLM = ClaudeSonnetLLM(system_message='', temperature=0.1)

    #     tests = []
    #     # How it harms input is actually an activity
    #     tests.append(TestPromptOnSingleExample(
    #         LLM=LLM,
    #         input_object=HowItHarmsInContext(
    #             activity="Riding a bike",
    #             hazard="Collision with car",
    #             how_it_harms="Riding a bike"),
    #         expected_output=False))
        
    #     for test in tests:
    #         self.assertTrue(test.is_pattern_matched_equal_to_expected_output())
    
    # def test_how_it_harms_in_context_prompt__risk_domain(self):
    #     LLM = GPT_3_point_5_turbo(temperature=0.1)

    #     tests = []

    #     tests.append(TestPromptOnSingleExample(
    #         LLM=LLM,
    #         input_object=HowItHarmsInContext(
    #             activity="Fluids laboratory",
    #             hazard="Syringes with sharp needles",
    #             how_it_harms="Sharp needles can pierce the skin and cause bleeding"),
    #         expected_output=True))
        
    #     tests.append(TestPromptOnSingleExample(
    #         LLM=LLM,
    #         input_object=HowItHarmsInContext(
    #             activity="Camping near a forest",
    #             hazard="Wildfire",
    #             how_it_harms="Wildfires can cause extensive damage to wildlife habitats"),
    #         expected_output=True))
        
    #     tests.append(TestPromptOnSingleExample(
    #         LLM=LLM,
    #         input_object=HowItHarmsInContext(
    #             activity="Fluids laboratory",
    #             hazard="Syringes with sharp needles",
    #             how_it_harms="Wildfires can cause extensive damage to wildlife habitats"),
    #         expected_output=False))
        
    #     tests.append(TestPromptOnSingleExample(
    #         LLM=LLM,
    #         input_object=HowItHarmsInContext(
    #             activity="Camping near a forest",
    #             hazard="Wildfire",
    #             how_it_harms="Sharp needles can pierce the skin and cause bleeding"),
    #         expected_output=False))
        
    #     for test in tests:
    #         self.assertTrue(test.is_pattern_matched_equal_to_expected_output())
    
    # def test_who_it_harms_in_context_prompt__input_field(self):
    #     LLM = GPT_3_point_5_turbo(temperature=0.1)
    #     tests = []

    #     # Who it harms input is actually an activity
    #     # TODO: Add a test
        
    #     # Who it harms input is actually a hazard
    #     # Add a test

    #     for test in tests:
    #         self.assertTrue(test.is_pattern_matched_equal_to_expected_output())

    # def test_who_it_harms_in_context_prompt__people_who_cannot_be_harmed(self):
    #     LLM = ClaudeSonnetLLM(system_message='', temperature=0.1)

    #     tests = []

    #     tests.append(TestPromptOnSingleExample(
    #         LLM=LLM,
    #         input_object=WhoItHarmsInContext(
    #                 activity="Sitting at desk with poor ergonomics",
    #                 hazard="Sitting for long periods of time",
    #                 how_it_harms="Development of chronic pain and discomfort",
    #                 who_it_harms="Dogs"
    #             ),
    #         expected_output=False))
        
    #     tests.append(TestPromptOnSingleExample(
    #         LLM=LLM,
    #         input_object=WhoItHarmsInContext(
    #                 activity="Going outside on sunny day without sunscreen",
    #                 hazard="UV radiation",
    #                 how_it_harms="Increased risk of skin cancer and premature aging",
    #                 who_it_harms="People with adequate sun protection"
    #             ),
    #         expected_output=False))
        
    #     for test in tests:
    #         self.assertTrue(test.is_pattern_matched_equal_to_expected_output())

    # def test_an_input_that_is_neither_prevention_nor_mitigation(self):
    #     # LLM = GPT_3_point_5_turbo(temperature=0.1)
    #     LLM = ClaudeSonnetLLM(system_message='', temperature=0.1)

    #     tests = []
        
    #     # TODO: Add more examples
    #     RA_cycling_high_viz__neither = RiskAssessmentWithoutNumberInputs(
    #         activity = "Riding a Bike",
    #         hazard = "Getting hit",
    #         how_it_harms = "Could injure",
    #         who_it_harms = "The cyclist",
    #         prevention = "Wear non reflective clothing",
    #         mitigation = "Wear a t-shirt",
    #         prevention_prompt_expected_class = "neither",
    #         mitigation_prompt_expected_class = "neither",
    #         risk_domain="physical risk to individuals"
    #     )

    #     # Test prevention input
    #     tests.append(TestPreventionPromptOnSingleExample(
    #         LLM=LLM,
    #         input_object=RA_cycling_high_viz__neither,
    #         expected_output=RA_cycling_high_viz__neither.prevention_prompt_expected_class))
        
    #     # Test mitigation input
    #     tests.append(TestMitigationPromptOnSingleExample(
    #         LLM=LLM,
    #         input_object=RA_cycling_high_viz__neither,
    #         expected_output=RA_cycling_high_viz__neither.mitigation_prompt_expected_class))
        
    #     for test in tests:
    #         self.assertTrue(test.is_pattern_matched_equal_to_expected_output())

    # def test_prevention_and_mitigation_are_switched(self):
    #     # LLM = GPT_3_point_5_turbo(temperature=0.1)
    #     LLM = ClaudeSonnetLLM(system_message='', temperature=0.1)

    #     tests = []

    #     # TODO: Add more examples
    #     RA_cycling_high_viz = RiskAssessmentWithoutNumberInputs(
    #         activity = "Riding a Bike",
    #         hazard = "Getting hit",
    #         how_it_harms = "Could injure",
    #         who_it_harms = "The cyclist",
    #         prevention = "Wear helmet",
    #         mitigation = "Wear high viz clothing", 
    #         prevention_prompt_expected_class = "mitigation",
    #         mitigation_prompt_expected_class = "prevention",
    #         risk_domain="physical risk to individuals"
    #     )

    #     # Test prevention input
    #     tests.append(TestPreventionPromptOnSingleExample(
    #         LLM=LLM,
    #         input_object=RA_cycling_high_viz,
    #         expected_output=RA_cycling_high_viz.prevention_prompt_expected_class))
        
    #     # Test mitigation input
    #     tests.append(TestMitigationPromptOnSingleExample(
    #         LLM=LLM,
    #         input_object=RA_cycling_high_viz,
    #         expected_output=RA_cycling_high_viz.mitigation_prompt_expected_class))
        
    #     for test in tests:
    #         self.assertTrue(test.is_pattern_matched_equal_to_expected_output())

    # ###  UNIT TESTS SMALL FUNCTIONS ###
    # def test_when_is_text_feedback_true(self):
    #     response = [['It was good']]
        
    #     answer = None
    #     params: Params = {"is_feedback_text": True, "is_risk_matrix": False, "is_risk_assessment": False}

    #     result = evaluation_function(response, answer, params)

    #     self.assertEqual(result.get("feedback"), "Thank you for your feedback")

    #     self.assertEqual(result.get("is_correct"), True)
    
    # def test_risk_matrix_false(self):
    #     response = [["1", "1", "1"],
    #                 ["1", "1", "1"]]
        
    #     answer = None
    #     params: Params = {"is_feedback_text": False, "is_risk_matrix": True, "is_risk_assessment": False}

    #     result = evaluation_function(response, answer, params)
    #     self.assertEqual(result.get("is_correct"), False)

    # def test_risk_matrix_true(self):
    #     response = [["4", "2", "8"],
    #                 ["2", "2", "4"]]
        
    #     answer = None
    #     params: Params = {"is_feedback_text": False, "is_risk_matrix": True, "is_risk_assessment": False}

    #     result = evaluation_function(response, answer, params)

    #     print(result.get("feedback"))
        
    #     self.assertEqual(result.get("is_correct"), True)

    # def test_handles_empty_input(self):
    #     self.assertEqual(RA_empty_input.get_empty_fields(), ['Activity'])
    #     self.assertEqual(RA_hearing_damage.get_empty_fields(), [])
    
    # def test_does_string_represent_an_integer(self):

    #     self.assertEqual(RA_hearing_damage.does_string_represent_an_integer('1'), True)
    #     self.assertEqual(RA_hearing_damage.does_string_represent_an_integer('1.0'), False)
    #     self.assertEqual(RA_hearing_damage.does_string_represent_an_integer('One'), False)
    
    # def test_does_string_represent_words(self):

    #     self.assertEqual(RA_hearing_damage.does_string_represent_words('1'), False)
    #     self.assertEqual(RA_hearing_damage.does_string_represent_words('1.0'), False)
    #     self.assertEqual(RA_hearing_damage.does_string_represent_words('One'), True)

    # def test_get_word_fields_incorrect(self):
    #     self.assertEqual(RA_mitigation_wrong_type.get_word_fields_incorrect(), ['Mitigation'])

    # def test_get_integer_fields_incorrect(self):
    #     self.assertEqual(RA_controlled_likelihood_wrong_type.get_integer_fields_incorrect(), ['Controlled Likelihood'])

    # def test_regex_pattern_matcher(self):
    #     regex = RegexPatternMatcher()
    #     self.assertEqual(regex.check_string_for_prevention_mitigation_or_neither('Answer: prevention'), 'prevention')
    #     self.assertEqual(regex.check_string_for_prevention_mitigation_or_neither('Therefore, answer: mitigation'), 'mitigation')
    #     self.assertEqual(regex.check_string_for_prevention_mitigation_or_neither('Thus, answer: Neither'), 'neither')

    # ###  INTEGRATION TESTS ON EVALUATION FUNCTION ###
    def test_evaluation_function_with_correct_prevention_and_mitigation(self):
        response = [["Fluids laboratory"],
                    ["Water being spilt on the floor"],
                    ["Slipping on the water on the floor causing impact injuries"],
                    ["Students"],
                    ["4"],
                    ["1"],
                    ["4"],
                    ["Do not move the water tank when it is full"],
                    ["""If someone gets injured due to slipping, apply an ice pack to the injured area and 
                    seek medical advice without delay."""],
                    ["1"],
                    ["1"], 
                    ["1"]]
        
        answer = None
        params: Params = {"is_feedback_text": False, "is_risk_matrix": False, "is_risk_assessment": True, "LLM": "GPT-3.5 Turbo 1106"}

        result = evaluation_function(response, answer, params)

        print(result.get("feedback"))

        self.assertTrue(result.get("is_correct"))

    # def test_evaluation_function_with_prevention_entered_in_mitigation_field(self):
    #     response = [["Fluids laboratory"],
    #                 ["Water being spilt on the floor"],
    #                 ["Slipping on the water on the floor causing impact injuries"],
    #                 ["Students"],
    #                 ["4"],
    #                 ["1"],
    #                 ["4"],
    #                 ["Do not move the water tank when it is full"],
    #                 ["Do not move the water tank when it is full"],
    #                 ["1"],
    #                 ["1"], 
    #                 ["1"]]
        
    #     answer = None
    #     params: Params = {"is_feedback_text": False, "is_risk_matrix": False, "is_risk_assessment": True}

    #     result = evaluation_function(response, answer, params)

    #     print(result.get("feedback"))

    #     self.assertFalse(result.get("is_correct"))

    # def test_evaluation_function_with_neither_prevention_nor_mitigation_entered_in_prevention_field(self):
    #     response = [["Fluids laboratory"],
    #                 ["Water being spilt on the floor"],
    #                 ["Slipping on the water on the floor causing impact injuries"],
    #                 ["Students"],
    #                 ["4"],
    #                 ["1"],
    #                 ["4"],
    #                 ["Do not move the water tank when it is full"],
    #                 ["Do not move the water tank when it is full"],
    #                 ["1"],
    #                 ["1"], 
    #                 ["1"]]
        
    #     answer = None
    #     params: Params = {"is_feedback_text": False, "is_risk_matrix": False, "is_risk_assessment": True}

    #     result = evaluation_function(response, answer, params)

    #     print(result.get("feedback"))

    #     self.assertFalse(result.get("is_correct"))
    
    # def test_evaluation_function_with_empty_activity_field(self):
    #     response = [[""],
    #                 ["Water being spilt on the floor"],
    #                 ["Slipping on the water on the floor causing impact injuries"],
    #                 ["Students"],
    #                 ["4"],
    #                 ["1"],
    #                 ["4"],
    #                 ["Move the water tank when it is full"],
    #                 ["""If someone gets injured due to slipping, apply an ice pack to the injured area and 
    #                 seek medical advice without delay."""],
    #                 ["1"],
    #                 ["1"], 
    #                 ["1"]]
        
    #     answer = None
    #     params: Params = {"is_feedback_text": False, "is_risk_matrix": False, "is_risk_assessment": True}

    #     result = evaluation_function(response, answer, params)

    #     print(result.get("feedback"))

    #     self.assertFalse(result.get("is_correct"))

    # def test_evaluation_function_with_activity_field_input_of_incorrect_type(self):
    #     response = [["1"],
    #                 ["Water being spilt on the floor"],
    #                 ["Slipping on the water on the floor causing impact injuries"],
    #                 ["Students"],
    #                 ["4"],
    #                 ["1"],
    #                 ["4"],
    #                 ["Do not move the water tank when it is full"],
    #                 ["Do not move the water tank when it is full"],
    #                 ["1"],
    #                 ["1"], 
    #                 ["1"]]
        
    #     answer = None
    #     params: Params = {"is_feedback_text": False, "is_risk_matrix": False, "is_risk_assessment": True}

    #     result = evaluation_function(response, answer, params)

    #     print(result.get("feedback"))

    #     self.assertFalse(result.get("is_correct"))  

    # def test_evaluation_function_with_incorrect_risk_multiplication(self):
    #     response = [["Fluids laboratory"],
    #                 ["Water being spilt on the floor"],
    #                 ["Slipping on the water on the floor causing impact injuries"],
    #                 ["Students"],
    #                 ["4"],
    #                 ["1"],
    #                 ["2"],
    #                 ["Do not move the water tank when it is full"],
    #                 ["Do not move the water tank when it is full"],
    #                 ["1"],
    #                 ["1"], 
    #                 ["2"]]
        
    #     answer = None
    #     params: Params = {"is_feedback_text": False, "is_risk_matrix": False, "is_risk_assessment": True}

    #     result = evaluation_function(response, answer, params)

    #     print(result.get("feedback"))

    #     self.assertFalse(result.get("is_correct"))       

if __name__ == "__main__":
    unittest.main()
