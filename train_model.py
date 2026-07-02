import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load Dataset
data = pd.read_csv("Crop_recommendation.csv")

# Split Features and Label
X = data.drop("label", axis=1)
y = data["label"]

# Train Model
model = RandomForestClassifier()
model.fit(X, y)

# Save Model
pickle.dump(model, open("model.pkl", "wb"))

print("Model Trained Successfully!")