Head Size vs Brain Weight Prediction using Linear Regression

Project Overview

This project demonstrates Simple Linear Regression using Python to analyze the relationship between Head Size (cm³) and Brain Weight (grams).

The goal of the model is to predict brain weight based on head size using a machine learning regression algorithm.

---

Features

* Load and analyze dataset
* Perform statistical analysis
* Split dataset into training and testing sets
* Train a Linear Regression model
* Predict brain weight from head size
* Evaluate model performance
* Visualize regression results with a graph

---

Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn

---

Project Structure

HeadBrainClassification
│
├── MarvellousHeadBrain.csv
├── HeadBrainClassification.py
└── README.md

---

Dataset Description

The dataset contains information about head size and brain weight.

| Column               | Description           |
| -------------------- | --------------------- |
| Head Size (cm³)      | Head size measurement |
| Brain Weight (grams) | Weight of the brain   |

---

Project Workflow

1. Load dataset using Pandas
2. Display first few records
3. Perform statistical analysis using `describe()`
4. Define:
   * Independent Variable (X) → Head Size
   * Dependent Variable (Y) → Brain Weight
5. Split dataset into training and testing data
6. Train Linear Regression Model
7. Predict brain weight
8. Evaluate model using:
   * Mean Squared Error (MSE)
   * Root Mean Squared Error (RMSE)
   * R² Score
9. Visualize regression line and data points

---

How to Run the Project

Step 1: Install Required Libraries

  pip install pandas numpy matplotlib scikit-learn

Step 2: Run the Python Script

  python HeadBrainClassification.py

Make sure the dataset MarvellousHeadBrain.csv is in the same folder as the script.

---

Model Evaluation Metrics

The model calculates the following metrics:

* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* R² Score

These metrics evaluate how well the regression model fits the data.

---

Visualization

The project generates a graph showing:

* Actual data points (Head Size vs Brain Weight)
* Regression line predicted by the model

This helps visualize the relationship between head size and brain weight.

---

Applications

* Understanding regression analysis
* Machine learning learning project
* Predictive modeling practice
* Data science case study

---

This project is created for educational and learning purposes.