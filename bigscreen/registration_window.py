# import tkinter
import customtkinter as tk
import requests
import json
import sqlite3 
import os

# city = input("Enter the city name: ")
# url_api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
# path = os.path.abspath(__file__+"/../../user_data")
# os.chdir(path)


db = sqlite3.connect('user_data.db')

pen = db.cursor()

go_to_main = False

# pen.execute("""CREATE TABLE IF NOT EXISTS users ( 
#         country TEXT,
#         city TEXT,
#         name TEXT,
#         surname TEXT
# )""")




class Register(tk.CTk):
    def __init__(self):
        super().__init__()
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

        

        # city_name = input("Enter the city name: ")
        
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
    

        # cities={
        #     'Ukraine':"Dnipro" "Odessa"
        # }
        # API_KEY = 'c3c7dd0d8e63c30b03f32d8c5b575f19'

        # url_api = f"https://api.openweathermap.org/data/2.5/weather?q={self.city_field}&appid={API_KEY}"

        # response = requests.get(url_api)

        # if response.status_code == 200:
        #     data = response.json()
        #     dict_weather = json.dumps(data, indent=4)
        #     print(dict_weather)
        # else:
        #     print("Error requests")
        #     print(response)

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
        

        def inputs():
            pen.execute(f"INSERT INTO users VALUES('{self.country_field.get("0.0", "end").replace("\n","")}', '{self.city_field.get("0.0", "end").replace("\n","")}', '{self.name_field.get("0.0", "end").replace("\n","")}', '{self.surname_field.get("0.0", "end").replace("\n","")}')")

            pen.execute("SELECT rowid, * FROM users")
            print(pen.fetchall())
            db.commit()
            db.close()
            go_to_main = True
            
        self.save_button = tk.CTkButton(self, fg_color = "#096C82", width = 218, height = 46, text='Зберегти', hover_color='#074A59',bg_color='#5DA7B1',border_color='white',border_width=2,corner_radius=15, font = ("Roboto Slab", 18), command=inputs)
        self.save_button.grid(row=0, column=0, padx=0, pady=(320,0), )
            


            
register = Register()
# API_key = "58cd4aa232816cd0ae10351cb15604aa"
# url_api = f"https://api.openweathermap.org/data/2.5/weather?q={register.city_field}&appid={API_key}"
# response = requests.get(url_api)
# print(response.temp , 'red')
# print(url_api, 'green')

register.mainloop()

# from create_window import *

# if go_to_main == True:
#     App()