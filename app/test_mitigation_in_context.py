from PromptInputs import Mitigation
from ExamplesGenerator import ExamplesGenerator
from TestModelAccuracy import TestModelAccuracy
from LLMCaller import OpenAILLM

from example_mitigations import correct_mitigation_examples_list, MitigationExamplesGenerator

if __name__ == '__main__':
    examples_generator = MitigationExamplesGenerator(correct_examples_list=correct_mitigation_examples_list)
    examples = examples_generator.get_input_and_expected_output_list()
    test_accuracy = TestModelAccuracy(LLM=OpenAILLM(),
                                                LLM_name='gpt-3.5-turbo',
                                                list_of_input_and_expected_outputs=examples,
                                                sheet_name='Mitigation In Context')
    test_accuracy.run_test()