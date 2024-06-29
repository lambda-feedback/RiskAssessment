# riskAssessment
*Brief description of what this evaluation function does, from the developer perspective*
This evaluation function is used to provide feedback to students on their risk assessment inputs. 
The response input for the evaluation function is 12 risk assessment inputs, 6 of which are text inputs (activity, hazard, how it harms, who it harms, prevention and mitigation) and 6 of which are number inputs used to fill out a risk matrix (uncontrolled likelihood, uncontrolled severity, uncontrolled risk, controlled likelihood, controlled severity, controlled risk).

The evaluation function checks that the risk matrix number inputs follow convention (i.e. risk = likelihood x severity, & uncontrolled risk <= controlled risk).

![Overall prompting structure](https://github.com/lambda-feedback/riskAssessment/blob/main/app/docs/prompt%201.png)

If the risk matrix inputs are correct, then the above prompt structure is followed to provide feedback on the text inputs. Textboxes with a blue border are prompts to an LLM while those with a purple border contain the logic shown below. The logic above starts by checking for blank input fields; if there are no blank input fields, a prompt to the LLM is used to determine whether the “how it harms” risk assessment input is correct given the context of other relevant inputs. If it is correct, a similar prompt is run for the “who it harms” input. If either of these prompts suggest that the corresponding input is incorrect, then appropriate feedback is given and the prompts that follow are not run.

![Control measure logic structure](https://github.com/lambda-feedback/riskAssessment/blob/main/app/docs/prompt%202.png)

The inner logic of the purple “control measure logic” is shown above. The control measure logic is used to provide feedback on a control measure input; the same logic is used to provide feedback on the prevention and mitigation inputs. Since it is possible that a prevention or mitigation does not exist for a particular hazard, it is only mandatory that either one of the prevention or mitigation fields is filled; as such, the initial logic checks whether the control measure input is either blank or whether no information is entered, e.g. “N.A.”. If information is provided, a prompt is used to extract the “event that leads to harm” (hazard event) and the “harm caused” from the risk assessment inputs. The inferences of the “hazard event” and “harm caused” are then used by the control measure classification prompt which classifies the control measure as either “prevention”, “mitigation”, “neither” or “both”; if the control measure reduces the likelihood of the “hazard event” then it is a “prevention” and, assuming the “hazard event” has occurred, if the control measures reduces the severity of this event, then it is a “mitigation”.


## Prompt Results
A spreadsheet showing the results from testing different prompts can be found [here](https://docs.google.com/spreadsheets/d/1d7Tq7qEaNTrhm1E7qcGvl3Dkr8cFNdSpOul9RezjVs4/edit?usp=sharing).

## Inputs
*Specific input parameters which can be supplied when the `eval` command is supplied to this function.*

## Outputs
*Output schema/values for this function*

## Examples
*List of example inputs and outputs for this function, each under a different sub-heading*

### Simple Evaluation

```python
{
  "example": {
    "Something": "something"
  }
}
```

```python
{
  "example": {
    "Something": "something"
  }
}
```
