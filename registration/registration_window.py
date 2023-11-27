# import tkinter
import customtkinter as tk
import requests
import json


# city = input("Enter the city name: ")
# url_api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"



# class Fields(tk.CTk):
#     def __init__(self):
#         super().__init__()

#         self.city_text = tk.CTkLabel(self.fields, text = "Країна:", font = ("Roboto Slab", 22))
#         self.city_text.grid(row=0, column=0,padx=14,pady=10,sticky='wn')

#         self.city_field = tk.CTkTextbox(self.fields,
#                                 width = 218,
#                                 height = 46, 
#                                 fg_color = "#096C82",
#                                 # bg_color = "#096C82",
#                                 corner_radius = 15,
#                                 border_width = 2,
#                                 border_color = "white"
#                                 )
#         self.city_field.grid(row=0, column=0,padx=8,pady=44,sticky='wn')






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
        
        self.fields = tk.CTkButton(self, fg_color = "#5DA7B1", width = 400, height = 400, text='', hover_color='#5DA7B1',bg_color='#5DA7B1')#border_color='white',border_width=2
        self.fields.grid(row=0, column=0, padx=0, pady=(100,0), )



        self.city_text = tk.CTkLabel(self.fields, text = "Країна:", font = ("Roboto Slab", 22))
        self.city_text.grid(row=0, column=0,padx=14,pady=10,sticky='wn')

        self.city_field = tk.CTkTextbox(self.fields,
                                width = 218,
                                height = 46, 
                                fg_color = "#096C82",
                                # bg_color = "#096C82",
                                corner_radius = 15,
                                border_width = 2,
                                border_color = "white"
                                )
        self.city_field.grid(row=0, column=0,padx=8,pady=44,sticky='wn')

        # Fields()





        self.city_text = tk.CTkLabel(self.fields, text = "Місто:", font = ("Roboto Slab", 22))
        self.city_text.grid(row=0, column=0,padx=14,pady=10+90,sticky='wn')

        self.city_field = tk.CTkTextbox(self.fields,
                                width = 218,
                                height = 46, 
                                fg_color = "#096C82",
                                # bg_color = "#096C82",
                                corner_radius = 15,
                                border_width = 2,
                                border_color = "white"
                                )
        self.city_field.grid(row=0, column=0,padx=8,pady=44+90,sticky='wn')




        self.city_text = tk.CTkLabel(self.fields, text = "Ім'я:", font = ("Roboto Slab", 22))
        self.city_text.grid(row=0, column=0,padx=14,pady=10+180,sticky='wn')

        self.city_field = tk.CTkTextbox(self.fields,
                                width = 295,
                                height = 46, 
                                fg_color = "#096C82",
                                # bg_color = "#096C82",
                                corner_radius = 15,
                                border_width = 2,
                                border_color = "white"
                                )
        self.city_field.grid(row=0, column=0,padx=8,pady=44+180,sticky='wn')



        self.city_text = tk.CTkLabel(self.fields, text = "Прізвище:", font = ("Roboto Slab", 22))
        self.city_text.grid(row=0, column=0,padx=14,pady=10+270,sticky='wn')

        self.city_field = tk.CTkTextbox(self.fields,
                                width = 295,
                                height = 46, 
                                fg_color = "#096C82",
                                # bg_color = "#096C82",
                                corner_radius = 15,
                                border_width = 2,
                                border_color = "white"
                                )
        self.city_field.grid(row=0, column=0,padx=8,pady=44+270,sticky='wn')
        

register = Register()
# API_key = "58cd4aa232816cd0ae10351cb15604aa"
# url_api = f"https://api.openweathermap.org/data/2.5/weather?q={register.city_field}&appid={API_key}"
# response = requests.get(url_api)
# print(response.temp , 'red')
# print(url_api, 'green')

register.mainloop()