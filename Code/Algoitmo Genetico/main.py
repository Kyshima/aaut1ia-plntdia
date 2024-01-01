import pandas as pd
import random
import numpy as np

# Definir a semente para geração de números aleatórios
seed = 42  # Pode ser qualquer número inteiro
random.seed(seed)
np.random.seed(seed)

def initialize_population(population_size):
    population = []
    for _ in range(population_size):
        genes = [random.choice([0, 1]) for _ in range(len(selected_columns) - 3)]  # 0: Não selecionado, 1: Selecionado
        population.append(genes)
    return population

def crossover(parent1, parent2):
    # Ponto de crossover (escolhido aleatoriamente)
    crossover_point = random.randint(1, len(parent1) - 1)

    # Criar o filho combinando os genes dos pais até o ponto de crossover
    child = parent1[:crossover_point] + parent2[crossover_point:]

    return child

def mutate(individual, mutation_rate):
    # Aplicar mutação a cada gene com uma taxa de mutação
    mutated_individual = [gene if random.random() > mutation_rate else 1 - gene for gene in individual]

    return mutated_individual

def evaluate_fitness(individual, selected_columns):
    # Mapear os índices selecionados para os nomes das colunas relevantes
    selected_columns = selected_columns[2:-1]  # Excluir as colunas 'Crop_Year' e 'State'
    selected_columns = [col for col, gene in zip(selected_columns, individual) if gene == 1]

    # Filtrar o dataframe com base nas colunas selecionadas
    filtered_data = relevant_data[['Crop_Year', 'State'] + selected_columns]

    # Agrupar por ano e estado e calcular a média do Yield_Mean
    grouped_data = filtered_data.groupby(['Crop_Year', 'State']).mean().reset_index()

    # Calcular o fitness como a média ponderada do Yield_Mean
    weighted_mean_yield = grouped_data[selected_columns].mean(axis=1)

    # Verificar se há valores válidos antes de calcular a média
    if weighted_mean_yield.isnull().any():
        fitness = float('-inf')  # Defina um valor negativo grande para indicar fitness inválido
    else:
        fitness = weighted_mean_yield.mean()

    return fitness


def genetic_algorithm(population, generations, mutation_rate=0.1):
    for _ in range(generations):
        # Avaliar a aptidão de cada indivíduo na população
        fitness_scores = [evaluate_fitness(individual, selected_columns) for individual in population]

        # Selecionar os melhores indivíduos
        selected_indices = sorted(range(len(fitness_scores)), key=lambda k: fitness_scores[k], reverse=True)[:int(len(population) * 0.2)]
        selected_population = [population[i] for i in selected_indices]

        # Se a população selecionada estiver vazia, não há filhos para crossover e mutação
        if not selected_population:
            continue

        # Cruzamento (crossover)
        children = []
        for i in range(0, len(selected_population), 2):
            parent1 = selected_population[i]
            parent2 = selected_population[i + 1]

            # Aplicar crossover para gerar dois filhos
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent2, parent1)

            children.extend([child1, child2])

        # Mutação
        mutated_population = [mutate(individual, mutation_rate) for individual in children]

        # Substituir a população original pela nova população mutada
        population = mutated_population

    # Se a população final estiver vazia, retorne um indivíduo aleatório
    if not population:
        return initialize_population(1)[0]

    # Retornar o melhor indivíduo ou a população final
    return max(population, key=lambda ind: evaluate_fitness(ind, selected_columns))

if __name__ == "__main__":
    # Carregar o dataset
    dataset_path = "Dataset_Planning.csv"
    dataset = pd.read_csv(dataset_path)

    # Selecionar as colunas relevantes
    selected_columns = ['Crop_Year', 'State', 'ProdCost', 'CultCost', 'OperCost', 'FixedCost', 'TotalCost', 'Area_Total', 'Production_Total', 'Yield_Mean']
    relevant_data = dataset[selected_columns]

    # Uso do algoritmo genético
    population_size = 50
    generations = 100
    population = initialize_population(population_size)
    best_individual = genetic_algorithm(population, generations)

    # Exibir os resultados
    print("Melhor indivíduo:", best_individual)

    # Calcular o fitness final para o melhor indivíduo
    final_fitness = evaluate_fitness(best_individual, selected_columns)
    print("Fitness final:", final_fitness)
