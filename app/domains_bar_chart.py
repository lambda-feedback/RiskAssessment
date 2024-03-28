import matplotlib.pyplot as plt
import numpy as np

# Define the data
prevention_domains = ['Physical', 'Terrorism', 'Cybersecurity', 'Biohazard']
mitigation_domains = ['Physical', 'Terrorism', 'Cybersecurity', 'Biohazard', 'Natural Disaster']

prevention_accuracy_scores_as_decimal = np.array([25/27, 10/10, 10/10, 5/6])
mitigation_accuracy_scores_as_decimal = np.array([15/22, 8/10 , 9/10, 2/10, 9/10])

prevention_accuracy_scores_as_percentage = prevention_accuracy_scores_as_decimal * 100
mitigation_accuracy_scores_as_percentage = mitigation_accuracy_scores_as_decimal * 100

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Define the x locations for the groups
x_prevention = np.arange(len(prevention_domains))
x_mitigation = np.arange(len(mitigation_domains))

# Plot prevention accuracy scores
ax.bar(x_prevention - 0.2, prevention_accuracy_scores_as_percentage, width=0.4, label='Prevention')
# Plot mitigation accuracy scores
ax.bar(x_mitigation + 0.2, mitigation_accuracy_scores_as_percentage, width=0.4, label='Mitigation')


# Add labels, title, and legend
ax.set_xlabel('Domains')
ax.set_ylabel('Accuracy Score')
ax.set_title('Accuracy Scores by Domains')
ax.set_xticks(np.arange(len(mitigation_domains)))
ax.set_xticklabels(mitigation_domains)
ax.legend()

# Show the plot
plt.tight_layout()
plt.show()