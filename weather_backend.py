import requests

# Obtain weather data
def get_location(location):
    API_TOKEN = "[Your API key here]"
    API_URL = f"http://api.weatherapi.com/v1/current.json?key={API_TOKEN}&q={str(location)}&aqi=no"
    response = requests.get(API_URL)

    if response.status_code == 200:
        data = response.json()
        return {
            "city": data["location"]["name"],
            "state": data["location"]["region"],
            "temp": data["current"]["temp_f"],
            "wind_s": data["current"]["wind_mph"],
            "condition": data["current"]["condition"]["text"],
            "feelslike": data["current"]["feelslike_f"],
            "icon": data["current"]["condition"]["icon"]
        }
    else:
        print("Error: Cannot obtain weather data.")
        return None
