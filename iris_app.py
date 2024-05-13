from flask import Flask, request, jsonify
import joblib

model = joblib.load('model.pkl')

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    print(f"Request: {data}")
    prediction = model.predict(data['data'])
    print(f"Prediction: {prediction}")
    return jsonify(prediction.tolist())


if __name__ == '__main__':
    app.run(port=5000, debug=True)
