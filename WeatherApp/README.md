# ☁️ Weather App (Tkinter + Open-Meteo API)

This is a simple yet effective desktop GUI application that shows current weather data (temperature and wind speed) based on the city you enter. The app is built using Python's `tkinter` for the interface and `geopy` + `Open-Meteo API` for location and weather data.

## 📌 Features

- User-friendly GUI with `tkinter`
- Uses `geopy` to geocode city names into latitude and longitude
- Fetches real-time weather using the **Open-Meteo API**
- Displays:
  - 🌡️ Temperature (°C)
  - 🌬️ Wind Speed (km/h)
- Handles invalid input or unavailable data with error messages

## 🚀 How to Run

1. Make sure you have Python installed (`>=3.7`).
2. Install required libraries:

   ```bash
   pip install geopy requests
3. Save the script as weather_app.py
4. Run the app:
   ```bash
   python weather_app.py
Enter any city name (e.g., "chennai", "Banglore") and click Get Weather.
##⚙️ Tech Stack
  Python

  Tkinter

  Geopy

  Open-Meteo API
