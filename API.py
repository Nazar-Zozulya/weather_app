import requests

API_key = "58cd4aa232816cd0ae10351cb15604aa"
city_name = input("Enter the city name: ")
url_api = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}"