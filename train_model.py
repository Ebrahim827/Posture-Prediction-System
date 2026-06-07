import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

print("Loading data...")

df = pd.read_csv("posture_data.csv")

# Create features
df["Avg10"] = df["Distance"].rolling(10).mean()
df["Avg30"] = df["Distance"].rolling(30).mean()

df["Trend10"] = df["Distance"] - df["Distance"].shift(10)
df["Trend30"] = df["Distance"] - df["Distance"].shift(30)

# Create future-risk labels
future_window = 30

labels = []

for i in range(len(df)):

    future = df["Distance"].iloc[i+1:i+future_window+1]

    if len(future) < future_window:
        labels.append(None)
        continue

    if (future < 50).any():
        labels.append(1)
    else:
        labels.append(0)

df["Label"] = labels

df.dropna(inplace=True)

X = df[
    [
        "Distance",
        "Avg10",
        "Avg30",
        "Trend10",
        "Trend30"
    ]
]

y = df["Label"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print()
print("MODEL TRAINED")
print("------------------")
print(f"Accuracy: {accuracy*100:.2f}%")

joblib.dump(model, "posture_model.pkl")

print("Model saved as posture_model.pkl")