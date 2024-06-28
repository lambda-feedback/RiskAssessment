# Base image that bundles AWS Lambda Python 3.8 image with some middleware functions
# FROM base-eval-tmp
FROM rabidsheep55/python-base-eval-layer

WORKDIR /app

# Copy and install any packages/modules needed for your evaluation script.
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Copy the evaluation and testing scripts
COPY evaluation.py ./app/
COPY evaluation_tests.py ./app/

# Copy the preview and testing scripts
COPY preview.py ./app/
COPY preview_tests.py ./app/

# Copy additional files not included in the template repository
# that are used in evaluation.py
COPY BasePromptInput.py ./app/prompts/
COPY ControlMeasureClassification.py ./app/prompts/
COPY ControlMeasureClassification__FewShot_NoChainOfThought.py ./app/prompts/
COPY ControlMeasureClassification__ZeroShot_ChainOfThought.py ./app/prompts/
COPY ControlMeasureClassification__ZeroShot_NoChainOfThought.py ./app/prompts/
COPY HarmCausedAndHazardEvent.py ./app/prompts/
COPY HowItHarmsInContext.py ./app/prompts/
COPY WhoItHarmsInContext.py ./app/prompts/
COPY MitigationInput__ControlMeasureClassification.py ./app/prompts/
COPY PreventionInput__ControlMeasureClassification.py ./app/prompts/
COPY PreventionClassificationWithoutContextOfOtherInputs.py ./app/prompts/
COPY MitigationClassificationWithoutContextOfOtherInputs.py ./app/prompts/
COPY NoInformationProvided.py ./app/prompts/
COPY SummarizeControlMeasureFeedback.py ./app/prompts/
COPY RiskAssessment.py ./app/
COPY LLMCaller.py ./app/
COPY RegexPatternMatcher.py ./app/

# Copy Documentation
COPY docs/dev.md ./app/docs/dev.md
COPY docs/user.md ./app/docs/user.md

# Set permissions so files and directories can be accessed on AWS
RUN chmod 644 $(find . -type f)
RUN chmod 755 $(find . -type d)

# The entrypoint for AWS is to invoke the handler function within the app package
CMD [ "/app/app.handler" ]
