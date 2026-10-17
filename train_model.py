
# Train a Weather Prediction ML Model

import pickle
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Sample training dataset
X = [
    [32, 40], [30, 45], [28, 50],
    [34, 35], [31, 42], [29, 48],
    [24, 60], [22, 65], [26, 70],
    [25, 62], [23, 68], [27, 66],
    [20, 90], [23, 95], [25, 85],
    [18, 92], [21, 88], [24, 91],
]

y = [
    "Sunny", "Sunny", "Sunny",
    "Sunny", "Sunny", "Sunny",
    "Cloudy", "Cloudy", "Cloudy",
    "Cloudy", "Cloudy", "Cloudy",
    "Rainy", "Rainy", "Rainy",
    "Rainy", "Rainy", "Rainy",
]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# Create and train the ML model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# Evaluate the model
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print("Weather Prediction Model Trained!")
print(f"Test accuracy: {accuracy:.2%}")

# Save the trained model
with open("weather_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved as weather_model.pkl")
