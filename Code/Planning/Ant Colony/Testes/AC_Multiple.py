import pandas as pd
import numpy as np
import random
import time
from collections import Counter

# Load CSV data
path = "./Dataset_Planning.csv"
df = pd.read_csv(path)

# Variáveis Globais para usar
weights = [0.1, 0.2, 0.3, 0.4]
state = 'Andhra Pradesh'
year = 2019
number_crops = 3
pheromone_initial = 1.0
pheromone_decay = 0.5
alpha = 1.0
beta = 2.0
num_ants = 20
num_iterations = 100
temporal = False
max_time = 4  # (segundos)

# Selecionar as colunas relevantes
selected_columns = ['Crop_Year', 'State', 'Crop', 'ProdCost', 'CultCost', 'OperCost', 'FixedCost', 'TotalCost', 'Area_Total', 'Production_Total', 'Yield_Mean']
relevant_data = df[selected_columns]
filtered_data = df[(df['Crop_Year'] == year) & (df['State'] == state)]
crops = filtered_data['Crop'].unique()

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

# Função para executar o Algoritmo ACO uma vez e retornar os resultados
def run_aco_once(pheromones):
    best_solution = None
    best_score = float('inf')

    start_time = time.time()

    for iteration in range(num_iterations):
        solutions = []
        scores = []

        for ant in range(num_ants):
            current_crops = random.sample(list(crops), number_crops)
            solutions.append(current_crops)
            scores.append(np.sum(calculate_score(current_crops)))

        elapsed_time = time.time() - start_time

        if temporal and elapsed_time > max_time:
            print("Tempo máximo atingido. Parando a execução.")
            break

        pheromones = update_pheromones(pheromones, solutions, scores, pheromone_decay)

        if min(scores) < best_score:
            best_score = min(scores)
            best_solution = solutions[np.argmin(scores)]

    return best_solution, best_score, elapsed_time, pheromones

# Inicializar pheromones uma vez fora do loop principal
pheromones = np.ones((len(crops), len(crops))) * pheromone_initial

# Executar o Algoritmo ACO 50 vezes
results_list = []
cultura_counts = Counter()
custos_culturas = {}
melhor_tempo = {}

with open("output.txt", "w") as output_file:
    for i in range(50):
        print(f"\nExecução {i + 1}:")
        print(f"\nExecucao {i + 1}:", file=output_file)
        best_solution, best_score, elapsed_time, pheromones = run_aco_once(pheromones)

        # Exibir resultados na tela após cada execução
        print(f"Melhor Solução: {best_solution}")
        print(f"Melhor Score/Menor Custo: {best_score}")
        print(f"Tempo decorrido: {elapsed_time:.2f} segundos")

        # Gravar resultados no arquivo "output.txt"
        print(f"Melhor Solucao: {best_solution}", file=output_file)
        print(f"Melhor Score/Menor Custo: {best_score}", file=output_file)
        print(f"Tempo decorrido: {elapsed_time:.2f} segundos", file=output_file)

        # Armazenar resultados para cálculos de estatísticas
        results_list.append({
            "Iteration": i + 1,
            "Best Solution": best_solution,
            "Best Score": best_score,
            "Elapsed Time": elapsed_time
        })

        # Contar a ocorrência de cada cultura na melhor solução
        for cultura in best_solution:
            cultura_counts[cultura] += 1

        # Calcular custo para cada cultura na melhor solução
        for cultura in best_solution:
            if cultura not in custos_culturas:
                custos_culturas[cultura] = []

            custo = best_score
            custos_culturas[cultura].append(custo)


        melhor_tempo[i] = elapsed_time

# Exibir a percentagem de uso de cada cultura
total_execucoes = len(results_list)
total_culturas = len(cultura_counts)

# Calcular a média do tempo no final
print(melhor_tempo.values())
average_execution_time = sum(melhor_tempo.values()) / total_execucoes

# Exibir a percentagem de uso de cada cultura
print("\nPercentagem de uso:")
with open("estatisticas.txt", "a") as estatisticas_file:
    print(f"---------------------------------------------------------------", file=estatisticas_file)
    print(f"Media de Tempo de Execucao: {average_execution_time:.2f} segundos, usando {num_ants} formigas, e {num_iterations} iteracoes:", file=estatisticas_file)

    print("\nPercentagem de uso:", file=estatisticas_file)

    for cultura, count in cultura_counts.most_common():
        percentagem = (count / total_execucoes) * 100
        print(f"{cultura}: {percentagem:.2f}%")
        print(f"{cultura}: {percentagem:.2f}%", file=estatisticas_file)

# Exibir a média de custo para cada cultura
print("\nCalculo da média de custo:")
with open("estatisticas.txt", "a") as estatisticas_file:
    print("\nCalculo da media de custo:", file=estatisticas_file)

    # Ordenar as culturas com base na média de custo
    culturas_ordenadas = sorted(custos_culturas.items(), key=lambda x: sum(x[1]) / len(x[1]))

    for cultura, custos in culturas_ordenadas:
        media_custo = sum(custos) / len(custos)
        print(f"{cultura}: Média de {media_custo:.2f}")
        print(f"{cultura}: Media de {media_custo:.2f}", file=estatisticas_file)
