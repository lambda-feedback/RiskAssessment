from TestModelAccuracy import TestModelAccuracy
from LLMCaller import *
from ExamplesGenerator import RiskAssessmentExamplesGeneratorForSinglePrompt
from example_risk_assessments import physical_risks_to_individuals__original_student_data

examples = RiskAssessmentExamplesGeneratorForSinglePrompt(
    risk_assessments=physical_risks_to_individuals__original_student_data['risk_assessments'],
    ground_truth_parameter='prevention_classification_prompt_ground_truth',
    method_to_get_prompt_input='get_prevention_classification_prompt_input'
)

if __name__ == '__main__':
    test = TestModelAccuracy(
        LLM=MistralLarge(temperature=0.1),
        list_of_input_and_expected_outputs=examples.get_input_and_expected_output_list(),
        sheet_name='Prevention Classification 2',
        examples_gathered_or_generated_message='Risk Assessments gathered from students',
        domain='Physical Risks to Individuals',
        is_first_test=True
    )

    test.run_test()