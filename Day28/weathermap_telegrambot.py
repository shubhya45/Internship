import requests

# -------- CONFIG --------
CITY = "Igatpuri"
OPENWEATHER_API_KEY = "223feb02434cd47149516a0680fb8526"  # Replace with your OpenWeather API key
TEMP_THRESHOLD = 30  # Celsius

# -------- STEP 1: Get Weather Data --------
weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={OPENWEATHER_API_KEY}"

response = requests.get(weather_url)
data = response.json()

# Extract temperature in Celsius
temp_kelvin = data["main"]["temp"]
temp_celsius = temp_kelvin - 273.15

print(f"Current temperature in {CITY}: {temp_celsius:.2f}°C")

if temp_celsius > TEMP_THRESHOLD:
    message = f"🌡️ Alert! Current temperature in {CITY} is {temp_celsius:.2f}°C, which is above {TEMP_THRESHOLD}°C."

else:
    print("✅ Temperature is normal. No alert needed.")
