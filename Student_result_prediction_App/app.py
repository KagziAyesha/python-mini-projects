from flask import Flask, request, jsonify
import joblib
import numpy as np

# Load model
model = joblib.load("hours_pass_model.pkl")

app = Flask(__name__)

@app.route("/")
def home():
    return "Hours Pass Prediction API is running 🚀"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    hours = data["hours_studied"]

    prediction = model.predict([[hours]])

    result = "Pass" if prediction[0] == 1 else "Fail"

    return jsonify({
        "hours_studied": hours,
        "prediction": result
    })

if __name__ == "__main__":
    app.run(debug=True)