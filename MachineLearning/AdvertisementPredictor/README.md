#Advertising Sales Prediction using Linear Regression

#Project Overview

This project uses Machine Learning (Linear Regression)** to predict product sales based on advertising budgets in different media such as TV, Radio, and Newspaper.

The model analyzes the relationship between advertising expenditure and sales using data visualization and statistical analysis.

---

# Features

* Data preprocessing and cleaning
* Exploratory Data Analysis (EDA)
* Correlation analysis using heatmap
* Data visualization using pairplots
* Linear Regression model training
* Model performance evaluation using metrics
* Sales prediction visualization

---

#Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn

---

#Project Structure

AdvertismentPredictor
│
├── Advertising.csv
├── AdvertismentPredictior.py
└── README.md

---

#Dataset Description

The dataset contains advertising budgets for different media channels.

| Column    | Description                           |
| --------- | ------------------------------------- |
| TV        | Advertising budget spent on TV        |
| Radio     | Advertising budget spent on radio     |
| Newspaper | Advertising budget spent on newspaper |
| Sales     | Product sales                         |

---

#Project Workflow

1. Load dataset using Pandas
2. Clean dataset by removing unnecessary columns
3. Check missing values
4. Perform statistical analysis
5. Generate correlation heatmap
6. Visualize relationships using pairplots
7. Split dataset into training and testing sets
8. Train Linear Regression Model
9. Predict sales using the trained model
10. Evaluate model performance using:

* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* R² Score

---

#How to Run the Project

#Step 1: Install Required Libraries

  pip install pandas numpy matplotlib seaborn scikit-learn

#Step 2: Run the Python Script

  python AdvertismentPredictor.py


Make sure the dataset Advertising.csv is in the same folder as the script.

---

#Model Evaluation Metrics

The model calculates the following performance metrics:

* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* R² Score**

These metrics help evaluate how accurately the model predicts sales.

---

#Visualizations Included

* Correlation Heatmap
* Pairplot of features
* Actual vs Predicted Sales Scatter Plot

These visualizations help understand the relationship between advertising channels and sales.

---

#Applications

* Marketing budget optimization
* Sales forecasting
* Business decision making
* Data analysis learning project

---

This project is created for educational and learning purposes.