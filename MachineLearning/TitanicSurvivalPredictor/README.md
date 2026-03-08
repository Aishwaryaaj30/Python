Titanic Survival Analysis using Logistic Regression

Project Overview

This project analyzes the Titanic dataset to study the survival patterns of passengers.
Using data analysis and visualization techniques, the project explores how factors such as gender, passenger class, age, and fare affected survival.

The project prepares the dataset for Logistic Regression, a machine learning algorithm used for classification problems.

---

Features

* Load and analyze Titanic dataset
* Perform data preprocessing
* Handle missing values
* Data visualization using graphs
* Survival analysis based on gender and passenger class
* Histogram visualization for Age and Fare distribution

---

Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn

---

Project Structure

TitanicSurvivalPredictor
│
├── MarvellousTitanicDataset.csv
├── TitanicSurvivalPredictor.py
└── README.md

---

Dataset Description

The dataset contains passenger information from the Titanic ship.

| Feature     | Description                       |
| ----------- | --------------------------------- |
| PassengerId | Unique passenger identifier       |
| Survived    | Survival status (0 = No, 1 = Yes) |
| Pclass      | Passenger class                   |
| Sex         | Gender of passenger               |
| Age         | Age of passenger                  |
| Fare        | Ticket fare                       |
| Embarked    | Port of embarkation               |

---

Project Workflow

1. Load dataset using Pandas
2. Display dataset structure
3. Remove unnecessary columns
4. Handle missing values
5. Perform Exploratory Data Analysis (EDA)
6. Generate visualizations:
   * Survival count plot
   * Survival based on gender
   * Survival based on passenger class
   * Age distribution
   * Fare distribution

---

How to Run the Project

Step 1: Install Required Libraries

  pip install pandas numpy matplotlib seaborn scikit-learn

Step 2: Run the Python Script

  python TitanicSurvivalPredictor.py

Make sure the dataset MarvellousTitanicDataset.csv is in the same folder as the script.

---

Visualizations Included

The project generates the following graphs:

* Survived vs Non-Survived Count Plot
* Survival Based on Gender
* Survival Based on Passenger Class
* Age Distribution Histogram
* Fare Distribution Histogram

These graphs help understand patterns in passenger survival.

---

Applications

* Data exploration and visualization
* Machine learning dataset preparation
* Understanding classification problems
* Educational data science project

---

This project is created for educational purposes.