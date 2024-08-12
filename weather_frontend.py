import tkinter as tk
import requests
from tkinter import ttk
from weather_backend import get_location
from PIL import Image, ImageTk
from io import BytesIO

# Function to update GUI with weather data
def update_gui():
    location = location_entry.get()  # Get location from entry box
    data = get_location(location)  # Pass location to backend and get data

    if data:
        result_label.config(text= f"Current weather in {data['city']}, {data['state']}:\n\n"
                                  f"Temperature: {data['temp']} °F\n"
                                  f"Feels like: {data['feelslike']} °F\n"
                                  f"Wind Speed: {data['wind_s']} mph\n"
                                  f"Condition: {data['condition']}\n")
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

# Set up GUI
root = tk.Tk()
root.title("Weather App")
root.geometry("400x400")

# Label for area input
label = tk.Label(root, text="Enter Zip Code: ")
label.pack(pady=10)

# Entry box for zip
location_entry = tk.Entry(root)
location_entry.pack(pady=5)

# Button to check weather
check_weather_btn = ttk.Button(root, text="Check Weather", command=update_gui)
check_weather_btn.pack(pady=20)

# Label to display result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Label to display icon
icon_label = tk.Label(root, text="")
icon_label.pack(pady=10)

# Start GUI loop
root.mainloop()
