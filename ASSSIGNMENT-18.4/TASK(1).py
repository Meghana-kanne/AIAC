def display_weather_json():
    import requests
    import json

    api_key = input("Enter your OpenWeatherMap API key: ")
    city = input("Enter city name: ")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    print(json.dumps(data, indent=4))

display_weather_json()
