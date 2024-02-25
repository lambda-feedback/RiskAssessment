# pytest -v -s evaluation_tests.py

# The -s option above is so you can see printouts even if the test fails

import unittest

try:
    from .evaluation import Params, evaluation_function
    from .example_risk_assessments import RA_5, RA_mitigation_wrong_type, RA_controlled_likelihood_wrong_type, RA_empty_input
    from .LLMCaller import LLMCaller, LLMWithCandidateLabels, LLMWithGeneratedText, OpenAILLM
    from .PromptInputs import Activity
    from .RegexPatternMatcher import RegexPatternMatcher
except:
    from evaluation import Params, evaluation_function
    from example_risk_assessments import RA_5, RA_mitigation_wrong_type, RA_controlled_likelihood_wrong_type, RA_empty_input
    from LLMCaller import LLMCaller, LLMWithCandidateLabels, LLMWithGeneratedText, OpenAILLM
    from PromptInputs import Activity
    from RegexPatternMatcher import RegexPatternMatcher

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

    # def test_returns_incorrect_field(self):
    #     response = [["Students"],
    #                 ["Water being spilt on the floor"],
    #                 ["Slipping on the water on the floor causing Impact injuries"],
    #                 ["Students"],
    #                 ["4"],
    #                 ["1"],
    #                 ["4"],
    #                 ["Do not move the water tank when it is full"],
    #                 ["""If someone gets injured due to slipping, apply an ice pack to the injured area and 
    #                 seek medical advice without delay."""],
    #                 ["1"],
    #                 ["1"], 
    #                 ["1"]]
        
    #     answer, params = None, None

    #     result = evaluation_function(response, answer, params)

    #     print(result.get("feedback"))

    #     self.assertEqual(result.get("is_correct"), False)

    # def test_returns_is_correct_true(self):
    #     response = [["Fluids laboratory"],
    #                 ["Water being spilt on the floor"],
    #                 ["Slipping on the water on the floor causing impact injuries"],
    #                 ["Students"],
    #                 ["4"],
    #                 ["1"],
    #                 ["4"],
    #                 ["Do not move the water tank when it is full"],
    #                 ["""If someone gets injured due to slipping, apply an ice pack to the injured area and 
    #                 seek medical advice without delay."""],
    #                 ["1"],
    #                 ["1"], 
    #                 ["1"]]
    #     answer = None
    #     params: Params = {"is_feedback_text": False, "is_risk_matrix": False, "is_risk_assessment": True}

    #     result = evaluation_function(response, answer, params)

    #     print(result.get("feedback"))

    #     self.assertEqual(result.get("is_correct"), True)

    def test_no_information_provided_in_mitigation_input(self):
        response = [["Fluids laboratory"],
                    ["Water being spilt on the floor"],
                    ["Slipping on the water on the floor causing impact injuries"],
                    ["Students"],
                    ["4"],
                    ["1"],
                    ["4"],
                    ["Do not move the water tank when it is full"],
                    ["Not applicable"],
                    ["1"],
                    ["1"], 
                    ["1"]]
        answer = None
        params: Params = {"is_feedback_text": False, "is_risk_matrix": False, "is_risk_assessment": True}

        result = evaluation_function(response, answer, params)

        print(result.get("feedback"))

        self.assertEqual(result.get("is_correct"), True)

    # def test_when_prevention_entered_as_mitigation(self):
    #     response = [["Fluids laboratory"],
    #                 ["Water being spilt on the floor"],
    #                 ["Slipping on the water on the floor causing impact injuries"],
    #                 ["Students"],
    #                 ["4"],
    #                 ["1"],
    #                 ["4"],
    #                 ["Do not move the water tank when it is full"],
    #                 ["Taking care when moving water bucket"],
    #                 ["1"],
    #                 ["1"], 
    #                 ["1"]]
        
    #     answer = None
    #     params: Params = {"is_feedback_text": False, "is_risk_matrix": False, "is_risk_assessment": True}

    #     result = evaluation_function(response, answer, params)

    #     print(result.get("feedback"))

    #     self.assertIn(result.get("is_correct"), [True, False])

    def test_when_is_text_feedback_true(self):
        response = [['It was good']]
        
        answer = None
        params: Params = {"is_feedback_text": True, "is_risk_matrix": False, "is_risk_assessment": False}

        result = evaluation_function(response, answer, params)

        self.assertEqual(result.get("feedback"), "Thank you for your feedback")

        self.assertEqual(result.get("is_correct"), True)
    
    def test_risk_matrix_false(self):
        response = [["1", "1", "1"],
                    ["1", "1", "1"]]
        
        answer = None
        params: Params = {"is_feedback_text": False, "is_risk_matrix": True, "is_risk_assessment": False}

        result = evaluation_function(response, answer, params)
        self.assertEqual(result.get("is_correct"), False)

    def test_risk_matrix_true(self):
        response = [["4", "2", "8"],
                    ["2", "2", "4"]]
        
        answer = None
        params: Params = {"is_feedback_text": False, "is_risk_matrix": True, "is_risk_assessment": False}

        result = evaluation_function(response, answer, params)

        print(result.get("feedback"))
        
        self.assertEqual(result.get("is_correct"), True)

                
    def test_handles_empty_input(self):
        self.assertEqual(RA_empty_input.get_empty_fields(), ['Activity'])
        self.assertEqual(RA_5.get_empty_fields(), [])
    
    def test_does_string_represent_an_integer(self):

        self.assertEqual(RA_5.does_string_represent_an_integer('1'), True)
        self.assertEqual(RA_5.does_string_represent_an_integer('1.0'), False)
        self.assertEqual(RA_5.does_string_represent_an_integer('One'), False)
    
    def test_does_string_represent_words(self):

        self.assertEqual(RA_5.does_string_represent_words('1'), False)
        self.assertEqual(RA_5.does_string_represent_words('1.0'), False)
        self.assertEqual(RA_5.does_string_represent_words('One'), True)

    def test_get_word_fields_incorrect(self):
        self.assertEqual(RA_mitigation_wrong_type.get_word_fields_incorrect(), ['Mitigation'])

    def test_get_integer_fields_incorrect(self):
        self.assertEqual(RA_controlled_likelihood_wrong_type.get_integer_fields_incorrect(), ['Controlled Likelihood'])

    def test_regex_prevention_mitigation_neither(self):
        regex = RegexPatternMatcher()
        self.assertEqual(regex.check_string_for_prevention_mitigation_or_neither('Answer: prevention'), 'prevention')
        self.assertEqual(regex.check_string_for_prevention_mitigation_or_neither('Therefore, answer: mitigation'), 'mitigation')
        self.assertEqual(regex.check_string_for_prevention_mitigation_or_neither('Thus, answer: Neither'), 'neither')

if __name__ == "__main__":
    unittest.main()
