# Data-Science-Fundamentals-Intenship
Data science fundamentals assessment - Task 1
Hands-On Data Lab Implementation

📌 Project Overview

This project is part of my Data Science with Python internship and focuses on practical data analysis using the Titanic passenger dataset.

The objective of this task was to understand and implement the complete basic data analysis workflow, including data loading, inspection, cleaning, transformation, statistical analysis, and visualization using Python.

🎯 Objectives

- Set up a Python Data Science environment
- Load and inspect a real-world dataset
- Perform data cleaning and handle missing values
- Check and handle duplicate records
- Perform data selection, filtering, sorting, and grouping
- Calculate descriptive statistics
- Create meaningful data visualizations
- Analyze relationships and patterns within the dataset

🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

📊 Dataset

The Titanic dataset contains 891 passenger records and 12 columns. The target variable is "Survived", where:

- "0" = Did not survive
- "1" = Survived

Important variables analyzed include:

- Passenger Class
- Gender
- Age
- Fare
- Survival Status

🧹 Data Cleaning

The dataset was checked for missing values and duplicate records.

- Missing "Age" values were filled using the median.
- Missing "Embarked" values were filled using the mode.
- Missing "Cabin" values were replaced with ""Unknown"".
- Duplicate records were checked.

After cleaning, the dataset contained no missing values or duplicate rows.

📈 Data Analysis & Visualization

The project includes:

- Survival distribution
- Age distribution
- Gender distribution
- Survival by gender
- Survival by passenger class
- Age distribution by survival status
- Fare distribution
- Fare comparison by survival status
- Correlation heatmap

The analysis helped identify patterns and relationships between passenger characteristics and survival outcomes.

🔍 Key Findings

- The dataset contains 891 passenger records.
- There were 314 female passengers.
- Passenger class showed a noticeable relationship with survival.
- First-class passengers had the highest observed survival rate.
- Third-class passengers had the lowest observed survival rate.
- Fare values showed considerable variation.
- Gender, passenger class, age, and fare showed noticeable associations with survival.

📁 Project Files

- "Task2_Data_Lab.ipynb" — Complete Jupyter Notebook containing the analysis, code, outputs, and visualizations.
- "README.md" — Project documentation.
- Real-World Dataset Analysis — Diabetes Disease Progression

📌 Project Overview

This project performs a complete real-world data analysis using the Diabetes Disease Progression dataset from scikit-learn.

The project covers the complete data science workflow:

Data Understanding → Data Cleaning → EDA → Visualization → Statistical Analysis → Predictive Modeling → Model Evaluation

The main objective is to identify meaningful patterns and relationships in the dataset and evaluate machine-learning models for predicting disease progression.

---

📊 Dataset

- Observations: 442
- Predictor Variables: 10
- Target Variable: Disease progression score
- Data Type: Numerical
- Problem Type: Regression

Features

- Age
- Sex
- BMI
- Blood Pressure
- S1
- S2
- S3
- S4
- S5
- S6

---

🔍 Analysis Performed

1. Data Exploration

- Dataset shape
- Data types
- Statistical summary
- Missing-value analysis
- Duplicate-record analysis

2. Data Cleaning

- Missing-value verification
- Duplicate verification
- Data-type verification
- IQR-based outlier detection

3. Exploratory Data Analysis

- Target distribution
- Feature distributions
- Feature-target relationships
- Correlation analysis
- Correlation heatmap

4. Data Visualization

The project includes:

- Histogram
- Scatter plot
- Correlation heatmap
- Correlation bar chart
- Box plots
- Actual vs Predicted plot
- Residual plot
- Feature-importance visualization

---

🤖 Predictive Modeling

Four regression models were evaluated:

1. Linear Regression
2. Ridge Regression
3. Random Forest Regression
4. Gradient Boosting Regression

Evaluation Metrics

- MAE — Mean Absolute Error
- RMSE — Root Mean Squared Error
- R² — R-squared

Best Test-Split Result

Gradient Boosting Regression

- MAE: 42.41
- RMSE: 52.31
- R²: 0.484

Five-fold cross-validation was also performed to check model stability.

---

💡 Key Findings

- BMI showed one of the strongest positive relationships with the target.
- Feature "s5" also showed a strong positive association with disease progression.
- Feature "s3" showed a negative relationship with the target.
- Gradient Boosting produced the strongest test-set performance among the evaluated models.
- The model explains a meaningful portion of target variation, but substantial variation remains unexplained.

«Correlation and feature importance indicate statistical relationships or predictive contribution; they do not establish causation.»

---

🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook

---

📁 Project Structure

Real-World-Dataset-Analysis/
│
├── real_world_dataset_analysis.ipynb
├── diabetes_dataset.csv
├── Real_World_Dataset_Analysis_Report.docx
├── requirements.txt
├── README.md
│
└── figures/
    ├── 01_target_distribution.png
    ├── 02_correlation_heatmap.png
    ├── 03_bmi_vs_target.png
    ├── 04_target_correlations.png
    ├── 05_feature_boxplots.png
    ├── 06_actual_vs_predicted.png
    ├── 07_residuals.png
    └── 08_feature_importance.png

