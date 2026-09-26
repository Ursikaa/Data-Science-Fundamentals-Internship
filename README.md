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


