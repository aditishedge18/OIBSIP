import requests

print("================================")
print("       WEATHER APPLICATION      ")
print("================================")

api_key = "bd547519a8c95ae8e712f4c47700f601"

city = input("\nEnter city name: ")

url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_key + "&units=metric"

response = requests.get(url)

data = response.json()

if str(data["cod"]) == "200":

    city_name = data["name"]
    country = data["sys"]["country"]

    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]

    weather = data["weather"][0]["main"]

    print("\n========== WEATHER DETAILS ==========")

    print("City:", city_name)
    print("Country:", country)

    print("Temperature:", temperature, "°C")
    print("Humidity:", humidity, "%")

    print("Weather:", weather)

    print("=====================================")

else:
    print("\nCity not found")