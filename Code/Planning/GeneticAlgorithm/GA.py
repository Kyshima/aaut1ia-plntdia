import numpy as np
import time

# Define parameters
population_size = 50
num_crops = 10
mutation_rate = 0.01
crossover_rate = 0.7
num_generations = 100

# Sample dataset (replace this with your actual dataset)
# Assume each gene represents a crop, and the value is the amount to plant
crop_dataset = np.random.rand(num_crops)
# Assume each gene represents a cost for planting a specific crop
cost_dataset = np.random.rand(num_crops)

# Define the objective function (fitness function)
def objective_function(individual, cost_dataset):
    # Calculate total yield (sum of individual values)
    total_yield = sum(individual)
    # Calculate total cost (sum of costs for each crop)
    total_cost = np.dot(individual, cost_dataset)
    # The objective is to maximize yield while considering costs
    return total_yield - total_cost

# Initialize the population
population = np.random.rand(population_size, num_crops)

start_time = time.time()
# Main Genetic Algorithm loop
for generation in range(num_generations):
    # Evaluate fitness for each individual in the population
    fitness_scores = np.array([objective_function(ind, cost_dataset) for ind in population])

    # Selection: Choose individuals based on fitness
    selected_indices = np.random.choice(population_size, size=population_size, p=fitness_scores/fitness_scores.sum())

    # Create a new population through crossover and mutation
    new_population = []
    for i in range(0, population_size, 2):
        parent1 = population[selected_indices[i]]
        parent2 = population[selected_indices[i + 1]]

        # Crossover
        crossover_mask = np.random.rand(num_crops) < crossover_rate
        child1 = np.where(crossover_mask, parent1, parent2)
        child2 = np.where(crossover_mask, parent2, parent1)

        # Mutation
        mutation_mask = np.random.rand(num_crops) < mutation_rate
        child1[mutation_mask] = np.random.rand(np.sum(mutation_mask))
        child2[mutation_mask] = np.random.rand(np.sum(mutation_mask))

        new_population.extend([child1, child2])

    population = np.array(new_population)

# Find the best individual in the final population
best_individual_index = np.argmax([objective_function(ind, cost_dataset) for ind in population])
best_individual = population[best_individual_index]
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

print("Best Individual (Yield):", best_individual)
print("Total Yield:", sum(best_individual))
print("Total Cost:", np.dot(best_individual, cost_dataset))
print("Running Time:", elapsed_time)
