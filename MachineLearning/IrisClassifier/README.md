Iris Flower Clustering using K-Means

 Project Overview

This project demonstrates Unsupervised Machine Learning using the -Means Clustering algorithm on the Iris dataset.

The goal of the project is to group iris flowers into clusters based on their features without using labeled outputs.

The model uses the Elbow Method to determine the optimal number of clusters and then applies K-Means clustering to classify the flowers.

---

Features

* Load and analyze the Iris dataset
* Apply K-Means clustering algorithm
* Use Elbow Method to determine optimal clusters
* Visualize clusters using scatter plots
* Display cluster centroids

---

 Technologies Used

* Python
* Pandas
* Matplotlib
* Scikit-learn

---

Project Structure

IrisClassifier
│
├── iris.csv
├── IrisClassifier.py
└── README.md

---

Dataset Description

The Iris dataset contains measurements of iris flowers.

| Feature      | Description          |
| ------------ | -------------------- |
| Sepal Length | Length of sepal (cm) |
| Sepal Width  | Width of sepal (cm)  |
| Petal Length | Length of petal (cm) |
| Petal Width  | Width of petal (cm)  |

These features are used to group flowers into clusters.

---

Project Workflow

1. Load Iris dataset using Pandas
2. Extract features for clustering
3. Apply Elbow Method to determine optimal value of K
4. Train K-Means clustering model
5. Predict cluster groups
6. Visualize clusters and centroids using scatter plot

---

How to Run the Project

Step 1: Install Required Libraries

  pip install pandas matplotlib scikit-learn

Step 2: Run the Python Script

  python IrisClassifier.py

Make sure the dataset iris.csv is in the same folder as the script.

---

Elbow Method

The Elbow Method helps determine the optimal number of clusters by plotting:

* Number of clusters (K)
* Within Cluster Sum of Squares (WCSS)

The point where the graph bends like an elbow indicates the best value of K.

---

Output Visualization

The program generates:

* Elbow graph to find optimal clusters
* Cluster visualization graph
* Centroids of clusters

Each cluster represents a type of iris flower.

---

Applications

* Pattern recognition
* Data clustering
* Unsupervised machine learning learning project
* Biological data classification

---

This project is created for educational and learning purposes.