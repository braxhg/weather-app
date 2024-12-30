import requests
from api import define_api

api_key = define_api()

def get_location_data(data):
    
    # Access alerts field
    alerts = data.get("alerts", {}).get("alert", [])
    
    if alerts:
        a_event = alerts[0].get("event", "No weather alert.")
        a_severity = alerts[0].get("severity", "")
    else:
        a_event = "No alerts"
        a_severity = "N/A"
    
    return {

        "city": data["location"]["name"],
        "state": data["location"]["region"],
        "w_alert": a_event,
        "w_severity": a_severity
    }

# Obtain weather data
def get_current(current):
    API_URL = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={str(current)}&aqi=no"
    response = requests.get(API_URL)

    if response.status_code == 200:
        data = response.json()
        #print("Current weather data: ", data) # Debug
        location_data = get_location_data(data)
        date_only = data["location"]["localtime"].split(" ")[0]
        #print("Parsed data: ", date_only) # Debug

        return {

            **location_data,
            "date": date_only,
            "temp": data["current"]["temp_f"],
            "wind_s": data["current"]["wind_mph"],
            "condition": data["current"]["condition"]["text"],
            "feelslike": data["current"]["feelslike_f"],
            "icon": data["current"]["condition"]["icon"],
            "status": data["current"]["condition"]["text"]
        }
    else:
        print("Error: Cannot obtain weather data.\nStatus code: ", response.status_code)
        return None

def get_forecast(forecast):
    API_URL = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={str(forecast)}&days=2&aqi=no&alerts=yes"
    response = requests.get(API_URL)

    if response.status_code == 200:
        data = response.json()
        #print("Forecast data: ", data) # Debug
        location_data = get_location_data(data)
        date_only = data["forecast"]["forecastday"][1]["date"].split(" ")[0]
        #print("Parsed data: ", date_only) # Debug

        return {

            **location_data,
            "fdate": date_only,
            "ftemp_max": data["forecast"]["forecastday"][1]["day"]["maxtemp_f"],
            "ftemp_min": data["forecast"]["forecastday"][1]["day"]["mintemp_f"],
            "ficon": data["forecast"]["forecastday"][1]["day"]["condition"]["icon"],
            "frain_chance": data["forecast"]["forecastday"][1]["day"]["daily_chance_of_rain"]
        }
    else:
        print("Error: Cannot obtain weather data.\nStatus code: ", response.status_code)
        return None
    
