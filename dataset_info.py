import pandas as pd

# Load dataset
df = pd.read_csv("Crop_recommendation.csv")

# Shape of dataset
print(df.shape)

# Dataset information
df.info()

# Statistical summary
print(df.describe())

# Missing values
print(df.isnull().sum())