from TestModelAccuracy import TestModelAccuracy, TestModelAccuracyWithGPT
from LLMCaller import OpenAILLM
from example_how_it_harms import HowItHarmsLists

if __name__ == "__main__":
    how_it_harms = HowItHarmsLists()
    how_it_harms_examples = how_it_harms.get_input_and_expected_output_list()
    test_accuracy = TestModelAccuracyWithGPT(LLM=OpenAILLM(),
                                                LLM_name='GPT',
                                                list_of_input_and_expected_outputs=how_it_harms_examples,
                                                folder_name='how_it_harms')
    test_accuracy.run_test()
    test_accuracy.save_cost_of_calling_LLM_API(test_accuracy.total_cost_of_calling_LLM_API())