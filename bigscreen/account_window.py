import customtkinter as tk
import sqlite3
import os
from PIL import Image
# from create_window import App
# import create_window
# from functions import *


db = sqlite3.connect('user_data.db')

pen = db.cursor()

class Account(tk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("460x645")
        self.title("Регистрація")
        self.resizable(False, False)
        self.config(bg="#5DA7B1",)
        
        # if pen is not None:


        pen.execute("SELECT rowid, * FROM users")

        for i in pen:
            country = i[1]
            city = i[2]
            name = i[3]
            surname = i[4]


        # self.image_path = os.path.join(os.path.dirname(__file__), 'icon/left-arrow.png')
        # self.image = tk.CTkImage(light_image= Image.open(self.image_path), size=(50,50),)
        # # self.image.grid(row=0,column=0, padx=100)
        # self.image_label = tk.CTkLabel(self, image=self.image,fg_color="#5DA7B1", text=' ')
        # self.image_label.grid(row=0,column=0, padx=400,sticky='ne'), 
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

        def close_window():
            self.destroy()

        self.save_button = tk.CTkButton(self, fg_color = "#096C82", width = 218, height = 39, text='Перейти до додатку', hover_color='#074A59',bg_color='#5DA7B1',border_color='white',border_width=2,corner_radius=15, font = ("Roboto Slab", 18), command=close_window)
        self.save_button.grid(row=0, column=0, padx=115, pady=(530,0), sticky="wn")
            

# API_key = "58cd4aa232816cd0ae10351cb15604aa"
# url_api = f"https://api.openweathermap.org/data/2.5/weather?q={register.city_field}&appid={API_key}"
# response = requests.get(url_api)
# print(response.temp , 'red')
# print(url_api, 'green')






# Account().mainloop()