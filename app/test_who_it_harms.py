from ExamplesGenerator import InputAndExpectedOutputGenerator
from TestModelAccuracy import TestModelAccuracy
from LLMCaller import OpenAILLM
from PromptInputs import WhoItHarms

def create_classification_objects(*lists):
    combined_list = []

    for sublist in lists:
        combined_list.extend(sublist)

    # Flattening the list using list comprehension
    flattened_list = [item for sublist in combined_list for item in sublist.split(', ')]

    classification_objects = []

    for who_it_harms in flattened_list:
        classification_objects.append(WhoItHarms(who_it_harms))

    return classification_objects

individuals = [
    "Employees",
    "Customers",
    "Residents",
    "Passengers",
    "Students"
]

groups = [
    "Workers",
    "Children",
    "Elderly",
    "Commuters",
    "Pedestrians"
]

occupational_roles = [
    "Managers",
    "Maintenance staff",
    "Health professionals",
    "Security personnel",
    "Supervisors"
]

specific_demographics = [
    "Pregnant women",
    "Individuals with pre-existing health conditions",
    "Low-income families",
    "Vulnerable populations"
]

community_members = [
    "Homeowners",
    "Local businesses",
    "Civic organizations",
    "Educational institutions"
]

environmental_components = [
    "Air quality",
    "Water sources",
    "Ecosystems",
    "Soil integrity",
    "Biodiversity"
]

specific_individuals = [
    "John Doe (if there's a specific person affected)",
    "Jane Smith (if there's a specific person affected)",
    "Key stakeholders",
    "Project team members"
]

infrastructure = [
    "Buildings and structures",
    "Roads and transportation systems",
    "Utility networks",
    "Information systems"
]

correct_examples_list = create_classification_objects(
    individuals,
    groups,
    occupational_roles,
    specific_demographics,
    community_members,
    environmental_components,
    specific_individuals,
    infrastructure
)

abstract_concepts = [
    "Happiness",
    "Well-being",
    "Satisfaction"
]

general_terms = [
    "Society",
    "Humanity",
    "Everyone"
]

vague_descriptions = [
    "Things",
    "Stuff",
    "Everything"
]

broad_categories = [
    "People in general",
    "The environment",
    "Future generations"
]

unquantifiable_terms = [
    "Quality of life",
    "Morale",
    "Ethical values"
]

overly_generalized_groups = [
    "World population",
    "Global community",
    "Mankind"
]

generic_descriptions = [
    "Various entities",
    "Multiple stakeholders",
    "Different people"
]

undefined_terms = [
    "Things we care about",
    "General interests",
    "Everything and everyone"
]

unspecified_entities = [
    "Random people",
    "Some individuals",
    "Anybody"
]

incorrect_examples_list = create_classification_objects(
    abstract_concepts,
    general_terms,
    vague_descriptions,
    broad_categories,
    unquantifiable_terms,
    overly_generalized_groups,
    generic_descriptions,
    undefined_terms,
    unspecified_entities
)

if __name__ == '__main__':

    examples_generator = InputAndExpectedOutputGenerator(correct_examples_list=correct_examples_list,
                                                         incorrect_examples_list=incorrect_examples_list)
    
    who_it_harms_classification_examples = examples_generator.get_input_and_expected_output_list()
    test_accuracy = TestModelAccuracy(LLM=OpenAILLM(),
                                            LLM_name='gpt-3.5-turbo',
                                            list_of_input_and_expected_outputs=who_it_harms_classification_examples,
                                            sheet_name='Who It Harms')
    test_accuracy.run_test()