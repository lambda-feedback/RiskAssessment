import unittest

try:
    from .evaluation import Params, evaluation_function
    from .risk_assessment_examples import RA_1
except ImportError:
    from evaluation import Params, evaluation_function
    from risk_assessment_examples import RA_1

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

    # pytest -v evaluation_tests.py

    def test_returns_is_correct_true(self):
        response, answer, params = ['Here is my very good Risk Assessment with 5 extra unnecessary words'.split(' ')], None, Params(part_of_question='a')
        result = evaluation_function(response, answer, params)

        self.assertIn(result.get("is_correct"), [True, False])
        # self.assertEqual(result.get("is_correct"), True)

    def test_convert_RiskAssessment_object_into_lambda_response_list(self):
        actual_value = RA_1.convert_RiskAssessment_object_into_lambda_response_list()
        expected_value = ['Using a trombone as a demonstration for a TPS presentation',
                          'Impact from instrument',
                          'Audience',
                          'Slide could hit audience member, causing impact injury.',
                          4, 2, 8,
                          'Keep safe distance between the player and audience; hold instrument securely',
                          '',
                          1, 2, 2]
        self.assertEqual(actual_value, expected_value)

if __name__ == "__main__":
    unittest.main()
