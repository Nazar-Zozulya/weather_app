import customtkinter as tk
import requests
import json
import sqlite3 
import os
from PIL import Image


db = sqlite3.connect('user_data.db')

pen = db.cursor()

go_to_main = False

pen.execute("SELECT rowid, * FROM users")

for i in pen:
    country = i[1]
    city = i[2]
    name = i[3]
    surname = i[4]


class ToplevelWindow(tk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("460x645")
        self.title("Регистрація")
        self.resizable(False, False)
        self.config(bg="#5DA7B1",)
        
        # if pen is not None:


        pen.execute("SELECT rowid, * FROM users")
        # if pen is not None:
        #     country = pen.fetchone()[0]
        #     city = pen.fetchone()[1]
        #     name = pen.fetchone()[2]
        # else:
        #     surname = pen.fetchone()[3]
        # print(pen.fetchall())
        # a = pen.fetchone()
        # print(a)
        # country = pen.fetchone()[0]
        # city = pen.fetchone()[1]
        # name = pen.fetchone()[2]
        # surname = pen.fetchone()[3]
        # bebra = [
            # pen.fetchone()[0],
            # pen.fetchone()[1],
            # pen.fetchone()[2],
            # pen.fetchone()[3],
        # ]
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

        self.label = tk.CTkLabel(self, text="ToplevelWindow")
        self.label.pack(padx=20, pady=20)



class App(tk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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
        

        pen.execute("SELECT * FROM users")

        for i in pen:
            country = i[0]
            city = i[1]
            name = i[2]
            surname = i[3]
            
        def inputs():
            pen.execute(f"INSERT INTO users VALUES('{self.country_field.get("0.0", "end").replace("\n","")}', '{self.city_field.get("0.0", "end").replace("\n","")}', '{self.name_field.get("0.0", "end").replace("\n","")}', '{self.surname_field.get("0.0", "end").replace("\n","")}')")

            pen.execute("SELECT rowid, * FROM users")
            print(pen.fetchall())
            db.commit()
            db.close()

            
        self.save_button = tk.CTkButton(self, fg_color = "#096C82", width = 218, height = 46, text='Зберегти', hover_color='#074A59',bg_color='#5DA7B1',border_color='white',border_width=2,corner_radius=15, font = ("Roboto Slab", 18), command=self.open_toplevel)
        self.save_button.grid(row=0, column=0, padx=0, pady=(320,0), )

        self.toplevel_window = None

    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it


app = App()
app.mainloop()