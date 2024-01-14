import pandas as pd
import numpy as np
import random
import time

# Load CSV data
path = "Dataset_Planning.csv"
df = pd.read_csv(path)

# Variáveis Globais para usar
weights = [0.1, 0.2, 0.3, 0.4]
state = 'Andhra Pradesh'
year = 2019
number_crops = 4
pheromone_initial = 1.0
pheromone_decay = 0.5
alpha = 1.0
beta = 2.0
num_ants = 50
num_iterations = 100
temporal = True
max_time = 4  # (segundos)

# Selecionar as colunas relevantes

filtered_data = df[(df['Crop_Year'] == year) & (df['State'] == state)]

crops = filtered_data['Crop'].unique()
cropsCosts = filtered_data[['Crop', 'ProdCost', 'CultCost', 'OperCost', 'FixedCost']].groupby('Crop').mean().reset_index()

cropsCosts['Heuristic'] = 1 / ((cropsCosts['ProdCost'] * weights[0]) + (cropsCosts['CultCost'] * weights[1]) + (cropsCosts['OperCost'] * weights[2]) + (cropsCosts['FixedCost'] * weights[3]))

# Inicialização de feromônios
pheromones = np.ones((len(crops), len(crops))) * pheromone_initial

# Função para calcular a pontuação de uma solução
def calculate_score(solution):
    total_cost = np.zeros(len(weights))
    for crop in solution:
        crop_data = filtered_data[filtered_data['Crop'] == crop]
        total_cost += weights * crop_data[['ProdCost', 'CultCost', 'OperCost', 'FixedCost']].values.flatten()
    return total_cost

# Função para atualizar feromônios
def update_pheromones(pheromones, solutions, scores, decay_rate):
    pheromones *= (1.0 - decay_rate)
    for solution, score in zip(solutions, scores):
        for i in range(len(solution) - 1):
            idx_i = np.where(crops == solution[i])[0][0]
            idx_j = np.where(crops == solution[i + 1])[0][0]
            pheromones[idx_i, idx_j] += 1.0 / score
    return pheromones

# Algoritmo ACO
best_solution = None
best_score = float('inf')

start_time = time.time()

for iteration in range(num_iterations):
    solutions = []
    scores = []
    probabilities = [13]
    for ant in range(num_ants):
        
        for pheromoneLine in pheromones:
            probabilities += (pheromoneLine ** alpha) * ((cropsCosts['Heuristic'] + 1e-10) ** beta)
            
        probabilities /= probabilities.sum()
        cropIndexes = random.sample(list(probabilities.index), number_crops)

        current_crops = list()
        for x in cropIndexes:
             current_crops.append(crops[x])

        #current_crops = random.sample(list(crops), number_crops)

        solutions.append(current_crops)
        scores.append(np.sum(calculate_score(current_crops)))

    elapsed_time = time.time() - start_time

    if temporal and elapsed_time > max_time:
        break

    pheromones = update_pheromones(pheromones, solutions, scores, pheromone_decay)

    if min(scores) < best_score:
        best_score = min(scores)
        best_solution = solutions[np.argmin(scores)]




# Resultados
print(f"Melhor Solução: {best_solution}")
print(f"Melhor Score/Dinheiro: {best_score}")
print("Tempo decorrido: {:.2f} segundos".format(elapsed_time))
