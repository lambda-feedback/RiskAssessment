from TestModelAccuracy import TestModelAccuracy
from LLMCaller import OpenAILLM
from example_risk_assessments_exemplar import example_risk_assessments

from ExamplesGenerator import RiskAssessmentExamplesGeneratorForSinglePrompt

clothing_items = [
    "T-shirt",
    "Jeans",
    "Hoodie"
]

non_clothing_items = [
    "Car",
    "Computer",
    "Chair"
]

if __name__ == '__main__':
    # examples = []

    # for example in clothing_items:
    #     examples.append(InputAndExpectedOutputForSinglePrompt(input=Clothing(control_measure=example), expected_output=True))

    # for example in non_clothing_items:
    #     examples.append(InputAndExpectedOutputForSinglePrompt(input=Clothing(control_measure=example), expected_output=False))

    examples_generator_prevention = RiskAssessmentExamplesGeneratorForSinglePrompt(risk_assessments=example_risk_assessments,
                                                         ground_truth_parameter='prevention_clothing',
                                                        method_to_get_prompt_input='get_prevention_clothing')
    
    examples_prevention = examples_generator_prevention.get_input_and_expected_output_list()

    examples_generator_mitigation = RiskAssessmentExamplesGeneratorForSinglePrompt(risk_assessments=example_risk_assessments,
                                                         ground_truth_parameter='mitigation_clothing',
                                                        method_to_get_prompt_input='get_mitigation_clothing')
    
    examples_mitigation = examples_generator_mitigation.get_input_and_expected_output_list()

    examples = examples_prevention + examples_mitigation
    
    test_accuracy = TestModelAccuracy(test_description="""Testing clothing prompt on prevention/mitigation input from student risk assessment examples""",
                                      LLM=OpenAILLM(),
                                                LLM_name='gpt-3.5-turbo',
                                                list_of_input_and_expected_outputs=examples,
                                                sheet_name='Clothing')
    test_accuracy.run_test()