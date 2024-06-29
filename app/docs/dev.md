# riskAssessment
This evaluation function is used to provide feedback to students on their risk assessment inputs. 
The response input for the evaluation function is 12 risk assessment inputs, 6 of which are text inputs (activity, hazard, how it harms, who it harms, prevention and mitigation) and 6 of which are number inputs used to fill out a risk matrix (uncontrolled likelihood, uncontrolled severity, uncontrolled risk, controlled likelihood, controlled severity, controlled risk).

The evaluation function checks that the risk matrix number inputs follow the convention (i.e. risk = likelihood x severity, & uncontrolled risk <= controlled risk).

![Overall prompting structure](https://github.com/lambda-feedback/riskAssessment/blob/main/app/docs/prompt%201.png)

If the risk matrix inputs are correct, then the above prompt structure is followed to provide feedback on the text inputs. Textboxes with a blue border are prompts to an LLM while those with a purple border contain the logic shown below. The logic above starts by checking for blank input fields; if there are no blank input fields, a prompt to the LLM is used to determine whether the “how it harms” risk assessment input is correct given the context of other relevant inputs. If it is correct, a similar prompt is run for the “who it harms” input. If either of these prompts suggest that the corresponding input is incorrect, then appropriate feedback is given and the prompts that follow are not run.

![Control measure logic structure](https://github.com/lambda-feedback/riskAssessment/blob/main/app/docs/prompt%202.png)

The inner logic of the purple “control measure logic” is shown above. The control measure logic is used to provide feedback on a control measure input; the same logic is used to provide feedback on the prevention and mitigation inputs. Since it is possible that a prevention or mitigation does not exist for a particular hazard, it is only mandatory that either one of the prevention or mitigation fields is filled; as such, the initial logic checks whether the control measure input is either blank or whether no information is entered, e.g. “N.A.”. If information is provided, a prompt is used to extract the “event that leads to harm” (hazard event) and the “harm caused” from the risk assessment inputs. The inferences of the “hazard event” and “harm caused” are then used by the control measure classification prompt which classifies the control measure as either “prevention”, “mitigation”, “neither” or “both”; if the control measure reduces the likelihood of the “hazard event” then it is a “prevention” and, assuming the “hazard event” has occurred, if the control measures reduces the severity of this event, then it is a “mitigation”.

## Setup
1. Clone the github repository.
2. Create an API key for Open AI, Mistral and Anthropic
3. Store the API key strings in a .env file that is created in the app folder. The variable names should be the same as those from the .env.example file.

## Running tests
To test the different prompts to LLMs in the prompt structure diagrams shown above, a series of scripts have been created in the app/test_scripts folder. To run these tests, copy and paste the commented out command from the top of the file (e.g. 

## Prompt Results
A spreadsheet showing the results from testing different prompts can be found [here](https://docs.google.com/spreadsheets/d/1d7Tq7qEaNTrhm1E7qcGvl3Dkr8cFNdSpOul9RezjVs4/edit?usp=sharing).

## Inputs
![Example lambda feedback evaluation function parameters](https://github.com/lambda-feedback/riskAssessment/blob/main/app/docs/example%20lambda%20feedback%20parameters.png)

The input parameters which should be specified in the Lambda Feedback "Teacher" mode are:
- is_risk_matrix (bool)
- is_feedback_text (bool)
- is_risk_assessment (bool)
- LLM (string)

Note: only 1 of the boolean parameters should be True:
- If is_risk_matrix is True, then the input should be a 2x3 array of integers (a risk matrix) and feedback is provided on the risk matrix. This is used in one of the questions from part 1 of the risk assessment exercise.
- If is_feedback_text is True, then no matter the input, the feedback is "Thank you for your feedback". This is used in the student feedback section of the exercise.
- If is_risk_assessment is True, the input should be a 12x1 array of risk assessment inputs in the following order: activity, hazard, how it harms, who it harms, uncontrolled likelihood, uncontrolled severity, uncontrolled risk, prevention, mitigation, controlled likelihood, controlled severity, controlled risk. The logic described above is then used to provide feedback on the risk assessment inputs.

The LLM parameter allows the teacher to choose which Large Language Model (LLM) they would like to use. The options are currently:
- "Claude Opus"
- "Claude Sonnet"
- "Claude Haiku"
- "GPT-4 Turbo"
- "GPT-3.5 Turbo 1106"
- "Mistral Large"
- "Mixtral 8x22B"
- "Mixtral 8x7B"

## Outputs
**Example risk assessment inputs**
![Example inputs](https://github.com/lambda-feedback/riskAssessment/blob/main/app/docs/example%20inputs.png)

**Coresponding risk assessment outputs**
![Example outputs](https://github.com/lambda-feedback/riskAssessment/blob/main/app/docs/example%20ouptut.png)
