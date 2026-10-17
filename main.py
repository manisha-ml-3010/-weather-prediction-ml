
# Weather Prediction using Machine Learning

weather_data = [
    (32, 40, "Sunny"),
    (30, 45, "Sunny"),
    (28, 50, "Sunny"),
    (24, 60, "Cloudy"),
    (22, 65, "Cloudy"),
    (26, 70, "Cloudy"),
    (20, 90, "Rainy"),
    (23, 95, "Rainy"),
    (25, 85, "Rainy")
]

def predict_weather(temperature, humidity):
    distances = []

    for temp, hum, label in weather_data:
        distance = (
            ((temperature - temp) / 20) ** 2
            + ((humidity - hum) / 100) ** 2
        ) ** 0.5

        distances.append((distance, label))

    distances.sort(key=lambda item: item[0])
    nearest = distances[:3]

    votes = {}
    for distance, label in nearest:
        votes[label] = votes.get(label, 0) + 1

    return max(votes, key=votes.get)


print("=== Weather Prediction ML ===")

try:
    temperature = float(input("Enter temperature (C): "))
    humidity = float(input("Enter humidity (%): "))

    if not 0 <= humidity <= 100:
        print("Humidity must be between 0 and 100.")
    else:
        result = predict_weather(temperature, humidity)
        print("Predicted weather:", result)

except ValueError:
    print("Please enter valid numbers.")
  
