import datetime as dt
import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "c8ec093ab26de351de94387d6d3821d9"
CITY = "London"

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
response = requests.get(url).json()

temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)

temp_feels_like = response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(temp_feels_like)
wind = response['wind']['speed']
humidity = response['main']['humidity']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])


print(f"Temprature in {CITY} feels like : {temp_celsius:.2f}*C OR {temp_fahrenheit:.2f} F")
print(f"Temprature in {CITY}: {temp_celsius:.2f}*C OR {temp_fahrenheit:.2f} F")
print(f"Humidity in {CITY}: {humidity}%")
print(f"Sun rises in {CITY} at {sunrise_time} local")
print(f"Sun sets in {CITY} at {sunset_time} local")