import json, requests

api_key = "2dec2adfa6d7b066a1e11e5aa983c182"

def weather(city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)

    x = response.json()

    if x["cod"] != "404":
        y = x["main"]
        z = x["weather"]

        temp = y["temp"] - 273.1 # Celcius
        desc = z[0]["description"]
        pressure = y["pressure"]
        humidity = y["humidity"]

        return temp, desc, humidity, pressure

    else:
        print(" City Not Found ")
