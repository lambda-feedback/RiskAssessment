from TestModelAccuracy import TestModelAccuracy
from LLMCaller import OpenAILLM, ClaudeSonnetLLM
from ExamplesGenerator import ExamplesGeneratorFromCorrectExamples
from PromptInputs import WhoItHarmsInContext
from example_risk_assessments import physical_risks_to_individuals__original_student_data, natural_disaster_risks, cybersecurity_risks, terrorism_risks, biohazard_risks
from InputAndExpectedOutput import InputAndExpectedOutputForSinglePrompt

class WhoItHarmsInContextExamplesGenerator(ExamplesGeneratorFromCorrectExamples):
    def generate_incorrect_example(self, correct_index, incorrect_index):
        return WhoItHarmsInContext(
                activity=self.correct_examples_list[correct_index].activity,
                hazard=self.correct_examples_list[correct_index].hazard,
                how_it_harms=self.correct_examples_list[correct_index].how_it_harms,
                who_it_harms=self.correct_examples_list[incorrect_index].who_it_harms)

# risk_assessments_list = []

# for i in range(10):
#     risk_assessments_list.append(physical_risks_to_individuals__original_student_data['risk_assessments'][i])
#     risk_assessments_list.append(cybersecurity_risks['risk_assessments'][i])

# correct_examples_list = []

# for risk_assessment in risk_assessments_list:
#     correct_examples_list.append(risk_assessment.get_who_it_harms_in_context_input())

correct_examples_list = [
            # WhoItHarmsInContext(
            #     activity="Driving without Seatbelt",
            #     hazard="Potential vehicle collision or sudden stop",
            #     how_it_harms="Increased risk of severe injury or fatality in the event of an accident",
            #     who_it_harms="Passengers in the vehicle"
            # ),
            # WhoItHarmsInContext(
            #     activity="Working long hours without breaks",
            #     hazard="Increased risk of burnout and mental health issues",
            #     how_it_harms="Reduced overall well-being and productivity",
            #     who_it_harms="Professionals working long hours without adequate breaks"
            # ),
            # WhoItHarmsInContext(
            #     activity="Going outside on sunny day without sunscreen",
            #     hazard="UV radiation",
            #     how_it_harms="Increased risk of skin cancer and premature aging",
            #     who_it_harms="Individuals exposed to the sun without protection"
            # ),
            # WhoItHarmsInContext(
            #     activity="Sitting at desk with poor ergonomics",
            #     hazard="Musculoskeletal strain",
            #     how_it_harms="Development of chronic pain and discomfort",
            #     who_it_harms="Office workers"
            # ),
            # WhoItHarmsInContext(
            #     activity="Excessive Alcohol Consumption",
            #     hazard="Impaired judgment and coordination",
            #     how_it_harms="Increased risk of accidents and health issues",
            #     who_it_harms="Individual consuming alcohol"
            # ),
            # WhoItHarmsInContext(
            #     activity="Smoking in Closed Spaces",
            #     hazard="Secondhand smoke exposure",
            #     how_it_harms="Increased risk of respiratory issues for nonsmokers",
            #     who_it_harms="Non-smokers sharing the same space"
            # ),
            # WhoItHarmsInContext(
            #     activity="Eating fast food regularly",
            #     hazard="Risk of obesity and related health issues",
            #     how_it_harms="Higher likelihood of weight gain, cardiovascular problems, and diabetes",
            #     who_it_harms="Frequent consumers of fast food"
            # ),
            # WhoItHarmsInContext(
            #     activity="Using headphones at high volumes",
            #     hazard="Hearing damage and loss",
            #     how_it_harms="Permanent damage to hearing structures and increased risk of deafness",
            #     who_it_harms="Individuals listening to music at excessively high volumes"
            # ),
            # WhoItHarmsInContext(
            #     activity="Consuming excessively sugary beverages",
            #     hazard="Increased risk of obesity and dental issues",
            #     how_it_harms="Higher likelihood of weight gain and tooth decay",
            #     who_it_harms="Individuals consuming sugary drinks excessively"
            # ),
            # WhoItHarmsInContext(
            #     activity="Neglecting regular eye breaks while using screens",
            #     hazard="Digital eye strain and potential vision problems",
            #     how_it_harms="Increased risk of headaches, blurred vision, and long-term impact on eyesight",
            #     who_it_harms="People spending extended periods on digital devices without breaks"
            # )
        ]

