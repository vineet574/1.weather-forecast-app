# Weather Forecasting App

A simple command-line weather forecasting application that provides real-time weather data for a specified city. This app uses the OpenWeatherMap API to fetch weather information such as temperature, pressure, humidity, and weather description.

## Features
- Fetches current weather information for any city.
- Displays temperature, atmospheric pressure, humidity, and weather conditions.
- Simple and user-friendly command-line interface.

## Technologies Used
- Python
- OpenWeatherMap API

## Setup Instructions

### Prerequisites
- Python 3.x installed on your system
- `requests` library (install with `pip install requests`)

### Getting Started
1. Clone this repository or download the code files.
2. Sign up on [OpenWeatherMap](https://home.openweathermap.org/users/sign_up) and obtain an API key.
3. Open the `weather_app.py` file and replace `YOUR_API_KEY` with your actual API key.

   ```python
   api_key = "YOUR_API_KEY"


Installation
Install the requests library by running:


pip install requests

Running the App
Open a terminal or command prompt.

Navigate to the directory where the weather_app.py file is located.
Run the application with the following command:


python weather_app.py
Enter the city name when prompted to get the current weather information.
Example Output
plaintext
Copy code
Enter city name: London
Temperature: 13.83°C
Pressure: 1024 hPa
Humidity: 93%
Description: Overcast clouds
Usage
Enter the name of any city to get its weather data.
View details like temperature (in Celsius), pressure, humidity, and a brief description of the weather.
Limitations
This app currently displays temperature in Celsius only.
Requires an active internet connection to fetch data from the OpenWeatherMap API.
