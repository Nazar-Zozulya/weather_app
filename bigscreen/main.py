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
from time_api import *


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



class Account(tk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry("460x645")
        self.title("Регистрація")
        self.resizable(False, False)
        self.config(bg="#5DA7B1",)
        
        # if pen is not None:


        pen.execute("SELECT rowid, * FROM users")        # ]
        for i in pen:
            country = i[1]
            city = i[2]
            name = i[3]
            surname = i[4]

        # self.city_image_path = os.path.join(os.path.dirname(__file__), 'icon\user.png')

        self.image_path = os.path.join(os.path.dirname(__file__), 'icon\\left-arrow.png')
        self.image = tk.CTkImage(light_image= Image.open(self.image_path), size=(50,50),)
        # self.image.grid(row=0,column=0, padx=100)
        self.image_label = tk.CTkLabel(self, image=self.image,fg_color="#5DA7B1", text=' ')
        self.image_label.grid(row=0,column=0, padx=400,sticky='ne'), 
        self.text_label = tk.CTkLabel(self, fg_color="#5DA7B1", text='Вихід',bg_color='#5DA7B1',font = ("Roboto Slab", 16))
        self.text_label.grid(row=0,column=0, padx=363,pady=10,sticky='wn')
        self.title = tk.CTkLabel(self, text = "Особистий кабінет", font = ("Inter", 28), fg_color = "#5DA7B1", width=100)
        self.title.grid(row=0, column=0, padx=112, pady=65, sticky='wn')
        
        self.fields = tk.CTkButton(self, fg_color = "#5DA7B1", width = 400, height = 40, text='', hover_color='#5DA7B1',bg_color='#5DA7B1')
        self.fields.grid(row=0, column=0, padx=20, pady=(100,0), sticky="wn")


        self.country_text = tk.CTkLabel(self.fields, text = "Країна:", font = ("Roboto Slab", 22))
        self.country_text.grid(row=0, column=0,padx=14,pady=10,sticky='wn')

        self.country_field= tk.CTkLabel(self.fields,
                                width = 218,
                                height = 46, 
                                fg_color = "#5DA7B1",
                                text= f"{country}",
                                font = ("Roboto Slab", 28)
                                )
        
        self.country_field.grid(row=0, column=0,padx=20,pady=40,sticky='wn')

        self.city_text = tk.CTkLabel(self.fields, text = "Місто:", font = ("Roboto Slab", 22))
        self.city_text.grid(row=0, column=0,padx=14,pady=10+90,sticky='wn')

        self.city_field= tk.CTkLabel(self.fields,
                                width = 218,
                                height = 46, 
                                fg_color = "#5DA7B1",
                                text = f'{city}',
                                font = ("Roboto Slab", 28)
                                )
        
        self.city_field.grid(row=0, column=0,padx=20,pady=40+90,sticky='wn')




        self.name_text = tk.CTkLabel(self.fields, text = "Ім'я:", font = ("Roboto Slab", 22))
        self.name_text.grid(row=0, column=0,padx=14,pady=10+180,sticky='wn')

        self.name_field= tk.CTkLabel(self.fields,
                                width = 218,
                                height = 46, 
                                fg_color = "#5DA7B1",
                                text= f"{name}",
                                font = ("Roboto Slab", 28)
                                )
        
        self.name_field.grid(row=0, column=0,padx=20,pady=40+180,sticky='wn')
                                
        self.surname_text = tk.CTkLabel(self.fields, text = "Прізвище:", font = ("Roboto Slab", 22))
        self.surname_text.grid(row=0, column=0,padx=14,pady=10+270,sticky='wn')

        self.surname_field= tk.CTkLabel(self.fields,
                                width = 218,
                                height = 46, 
                                fg_color = "#5DA7B1",
                                text= f"{surname}",
                                font = ("Roboto Slab", 28)
                                )
        
        self.surname_field.grid(row=0, column=0,padx=20,pady=40+270,sticky='wn')

        self.save_button = tk.CTkButton(self, fg_color = "#096C82", width = 218, height = 39, text='Перейти до додатку', hover_color='#074A59',bg_color='#5DA7B1',border_color='white',border_width=2,corner_radius=15, font = ("Roboto Slab", 18),)
        self.save_button.grid(row=0, column=0, padx=115, pady=(530,0), sticky="wn")

























































class App(tk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("1200x800")
        self.title("Wether")
        self.resizable(False, False)
        self.config(bg="#5DA7B1",)

        self.side_frame = tk.CTkFrame(self, 
                                width = 275, 
                                height = 800, 
                                fg_color = "#096C82", 
                                bg_color="#096C82",
                                corner_radius=0,                              
                                )
        self.side_frame.grid(row = 0, column = 0,padx=0,pady=0, sticky='wn')

        self.border_frame = tk.CTkFrame(self, 
                                width =2, 
                                height=800,
                                fg_color='#FFFFFF',
                                bg_color='#FFFFFF',
                                corner_radius=0,
                                #    border_color='white',
                                    )
        self.border_frame.grid(row = 0, column = 1,padx=1,sticky='n')

        self.pointed_minidate = tk.CTkButton(self.side_frame,
                                    text=' ',
                                    width = 236,
                                    height = 101,
                                    hover_color='#4599A4',
                                    fg_color = "#4599A4",
                                    border_color = 'white',
                                    border_width=2.5,
                                    corner_radius=20
                                    )
        self.pointed_minidate.grid(row = 0, column = 0, padx = 10, pady = 10,sticky='n')

        self.title1 = tk.CTkLabel(self.pointed_minidate, text = "Поточна позиція", font = ("Roboto Slab", 18), height=0,width=0,fg_color="transparent")
        self.title1.grid(row=0,column=0, padx=10, pady=10,sticky='nw')
                        
        self.city1 = tk.CTkLabel(self.pointed_minidate, text = city, font = ("Roboto Slab", 12), bg_color = "transparent", height=1)
        self.city1.grid(row=0,column=0, padx=10, pady=31,sticky='nw')

        self.temp1 = tk.CTkLabel(self.pointed_minidate, text = f"{response_pointed.json()["main"]["temp"]}°", font = ("Roboto Slab", 40),bg_color='transparent',fg_color='transparent',height=1,width=1)
        self.temp1.grid(row=0,column=3, ipadx=0, pady=3,sticky='ne')

        self.text_temp1 = tk.CTkLabel(self.pointed_minidate, text = f"\n{response_pointed.json()["weather"][0]["description"]}", font = ("Roboto Slab", 12),bg_color='transparent',fg_color='transparent',height=1,width=1)
        self.text_temp1.grid(row=0,column=0, padx=10, pady=(60,0),sticky='nw')

        self.text_temp1 = tk.CTkLabel(self.pointed_minidate, text = f"\nмакс.: {response_pointed.json()["main"]["temp_max"]}, мін.:{response_pointed.json()["main"]["temp_min"]}", font = ("Roboto Slab", 12),bg_color='transparent',fg_color='transparent',height=1,width=1)
        self.text_temp1.grid(row=0,column=3, ipadx=0, pady=(60,0),sticky='ne')



        self.minidate = tk.CTkButton(self.side_frame,
                                    text=' ',
                                    width = 270,
                                    height = 101,
                                    hover_color='#096C82',
                                    fg_color = "transparent",
                                    border_color = 'white',
                                    border_width=2.5,
                                    corner_radius=20
                                    )
        self.minidate.grid(row = 2, column = 0, padx = 10, pady = 14,sticky='n')

        self.title1 = tk.CTkLabel(self.minidate, text = cities[0], font = ("Roboto Slab", 18), height=0,width=0,fg_color="transparent")
        self.title1.grid(row=0,column=0, padx=10, pady=10,sticky='nw')
                        
        self.city1 = tk.CTkLabel(self.minidate, text = f'{kyiv_hour}:{kyiv_minute}', font = ("Roboto Slab", 12), bg_color = "transparent", height=1)
        self.city1.grid(row=0,column=0, padx=10, pady=31,sticky='nw')

        self.temp1 = tk.CTkLabel(self.minidate, text = f"{kyiv_response.json()["main"]["temp"]}°", font = ("Roboto Slab", 50),bg_color='transparent',fg_color='transparent',height=1,width=1)
        self.temp1.grid(row=0,columnspan=10,column=1, padx=10, pady=4,sticky='ne')

        self.text_temp1 = tk.CTkLabel(self.minidate, text = f"\n{kyiv_response.json()["weather"][0]["description"]}", font = ("Roboto Slab", 12),bg_color='transparent',fg_color='transparent',height=1,width=1)
        self.text_temp1.grid(row=0,column=0, padx=10, pady=(60,0),sticky='nw')

        self.text_temp1 = tk.CTkLabel(self.minidate, text = f"\nмакс.: {kyiv_response.json()["main"]["temp_max"]}, мін.:{response_pointed.json()["main"]["temp_min"]}", font = ("Roboto Slab", 12),bg_color='transparent',fg_color='transparent',height=1,width=1)
        self.text_temp1.grid(row=0,columnspan=10, column=1,padx=10, pady=(60,0),sticky='ne')




        self.minidate = tk.CTkButton(self.side_frame,
                                    text=' ',
                                    width = 270,
                                    height = 101,
                                    hover_color='#096C82',
                                    fg_color = "transparent",
                                    border_color = 'white',
                                    border_width=2.5,
                                    corner_radius=20
                                    )
        self.minidate.grid(row = 3, column = 0, padx = 10, pady = 14,sticky='n')

        self.title1 = tk.CTkLabel(self.minidate, text = cities[1], font = ("Roboto Slab", 18), height=0,width=0,fg_color="transparent")
        self.title1.grid(row=0,column=0, padx=10, pady=10,sticky='nw')
                        
        self.city1 = tk.CTkLabel(self.minidate, text = f'{rym_hour}:{rym_minute}', font = ("Roboto Slab", 12), bg_color = "transparent", height=1)
        self.city1.grid(row=0,column=0, padx=10, pady=31,sticky='nw')

        self.temp1 = tk.CTkLabel(self.minidate, text = f"{rym_response.json()["main"]["temp"]}°", font = ("Roboto Slab", 50),bg_color='transparent',fg_color='transparent',height=1,width=1)
        self.temp1.grid(row=0,columnspan=10,column=1, padx=10, pady=4,sticky='ne')

        self.text_temp1 = tk.CTkLabel(self.minidate, text = f"\n{rym_response.json()["weather"][0]["description"]}", font = ("Roboto Slab", 12),bg_color='transparent',fg_color='transparent',height=1,width=1)
        self.text_temp1.grid(row=0,column=0, padx=10, pady=(60,0),sticky='nw')

        self.text_temp1 = tk.CTkLabel(self.minidate, text = f"\nмакс.: {rym_response.json()["main"]["temp_max"]}, мін.:{response_pointed.json()["main"]["temp_min"]}", font = ("Roboto Slab", 12),bg_color='transparent',fg_color='transparent',height=1,width=1)
        self.text_temp1.grid(row=0,columnspan=10, column=1,padx=10, pady=(60,0),sticky='ne')





        self.minidate = tk.CTkButton(self.side_frame,
                                    text=' ',
                                    width = 270,
                                    height = 101,
                                    hover_color='#096C82',
                                    fg_color = "transparent",
                                    border_color = 'white',
                                    border_width=2.5,
                                    corner_radius=20
                                    )
        self.minidate.grid(row = 4, column = 0, padx = 10, pady = 14,sticky='n')

        self.title1 = tk.CTkLabel(self.minidate, text = cities[2], font = ("Roboto Slab", 18), height=0,width=0,fg_color="transparent")
        self.title1.grid(row=0,column=0, padx=10, pady=10,sticky='nw')
                        
        self.city1 = tk.CTkLabel(self.minidate, text = f'{london_hour}:{london_minute}', font = ("Roboto Slab", 12), bg_color = "transparent", height=1)
        self.city1.grid(row=0,column=0, padx=10, pady=31,sticky='nw')

        self.temp1 = tk.CTkLabel(self.minidate, text = f"{london_response.json()["main"]["temp"]}°", font = ("Roboto Slab", 50),bg_color='transparent',fg_color='transparent',height=1,width=1)
        self.temp1.grid(row=0,columnspan=10,column=1, padx=10, pady=4,sticky='ne')

        self.text_temp1 = tk.CTkLabel(self.minidate, text = f"\n{london_response.json()["weather"][0]["description"]}", font = ("Roboto Slab", 12),bg_color='transparent',fg_color='transparent',height=1,width=1)
        self.text_temp1.grid(row=0,column=0, padx=10, pady=(60,0),sticky='nw')

        self.text_temp1 = tk.CTkLabel(self.minidate, text = f"\nмакс.: {london_response.json()["main"]["temp_max"]}, мін.:{response_pointed.json()["main"]["temp_min"]}", font = ("Roboto Slab", 12),bg_color='transparent',fg_color='transparent',height=1,width=1)
        self.text_temp1.grid(row=0,columnspan=10, column=1,padx=10, pady=(60,0),sticky='ne')





        self.minidate = tk.CTkButton(self.side_frame,
                                    text=' ',
                                    width = 270,
                                    height = 101,
                                    hover_color='#096C82',
                                    fg_color = "transparent",
                                    border_color = 'white',
                                    border_width=2.5,
                                    corner_radius=20
                                    )
        self.minidate.grid(row = 5, column = 0, padx = 10, pady = 14,sticky='n')

        self.title1 = tk.CTkLabel(self.minidate, text = cities[3], font = ("Roboto Slab", 18), height=0,width=0,fg_color="transparent")
        self.title1.grid(row=0,column=0, padx=10, pady=10,sticky='nw')
                        
        self.city1 = tk.CTkLabel(self.minidate, text = f'{varchava_hour}:{varchava_minute}', font = ("Roboto Slab", 12), bg_color = "transparent", height=1)
        self.city1.grid(row=0,column=0, padx=10, pady=31,sticky='nw')

        self.temp1 = tk.CTkLabel(self.minidate, text = f"{varchava_response.json()["main"]["temp"]}°", font = ("Roboto Slab", 50),bg_color='transparent',fg_color='transparent',height=1,width=1)
        self.temp1.grid(row=0,columnspan=10,column=1, padx=10, pady=4,sticky='ne')

        self.text_temp1 = tk.CTkLabel(self.minidate, text = f"\n{varchava_response.json()["weather"][0]["description"]}", font = ("Roboto Slab", 12),bg_color='transparent',fg_color='transparent',height=1,width=1)
        self.text_temp1.grid(row=0,column=0, padx=10, pady=(60,0),sticky='nw')

        self.text_temp1 = tk.CTkLabel(self.minidate, text = f"\nмакс.: {varchava_response.json()["main"]["temp_max"]}, мін.:{response_pointed.json()["main"]["temp_min"]}", font = ("Roboto Slab", 12),bg_color='transparent',fg_color='transparent',height=1,width=1)
        self.text_temp1.grid(row=0,columnspan=10, column=1,padx=10, pady=(60,0),sticky='ne')





        self.minidate = tk.CTkButton(self.side_frame,
                                    text=' ',
                                    width = 270,
                                    height = 101,
                                    hover_color='#096C82',
                                    fg_color = "transparent",
                                    border_color = 'white',
                                    border_width=2.5,
                                    corner_radius=20
                                    )
        self.minidate.grid(row = 6, column = 0, padx = 10, pady = 14,sticky='n')

        self.title1 = tk.CTkLabel(self.minidate, text = cities[4], font = ("Roboto Slab", 18), height=0,width=0,fg_color="transparent")
        self.title1.grid(row=0,column=0, padx=10, pady=10,sticky='nw')
                        
        self.city1 = tk.CTkLabel(self.minidate, text = f'{praga_hour}:{praga_minute}', font = ("Roboto Slab", 12), bg_color = "transparent", height=1)
        self.city1.grid(row=0,column=0, padx=10, pady=31,sticky='nw')

        self.temp1 = tk.CTkLabel(self.minidate, text = f"{praga_response.json()["main"]["temp"]}°", font = ("Roboto Slab", 50),bg_color='transparent',fg_color='transparent',height=1,width=1)
        self.temp1.grid(row=0,columnspan=10,column=1, padx=10, pady=4,sticky='ne')

        self.text_temp1 = tk.CTkLabel(self.minidate, text = f"\n{praga_response.json()["weather"][0]["description"]}", font = ("Roboto Slab", 12),bg_color='transparent',fg_color='transparent',height=1,width=1)
        self.text_temp1.grid(row=0,column=0, padx=10, pady=(60,0),sticky='nw')

        self.text_temp1 = tk.CTkLabel(self.minidate, text = f"\nмакс.: {praga_response.json()["main"]["temp_max"]}, мін.:{response_pointed.json()["main"]["temp_min"]}", font = ("Roboto Slab", 12),bg_color='transparent',fg_color='transparent',height=1,width=1)
        self.text_temp1.grid(row=0,columnspan=10, column=1,padx=10, pady=(60,0),sticky='ne')
        self.content_up = tk.CTkButton(self,width=900,height=100,fg_color='red',text='',hover_color='red')
        self.content_up.grid(row=0,column=2,sticky='ne',padx=10,pady=10)




        self.account_button = tk.CTkButton(self.content_up, fg_color='red', width=50, height=40, text="", command=self.open_toplevel)
        self.account_button.grid(row=0,column=0,padx=40,pady=20,sticky="wn")

        self.text_label = tk.CTkLabel(self.account_button, fg_color="#5DA7B1", text=f'{name} {surname}',bg_color='#5DA7B1',font = ("Roboto Slab", 20),)
        self.text_label.grid(row=0,column=0, padx=50,pady=12,sticky='wn')

        self.image_path = os.path.join(os.path.dirname(__file__), 'icon\\user.png')
        self.image = tk.CTkImage(light_image= Image.open(self.image_path), size=(50,50),)
        self.image_label = tk.CTkLabel(self.account_button, image=self.image,fg_color="#5DA7B1", text=' ')
        self.image_label.grid(row=0,column=0, padx=0,pady=0,sticky='wn'), 

        self.search_field = tk.CTkTextbox(self.content_up, width=218, height=1, fg_color="#096C82", border_color='white', border_width=3,corner_radius=20)
        self.search_field.grid(row=0,column=4, padx=0, pady=18,)

        self.search_image_path = os.path.join(os.path.dirname(__file__), 'icon\\search.png')
        self.search_image = tk.CTkImage(light_image= Image.open(self.search_image_path), size=(37,37),)
        self.search_image_label = tk.CTkLabel(self.search_field, image=self.search_image,fg_color="#096C82", text=' ',corner_radius=100,height=1)
        self.search_image_label.grid(row=0,column=0, padx=8,ipady=0,pady=10,sticky='ws'), 





        self.content_middle = tk.CTkButton(self,width=900,height=300,fg_color='blue',text='')
        self.content_middle.grid(row=0,column=2,sticky='ne',padx=10,pady=140)

        self.line_position = tk.CTkLabel(self.content_middle, fg_color="#5DA7B1", text="Поточна позиція", bg_color='#5DA7B1', font = ("Roboto Slab", 35))
        self.line_position.grid(row=0,column=2,sticky="wne")
        self.city_position = tk.CTkLabel(self.content_middle, fg_color="#5DA7B1", text=city, bg_color='#5DA7B1', font = ("Roboto Slab", 22))
        self.city_position.grid(row=0,column=2,pady=50,sticky="wne")
        self.temp_position = tk.CTkLabel(self.content_middle, fg_color="#5DA7B1", text=f"{response_pointed.json()["main"]["temp"]}°", bg_color='#5DA7B1', font = ("Roboto Slab", 80))
        self.temp_position.grid(row=0,column=2,pady=80,sticky="wne")
        self.description_position = tk.CTkLabel(self.content_middle, fg_color="#5DA7B1", text=f"{response_pointed.json()["weather"][0]["description"]}", bg_color='#5DA7B1', font = ("Roboto Slab", 30))
        self.description_position.grid(row=0,column=2,pady=190,sticky="wne")
        self.min_max_temp_position = tk.CTkLabel(self.content_middle, fg_color="#5DA7B1", text=f"↓ {response_pointed.json()["main"]["temp_min"]}° ↑ {response_pointed.json()["main"]["temp_max"]}°", bg_color='#5DA7B1', font = ("Roboto Slab", 30))
        self.min_max_temp_position.grid(row=0,column=2,pady=230,sticky="wne")

        self.search_image_path = os.path.join(os.path.dirname(__file__), 'icon\\sunrise.png')
        self.search_image = tk.CTkImage(light_image= Image.open(self.search_image_path), size=(170,170),)
        self.search_image_label = tk.CTkLabel(self.content_middle, image=self.search_image,fg_color="#096C82", text=' ',corner_radius=100,height=1)
        self.search_image_label.grid(row=0,column=0, ipadx=0,ipady=0,pady=55,sticky='n'), 

        self.pointed_day_of_time = tk.CTkLabel(self.content_middle, fg_color="#5DA7B1", text= pointed_day_of_week, bg_color='#5DA7B1', font = ("Roboto Slab", 20))
        self.pointed_day_of_time.grid(row=0,column=3,pady=80,padx=60,sticky="ne")

        self.pointed_date = tk.CTkLabel(self.content_middle, fg_color="#5DA7B1", text= pointed_date, bg_color='#5DA7B1', font = ("Roboto Slab", 40))
        self.pointed_date.grid(row=0,column=3,pady=110,sticky="ne")

        self.pointed_time = tk.CTkLabel(self.content_middle, fg_color="#5DA7B1", text= f"{pointed_hour}:{pointed_minute}", bg_color='#5DA7B1', font = ("Roboto Slab", 30))
        self.pointed_time.grid(row=0,column=3,pady=160,padx=60,sticky="ne")



        self.content_bottom = tk.CTkFrame(self,width=900,height=250,fg_color='green')
        self.content_bottom.grid(row=0,column=2,sticky='we',padx=10,pady=430)


        self.toplevel_window = None

    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = Account(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it









































class Register(tk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        # Fields()
        self.geometry("460x645")
        self.title("Регистрація")
        self.resizable(False, False)
        self.config(bg="#5DA7B1",)
        
        self.title = tk.CTkLabel(self, text = "Реєстрація користувача", font = ("Inter", 28), fg_color = "#5DA7B1", width=100)
        self.title.grid(row=0, column=0, ipadx=100, pady=50, sticky='n')
        
        self.fields = tk.CTkButton(self, fg_color = "#5DA7B1", width = 400, height = 400, text='', hover_color='#5DA7B1',bg_color='#5DA7B1')
        self.fields.grid(row=0, column=0, padx=0, pady=(100,0), )



        self.country_text = tk.CTkLabel(self.fields, text = "Країна:", font = ("Roboto Slab", 22))
        self.country_text.grid(row=0, column=0,padx=14,pady=10,sticky='wn')

        self.country_field = tk.CTkTextbox(self.fields,
                                width = 218,
                                height = 46, 
                                fg_color = "#096C82",
                                # bg_color = "#096C82",
                                corner_radius = 15,
                                border_width = 2,
                                border_color = "white",
                                )
        
        self.country_field.grid(row=0, column=0,padx=8,pady=44,sticky='wn')



        self.city_text = tk.CTkLabel(self.fields, text = "Місто:", font = ("Roboto Slab", 22))
        self.city_text.grid(row=0, column=0,padx=14,pady=10+90,sticky='wn')

        
        self.city_field = tk.CTkTextbox(self.fields,
                                width = 218,
                                height = 46, 
                                fg_color = "#096C82",
                                # bg_color = "#096C82",
                                corner_radius = 15,
                                border_width = 2,
                                border_color = "white",
                                )
        self.city_field.grid(row=0, column=0,padx=8,pady=44+90,sticky='wn')
    

        self.name_text = tk.CTkLabel(self.fields, text = "Ім'я:", font = ("Roboto Slab", 22))
        self.name_text.grid(row=0, column=0,padx=14,pady=10+180,sticky='wn')

        self.name_field = tk.CTkTextbox(self.fields,
                                width = 295,
                                height = 46, 
                                fg_color = "#096C82",
                                # bg_color = "#096C82",
                                corner_radius = 15,
                                border_width = 2,
                                border_color = "white"
                                )
        self.name_field.grid(row=0, column=0,padx=8,pady=44+180,sticky='wn')



        self.surname_text = tk.CTkLabel(self.fields, text = "Прізвище:", font = ("Roboto Slab", 22))
        self.surname_text.grid(row=0, column=0,padx=14,pady=10+270,sticky='wn')

        self.surname_field = tk.CTkTextbox(self.fields,
                                width = 295,
                                height = 46, 
                                fg_color = "#096C82",
                                # bg_color = "#096C82",
                                corner_radius = 15,
                                border_width = 2,
                                border_color = "white"
                                )
        self.surname_field.grid(row=0, column=0,padx=8,pady=44+270,sticky='wn')
        

        pen.execute("SELECT * FROM users")
            
        def inputs():
            pen.execute(f"INSERT INTO users VALUES('{self.country_field.get("0.0", "end").replace("\n","")}', '{self.city_field.get("0.0", "end").replace("\n","")}', '{self.name_field.get("0.0", "end").replace("\n","")}', '{self.surname_field.get("0.0", "end").replace("\n","")}')")

            pen.execute("SELECT rowid, * FROM users")
            print(pen.fetchall())
            db.commit()
            db.close()

            
        self.save_button = tk.CTkButton(self, fg_color = "#096C82", width = 218, height = 46, text='Зберегти', hover_color='#074A59',bg_color='#5DA7B1',border_color='white',border_width=2,corner_radius=15, font = ("Roboto Slab", 18), command=self.open_toplevel)
        self.save_button.grid(row=0, column=0, padx=0, pady=(320,0), )
        
        self.gitler = None

    def open_toplevel(self):
        if self.gitler is None or not self.gitler.winfo_exists():
            self.gitler = App(self)  # create window if its None or destroyed
        else:
            self.gitler.focus()  # if window exists focus it
 
Register().mainloop()