from geopy import Nominatim
import requests
import json

def get_lat_long(city):
    """ Get longitude and latitude based on City input

    Args:
        city (string): Needed to query geocoding service

    Returns:
        tuple: latitude, longitude
    """
    loc = Nominatim(user_agent="GetLoc")
    get_loc = loc.geocode(city)
    return (get_loc.latitude, get_loc.longitude)


def get_weather(lat,long):
    """ Get current weather and forecast for location

    Args:
        lat (num): geographic latitude
        long (num): geographic longitude

    Returns:
        json: json string that contains current weather and forecast
    """
    httpreq = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&hourly=temperature_2m,precipitation_probability&current_weather=true"
    response = requests.get(httpreq)
    return response.content



city = input("please enter a city: ")
content = get_weather(*get_lat_long(city))

with open("forecast.txt", 'wb+') as file:
    file.write(content)
    


with open("forecast.txt", 'r') as file:
    content = file.read()
    
parsed = json.loads(content)
print(parsed["current_weather"])