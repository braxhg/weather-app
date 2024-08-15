import requests

def get_location_data(data):
    
    return {

        "city": data["location"]["name"],
        "state": data["location"]["region"]
    }

# Obtain weather data
def get_current(current):
    API_TOKEN = "18550c6d76c64aef84a55339240308"
    API_URL = f"http://api.weatherapi.com/v1/current.json?key={API_TOKEN}&q={str(current)}&aqi=no"
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
            "icon": data["current"]["condition"]["icon"]
        }
    else:
        print("Error: Cannot obtain weather data.\nStatus code: ", response.status_code)
        return None

def get_forecast(forecast):
    API_TOKEN = "18550c6d76c64aef84a55339240308"
    API_URL = f"http://api.weatherapi.com/v1/forecast.json?key={API_TOKEN}&q={str(forecast)}&days=2&aqi=no&alerts=yes"
    response = requests.get(API_URL)

    if response.status_code == 200:
        data = response.json()
        #print("Forecast data: ", data)
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
    
# Test block to run the functions directly
"""
if __name__ == "__main__":
    print("Testing get_current:")
    current_weather = get_current("29108")  # Replace "10001" with any valid zip code or location
    print("Output of get_current:", current_weather)

    print("\nTesting get_forecast:")
    forecast_weather = get_forecast("29108")  # Replace "10001" with any valid zip code or location
    print("Output of get_forecast:", forecast_weather)
"""