incorrect_examples_list = [
                WhoItHarmsInContext(
                    activity="Driving without Seatbelt",
                    hazard="Potential vehicle collision or sudden stop",
                    how_it_harms="Increased risk of severe injury or fatality in the event of an accident",
                    who_it_harms="Driving without Seatbelt"
                ),
                WhoItHarmsInContext(
                    activity="Smoking in Closed Spaces",
                    hazard="Secondhand smoke exposure",
                    how_it_harms="Increased risk of respiratory issues for nonsmokers",
                    who_it_harms="Secondhand smoke exposure"
                ),
                WhoItHarmsInContext(
                    activity="Using headphones at high volumes",
                    hazard="Hearing damage and loss",
                    how_it_harms="Permanent damage to hearing structures and increased risk of deafness",
                    who_it_harms="Permanent damage to hearing structures and increased risk of deafness"
                ),
                WhoItHarmsInContext(
                    activity="Working long hours without breaks",
                    hazard="Increased risk of burnout and mental health issues",
                    how_it_harms="Reduced overall well-being and productivity",
                    who_it_harms="Individuals who don't work long hours without breaks"
                ),
                WhoItHarmsInContext(
                    activity="Going outside on sunny day without sunscreen",
                    hazard="UV radiation",
                    how_it_harms="Increased risk of skin cancer and premature aging",
                    who_it_harms="People with adequate sun protection"
                ),
                WhoItHarmsInContext(
                    activity="Sitting at desk with poor ergonomics",
                    hazard="Sitting for long periods of time",
                    how_it_harms="Development of chronic pain and discomfort",
                    who_it_harms="Dogs"
                ),
                WhoItHarmsInContext(
                    activity="Excessive Alcohol Consumption",
                    hazard="Impaired judgment and coordination",
                    how_it_harms="Increased risk of accidents and health issues",
                    who_it_harms="Individuals who don't drink alcohol"
                ),
                WhoItHarmsInContext(
                    activity="Eating fast food regularly",
                    hazard="Risk of obesity and related health issues",
                    how_it_harms="Higher likelihood of weight gain, cardiovascular problems, and diabetes",
                    who_it_harms="Individuals who don't eat fast food"
                ),
                WhoItHarmsInContext(
                    activity="Consuming excessively sugary beverages",
                    hazard="Increased risk of obesity and dental issues",
                    how_it_harms="Higher likelihood of weight gain and tooth decay",
                    who_it_harms="Individuals who don't eat sugar"
                )
]

examples = []

for correct_example in correct_examples_list:
    examples.append(InputAndExpectedOutputForSinglePrompt(prompt_input_object=correct_example, expected_output=True))

for incorrect_example in incorrect_examples_list:
    examples.append(InputAndExpectedOutputForSinglePrompt(prompt_input_object=incorrect_example, expected_output=False))

def test_who_it_harms_in_context(examples, LLM, is_first_test: bool = False):

    test_accuracy = TestModelAccuracy(
                        LLM=LLM,
                        is_first_test=is_first_test,
                        domain='Risk domain not specified',       
                        list_of_input_and_expected_outputs=examples,
                        examples_gathered_or_generated_message='Risk assessments ARE AI-generated',
                        sheet_name='Who It Harms In Context')
    
    test_accuracy.run_test()

if __name__ == "__main__":
    LLM = ClaudeSonnetLLM(system_message='', temperature=0.1, max_tokens=200)

    test_who_it_harms_in_context(examples=examples, 
                                 LLM=LLM, 
                                 is_first_test=True)