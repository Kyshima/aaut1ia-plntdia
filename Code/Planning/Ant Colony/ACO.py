import pandas as pd
import numpy as np

# Create a DataFrame from the CSV data
df = pd.read_csv("Code/Planning/GeneticAlgorithm/Dataset_Planning.csv")

weights = [0.1,0.2,0.3,0.4]
state='Andhra Pradesh'

# Selecionar as colunas relevantes
selected_columns = ['Crop_Year', 'State','Crop' ,'ProdCost', 'CultCost', 'OperCost', 'FixedCost', 'TotalCost', 'Area_Total', 'Production_Total', 'Yield_Mean']
relevant_data = df[selected_columns]
filtered_data = df[(df['State'] == state)].reset_index()

# Define parameters for the ACO algorithm
pheromone_initial = 1.0
pheromone_decay = 0.5
alpha = 1.0  # importance of pheromone
beta = 2.0   # importance of heuristic information
num_ants = 5
num_iterations = 5

# Calculate heuristic information (inverse of TotalCost) for each crop
filtered_data['Heuristic'] = 1 / filtered_data['TotalCost']

# Initialize pheromone levels
pheromone = np.full(len(filtered_data), pheromone_initial)

# ACO algorithm
for iteration in range(num_iterations):
    solutions = []

    #for state in range(df['State']): tem de ser por state senão vai merdar
    for ant in range(num_ants):
        probabilities = (pheromone ** alpha) * ((filtered_data['Heuristic'] + 1e-10) ** beta)
        probabilities /= probabilities.sum()

        chosen_crop = np.random.choice(filtered_data.index, p=probabilities)
        solutions.append((ant, chosen_crop))

    # Update pheromone levels
    pheromone *= (1 - pheromone_decay)
    for ant, crop in solutions:
        pheromone[crop] += 1 / ((filtered_data.loc[crop, 'TotalCost'] + 1e-10)+((filtered_data.loc[crop, 'ProdCost'] + 1e-10)*weights[0])+((filtered_data.loc[crop, 'CultCost'] + 1e-10)*weights[1])+((filtered_data.loc[crop, 'OperCost'] + 1e-10)*weights[2])+((filtered_data.loc[crop, 'FixedCost'] + 1e-10)*weights[3]))


# Find the unique values and their corresponding indices
unique_values, unique_indices = np.unique(pheromone, return_index=True)

# # Sort the unique values in descending order
sorted_indices = np.argsort(unique_values)[::-1]

# # Get the three unique largest values and their corresponding indices
top_three_values = unique_values[sorted_indices[:3]]
top_three_indices = unique_indices[sorted_indices[:3]]

print(filtered_data.loc[top_three_indices[0], 'Crop'])
print(filtered_data.loc[top_three_indices[1], 'Crop'])
print(filtered_data.loc[top_three_indices[2], 'Crop'])