import tkinter as tk
from tkinter import messagebox
import requests
from geopy.geocoders import Nominatim

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Input Error", "Please enter a city name.")
        return

    try:
        # Geocoding to get latitude and longitude
        geolocator = Nominatim(user_agent="weather_app")
        location = geolocator.geocode(city)
        if not location:
            messagebox.showerror("Error", f"City '{city}' not found.")
            return

        latitude = location.latitude
        longitude = location.longitude

        # Open-Meteo API endpoint
        api_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"

        response = requests.get(api_url)
        data = response.json()

        if 'current_weather' in data:
            weather = data['current_weather']
            temperature = weather['temperature']
            windspeed = weather['windspeed']
            weather_info = f"Temperature: {temperature}°C\nWind Speed: {windspeed} km/h"
            result_label.config(text=weather_info)
        else:
            messagebox.showerror("Error", "Weather data not available for this location.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Setting up the GUI
root = tk.Tk()
root.title("Weather App")

frame = tk.Frame(root)
frame.pack(pady=20, padx=20)

city_label = tk.Label(frame, text="Enter City Name:")
city_label.grid(row=0, column=0, padx=5)

city_entry = tk.Entry(frame)
city_entry.grid(row=0, column=1, padx=5)

get_weather_button = tk.Button(frame, text="Get Weather", command=get_weather)
get_weather_button.grid(row=0, column=2, padx=5)

result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=20)

root.mainloop()
