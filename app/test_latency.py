from LLMCaller import *
from evaluation import evaluation_function, Params
from GoogleSheetsWriter import GoogleSheetsWriter
from datetime import datetime

from example_risk_assessments import physical_risks_to_individuals__original_student_data

def test_latency_of_evaluation_function(LLM_name: str, risk_assessments_dict):

    risk_assessments = risk_assessments_dict['risk_assessments']

    responses = [risk_assessment.convert_risk_assessment_to_evaluation_function_list_input() for risk_assessment in risk_assessments]
    
    start_time = time.time()

    for response in responses:
        answer = None
        params: Params = {"is_feedback_text": False, "is_risk_matrix": False, "is_risk_assessment": True, "LLM": LLM_name}

        result = evaluation_function(response, answer, params)

    end_time = time.time()

    elapsed_time = end_time - start_time

    average_latency = elapsed_time / len(risk_assessments)

    sheets_writer = GoogleSheetsWriter(sheet_name='Latency Test')

    sheets_writer.write_to_sheets([LLM_name, average_latency])

    return result

if __name__ == "__main__":
    for LLM_name in LLM_dictionary.keys():
        test_latency_of_evaluation_function(LLM_name, physical_risks_to_individuals__original_student_data)
    
    

