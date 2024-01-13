from flask import Flask, request, jsonify
from Code.backend.prediction.yield_prediction import predict
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/planning/geneticAlgorithm', methods=['POST'])
def get_planningGA():
    
    data = request.get_json()

    state = data.get('state')
    crop = data.get('crop')
    area = float(data.get('area'))
    prodAnt1 = float(data.get('prodAnt1'))
    areaAnt1 = float(data.get('areaAnt1'))
    prodAnt2 = float(data.get('prodAnt2'))
    areaAnt2 = float(data.get('areaAnt2'))
    prodAnt3 = float(data.get('prodAnt3'))
    areaAnt3 = float(data.get('areaAnt3'))

    result = predict(state, crop, area, prodAnt1, areaAnt1, prodAnt2, areaAnt2, prodAnt3, areaAnt3)

    return jsonify({'Yield': result})

@app.route('/planning/antColony', methods=['POST'])
def  get_planningACO():
    
    data = request.get_json()

    state = data.get('state')
    crop = data.get('crop')
    area = float(data.get('area'))
    prodAnt1 = float(data.get('prodAnt1'))
    areaAnt1 = float(data.get('areaAnt1'))
    prodAnt2 = float(data.get('prodAnt2'))
    areaAnt2 = float(data.get('areaAnt2'))
    prodAnt3 = float(data.get('prodAnt3'))
    areaAnt3 = float(data.get('areaAnt3'))

    result = predict(state, crop, area, prodAnt1, areaAnt1, prodAnt2, areaAnt2, prodAnt3, areaAnt3)

    return jsonify({'Yield': result})



if __name__ == '__main__':
    print('API is running on port 5001')
    app.run(host='localhost', port=5001)
