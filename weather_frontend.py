import random
import requests
import tkinter as tk
from io import BytesIO
from tkinter import ttk
from PIL import Image, ImageTk
from weather_backend import get_current
from weather_backend import get_forecast

# Function to update GUI with weather data
def get_current_weather():
    current = location_entry.get()  # Get location from entry box
    data = get_current(current)  # Pass location to backend and get data
    if data:
        result_label.config(text=

            f"{data['city']}, {data['state']}\n"
            f"Current Weather on {data['date']}\n\n"
            f"Temperature:  {data['temp']} °F\n"
            f"Feels like:  {data['feelslike']} °F\n"
            f"Wind Speed:  {data['wind_s']} mph\n"
            f"Condition:  {data['condition']}\n\n"
            f"Weather Alert: {data['w_alert']}\n"
            f"Severity: {data['w_severity']}")

        # Fetch icon
        icon_url = "http:" + data['icon']
        response = requests.get(icon_url)

        if response.status_code == 200:
            image_data = response.content

        # Open and display image
        image = Image.open(BytesIO(image_data))
        photo = ImageTk.PhotoImage(image)
        icon_label.config(image=photo)
        icon_label.image = photo

    else:
        result_label.config(text="Location not found.")

def get_forecast_weather():
    forecast = location_entry.get() # Get location from entry box
    data = get_forecast(forecast)

    if data:
        result_label.config(text=

            f"{data['city']}, {data['state']}\n"
            f"Forecast for {data['fdate']}\n\n"
            f"High of: {data['ftemp_max']} °F\n"
            f"Low of: {data['ftemp_min']} °F\n"
            f"Chance of rain: {data['frain_chance']}%\n\n"
            f"Weather alert: {data['w_alert']}\n"
            f"Severity: {data['w_severity']}")

        # Fetch icon
        icon_url = "http:" + data['ficon']
        response = requests.get(icon_url)

        if response.status_code == 200:
            image_data = response.content

        # Open and display image
        image = Image.open(BytesIO(image_data))
        photo = ImageTk.PhotoImage(image)
        icon_label.config(image=photo)
        icon_label.image = photo

    else:
        result_label.config(text="Error")

# Set up GUI
root = tk.Tk()
root.title("Weather App")
root.geometry("400x500")

top_frame = tk.Frame(root)
top_frame.pack(pady=10)

# Label for area input
label = tk.Label(root, text="Enter Zip Code: ")
label.pack(pady=10)

# Entry box for zip
location_entry = tk.Entry(root)
location_entry.pack(pady=5)

# Button to check weather
check_weather_btn = ttk.Button(root, text="Check Weather", command=get_current_weather)
check_weather_btn.pack(pady=10)

# Button to check forecast
check_forecast_btn = ttk.Button(root, text="Check Forecast", command=get_forecast_weather)
check_forecast_btn.pack(pady=10)

# Label to display result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Label to display icon
icon_label = tk.Label(root, text="")
icon_label.pack(pady=10)

# Start GUI loop
root.mainloop()
