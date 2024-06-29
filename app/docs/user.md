# riskAssessment

## Lambda Feedback Setup
1. In teacher mode, create a new response area.
2. Within the response area, click "Configure"
3. Click the "Input" tab and change the input type to Table and make the Table have 12 rows and 1 column.
4. Remove the column name and add the following names to the rows:
![column names](https://github.com/lambda-feedback/riskAssessment/blob/main/app/docs/response%20area.png)
5. Click the "Evaluate" tab and select "riskAssessment" from the Evaluation Function dropdown.
![Example lambda feedback evaluation function parameters](https://github.com/lambda-feedback/riskAssessment/blob/main/app/docs/example%20lambda%20feedback%20parameters.png)
6. Set is_risk_matrix = False, is_feedback_text = False, is_risk_assessment = True and LLM to one of the following options:
- "Claude Opus"
- "Claude Sonnet"
- "Claude Haiku"
- "GPT-4 Turbo"
- "GPT-3.5 Turbo 1106"
- "Mistral Large"
- "Mixtral 8x22B"
- "Mixtral 8x7B"

The recommended LLM is Claude Sonnet.

## Outputs
**Example risk assessment inputs**
![Example inputs](https://github.com/lambda-feedback/riskAssessment/blob/main/app/docs/example%20inputs.png)

**Coresponding risk assessment outputs**
![Example outputs](https://github.com/lambda-feedback/riskAssessment/blob/main/app/docs/example%20ouptut.png)
