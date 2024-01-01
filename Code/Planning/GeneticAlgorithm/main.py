import pandas as pd
import random
import numpy as np

# Definir a semente para geração de números aleatórios
#seed = 42  # Pode ser qualquer número inteiro
#random.seed(seed)
#np.random.seed(seed)
weights = [0.1,0.2,0.3,0.4]
year = 2019
state='Andhra Pradesh'

def initialize_population(population_size,cops):
    population = []
    for _ in range(population_size):
        genes = [random.choice(cops) for _ in range(1,4)]
        population.append(genes)
    return population

def crossover(parent1, parent2):
    # Ponto de crossover (escolhido aleatoriamente)
    crossover_point = random.randint(1, len(parent1) - 1)

    # Criar o filho combinando os genes dos pais até o ponto de crossover
    child = parent1[:crossover_point] + parent2[crossover_point:]

    return child

def mutate(individual, mutation_rate, crops):
    mutated_individual = []

    for gene in individual:
        # Check if the gene is numeric (float or int)
        if isinstance(gene, (int, float)):
            mutated_gene = gene if random.random() > mutation_rate else 1 - gene
        else:
            # If the gene is a string (crop name), randomly choose a different crop
            mutated_gene = random.choice(crops) if random.random() < mutation_rate else gene

        mutated_individual.append(mutated_gene)

    return mutated_individual


def evaluate_fitness(individual, selected_columns):
    # Mapear os índices selecionados para os nomes das colunas relevantes
    selected_columns = selected_columns[2:-1]  # Excluir as colunas 'Crop_Year' e 'State'

    # Filtrar o dataframe com base nas colunas selecionadas
    # filtered_data = relevant_data[['Crop_Year', 'State'] + selected_columns]

    # Inicializar a soma total dos custos
    total_cost = 0.0

    # Iterar pelos genes do indivíduo
    for gene in individual:
        # Verificar se o gene é selecionado (1)
        row = filtered_data.loc[filtered_data['Crop'] == gene]
        # print(row[['ProdCost','CultCost','OperCost','FixedCost']])
        # Calcular o custo para o gene atual e somar ao total
        total_cost += (row['ProdCost'] * weights[0] + row['CultCost'] * weights[1] + row['OperCost'] * weights[2] + row['FixedCost'] * weights[3]).sum()

    # Calcular o fitness como o inverso da soma total dos custos (minimizar custos)
    fitness = 1.0 / (total_cost + 1) if total_cost > 0 else float('-inf')

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
        for i in range(0, len(selected_population)-1, 2):
            parent1 = selected_population[i]
            parent2 = selected_population[i + 1]

            # Aplicar crossover para gerar dois filhos
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent2, parent1)

            children.extend([child1, child2])

        # Mutação
        mutated_population = [mutate(individual, mutation_rate, crops) for individual in children]

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
    selected_columns = ['Crop_Year', 'State','Crop' ,'ProdCost', 'CultCost', 'OperCost', 'FixedCost', 'TotalCost', 'Area_Total', 'Production_Total', 'Yield_Mean']
    relevant_data = dataset[selected_columns]
    filtered_data = dataset[(dataset['Crop_Year'] == year) & (dataset['State'] == state)]
    crops = filtered_data['Crop'].unique()
    # print(filtered_data[['Crop_Year', 'State', 'Crop']])
    # print(crops)

    #filtered_data = dataset[(dataset['Crop_Year'] == year) & (dataset['State'] == state) & (dataset['Crop'] == 'Groundnut')]
    #print(filtered_data[['ProdCost', 'CultCost', 'OperCost', 'FixedCost']])

    # Uso do algoritmo genético
    population_size = 50
    generations = 100
    population = initialize_population(population_size,crops)
    best_individual = genetic_algorithm(population, generations)

    # Exibir os resultados
    print("Melhor indivíduo:", best_individual)

    # Calcular o fitness final para o melhor indivíduo
    final_fitness = evaluate_fitness(best_individual, selected_columns)
    print("Fitness final:", final_fitness)
