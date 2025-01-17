import requests
import datetime
from utils import log_error

cache = {}

def get_weather(location, api_key, unit="metric"):
    
    if location in cache:
        print("Using cached data...")
        return cache[location]
    
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': unit
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()

        if data["cod"] != 200:
            return f"Error: {data['message']}."

        # Extract relevant weather data
        weather = {
            "location": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
            "visibility": data.get("visibility", "N/A"),
            "wind_speed": data["wind"]["speed"],
            "sunrise": datetime.datetime.fromtimestamp(data["sys"]["sunrise"]).strftime('%H:%M:%S'),
            "sunset": datetime.datetime.fromtimestamp(data["sys"]["sunset"]).strftime('%H:%M:%S')
        }
        cache[location] = weather 
        return weather

    except requests.exceptions.RequestException as e:
        log_error(f"Connection error: {e}")
        return "Error: Unable to connect to the weather service."
    except Exception as e:
        log_error(f"Error processing weather data: {e}")
        return "Error: Unable to process weather data."
