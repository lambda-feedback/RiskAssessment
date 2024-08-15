# riskAssessment

## [Final Year Project Report](https://drive.google.com/file/d/14VX1AJK-K-O7YWuquthELhR62eM6PzRz/view?usp=sharing)

## [Risk Assessment App](https://risk---assessment.streamlit.app/)

## [Read the Developer Documentation](https://github.com/lambda-feedback/riskAssessment/blob/main/app/docs/dev.md)

## [Read the User Documentation](https://github.com/lambda-feedback/riskAssessment/blob/main/app/docs/user.md)

## Table of Contents
- [Evaluation Function Template Repository](#evaluation-function-template-repository)
  - [Table of Contents](#table-of-contents)
  - [Repository Structure](#repository-structure)
  - [How it works](#how-it-works)
    - [Docker & Amazon Web Services (AWS)](#docker--amazon-web-services-aws)
    - [Middleware Functions](#middleware-functions)
  - [Contact](#contact)

## Repository Structure

```bash
app/
    __init__.py
    evaluation.py # Contains the evaluation_function, which is called by the Lambda Feedback platform
    preview.py # Script containing the preview_function
    docs.md # Documentation page for this function (required)
    evaluation_tests.py # Unit tests for the main evaluation_function
    preview_tests.py # Unit tests for the preview_function
    requirements.txt # list of packages needed for evaluation.py
    Dockerfile # for building whole image to deploy to AWS

    data/
      RiskAssessment.py # Class used to create Risk Assessment examples with methods to create LLM prompts specific to the risk assessment example from LLM prompt templates 
      example_risk_assessments.py # Risk Assessments used to test the accuracy of LLM prompts
    prompts/
      BasePromptInput.py # Base class that other PromptInput classes inherit from.
      ControlMeasureClassification.py # PromptInput class used to classify a control measure as either a prevention, mitigation, both or neither.
      HarmCausedAndHazardEventpy # PromptInput class used to infer the event that leads to harm and the harm caused from the student's risk assessment inputs.
      HowItHarmsInContext.py # PromptInput class that checks whether the "How it harms" input matches the "activity" and "hazard" inputs.
      WhoItHarmsInContext.py # PromptInput class that checks whether the "Who it harms" input matches the "activity", "hazard" and "how it harms" inputs.
      NoInformationProvided.py # PromptInput class that checks whether no information is provided in the "prevention" or "mitigation" input fields.
      SummarizeControlMeasureFeedback.py # PromptInput class that takes in the output from the ControlMeasureClassification prompt and shortens it to 3 sentences.
    test_classes/


.github/
    workflows/
        test-and-deploy.yml # Testing and deployment pipeline. Testing is performed every time a commit is made to this repo, before the image is built and deployed. 
```
---

## How it works

The function is built on top of a custom base layer, [BaseEvaluationFunctionLayer](https://github.com/lambda-feedback/BaseEvalutionFunctionLayer), which tools, tests and schema checking relevant to all evaluation functions.

### Docker & Amazon Web Services (AWS)

The grading scripts are hosted AWS Lambda, using containers to run a docker image of the app. Docker is a popular tool in software development that allows programs to be hosted on any machine by bundling all its requirements and dependencies into a single file called an **image**.

Images are run within **containers** on AWS, which give us a lot of flexibility over what programming language and packages/libraries can be used. For more information on Docker, read this [introduction to containerisation](https://www.freecodecamp.org/news/a-beginner-friendly-introduction-to-containers-vms-and-docker-79a9e3e119b/). To learn more about AWS Lambda, click [here](https://geekflare.com/aws-lambda-for-beginners/).

### Middleware Functions
In order to run the algorithm and schema on AWS Lambda, some middleware functions have been provided to handle, validate and return the data so all you need to worry about is the evaluation script and testing.

The code needed to build the image using all the middleware functions are available in the [BaseEvaluationFunctionLayer](https://github.com/lambda-feedback/BaseEvalutionFunctionLayer) repository.

### GitHub Actions
Whenever a commit is made to the GitHub repository, the new code will go through a pipeline, where it will be tested for syntax errors and code coverage. The pipeline used is called **GitHub Actions** and the scripts for these can be found in `.github/workflows/`.

On top of that, when starting a new evaluation function, you will have to complete a set of unit test scripts, which not only make sure your code is reliable, but also helps you to build a _specification_ for how the code should function before you start programming.

Once the code passes all these tests, it will then be uploaded to AWS and will be deployed and ready to go in only a few minutes.
