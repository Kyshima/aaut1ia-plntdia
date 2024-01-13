import pandas as pd
import random
import time
from collections import Counter

# Definir variáveis globais
weights = [0.1, 0.2, 0.3, 0.4]
year = 2019
number_genes = 3
state = 'Andhra Pradesh'
population_size = 100
max_generations_without_improvement = 20
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
    dataset_path = "../Dataset_Planning.csv"
    dataset = pd.read_csv(dataset_path)

    # Selecionar as colunas relevantes
    selected_columns = ['Crop_Year', 'State', 'Crop', 'ProdCost', 'CultCost', 'OperCost', 'FixedCost', 'TotalCost',
                        'Area_Total', 'Production_Total', 'Yield_Mean']
    relevant_data = dataset[selected_columns]
    filtered_data = dataset[(dataset['Crop_Year'] == year) & (dataset['State'] == state)]
    crops = filtered_data['Crop'].unique()

    melhor_tempo = []

    # Abrir o arquivo para escrita
    with open("output.txt", "w") as file:
        # Loop para executar X vezes
        for i in range(50):
            # Reiniciar a contagem de gerações sem melhoria a cada iteração
            current_generations_without_improvement = 0

            # Registrar o tempo de início
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

            # Exibir os resultados na consola
            print(f"\nExecução {i + 1}:")
            print("Melhor indivíduo:", best_individual)
            print("Fitness/Cost:", 1 / final_fitness)
            print("Tempo decorrido: {:.2f} segundos".format(elapsed_time))

            # Gravar os resultados no arquivo
            print(f"\nExecucao {i + 1}:", file=file)
            print("Melhor individuo:", best_individual, file=file)
            print("Fitness/Cost:", 1 / final_fitness, file=file)

            melhor_tempo.append([])
            melhor_tempo[i].append(elapsed_time)

    # Fechar o arquivo após o loop principal
    file.close()

    # Calcular a percentagem de uso de cada cultura
    total_execucoes = 50  # Defina o número total de execuções
    cultura_counts = Counter()

    for i in range(total_execucoes):
        population = initialize_population(population_size, crops)
        population, best_individual, final_fitness = genetic_algorithm(population)
        print(f"{i}")

        for cultura in best_individual:
            cultura_counts[cultura] += 1

    # Cálculos de estatísticas adicionados após o loop principal
    with open("estatisticas.txt", "a") as estatisticas_file:
        print("----------------------------------------------------------------", file=estatisticas_file)
        average_execution_time = sum(sum(run) for run in melhor_tempo) / total_execucoes
        print(f"Media de Tempo de Execucao: {average_execution_time:.2f} segundos, usando {population_size} individuos, e {max_generations_without_improvement} maximo de iteracoes:", file=estatisticas_file)

        print("\nPercentagem de uso:")
        print("\nPercentagem de uso:", file=estatisticas_file)
        total_culturas = len(cultura_counts)

        for cultura, count in cultura_counts.most_common():
            percentagem = (count / total_execucoes) * 100
            print(f"{cultura}: {percentagem:.2f}%")
            print(f"{cultura}: {percentagem:.2f}%", file=estatisticas_file)

        # Calcular a média de custo para cada cultura
        custos_culturas = {}

        for i in range(total_execucoes):
            print(f"{i}")
            population = initialize_population(population_size, crops)
            population, best_individual, final_fitness = genetic_algorithm(population)

            for cultura in best_individual:
                if cultura not in custos_culturas:
                    custos_culturas[cultura] = []

                custo = 1 / final_fitness
                custos_culturas[cultura].append(custo)

        print("\nCalculo da media de custo:")
        print("\nCalculo da media de custo:", file=estatisticas_file)

        # Ordenar as culturas com base na média de custo
        culturas_ordenadas = sorted(custos_culturas.items(), key=lambda x: sum(x[1]) / len(x[1]))

        for cultura, custos in culturas_ordenadas:
            media_custo = sum(custos) / len(custos)
            print(f"{cultura}: Média de {media_custo:.2f}")
            print(f"{cultura}: Media de {media_custo:.2f}", file=estatisticas_file)
