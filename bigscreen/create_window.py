# import tkinter
import customtkinter as tk



class App(tk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x800")
        self.title("Wether")
        self.resizable(False, False)
        self.config(bg="#5DA7B1",)

        self.side_frame = tk.CTkScrollableFrame(self, 
                                width = 275, 
                                height = 800, 
                                fg_color = "#096C82", 
                                bg_color="#096C82",
                                corner_radius=0,                              
                                )
        self.side_frame.grid(row = 1000, column = 800, )

        self.border_frame = tk.CTkFrame(self, 
                                width =2, 
                                height=800,
                                fg_color='#FFFFFF',
                                bg_color='#FFFFFF',
                                corner_radius=0,
                                #    border_color='white',
                                    )
        self.border_frame.grid(row = 1000, column = 1800,padx=1,)

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
        self.pointed_minidate.grid(row = 0, column = 0, padx = 23, pady = 22)

        self.title = tk.CTkLabel(self.pointed_minidate, text = "Поточна позиція", font = ("Roboto Slab", 18), )
        self.title.grid(row=0,column=0, padx=10, pady=8,sticky='nw')

        self.city = tk.CTkLabel(self.pointed_minidate, text = "Дніпро", font = ("Roboto Slab", 12), bg_color = "transparent", height=1)
        self.city.grid(row=0,column=0, padx=10, pady=31,sticky='nw')

        self.temp = tk.CTkLabel(self.pointed_minidate, text = "11°", font = ("Roboto Slab", 10),bg_color='red')
        self.temp.grid(row=0,column=0, padx=170, pady=10,sticky='ne')

        # self.pointed_minidate = tk.CTkButton(self.side_frame,
        #                                     text=' ',
        #                                     width = 236,
        #                                     height = 101,
        #                                     hover_color='#096C82',
        #                                     fg_color = "#096C82",
        #                                     border_color = 'white',
        #                                     border_width=2.5,
        #                                     corner_radius=20
        #                                     )
        # self.pointed_minidate.grid(row = 0, column = 0, padx = 23, pady = 22,)

        # self.title = tk.CTkLabel(self.pointed_minidate, text = "Поточна позиція", font = ("Roboto Slab", 18), )
        # self.title.grid(row=0,column=0, padx=10, pady=8,sticky='nw')

        # self.city = tk.CTkLabel(self.pointed_minidate, text = "Дніпро", font = ("Roboto Slab", 12), bg_color = "transparent", height=7)
        # self.city.grid(row=0,column=0, padx=10, pady=30,sticky='nw')

        # self.city = tk.CTkTextbox(master =self.pointed_minidate,
        #                         #  text="City",
        #                         width = 240,
        #                         height = 100, 
        #                         fg_color = "transparent",
        #                         # bg_color = "transparent"
        #                          )
        # self.city.insert("50.100", "herherherheherh ")
        # self.city.grid(row = 24, column = 24)


app = App()

app.mainloop()









