# riskAssessment
*Brief description of what this evaluation function does, from the developer perspective*
This evaluation function is used to provide feedback to students on their risk assessment inputs. 
The response input for the evaluation function is 12 risk assessment inputs, 6 of which are text inputs (activity, hazard, how it harms, who it harms, prevention and mitigation) and 6 of which are number inputs used to fill out a risk matrix (uncontrolled likelihood, uncontrolled severity, uncontrolled risk, controlled likelihood, controlled severity, controlled risk).

The evaluation function checks that the risk matrix inputs follow convention (i.e. risk = likelihood x severity, & uncontrolled risk <= controlled risk).

If the risk matrix inputs are correct, the following prompting structure 

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
