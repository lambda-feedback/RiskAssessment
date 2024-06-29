# riskAssessment

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
