import pandas as pd
import random
import time

# Definir variáveis globais
weights = [0.1, 0.2, 0.3, 0.4]
year = 2019
number_genes = 3
state = 'Andhra Pradesh'
population_size = 50
max_generations_without_improvement = 5
current_generations_without_improvement = 0
temporal = False
max_time = 4  #(segundos)
prev_fitness = 0

def initialize_population(population_size, crops):
    population = []
    crops_list = list(crops)
    for _ in range(population_size):
        unique_crops = random.sample(crops_list, number_genes)
        population.append(unique_crops)
    return population


def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child = parent1[:crossover_point] + [gene for gene in parent2 if gene not in parent1[:crossover_point]]

    while len(child) > number_genes:
        child.pop()  # Remover genes extras

    while len(child) < number_genes:
        remaining_genes = [gene for gene in parent1 if gene not in child and gene not in parent2[:crossover_point]]
        if remaining_genes:
            child.append(random.choice(remaining_genes))
        else:
            break  # Evitar um loop infinito se não houver genes restantes

    return child


def mutate(individual, mutation_rate, crops):
    mutated_individual = list(individual)

    for i, gene in enumerate(individual):
        if isinstance(gene, (int, float)):
            mutated_gene = gene if random.random() > mutation_rate else 1 - gene
        else:
            remaining_genes = [crop for crop in crops if crop not in mutated_individual]
            mutated_gene = random.choice(remaining_genes) if random.random() < mutation_rate else gene

        mutated_individual[i] = mutated_gene

    return mutated_individual


def evaluate_fitness(individual, selected_columns):
    total_cost = 0.0

    for gene in individual:
        row = filtered_data.loc[filtered_data['Crop'] == gene]
        total_cost += (row['ProdCost'] * weights[0] + row['CultCost'] * weights[1] + row['OperCost'] * weights[2] + row[
            'FixedCost'] * weights[3]).sum()

    fitness = 1.0 / (total_cost + 1) if total_cost > 0 else float('-inf')

    return fitness


def genetic_algorithm(population, mutation_rate=0.1):
    global current_generations_without_improvement


    fitness_scores = [evaluate_fitness(individual, selected_columns) for individual in population]

    selected_indices = sorted(range(len(fitness_scores)), key=lambda k: fitness_scores[k], reverse=True)[
                       :int(len(population) * 0.2)]

    if len(selected_indices) % 2 != 0:
        selected_indices.pop()

    selected_population = [population[i] for i in selected_indices]


    children = []
    for i in range(0, len(selected_population) - 1, 2):
        parent1 = selected_population[i]
        parent2 = selected_population[i + 1]
        child1 = crossover(parent1, parent2)
        child2 = crossover(parent2, parent1)
        children.extend([child1, child2])

    mutated_population = [mutate(individual, mutation_rate, crops) for individual in children]

    mutated_population = population + mutated_population
    population = sorted(mutated_population, key=lambda ind: evaluate_fitness(ind, selected_columns), reverse=True)[:population_size]

    best_individual = population[0]
    best_fitness = evaluate_fitness(best_individual, selected_columns)

    if best_fitness > prev_fitness:
        current_generations_without_improvement = 0
    else:
        current_generations_without_improvement += 1

    return population, best_individual, best_fitness


if __name__ == "__main__":
    # Carregar o dataset
    dataset_path = "Dataset_Planning.csv"
    dataset = pd.read_csv(dataset_path)

    # Selecionar as colunas relevantes
    selected_columns = ['Crop_Year', 'State', 'Crop', 'ProdCost', 'CultCost', 'OperCost', 'FixedCost', 'TotalCost',
                        'Area_Total', 'Production_Total', 'Yield_Mean']
    relevant_data = dataset[selected_columns]
    filtered_data = dataset[(dataset['Crop_Year'] == year) & (dataset['State'] == state)]
    crops = filtered_data['Crop'].unique()

    start_time = time.time()

    # Uso do algoritmo genético
    population = initialize_population(population_size, crops)
    prev_fitness = evaluate_fitness(population[0], selected_columns)
    while True:

        if temporal and (time.time() - start_time) >= max_time:
            break
        elif current_generations_without_improvement >= max_generations_without_improvement:
            break

        population, best_individual, final_fitness = genetic_algorithm(population)

        elapsed_time = time.time() - start_time
        prev_fitness = final_fitness
    # Exibir os resultados
    print("Melhor indivíduo:", best_individual)
    print("Fitness/Cost:", 1 / final_fitness)
    print("Tempo decorrido: {:.2f} segundos".format(elapsed_time))
