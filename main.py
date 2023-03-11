import numpy as np
import matplotlib.pyplot as plt

def apply_rule(rule, left, center, right):
    rule_bin = '{0:08b}'.format(rule)  # convert rule number to binary string
    pattern = str(left) + str(center) + str(right)  # concatenate the cell states as a string
    index = int(pattern, 2)  # convert pattern to decimal index
    return int(rule_bin[7 - index])  # apply the rule

def evolve(current_state, rule):
    new_state = []
    for i in range(len(current_state)):
        left = current_state[(i-1) % len(current_state)]
        center = current_state[i]
        right = current_state[(i+1) % len(current_state)]
        new_cell = apply_rule(rule, left, center, right)
        new_state.append(new_cell)
    return new_state

# Define the rule number and initial cell state
rule = 73
initial_state = [0] * 300
initial_state[len(initial_state) // 2] = 1
current_state = initial_state
matrix = [];
# Iterate over the generations
num_generations = 300


for i in range(num_generations):
    current_state = evolve(current_state, rule)
    print(current_state)
    matrix.append(current_state)

plt.imshow(matrix, cmap='viridis')

# show the plot
plt.show()