---

▶️ How to Run

Clone the repository and install the required libraries:

pip install -r requirements.txt

Then open:

real_world_dataset_analysis.ipynb

using Jupyter Notebook or JupyterLab and run the cells.

---

📚 Dataset Source

The dataset is the Diabetes dataset provided by scikit-learn, originally derived from a study of diabetes progression.

Dataset documentation:
https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html

---

👩‍💻 Author

Monika

B.Tech CSE — AI/ML

Data Science Tool Mastery Project

📌 Project Overview

This project demonstrates practical proficiency with key Data Science tools and libraries through an integrated Wine Classification and Exploratory Data Analysis workflow.

The project combines NumPy, Pandas, Matplotlib, Seaborn, and Scikit-learn to demonstrate how different Data Science tools work together in a complete analysis and machine learning pipeline.

🎯 Objectives

- Master commonly used Data Science tools and libraries.
- Perform practical data analysis using Python.
- Create meaningful data visualizations.
- Apply machine learning algorithms using Scikit-learn.
- Evaluate and compare machine learning models.
- Build a portfolio-ready Data Science project.

📊 Dataset

The project uses the Wine Dataset available through Scikit-learn.

- Samples: 178
- Features: 13
- Target Classes: 3
- Task: Multiclass Classification

The dataset contains chemical measurements of wine samples belonging to three different classes.

🛠️ Tools & Technologies

NumPy

Used for:

- Numerical array operations
- Mean and standard deviation calculations
- Vectorized operations
- Feature standardization

Pandas

Used for:

- Data loading and inspection
- Data cleaning
- Descriptive statistics
- Filtering and sorting
- Grouping and aggregation

Matplotlib

Used for:

- Bar charts
- Histograms
- Scatter plots
- Box plots
- Model comparison charts

Seaborn

Used for:

- Statistical visualizations
- Distribution plots
- Scatter plots
- Correlation heatmap

Scikit-learn

Used for:

- Train-test splitting
- Feature scaling
- Logistic Regression
- Random Forest Classification
- Model evaluation
- Cross-validation
- Confusion matrix analysis

🔍 Exploratory Data Analysis

The project includes:

- Dataset structure and statistical summary
- Missing-value analysis
- Duplicate-value analysis
- Class distribution
- Feature distributions
- Correlation analysis
- Relationship between important features
- Outlier/distribution analysis
- Feature contribution analysis

🤖 Machine Learning Models

Two classification models were implemented:

1. Logistic Regression
2. Random Forest Classifier

Model Performance

Model| Accuracy| Precision| Recall| F1 Score
Random Forest| 1.000| 1.000| 1.000| 1.000
Logistic Regression| 0.972| 0.974| 0.972| 0.972

Five-fold stratified cross-validation was also performed to obtain a more reliable performance estimate.

📈 Visualizations

The project contains visualizations including:

- Wine Class Distribution
- Alcohol Distribution
- Feature Correlation Heatmap
- Alcohol vs Flavanoids Scatter Plot
- Color Intensity Box Plot
- Confusion Matrix
- Feature Contribution
- Model Comparison

📁 Project Structure

Data-Science-Tool-Mastery/
│
├── data_science_tool_mastery.ipynb
├── wine_dataset.csv
├── Data_Science_Tool_Mastery_Report.docx
├── TuteDude_200_Word_Description.txt
├── requirements.txt
├── README.md
│
└── figures/
    ├── 01_class_distribution.png
    ├── 02_alcohol_distribution.png
    ├── 03_correlation_heatmap.png
    ├── 04_alcohol_vs_flavanoids.png
    ├── 05_color_intensity_boxplot.png
    ├── 06_confusion_matrix.png
    ├── 07_feature_importance.png
    └── 08_model_comparison.png

▶️ How to Run

Clone the repository and install the required libraries:

pip install -r requirements.txt

Then open:

data_science_tool_mastery.ipynb

using Jupyter Notebook or JupyterLab.

💡 Key Learnings

This project provided practical experience in:

- Numerical computation with NumPy
- Data manipulation with Pandas
- Data visualization with Matplotlib and Seaborn
- Machine learning with Scikit-learn
- Model evaluation and comparison
- Cross-validation
- Interpreting data patterns and model results
- Building a reproducible Data Science workflow

⚠️ Limitations

The Wine dataset is relatively small and is commonly used as a benchmark dataset. Therefore, the model results should not automatically be interpreted as production-level performance.

Feature importance indicates model-specific contribution and does not imply causation. Further experimentation with additional datasets, models, hyperparameter tuning, and external validation could extend this project.
📚 Dataset Source
Scikit-learn Wine Dataset:
https://scikit-learn.org/stable/datasets/toy_dataset.html#wine-dataset
👩‍💻 Author
Monika
B.Tech CSE — AI/ML


