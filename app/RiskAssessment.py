from typing import Type
import csv

try:
    from .PromptInputs import *
    from .HuggingfaceLLMCaller import *
except ImportError:
    from PromptInputs import *
    from HuggingfaceLLMCaller import *

class PromptAndPromptOutput:
    def __init__(self, prompt, prompt_output):
        self.prompt = prompt
        self.prompt_output = prompt_output

class RiskAssessment:
    def __init__(self, activity, hazard, who_it_harms, how_it_harms,
                  uncontrolled_likelihood, uncontrolled_severity, uncontrolled_risk,
                 prevention, mitigation, controlled_likelihood, controlled_severity, controlled_risk):
        self.activity = activity
        self.hazard = hazard
        self.who_it_harms = who_it_harms
        self.how_it_harms = how_it_harms
        self.uncontrolled_likelihood = uncontrolled_likelihood
        self.uncontrolled_severity = uncontrolled_severity
        self.uncontrolled_risk = uncontrolled_risk
        self.prevention = prevention
        self.mitigation = mitigation
        self.controlled_likelihood = controlled_likelihood
        self.controlled_severity = controlled_severity
        self.controlled_risk = controlled_risk

    def convert_RiskAssessment_object_into_lambda_response_list(self):
        return list(vars(self).values())
    
    def get_activity_input(self):
        return Activity(activity=self.activity)
    
    def get_hazard_input(self):
        return Hazard(activity=self.activity, hazard=self.hazard)
    
    def get_how_it_harms_input(self):
        return HowItHarms(how_it_harms=self.how_it_harms,
                          activity=self.activity,
                          hazard = self.hazard)

    def get_who_it_harms_input(self):
        return WhoItHarms(who_it_harms=self.who_it_harms,
                          how_it_harms=self.how_it_harms,
                          activity=self.activity,
                          hazard=self.hazard)
    
    def get_prevention_input(self):
        return Prevention(prevention=self.prevention,
                          activity=self.activity,
                          hazard=self.hazard,
                          how_it_harms=self.how_it_harms,
                          who_it_harms=self.who_it_harms)
    
    def get_mitigation_input(self):
        return Mitigation(mitigation=self.mitigation,
                          activity=self.activity,
                          hazard=self.hazard,
                          how_it_harms=self.how_it_harms,
                          who_it_harms=self.who_it_harms)
    
    # TODO: Add ability to see prompt output percentages

    # TODO: Put a function in each of the PromptInputs which gets the prompt output. Each PromptInput class
    # should inherit this method. That way, you would no longer need a PromptAndPromptOutput class.
    
    def get_list_of_prompt_outputs(self, LLM_caller: Type[HuggingfaceLLMCaller]):
        return [PromptAndPromptOutput(prompt=self.get_activity_input().generate_prompt(), prompt_output=LLM_caller.get_model_output(self.get_activity_input())),
                                  PromptAndPromptOutput(prompt=self.get_hazard_input().generate_prompt(), prompt_output=LLM_caller.get_model_output(self.get_hazard_input())),
                                  PromptAndPromptOutput(prompt=self.get_how_it_harms_input().generate_prompt(), prompt_output=LLM_caller.get_model_output(self.get_how_it_harms_input())),
                                  PromptAndPromptOutput(prompt=self.get_who_it_harms_input().generate_prompt(), prompt_output=LLM_caller.get_model_output(self.get_who_it_harms_input())),
                                  PromptAndPromptOutput(prompt=self.get_prevention_input().generate_prompt(), prompt_output=LLM_caller.get_model_output(self.get_prevention_input())),
                                  PromptAndPromptOutput(prompt=self.get_mitigation_input().generate_prompt(), prompt_output=LLM_caller.get_model_output(self.get_mitigation_input()))]
    
    def write_prompt_outputs_to_csv(self, LLM_caller: Type[HuggingfaceLLMCaller], file_name, folder_path):
        prompt_and_prompt_outputs =  self.get_list_of_prompt_outputs(LLM_caller=LLM_caller)

        output_file = folder_path / file_name

        # Open a CSV file for writing
        with open(output_file, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            
            # Write headers to the CSV file
            csv_writer.writerow(["Prompt", "Response"])
            
            for i in range(len(prompt_and_prompt_outputs)):

                prompt = prompt_and_prompt_outputs[i].prompt
                response = prompt_and_prompt_outputs[i].prompt_output
                
                # Write the prompt and response to the CSV file
                csv_writer.writerow([prompt, response])

                print(prompt)
                print(response)

        print(f"CSV file '{output_file}' has been created.")