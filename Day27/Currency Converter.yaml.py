# Currency Converter
# API: https://api.exchangerate-api.com/v4/latest/USD
# Goal: Convert a given amount in INR to USD, EUR, etc.
import requests

response = requests.get("https://api.exchangerate-api.com/v4/latest/INR")
data = response.json()

print("Exchange rates for INR:")
for currency, rate in data["rates"].items():
    print(f"1 INR = {rate} {currency}")

amount_in_inr = 45
print(f"\nConverting {amount_in_inr} INR:")
for currency, rate in data["rates"].items():
    converted_amount = amount_in_inr * rate
    print(f"{amount_in_inr} INR = {converted_amount:.2f} {currency}")