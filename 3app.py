from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

model = joblib.load("breast_cancer_model.pkl")

@app.route("/")
def home():
    return {"message": "Breast Cancer Prediction API"}

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json["features"]

    prediction = model.predict([data])[0]

    result = "Benign" if prediction == 1 else "Malignant"

    return jsonify({
        "prediction": result
    })

if __name__ == "__main__":
    app.run(debug=True)