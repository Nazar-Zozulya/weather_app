# from bigscreen.create_window import *
# from bigscreen.registration_window import *
# # import registration.registration_window              
# from bigscreen.time_api import *                                                                                        
# Register()

import customtkinter as tk
import sqlite3
import os
import requests
import json
from PIL import Image
from bigscreen.time_api import *
from bigscreen.create_window import *
from bigscreen.registration_window import *




db = sqlite3.connect('user_data.db')

pen = db.cursor()

pen.execute("SELECT rowid, * FROM users")

for i in pen:
    country = i[1]
    city = i[2]
    name = i[3]
    surname = i[4]


API_KEY = 'c3c7dd0d8e63c30b03f32d8c5b575f19'

cities = ["Київ", "Рим", "Лондон", "Варшава", "Прага"]


url_api_pointed = f"https://api.openweathermap.org/data/2.5/weather?q={"Dnipro"}&appid={API_KEY}&lang=uk&units=metric"
response_pointed = requests.get(url_api_pointed)

url_api_kyiv = f"https://api.openweathermap.org/data/2.5/weather?q={cities[0]}&appid={API_KEY}&lang=uk&units=metric"
url_api_rym = f"https://api.openweathermap.org/data/2.5/weather?q={cities[1]}&appid={API_KEY}&lang=uk&units=metric"
url_api_london = f"https://api.openweathermap.org/data/2.5/weather?q={cities[2]}&appid={API_KEY}&lang=uk&units=metric"
url_api_varchava = f"https://api.openweathermap.org/data/2.5/weather?q={cities[3]}&appid={API_KEY}&lang=uk&units=metric"
url_api_praga= f"https://api.openweathermap.org/data/2.5/weather?q={cities[4]}&appid={API_KEY}&lang=uk&units=metric"


kyiv_response = requests.get(url_api_kyiv)
rym_response = requests.get(url_api_rym)
london_response = requests.get(url_api_london)
varchava_response = requests.get(url_api_varchava)
praga_response = requests.get(url_api_praga)

# pen.execute("""CREATE TABLE IF NOT EXISTS users (
#         country TEXT,
#         city TEXT,
#         name TEXT,
#         surname TEXT
# )""")

Register().mainloop()

# if go_to_main == True:
#     App().mainloop()
#     go_to_main = False