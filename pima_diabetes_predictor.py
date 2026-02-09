import pandas as pd

# ----------------
# Data Collection
# ----------------

# Prima Indians Diabetes Dataset

# found at prima-indians-diabetes-dataset -> diabetes.csv
df = pd.read_csv("prima-indians-diabetes-dataset/diabetes.csv")

# -------------------
# Data Preprocessing
# -------------------

# Data Cleaning -------------------------------------

# Info about data

print(df.head())
print(df.info())
print(df.describe())

# missing values, noisy data (unrelated), duplicates

# Missing Values Check

print(df.isnull().sum()) # shows there are no null values in dataset, so no fix needed

# Duplicate Records Check

df = df.drop_duplicates()

# 

# Data Integration ----------------------------------

# unified dataset, already done

# Data Transformation -------------------------------

# encoding, scaling / normalisation

# Train / Test --------------------------------------