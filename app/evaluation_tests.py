import unittest

try:
    from .evaluation import Params, evaluation_function
except ImportError:
    from evaluation import Params, evaluation_function


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

    # run pytest -v evaluation_tests.py

    def test_returns_is_correct_true(self):
        response, answer, params = None, None, Params(part_of_question='a')
        result = evaluation_function(response, answer, params)

        self.assertIn(result.get("is_correct"), [True, False])

if __name__ == "__main__":
    unittest.main()
