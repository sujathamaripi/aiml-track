import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Crop_recommendation.csv")

# Numerical columns
columns = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]

# Boxplots
df[columns].plot(
    kind="box",
    subplots=True,
    layout=(2,4),
    figsize=(12,8),
    sharex=False,
    sharey=False,
    title="Outlier Detection (Box Plot)"
)

plt.tight_layout()
plt.show()