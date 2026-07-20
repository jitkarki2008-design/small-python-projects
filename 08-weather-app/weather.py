# 08 - Weather App using API + requests (no API key needed)
import requests

def get_weather(city):
    try:
        # wttr.in is a free weather API, returns JSON
        # format=j1 means JSON format
        url = f"https://wttr.in/{city}?format=j1"
        response = requests.get(url, timeout=10)

        if response.status_code!= 200:
            print(f"Error: City not found or API issue ({response.status_code})")
            return

        data = response.json()

        # current_condition is list with 1 item
        current = data['current_condition'][0]
        nearest = data['nearest_area'][0]

        location = f"{nearest['areaName'][0]['value']}, {nearest['country'][0]['value']}"
        temp = current['temp_C']
        feels = current['FeelsLikeC']
        desc = current['weatherDesc'][0]['value']
        humidity = current['humidity']
        wind = current['windspeedKmph']

        print("\n--- Weather Report ---")
        print(f"Location: {location}")
        print(f"Temperature: {temp}°C (Feels like {feels}°C)")
        print(f"Condition: {desc}")
        print(f"Humidity: {humidity}%")
        print(f"Wind: {wind} km/h")

    except requests.exceptions.ConnectionError:
        print("No internet! Check your connection.")
    except Exception as e:
        print(f"Error: {e}")

print("--- Weather App [requests + API] ---")
while True:
    city = input("\nEnter city (or 'exit'): ").strip()
    if city.lower() == 'exit':
        break
    if city == "":
        continue
    get_weather(city)