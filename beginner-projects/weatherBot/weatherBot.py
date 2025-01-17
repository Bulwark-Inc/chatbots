import requests
import datetime

cache = {}

def log_error(error_message):
    with open("error_log.txt", "a") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp} - {error_message}\n")

# Function to fetch weather data from the OpenWeatherMap API
def get_weather(location, api_key, unit="metric"):
    if location in cache:
        print("Using cached data...")
        return cache[location]

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,  # User's location input
        'appid': api_key,  # API key for authentication
        'units': unit,  # Use metric units (Celsius)
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()

        # Check if the API response is valid
        if data["cod"] != 200:
            return f"Error: {data['message']}. Please try again."
        
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
        return f"Error: Unable to connect to the weather service. {e}"

# Main function to interact with the user
def run_weather_bot():
    api_key = "2a4b088f68bb2a801f91bf4076d2c9aa"  # Replace with your OpenWeatherMap API key
    print("Welcome to the Weather Information Bot!")

    unit = "metric"  # Default unit
    while True:
        print("\nOptions:")
        print("1. Get weather information")
        print("2. Change temperature unit (Celsius/Fahrenheit)")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice.lower() == 'exit' or choice.lower() == 'quit':
            print("Goodbye! Have a great day!")
            break

        if choice == "1":
            location = input("Enter a city name: ").strip()

            weather = get_weather(location, api_key, unit)
            if isinstance(weather, dict):
                print(f"\nWeather in {weather['location']}:")
                print(f"Temperature: {weather['temperature']}°{'C' if unit == 'metric' else 'F'}")
                print(f"Description: {weather['description']}")
                print(f"Humidity: {weather['humidity']}%")
                print(f"Wind Speed: {weather['wind_speed']} m/s")
                print(f"Pressure: {weather['pressure']} hPa")
                print(f"Visibility: {weather['visibility']} meters")
                print(f"Sunrise: {weather['sunrise']}")
                print(f"Sunset: {weather['sunset']}")
            else:
                print(weather)

        elif choice == "2":
            print("Current unit: Celsius" if unit == "metric" else "Current unit: Fahrenheit")
            unit_choice = input("Enter 'C' for Celsius or 'F' for Fahrenheit: ").strip().upper()
            if unit_choice == "C":
                unit = "metric"
                print("Temperature unit set to Celsius.")
            elif unit_choice == "F":
                unit = "imperial"
                print("Temperature unit set to Fahrenheit.")
            else:
                print("Invalid choice. Unit not changed.")

        elif choice == "3":
            print("Goodbye! Have a great day!")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")


# Run the bot
if __name__ == "__main__":
    run_weather_bot()
