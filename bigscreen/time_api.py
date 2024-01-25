import customtkinter as tk
import sqlite3
import os
import requests
import json
from PIL import Image


db = sqlite3.connect('user_data.db')

pen = db.cursor()

pen.execute("SELECT rowid, * FROM users")

for i in pen:
    country = i[1]
    city = i[2]
    name = i[3]
    surname = i[4]

API_KEY = "EjK/pUSceurGv/tpIUDq9w==16ZFRu2PDzMdu8B6"

pointed_api_url = api_url_kyiv = f'https://api.api-ninjas.com/v1/worldtime?city=Dnipro'
pointed_response = requests.get(pointed_api_url, headers={'X-Api-Key': API_KEY})

api_url_kyiv = f'https://api.api-ninjas.com/v1/worldtime?city=Київ&lang=ua'
kyiv_response = requests.get(api_url_kyiv, headers={'X-Api-Key': API_KEY})

api_url_rym = f'https://api.api-ninjas.com/v1/worldtime?city=Рим'
rym_response = requests.get(api_url_rym, headers={'X-Api-Key': API_KEY})

api_url_london = f'https://api.api-ninjas.com/v1/worldtime?city=Лондон'
london_response = requests.get(api_url_london, headers={'X-Api-Key': API_KEY})

api_url_varshava = f'https://api.api-ninjas.com/v1/worldtime?city=Варшава'
varshava_response = requests.get(api_url_varshava, headers={'X-Api-Key': API_KEY})

api_url_praga = f'https://api.api-ninjas.com/v1/worldtime?city=Прага'
praga_response = requests.get(api_url_praga, headers={'X-Api-Key': API_KEY})


kyiv_hour = kyiv_response.json()["hour"]
kyiv_minute = kyiv_response.json()["minute"]

rym_hour = rym_response.json()["hour"]
rym_minute = rym_response.json()["minute"]

london_hour = london_response.json()["hour"]
london_minute = london_response.json()["minute"]

varchava_hour = varshava_response.json()["hour"]
varchava_minute = varshava_response.json()["minute"]

praga_hour = praga_response.json()["hour"]
praga_minute = praga_response.json()["minute"]


pointed_day_of_week = pointed_response.json()["day_of_week"]
pointed_date = pointed_response.json()["date"]
pointed_hour = pointed_response.json()["hour"]
pointed_minute = pointed_response.json()["minute"]

if kyiv_response.status_code == requests.codes.ok:
    print(kyiv_response.text)
else:
    print("Error:", kyiv_response.status_code, kyiv_response.text)