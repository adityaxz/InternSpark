# Model Deployment – API & Containerization for Breast Cancer Classification

## 1. Objective

The objective of this project is to deploy a machine learning model as a REST API using Flask and prepare it for containerized deployment using Docker. The deployed API accepts feature values from the Breast Cancer Wisconsin dataset and returns a prediction indicating whether a tumor is malignant or benign.

---

## 2. Dataset Description

The Breast Cancer Wisconsin dataset was obtained from the Scikit-learn library.

### Dataset Characteristics

* Total Samples: 569
* Total Features: 30
* Target Classes:

  * 0 = Malignant
  * 1 = Benign

The dataset contains numerical measurements extracted from digitized images of breast mass cell nuclei.

---

## 3. Model Development

A Random Forest Classifier was trained using the dataset and saved using the Joblib library.

### Training Process

* Dataset loaded from Scikit-learn
* Features and target extracted
* Random Forest model trained
* Model saved as:

```
breast_cancer_model.pkl
```

This serialized model file was later used by the API for inference.

---

## 4. API Development

A Flask-based REST API was developed to serve model predictions.

### API Endpoint

#### Home Endpoint

```
GET /
```

Response:

```json
{
  "message": "Breast Cancer Prediction API"
}
```

#### Prediction Endpoint

```
POST /predict
```

The endpoint accepts a JSON request containing the 30 input features required by the model.

Example Request:

```json
{
  "features": [17.99,10.38,122.8,1001.0,0.1184,0.2776,0.3001,
               0.1471,0.2419,0.0787,1.095,0.9053,8.589,153.4,
               0.0064,0.0490,0.0537,0.0158,0.0300,0.0061,
               25.38,17.33,184.6,2019.0,0.1622,0.6656,
               0.7119,0.2654,0.4601,0.1189]
}
```

Example Response:

```json
{
  "prediction": "Malignant"
}
```

---

## 5. Docker Containerization

A Dockerfile was created to package the Flask application and its dependencies.

### Docker Configuration

The Docker container:

* Uses a Python base image
* Installs required dependencies
* Copies application files
* Exposes port 5000
* Starts the Flask API automatically

### Docker Commands

Build Docker Image:

```bash
docker build -t breast-api .
```

Run Docker Container:

```bash
docker run -p 5000:5000 breast-api
```

These commands allow the API to run in an isolated and portable environment.

---

## 6. API Testing

The API was tested locally using a web browser and PowerShell.

### Home Endpoint Test

URL:

```
http://127.0.0.1:5000
```

Output:

```json
{
  "message": "Breast Cancer Prediction API"
}
```

### Prediction Test

A sample request was submitted to the `/predict` endpoint.

Prediction Result:

```
Malignant
```

The successful response confirmed correct API integration with the trained machine learning model.

---

## 7. Tools and Libraries Used

### Programming Language

* Python

### Development Environment

* Visual Studio Code
* Jupyter Notebook

### Libraries

* Flask
* Scikit-learn
* Joblib
* NumPy
* Pandas

### Containerization

* Docker

---

## 8. Results

The machine learning model was successfully deployed as a Flask REST API.

Key Achievements:

* Trained Random Forest model exported successfully
* REST API created using Flask
* Prediction endpoint implemented
* JSON request and response handling completed
* Docker configuration prepared
* Successful local inference testing performed

---

## 9. Conclusion

This project demonstrated the deployment of a machine learning model through a REST API and its preparation for containerized deployment. The Flask application successfully served predictions using the trained breast cancer classification model.

The integration of machine learning, API development, and Docker containerization provides a practical foundation for deploying AI solutions in real-world environments.

---

## 10. Repository Information

GitHub Repository:

https://github.com/adityaxz/InternSpark

Files Included:

* 3apiintegration.ipynb
* 3app.py
* 3dockerfile
* 3report.md
* breast_cancer_model.pkl
* Supporting screenshots

This report corresponds to the Model Deployment – API & Containerization task.
