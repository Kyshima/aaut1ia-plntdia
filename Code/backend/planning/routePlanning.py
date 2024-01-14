from flask import Flask, request, jsonify
from Code.backend.planning.antColony import ant_colony_optimization
from Code.backend.planning.geneticAlgorithm import run
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/planning/geneticAlgorithm', methods=['POST'])
def get_planningGA():
    
    data = request.get_json()

    state = data.get('state')
    weights = data.get('weights')
    year = 2019
    number_genes = data.get('number_genes')
    population_size = data.get('population_size')
    max_generations_without_improvement = data.get('max_generations_without_improvement')
    temporal = float(data.get('temporal'))
    max_time = float(data.get('max_time'))
    mutation_rate = float(data.get('mutation_rate'))

    result = run(weights, year, number_genes, state, population_size, max_generations_without_improvement, temporal, max_time, mutation_rate)

    return jsonify({'teste': result})

@app.route('/planning/antColony', methods=['POST'])
def  get_planningACO():
    
    data = request.get_json()

    weights = data.get('weights')
    state = data.get('state')
    number_crops = data.get('number_crops')
    pheromone_initial = float(data.get('pheromone_initial'))
    pheromone_decay = float(data.get('pheromone_decay'))
    alpha = float(data.get('alpha'))
    beta = float(data.get('beta'))
    num_ants = data.get('num_ants')
    num_iterations = data.get('num_iterations')
    temporal = float(data.get('temporal'))
    max_time = float(data.get('max_time'))
    year = 2017

    result = ant_colony_optimization(weights, state, year, number_crops, pheromone_initial, pheromone_decay, alpha, beta, num_ants, num_iterations, temporal, max_time)

    return jsonify({'teste': result})



if __name__ == '__main__':
    print('API is running on port 5001')
    app.run(host='localhost', port=5001)
