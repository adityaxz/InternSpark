# Breast Cancer Classification using Machine Learning

## 1. Objective

The objective of this project is to build and evaluate machine learning classification models capable of predicting whether a breast tumor is malignant or benign using the Breast Cancer Wisconsin dataset. The project compares the performance of Logistic Regression and Random Forest classifiers using multiple evaluation metrics.

---

## 2. Dataset Description

The Breast Cancer Wisconsin dataset was obtained from the Scikit-learn library. The dataset contains numerical measurements computed from digitized images of breast mass cell nuclei.

### Dataset Characteristics

* Total Samples: 569
* Total Features: 30
* Target Variable: Tumor Diagnosis

### Classes

* 0 = Malignant
* 1 = Benign

### Example Features

* Mean Radius
* Mean Texture
* Mean Perimeter
* Mean Area
* Mean Smoothness
* Mean Compactness
* Mean Concavity

The dataset is suitable for supervised machine learning classification tasks and is widely used for evaluating classification algorithms.

---

## 3. Data Exploration and Visualization

Exploratory Data Analysis (EDA) was performed to understand the structure and characteristics of the dataset.

### Summary Statistics

Statistical measures including count, mean, standard deviation, minimum, maximum, and quartiles were generated using the Pandas `describe()` function.

### Visualizations Performed

1. Histogram of Mean Radius
2. Boxplot of Mean Radius
3. Scatter Plot of Mean Radius vs Mean Texture
4. Bar Plot of the First Ten Mean Radius Values

These visualizations helped identify data distributions, outliers, and relationships among features.

---

## 4. Data Preprocessing

Before model training, the dataset was prepared using train-test splitting.

### Train-Test Split

* Training Data: 80%
* Testing Data: 20%
* Random State: 42

### Dataset Shapes

Training Data Shape:

(455, 30)

Testing Data Shape:

(114, 30)

The training data was used for model learning while the testing data was used to evaluate model performance on unseen samples.

---

## 5. Machine Learning Models

Two supervised classification algorithms were implemented and compared.

### Logistic Regression

Logistic Regression is a statistical classification algorithm that predicts the probability of a sample belonging to a specific class.

#### Advantages

* Simple and efficient
* Easy to interpret
* Fast training process

### Random Forest Classifier

Random Forest is an ensemble learning algorithm that combines multiple decision trees to improve prediction accuracy and robustness.

#### Advantages

* High predictive performance
* Resistant to overfitting
* Handles complex feature relationships effectively

---

## 6. Model Evaluation

The models were evaluated using several classification metrics.

### Accuracy

| Model               | Accuracy |
| ------------------- | -------- |
| Logistic Regression | 95.61%   |
| Random Forest       | 95.61%   |

Both models achieved excellent classification accuracy on the testing dataset.

### Precision, Recall and F1 Score

| Metric    | Value |
| --------- | ----- |
| Precision | 0.96  |
| Recall    | 0.96  |
| F1 Score  | 0.96  |

These results indicate strong classification performance and balanced predictions.

### ROC-AUC Score

ROC-AUC measures the ability of a model to distinguish between classes.

ROC-AUC Score:

0.9944

#### Interpretation

* 1.0 = Perfect Classification
* 0.5 = Random Guessing

The obtained score demonstrates outstanding classification capability.

---

## 7. Cross Validation

Five-fold cross validation was performed to evaluate model stability and generalization.

### Cross Validation Scores

[0.9298, 0.9386, 0.9825, 0.9825, 0.9735]

### Average Cross Validation Score

0.9614

The high average score indicates that the model performs consistently across different subsets of the dataset.

---

## 8. Model Comparison

| Evaluation Metric | Logistic Regression | Random Forest |
| ----------------- | ------------------- | ------------- |
| Accuracy          | 95.61%              | 95.61%        |
| Precision         | 0.96                | 0.96          |
| Recall            | 0.96                | 0.96          |
| F1 Score          | 0.96                | 0.96          |
| ROC-AUC           | 0.9944              | 0.9944        |

### Selected Model

Random Forest Classifier

### Reason for Selection

Random Forest was selected because it demonstrated excellent predictive performance while maintaining strong stability through cross-validation. Its ensemble approach makes it more robust for classification problems involving complex relationships between features.

---

## 9. Tools and Libraries Used

### Programming Language

* Python

### Development Environment

* Visual Studio Code
* Jupyter Notebook

### Libraries

* Pandas
* NumPy
* Matplotlib
* Scikit-learn

---

## 10. Repository Information

GitHub Repository:

https://github.com/adityaxz/InternSpark

### Files Included

* 1mlc.ipynb
* 1report.md
* Supporting screenshots

The repository contains multiple internship tasks. This report corresponds to the Machine Learning Classification Project.

---

## 11. Results

The implemented machine learning models achieved excellent performance on the Breast Cancer Wisconsin dataset.

### Key Results

* Accuracy: 95.61%
* Precision: 96%
* Recall: 96%
* F1 Score: 96%
* ROC-AUC: 99.44%
* Cross Validation Accuracy: 96.14%

The results indicate that the trained models can effectively classify tumors as malignant or benign with high reliability.

---

## 12. Conclusion

This project successfully demonstrated the application of supervised machine learning techniques for breast cancer classification. The dataset was explored using statistical analysis and visualization techniques before training and evaluating two machine learning algorithms: Logistic Regression and Random Forest.

Both models achieved high predictive performance, with Random Forest showing particularly strong results through excellent ROC-AUC and cross-validation scores. The project demonstrates the effectiveness of machine learning in predictive analytics and medical diagnosis support systems.

Future improvements may include feature selection, hyperparameter optimization, and evaluation of additional classification algorithms to further improve performance.
