# Data Science Fundamentals Assessment
# Task 1: Data Science Fundamentals
# Student: Monika

import pandas as pd
from pathlib import Path
# -------------------------------------------------
# 1. DATA ACQUISITION
# -------------------------------------------------

# Load the Titanic dataset
from pathlib import Path

file_path = Path(__file__).resolve().parent / "train.csv"
df = pd.read_csv(file_path)


print("=" * 60)
print("DATA SCIENCE FUNDAMENTALS - TITANIC DATASET")
print("=" * 60)
# -------------------------------------------------
# 2. UNDERSTANDING THE DATASET
# -------------------------------------------------

print("\n1. FIRST FIVE RECORDS")
print(df.head())

print("\n2. DATASET SHAPE")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\n3. COLUMN NAMES")
print(df.columns.tolist())

print("\n4. DATA TYPES")
print(df.dtypes)

# -------------------------------------------------
# 3. DATA QUALITY CHECK
# -------------------------------------------------

print("\n5. MISSING VALUES")
print(df.isnull().sum())

print("\n6. DUPLICATE RECORDS")
print("Number of duplicates:", df.duplicated().sum())

# -------------------------------------------------
# 4. BASIC STATISTICAL ANALYSIS
# -------------------------------------------------

print("\n7. STATISTICAL SUMMARY")
print(df.describe())

# -------------------------------------------------
# 5. TARGET VARIABLE ANALYSIS
# -------------------------------------------------

print("\n8. SURVIVAL DISTRIBUTION")
print(df["Survived"].value_counts())

print("\nSurvival Percentage:")
print(df["Survived"].value_counts(normalize=True) * 100)

# -------------------------------------------------
# 6. BASIC GROUP ANALYSIS
# -------------------------------------------------

print("\n9. SURVIVAL BY SEX")
print(df.groupby("Sex")["Survived"].mean())

print("\n10. SURVIVAL BY PASSENGER CLASS")
print(df.groupby("Pclass")["Survived"].mean())

print("\n" + "=" * 60)
print("ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 60)
