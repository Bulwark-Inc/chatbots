from weather import get_weather
from utils import log_error
from config import API_KEY

def run_weather_bot():
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

            weather = get_weather(location, API_KEY, unit)
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

if __name__ == "__main__":
    try:
        run_weather_bot()
    except Exception as e:
        log_error(f"Fatal error: {e}")