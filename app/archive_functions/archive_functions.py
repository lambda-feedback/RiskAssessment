def get_accuracy_in_different_domains(self, binary_correct_list):
    domains = self.number_of_examples_in_each_domain.keys()
    domain_accuracy_string = ''

    starting_index_of_current_domain_in_binary_correct_list = 0
    for domain in domains:
        number_of_risk_assessments_in_domain = self.number_of_examples_in_each_domain[domain]

        ending_index_of_current_domain_in_binary_correct_list = starting_index_of_current_domain_in_binary_correct_list + number_of_risk_assessments_in_domain
        
        number_of_risk_assessments_correctly_classified_in_domain = sum(binary_correct_list[starting_index_of_current_domain_in_binary_correct_list:ending_index_of_current_domain_in_binary_correct_list])

        domain_accuracy_string += f'{domain}: {number_of_risk_assessments_correctly_classified_in_domain}/{number_of_risk_assessments_in_domain}\n\n'

        starting_index_of_current_domain_in_binary_correct_list = ending_index_of_current_domain_in_binary_correct_list

    return domain_accuracy_string