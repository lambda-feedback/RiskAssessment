from LLMCaller import LLMCaller, OpenAILLM

prompt = """
Input:
Follow these instructions:
1. In one sentence, describe the hazard: 'Ink spillage' during the
activity: 'Fluids laboratory' given how the hazard harms: 'Serious eye damage'
and who the hazard harms: 'Students'.
2. Describe the hazard event, which is the event that leads to harm.
3. Explain whether or not 'First aid' reduces the likelihood that the hazard event occurs.
If so, it is a prevention measure.
4. Assuming the hazard event occurs, explain whether or not 'First aid' removes or reduces the harm caused by the event.
If so, it is a mitigation measure.
5. If it is a prevention measure, answer 'Prevention'. If it is a migitation meausure, answer 'Mitigation'.
If it is neither a prevention measure nor a mitigation measure, answer 'Neither'. If it is both a        
prevention measure and a mitigation measure, answer 'Both'.

Output: 
Hazard Description: The hazard of 'Ink spillage' during the activity 'Fluids laboratory' can lead to serious eye damage to students.
Hazard Event Description: Ink being spilled onto a student's face.
Prevention Explanation: 'First aid' will not reduce the likelihood of ink being spilled on the student's face; it is therefore not a prevention measure.
Mitigation Explanation: If ink has been spilled onto a student's face, 'first aid' will help to wash the ink out of the eyes and reduce eye damage after the hazard event has occurred; as it reduces the harm caused by the hazard event, it is therefore a mitigation measure.
Answer: Mitigation.

Input:
Follow these instructions:
1. In one sentence, describe the hazard: 'Water being spilt on the floor' during the
activity: 'Fluids laboratory' given how the hazard harms: 'Injuries caused by possible slipping on wet floor'
and who the hazard harms: 'Students'.
2. Describe the hazard event, which is the event that leads to harm.
3. Explain whether or not 'Do not move the water tank when it is full' reduces the likelihood that the hazard event occurs.
If so, it is a prevention measure.
4. Assuming the hazard event occurs, explain whether or not 'Do not move the water tank when it is full' removes or reduces the harm caused by the event.
If so, it is a mitigation measure.
5. If it is a prevention measure, answer 'Prevention'. If it is a migitation meausure, answer 'Mitigation'.
If it is neither a prevention measure nor a mitigation measure, answer 'Neither'. If it is both a        
prevention measure and a mitigation measure, answer 'Both'.

Hazard Description: The hazard of 'Water being spilt on the floor' during the activity 'Fluids laboratory' can lead to injuries caused by possible slipping on a wet floor to students.
Hazard Event Description: Water is accidentally spilled on the floor.
Prevention Explanation: 'Keeping the water tank stationary when it's full' reduces the likelihood of spilling water as moving it increases the likelihood of water being spilled; as it reduces the likelihood of the hazard event, it is a prevention measure.
Mitigation Explanation: If water has been spilled on the floor, 'not moving the water tank when it is full' does not remove or reduce the harm caused by the hazard event, as the water is already spilled and poses a slipping hazard; as it does not reduce the harm caused by the hazard event, it is not a mitigation measure.
Answer: Prevention.

Input:
Follow these instructions:
1. In one sentence, describe the hazard: 'Loud noise' during the
activity: 'Using a trombone as a demonstration for a TPS presentation' given how the hazard harms: 'Loud noise from instrument can cause hearing damage.'
and who the hazard harms: 'Everyone present'.
2. Describe the hazard event, which is the event that leads to harm.
3. Explain whether or not 'Keep a space between the player and audience' reduces the likelihood that the hazard event occurs.
If so, it is a prevention measure.
4. Assuming the hazard event occurs, explain whether or not 'Keep a space between the player and audience' removes or reduces the harm caused by the event.
If so, it is a mitigation measure.
5. If it is a prevention measure, answer 'Prevention'. If it is a migitation meausure, answer 'Mitigation'.
If it is neither a prevention measure nor a mitigation measure, answer 'Neither'. If it is both a        
prevention measure and a mitigation measure, answer 'Both'.

Hazard Description: The hazard of 'Loud noise' during the activity 'Using a trombone as a demonstration for a TPS presentation' can cause hearing damage to everyone present.
Hazard Event Description: The trombone player plays the instrument at a high volume, producing a loud noise.
Prevention Explanation: 'Keeping a space between the player and the audience' does not reduce the likelihood of the trombone producing a loud noise. As it does not reduce the likelihood of the hazard event, it is not a prevention measure.
Mitigation Explanation: If the hazard event occurs and the trombone produces a loud noise, 'keeping a space between the player and the audience' will reduce the noise heard by the audience, hence reducing the severity of the hearing damage caused by the loud noise; as it reduces the harm caused by the hazard event, it is a mitigation measure.
Answer: Mitigation.

Input:
Follow these instructions:
1. In one sentence, describe the hazard: 'Syringes with sharp needles' during the
activity: 'Fluids laboratory' given how the hazard harms: 'Sharp needles can pierce the skin and cause bleeding'
and who the hazard harms: 'Students'.
2. Describe the hazard event, which is the event that leads to harm.
3. Explain whether or not 'Wear lab coat and PPE' reduces the likelihood that the hazard event occurs.   
If so, it is a prevention measure.
4. Assuming the hazard event occurs, explain whether or not 'Wear lab coat and PPE' removes or reduces the harm caused by the event.
If so, it is a mitigation measure.
5. If it is a prevention measure, answer 'Prevention'. If it is a migitation meausure, answer 'Mitigation'.
If it is neither a prevention measure nor a mitigation measure, answer 'Neither'. If it is both a        
prevention measure and a mitigation measure, answer 'Both'.

Hazard Description: The hazard of 'Syringes with sharp needles' during the activity 'Fluids laboratory' can lead to sharp needles piercing the skin and causing bleeding to students.
Hazard Event Description: A sharp syringe needle is directed towards an student.
Prevention Explanation: 'Wearing a lab coat and personal protective equipment (PPE)' does not reduce the likelihood of a student directing a syringe needle towards another student; as it does not reduce the likelihood of the hazard event, it is therefore not a prevention measure.
Mitigation Explanation: If a sharp syringe needle is directed towards a student, 'wearing a lab coat and PPE' will reduce the harm caused by the sharp needle as it is unlikely to pierce through the lab coat and PPE; as it reduces the harm caused by the hazard event, it is a mitigation measure.
Answer: Mitigation.

Input:
Follow these instructions:
1. In one sentence, describe the hazard: 'Water from instrument' during the
activity: 'Using a trombone as a demonstration for a TPS presentation' given how the hazard harms: 'Condensation formed in instrument could spread germs if released'
and who the hazard harms: 'Audience'.
2. Describe the hazard event, which is the event that leads to harm.
3. Explain whether or not 'Keep a space between the player and audience' reduces the likelihood that the hazard event occurs.
If so, it is a prevention measure.
4. Assuming the hazard event occurs, explain whether or not 'Keep a space between the player and audience' removes or reduces the harm caused by the event.
If so, it is a mitigation measure.
5. If it is a prevention measure, answer 'Prevention'. If it is a migitation meausure, answer 'Mitigation'.
If it is neither a prevention measure nor a mitigation measure, answer 'Neither'. If it is both a        
prevention measure and a mitigation measure, answer 'Both'.

Hazard Description: The hazard of 'Water from instrument' during the activity 'Using a trombone as a demonstration for a TPS presentation' can lead to the spread of germs to the audience if condensation formed in the instrument is released.
Hazard Event Description: Water from the trombone condenses and is released into the air.
Prevention Explanation: 'Keeping a space between the player and the audience' does not reduce the likelihood of water condensing in the instrument or being released; as it does not reduce the likelihood of the hazard event, it is not a prevention measure.
Mitigation Explanation: If water from the instrument is released, 'keeping a space between the player and the audience' will mean that fewer germs reach the audience members so will reduce the harm caused by the spread of germs; as it reduces the harm caused by the hazard event, it is a mitigation measure.
Answer: Mitigation.

Input:
N/A

Output format:
Answer: {your_answer}
"""

LLM = OpenAILLM(temperature=0.1, max_tokens=400)

prompt_output = LLM.get_model_output(prompt)

print(prompt_output)
