
import streamlit as st

st.set_page_config(
    page_title="Weather Prediction ML",
    page_icon="🌦️"
)

st.title("🌦️ Weather Prediction ML")
st.write("Enter weather details to predict a weather category.")

temperature = st.number_input(
    "Temperature (°C)", min_value=-20.0, max_value=60.0, value=32.0
)

humidity = st.slider(
    "Humidity (%)", min_value=0, max_value=100, value=40
)

if st.button("Predict Weather"):
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

    distances = []
    for temp, hum, label in weather_data:
        distance = (
            ((temperature - temp) / 20) ** 2
            + ((humidity - hum) / 100) ** 2
        ) ** 0.5
        distances.append((distance, label))

    distances.sort(key=lambda item: item[0])
    votes = {}
    for distance, label in distances[:3]:
        votes[label] = votes.get(label, 0) + 1

    prediction = max(votes, key=votes.get)
    st.success(f"Predicted category: {prediction}")

st.caption("Educational demo using sample data, not a real weather forecast.")
