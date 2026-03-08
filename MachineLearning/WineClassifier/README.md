Wine Classification using K-Nearest Neighbors (KNN)

Project Overview

This project uses Machine Learning (K-Nearest Neighbors Algorithm) to classify different types of wine based on their chemical properties.

The model trains on the dataset and predicts the wine class using the most suitable value of K (number of neighbors) for the best accuracy.

---

Features

* Load and preprocess wine dataset
* Handle missing values
* Feature scaling using StandardScaler
* Train KNN classification model
* Find optimal value of K
* Evaluate model accuracy
* Display Confusion Matrix

---

Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn

---

Project Structure

WineClassifier
│
├── WinePredictor.csv
├── WineClassifier.py
└── README.md

---

Dataset Description

The dataset contains different chemical properties of wine used to classify the wine type.

| Feature              | Description                     |
| -------------------- | ------------------------------- |
| Alcohol              | Alcohol content                 |
| Malic Acid           | Amount of malic acid            |
| Ash                  | Ash content                     |
| Alcalinity of Ash    | Mineral content                 |
| Magnesium            | Magnesium level                 |
| Total Phenols        | Phenol concentration            |
| Flavanoids           | Flavanoid compounds             |
| Nonflavanoid Phenols | Nonflavanoid compounds          |
| Proanthocyanins      | Antioxidant compounds           |
| Color Intensity      | Color concentration             |
| Hue                  | Wine color shade                |
| OD280/OD315          | Dilution ratio                  |
| Proline              | Amino acid level                |
| Class                | Wine category (Target variable) |

---

Project Workflow

1. Load dataset using Pandas
2. Clean dataset by removing missing values
3. Separate features (X) and target (Y)
4. Apply feature scaling using StandardScaler
5. Split dataset into training and testing data
6. Train KNN model with different values of K
7. Select the best K value based on accuracy
8. Train final model using best K
9. Evaluate model using:
   * Accuracy Score
   * Confusion Matrix

---

How to Run the Project

Step 1: Install Required Libraries

  pip install pandas numpy scikit-learn

Step 2: Run the Python Script

  python WineClassifier.py

Make sure the dataset WinePredictor.csv is in the same folder as the script.

---

Model Evaluation

The model calculates:

* Best value of K
* Accuracy Score
* Confusion Matrix

Example Output:

Best value of k is : 5
Final best accuracy is : 92.3
Confusion Matrix :
 [[12 0 0]
 [0 11 1]
 [0 1 10]]

Applications
* Wine quality classification
* Pattern recognition
* Machine learning classification practice
* Data science learning project

This project is created for educational purposes.