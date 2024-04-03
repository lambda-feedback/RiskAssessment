from LLMCaller import LLMCaller, OpenAILLM

prompt = """
Example Input:
Follow these instructions:
1. In one sentence, describe the hazard: 'Ink spillage' during the
activity: 'Fluids laboratory'.
2. In one sentence, explain whether or not 'Radiation exposure' is a way that this hazard causes harm.
3. If 'Radiation exposure' is a way that this hazard causes harm, answer True, else answer False.

Output:
Description: It is argued that an ink spillage during a fluids laboratory can cause radiation exposure.
Explanation: Radiation exposure is not a way that ink spillage during the fluids laboratory causes harm, 
as the hazard primarily involves physical contamination rather than radiation.
Answer: False.

Example Input
Follow these instructions:
1. In one sentence, describe the hazard: 'Electrocution' during the 
activity: 'Fluids laboratory'.
2. In one sentence, explain whether or not 'Electrocuted by mains voltage' is a way that this hazard causes harm. 
3. If 'Electrocuted by mains voltage' is a way that this hazard causes harm, answer True, else answer False.

Output:
Description: It is argued that wet hands during a fluids laboratory can cause harm through electrocution.
Explanation: As water is a conductor of electricity, touching electronics with wet hands can cause electrocution as
the water provides a path for electrical current to flow through the body.
Answer: True

Input:
N/A

Output format:
Answer: {answer}
"""

LLM = OpenAILLM(temperature=0.1, max_tokens=400)

prompt_output = LLM.get_model_output(prompt)

print(prompt_output)