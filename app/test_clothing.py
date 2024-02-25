from InputAndExpectedOutput import InputAndExpectedOutputForSinglePrompt
from LLMCaller import *
from PromptInputs import Clothing
from TestModelAccuracy import TestModelAccuracy

clothing_items = [
    "T-shirt",
    "Jeans",
    "Hoodie",
    # "Skirt",
    # "Dress",
    # "Blouse",
    # "Sweater",
    # "Shorts",
    # "Jacket",
    # "Coat",
    # "Leggings",
    # "Tank top",
    # "Polo shirt",
    # "Cardigan",
    # "Blazer",
    # "Sweatshirt",
    # "Chinos",
    # "Trench coat",
    # "Maxi dress",
    # "Cargo pants"
]

non_clothing_items = [
    "Car",
    "Computer",
    "Chair",
    # "Book",
    # "Coffee mug",
    # "Table",
    # "Laptop",
    # "Phone",
    # "Backpack",
    # "Headphones",
    # "Sunglasses",
    # "Watch",
    # "Umbrella",
    # "Notebook",
    # "Basketball",
    # "Television",
    # "Backpack",
    # "Guitar",
    # "Dumbbell",
    # "Plant"
]

examples = []

for example in clothing_items:
    examples.append(InputAndExpectedOutputForSinglePrompt(input=Clothing(control_measure=example), expected_output=True))

for example in non_clothing_items:
    examples.append(InputAndExpectedOutputForSinglePrompt(input=Clothing(control_measure=example), expected_output=False))

if __name__ == "__main__":
    
    test_accuracy = TestModelAccuracy(
        LLM=OpenAILLM(),
        LLM_name='gpt-3.5-turbo',
        list_of_input_and_expected_outputs=examples,
        sheet_name='Clothing',
        test_description='Evaluating clothing prompt on Chat GPT generated data.'
        )
    test_accuracy.run_test()