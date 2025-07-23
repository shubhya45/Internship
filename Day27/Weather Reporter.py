# Weather Reporter
# API: https://api.open-meteo.com/v1/forecast
# Goal: Input a city’s latitude/longitude → Get current temperature.

# If temp > 30°C → print “It’s hot!”

# If temp < 15°C → print “It’s cold!”

import requests

lat = 19.9975
lon = 73.7898

url = "https://api.open-meteo.com/v1/forecast"f"?latitude={lat}&longitude={lon}""&current=temperature_2m"


response = requests.get(url)
data = response.json()

temp = data["current"]["temperature_2m"]
print("Temperature:", temp, "°C")

if temp > 30:
    print("It’s hot!")
if temp < 15:
    print("It’s cold!")