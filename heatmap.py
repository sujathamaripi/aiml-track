import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Crop_recommendation.csv")

# Select only numeric columns
numeric_df = df.select_dtypes(include=["number"])

# Correlation matrix
corr = numeric_df.corr()

# Plot heatmap
plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap="Blues")

plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()