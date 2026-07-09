import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Crop_recommendation.csv")

# Scatter Plot
plt.figure(figsize=(10,6))
sns.scatterplot(
    data=df,
    x="humidity",
    y="temperature",
    hue="label"
)

plt.title("Bivariate Analysis: Humidity vs Temperature")
plt.xlabel("Humidity")
plt.ylabel("Temperature")

plt.show()