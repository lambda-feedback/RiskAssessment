from LLMCaller import *

LLM = MixtralLLM()

# json = LLM.get_JSON_output_from_API_call(prompt="""If the input is an example of an activity, answer True, else answer False.                                
# Input: "Bowling"
# Output: True

# Input: "Cheese"
# Output: False

# Input: "Dancing"
# Overall Answer: """)

def instruction_format(sys_message: str, query: str):
    # note, don't "</s>" to the end
    return f'<s> [INST] {sys_message} [/INST]\nUser: {query}\nAssistant: '
#     return f'<s> [INST] {sys_message} [/INST]\nUser: {query}\nAssistant: ```json\n{{\n"tool_name": '
    

sys_msg = """Classify the following input as either "No information provided" or "Control measure".

Use the following output format:
Overall Answer: <your answer>

Here are some examples:

Input: "Bike collides with car"
Overall Answer: Control measure

Input: "Not applicable at this time"
Overall Answer: No information provided

"""
query = "Input: 'Not applicable'"

input_prompt = instruction_format(sys_msg, query)

json = LLM.get_JSON_output_from_API_call(prompt=input_prompt)

print(json)