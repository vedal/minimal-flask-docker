from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.route('/predict',methods=['POST'])
def predict():
    payload = request.get_json(force=True)
    return jsonify(payload)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
