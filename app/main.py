import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
CITY = "Paris"
URL = f"http://api.weatherapi.com/v1/current.json" \
      f"?key={API_KEY}&q={CITY}&aqi=no"


def get_weather() -> None:
    print(f"Performing request to Weather API for city {CITY}...")

    response = requests.get(URL)
    if response.status_code != 200:
        print("Failed to get weather data.")
        return

    data = response.json()

    location = data["location"]["name"]
    country = data["location"]["country"]
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    localtime = data["location"]["localtime"]

    print(f"{location}/{country} {localtime}"
          f" Weather: {temp_c} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
