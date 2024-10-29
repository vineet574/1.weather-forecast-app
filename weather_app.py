import requests

# Use your OpenWeatherMap API key
api_key = "7be4e70e671dcb65662895615d7c91a1"

# Base URL for the OpenWeatherMap API
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Input city name
city_name = input("Enter city name: ")

# Complete URL with city name and API key
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

# Send request and get response
response = requests.get(complete_url)

# Convert response to JSON
weather_data = response.json()

# Check if the city was found
if weather_data["cod"] != "404":
    main = weather_data["main"]
    temperature = main["temp"]
    pressure = main["pressure"]
    humidity = main["humidity"]
    weather_description = weather_data["weather"][0]["description"]

    # Convert temperature from Kelvin to Celsius
    temperature_celsius = temperature - 273.15

    print(f"Temperature: {temperature_celsius:.2f}°C")
    print(f"Pressure: {pressure} hPa")
    print(f"Humidity: {humidity}%")
    print(f"Description: {weather_description.capitalize()}")
else:
    print("City Not Found.")
