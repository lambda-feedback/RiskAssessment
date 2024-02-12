from TestModelAccuracy import TestModelAccuracyForCompleteMitigationPromptPipeline
from LLMCaller import OpenAILLM
from example_risk_assessments_copy import example_risk_assessments

from ExamplesGenerator import RiskAssessmentExamplesGeneratorForMultiplePrompts

if __name__ == '__main__':

    examples_generator = RiskAssessmentExamplesGeneratorForMultiplePrompts(risk_assessments=example_risk_assessments,
                                                         ground_truth_parameter='mitigation_prompt_expected_output',
                                                         method_to_get_prompt_input='get_mitigation_input')
    
    examples = examples_generator.get_risk_assessment_and_expected_output_list()

    test_accuracy = TestModelAccuracyForCompleteMitigationPromptPipeline(
        test_description="""Testing mitigation input in student Fluids Lab and TPS presentation Risk Assessment examples.
                            
                            First time testing combination of first aid, protective clothing and mitigation prompts""",
                                      LLM=OpenAILLM(),
                                                LLM_name='gpt-3.5-turbo',
                                                list_of_risk_assessment_and_expected_outputs=examples,
                                                sheet_name='Combined Mitigation Prompts')
    test_accuracy.run_test()