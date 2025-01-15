import requests

# Function to fetch weather data from the OpenWeatherMap API
def get_weather(location, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,  # User's location input
        'appid': api_key,  # API key for authentication
        'units': 'metric',  # Use metric units (Celsius)
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
            "wind_speed": data["wind"]["speed"]
        }

        return weather

    except requests.exceptions.RequestException as e:
        return f"Error: Unable to connect to the weather service. {e}"

# Main function to interact with the user
def run_weather_bot():
    api_key = "2a4b088f68bb2a801f91bf4076d2c9aa"  # Replace with your OpenWeatherMap API key
    print("Welcome to the Weather Information Bot!")

    while True:
        location = input("Enter a city name to get the weather (or 'exit' to quit): ").strip()

        if location.lower() == 'exit' or location.lower() == 'quit':
            print("Goodbye! Have a great day!")
            break

        weather = get_weather(location, api_key)

        if isinstance(weather, dict):
            print(f"Weather in {weather['location']}:")
            print(f"Temperature: {weather['temperature']}°C")
            print(f"Description: {weather['description']}")
            print(f"Humidity: {weather['humidity']}%")
            print(f"Wind Speed: {weather['wind_speed']} m/s\n")
        else:
            print(weather)  # Display error message if not a valid response

# Run the bot
if __name__ == "__main__":
    run_weather_bot()
