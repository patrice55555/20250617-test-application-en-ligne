CopierModifier
from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import joblib
import numpy as np

app = Flask(__name__)

model = load_model("modele_client_banque.h5")
scaler = joblib.load("scaler_client_banque.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    values = [
        data['CreditScore'],
        data['Gender'],
        data['Age'],
        data['Tenure'],
        data['Balance'],
        data['NumOfProducts'],
        data['HasCrCard'],
        data['IsActiveMember'],
        data['EstimatedSalary'],
        data['France'],
        data['Germany'],
        data['Spain']
    ]
    arr = np.array([values])
    arr_scaled = scaler.transform(arr)
    proba = model.predict(arr_scaled)[0][0]
    pred = int(proba >= 0.5)
    return jsonify({'probability': float(proba), 'prediction': pred})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
