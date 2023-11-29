# pytest -v -s local_tests.py

# The -s option above is so you can see printouts even if the test fails

from TestModelAccuracy import TestModelAccuracy, TestModelAccuracyWithGPT
from LLMCaller import OpenAILLM
from example_activities import activities

if __name__ == "__main__":
    test_accuracy = TestModelAccuracyWithGPT(LLM=OpenAILLM(),
                                                LLM_name='gpt',
                                                list_of_input_and_expected_outputs=activities,
                                                folder_name='activities')
    test_accuracy.run_test()
    test_accuracy.save_cost_of_calling_LLM_API(test_accuracy.total_cost_of_calling_LLM_API())