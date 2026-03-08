Diabetes Prediction using Logistic Regression

Project Overview

This project uses Machine Learning (Logistic Regression) to predict whether a person has diabetes based on medical attributes.
The model is trained using the Pima Indians Diabetes Dataset and predicts the Outcome (0 = No Diabetes, 1 = Diabetes).

---

Features

* Load and analyze diabetes dataset
* Split dataset into training and testing sets
* Train a Logistic Regression model
* Predict diabetes outcomes
* Evaluate model accuracy

---

Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn

---

 Project Structure

DiabetesDetection
│
├── diabetes.csv
├── DiabetesDetection.py
└── README.md

---

Dataset Description

The dataset contains several medical predictor variables.

| Column                   | Description                       |
| ------------------------ | --------------------------------- |
| Pregnancies              | Number of pregnancies             |
| Glucose                  | Blood glucose level               |
| BloodPressure            | Blood pressure level              |
| SkinThickness            | Skin thickness measurement        |
| Insulin                  | Insulin level                     |
| BMI                      | Body Mass Index                   |
| DiabetesPedigreeFunction | Diabetes hereditary factor        |
| Age                      | Age of the patient                |
| Outcome                  | Diabetes result (0 = No, 1 = Yes) |

---

Project Workflow

1. Load dataset using Pandas
2. Explore dataset structure
3. Separate **features (X)** and **target variable (Y)**
4. Split dataset into **training and testing data**
5. Train **Logistic Regression model**
6. Evaluate model accuracy

---

How to Run the Project

Step 1: Install Required Libraries

  pip install pandas numpy scikit-learn

Step 2: Run the Python Script

  python DiabetesDetection.py

Make sure the dataset diabetes.csv is in the same folder as the script.

---

Model Evaluation

The model calculates:

* Training Accuracy
* Testing Accuracy

These metrics help evaluate how well the model predicts diabetes.

Example Output:

Training Accuracy : 0.78
Testing Accuracy : 0.75

---

Applications

* Early diabetes risk detection
* Healthcare data analysis
* Medical decision support systems
* Machine learning practice project

---

This project is created for educational purposes.