import requests

API_KEY = input("Enter your OpenWeatherMap API key: ")
URL = "https://api.openweathermap.org/data/2.5/weather"

while True:
    city = input("\nEnter city name (or 'exit'): ").strip()

    if city.lower() == "exit":
        print("Weather App closed.")
        break

    if not city:
        print("Error: City name cannot be empty.")
        continue

    try:
        r = requests.get(URL, params={
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }, timeout=10)

        if r.status_code == 401:
            print("Error: Invalid API key.")
            print("Please check your OpenWeatherMap API key.")
            continue

        if r.status_code == 404:
            print("Error: City not found.")
            continue

        r.raise_for_status()
        data = r.json()

        c = data["main"]["temp"]
        f = c * 9 / 5 + 32

        print("\n--- Weather Report ---")
        print("City:", data["name"])
        print(f"Temperature: {c:.1f} °C")
        print(f"Temperature: {f:.1f} °F")
        print("Humidity:", data["main"]["humidity"], "%")
        print("Condition:", data["weather"][0]["description"].title())
        print("Wind Speed:", data["wind"]["speed"], "m/s")

    except requests.exceptions.Timeout:
        print("Error: Network timeout.")

    except requests.exceptions.RequestException:
        print("Error: Unable to connect to weather service.")