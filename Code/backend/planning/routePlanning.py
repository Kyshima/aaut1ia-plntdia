from flask import Flask, request, jsonify
from antColony import ant_colony_optimization
from geneticAlgorithm import run
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/planning/geneticAlgorithm', methods=['POST'])
def get_planningGA():
    json_file_path = 'D:/Faculdade/mestrado/projeto2semestre/aaut1ia-plntdia/Code/backend/planning/configurationPlanning.json'
    with open(json_file_path, 'r') as file:
        # Load the JSON data from the file
        config_data = json.load(file)
    
    
    data = request.get_json()

    state = data.get('state')
    weights = data.get('weights')
    year = int(data.get('year'))
    number_genes = int(data.get('number_genes'))

    result = run(weights, year, number_genes, state, config_data['population_size'], config_data['max_generations_without_improvement'], config_data['temporalAG'], config_data['max_timeAG'], config_data['mutation_rate'])

    return jsonify({'teste': result})

@app.route('/planning/antColony', methods=['POST'])
def  get_planningACO():
    json_file_path = 'D:/Faculdade/mestrado/projeto2semestre/aaut1ia-plntdia/Code/backend/planning/configurationPlanning.json'
    with open(json_file_path, 'r') as file:
        # Load the JSON data from the file
        config_data = json.load(file)
    
    data = request.get_json()

    weights = data.get('weights')
    state = data.get('state')
    number_crops = int(data.get('number_crops'))
    year = int(data.get('year'))

    result = ant_colony_optimization(weights, state, year, number_crops, config_data['pheromone_initial'], config_data['pheromone_decay'], config_data['alpha'], config_data['beta'], config_data['num_ants'], config_data['num_iterations'], config_data['temporalACO'], config_data['max_timeACO'])

    return jsonify({'teste': result})



if __name__ == '__main__':
    print('API is running on port 5001')
    app.run(host='localhost', port=5001)
