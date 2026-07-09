import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Crop_recommendation.csv")

# Create histograms
df.hist(figsize=(12,8), bins=20)

plt.tight_layout()
plt.show()