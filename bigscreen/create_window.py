#import tkinter
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


url_api_pointed = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&lang=uk&units=metric"
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



class App(tk.CTk):
    def __init__(self):
        super().__init__()
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

        self.text_label = tk.CTkLabel(self.content_up, fg_color="#5DA7B1", text=f'{name} {surname}',bg_color='#5DA7B1',font = ("Roboto Slab", 20),)
        self.text_label.grid(row=0,column=0, padx=60+30,pady=28,sticky='wn')

        self.image_path = os.path.join(os.path.dirname(__file__), 'icon\\user.png')
        self.image = tk.CTkImage(light_image= Image.open(self.image_path), size=(50,50),)
        self.image_label = tk.CTkLabel(self.content_up, image=self.image,fg_color="#5DA7B1", text=' ')
        self.image_label.grid(row=0,column=0, padx=10+30,pady=20,sticky='wn'), 

        self.search_field = tk.CTkTextbox(self.content_up, width=218, height=1, fg_color="#096C82", border_color='white', border_width=3,corner_radius=20)
        self.search_field.grid(row=0,column=4, padx=0, pady=18,)

        self.search_image_path = os.path.join(os.path.dirname(__file__), 'icon\\search.png')
        self.search_image = tk.CTkImage(light_image= Image.open(self.search_image_path), size=(37,37),)
        self.search_image_label = tk.CTkLabel(self.search_field, image=self.search_image,fg_color="#096C82", text=' ',corner_radius=100,height=1)
        self.search_image_label.grid(row=0,column=0, padx=8,ipady=0,pady=10,sticky='ws'), 
        # self.search_image_path = os.path.join(os.path.dirname(__file__), 'img\\search.png')
        # self.search_image = tk.CTkImage(light_image= Image.open(self.image_path), size=(50,50),)
        # # self.image.grid(row=0,column=0, padx=100)
        # self.search_image_label = tk.CTkLabel(self.content_up, image=self.image,fg_color="#5DA7B1", text=' ')
        # self.search_image_label.grid(row=0,column=0, padx=400,sticky='ne'), 
        # self.text_label = tk.CTkTextbox(self.content_up, fg_color="#5DA7B1", bg_color='#5DA7B1',font = ("Roboto Slab", 16))
        # self.text_label.grid(row=0,column=0, padx=363,pady=10,sticky='wn')
 





        self.content_middle = tk.CTkFrame(self,width=900,height=300,fg_color='blue')
        self.content_middle.grid(row=0,column=2,sticky='ne',padx=10,pady=120)




        self.content_bottom = tk.CTkFrame(self,width=900,height=250,fg_color='green')
        self.content_bottom.grid(row=0,column=2,sticky='ne',padx=10,pady=430)







        
app = App()

app.mainloop()









