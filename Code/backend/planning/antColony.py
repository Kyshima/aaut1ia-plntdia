import pandas as pd
import numpy as np
import random
import time

def initialize_pheromones(num_crops, initial_pheromone):
    return np.ones((num_crops, num_crops)) * initial_pheromone

def calculate_score(solution, filtered_data, weights):
    total_cost = np.zeros(len(weights))
    for crop in solution:
        crop_data = filtered_data[filtered_data['Crop'] == crop]
        total_cost += weights * crop_data[['ProdCost', 'CultCost', 'OperCost', 'FixedCost']].values.flatten()
    return np.sum(total_cost)

def update_pheromones(pheromones, solutions, scores, decay_rate, crops):
    pheromones *= (1.0 - decay_rate)
    for solution, score in zip(solutions, scores):
        for i in range(len(solution) - 1):
            idx_i = np.where(crops == solution[i])[0][0]
            idx_j = np.where(crops == solution[i + 1])[0][0]
            pheromones[idx_i, idx_j] += 1.0 / score
    return pheromones

def ant_colony_optimization(weights, state, year, number_crops, pheromone_initial, pheromone_decay, alpha, beta, num_ants, num_iterations, temporal, max_time):
    # Load CSV data
    path = "Dataset_Planning.csv"
    df = pd.read_csv(path)

    # Selecionar as colunas relevantes
    selected_columns = ['Crop_Year', 'State', 'Crop', 'ProdCost', 'CultCost', 'OperCost', 'FixedCost', 'TotalCost', 'Area_Total', 'Production_Total', 'Yield_Mean']
    relevant_data = df[selected_columns]
    filtered_data = df[(df['Crop_Year'] == year) & (df['State'] == state)]
    crops = filtered_data['Crop'].unique()

    # Inicialização de feromônios
    pheromones = initialize_pheromones(len(crops), pheromone_initial)

    # Algoritmo ACO
    best_solution = None
    best_score = float('inf')

    start_time = time.time()

    for iteration in range(num_iterations):
        solutions = []
        scores = []

        for ant in range(num_ants):
            current_crops = random.sample(list(crops), number_crops)
            solutions.append(current_crops)
            scores.append(calculate_score(current_crops, filtered_data, weights))

        elapsed_time = time.time() - start_time

        if temporal and elapsed_time > max_time:
            break

        pheromones = update_pheromones(pheromones, solutions, scores, pheromone_decay, crops)

        if min(scores) < best_score:
            best_score = min(scores)
            best_solution = solutions[np.argmin(scores)]

    return best_solution, best_score, elapsed_time

result = ant_colony_optimization([0.1, 0.2, 0.3, 0.4], 'Andhra Pradesh', 2019, 3, 1.0, 0.5, 1.0, 2.0, 10, 100, True, 4)
print(f"Melhor Solução: {result[0]}")
print(f"Melhor Score/Dinheiro: {result[1]}")
print("Tempo decorrido: {:.2f} segundos".format(result[2]))
