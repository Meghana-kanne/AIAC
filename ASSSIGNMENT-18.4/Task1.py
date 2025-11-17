import sys
import requests
import json

# Task1.py
# Simple function to fetch and display weather details of a city as JSON using OpenWeatherMap API
# No error handling included (per request)


def display_weather(city: str, api_key: str, units: str = "metric") -> None:
    """
    Fetches current weather for `city` from OpenWeatherMap and prints JSON output.
    Example units: "metric", "imperial", or "standard".
    """
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": units}
    response = requests.get(url, params=params)
    # display the JSON response from the API
    print(json.dumps(response.json(), indent=2))

if __name__ == "__main__":
    # Usage: python Task1.py "City Name" YOUR_API_KEY
    if len(sys.argv) >= 3:
        city_arg = sys.argv[1]
        key_arg = sys.argv[2]
        display_weather(city_arg, key_arg)
    else:
        # fallback interactive prompt (still no error handling)
        city_arg = input("City: ").strip()
        key_arg = input("OpenWeatherMap API Key: ").strip()
        display_weather(city_arg, key_arg)