# import tkinter
import customtkinter as tk

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

        # self.pointed_minidate = tk.CTkButton(self.side_frame,
        #                                     text=' ',
        #                                     width = 236,
        #                                     height = 101,
        #                                     hover_color='#4599A4',
        #                                     fg_color = "#4599A4",
        #                                     border_color = 'white',
        #                                     border_width=2.5,
        #                                     corner_radius=20
        #                                     )
        # self.pointed_minidate.grid(row = 0, column = 0, padx = 10, pady = (10,0))

        # self.title = tk.CTkLabel(self.pointed_minidate, text = "Поточна позиція", font = ("Roboto Slab", 18), height=0,width=0,fg_color="transparent")
        # self.title.grid(row=0,column=0, padx=5, pady=10,sticky='nw')

        # self.city = tk.CTkLabel(self.pointed_minidate, text = "Дніпро", font = ("Roboto Slab", 12), bg_color = "transparent", height=1)
        # self.city.grid(row=0,column=0, padx=5, pady=31,sticky='nw')

        # self.temp = tk.CTkLabel(self.pointed_minidate, text = "11°", font = ("Roboto Slab", 50),bg_color='transparent',fg_color='transparent',height=1,width=1)
        # self.temp.grid(row=0,column=3, ipadx=0, pady=3,sticky='ne')

        # self.text_temp = tk.CTkLabel(self.pointed_minidate, text = "Хмарно з \nпроясненнями", font = ("Roboto Slab", 12),bg_color='transparent',fg_color='transparent',height=1,width=1)
        # self.text_temp.grid(row=0,column=0, padx=6, pady=(60,0),sticky='nw')

        # self.text_temp = tk.CTkLabel(self.pointed_minidate, text = "\nмакс.: 12 , мін.: 5  ", font = ("Roboto Slab", 12),bg_color='transparent',fg_color='transparent',height=1,width=1)
        # self.text_temp.grid(row=0,column=3, ipadx=0, pady=(60,0),sticky='ne')



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
                        
        self.city1 = tk.CTkLabel(self.pointed_minidate, text = "Дніпро", font = ("Roboto Slab", 12), bg_color = "transparent", height=1)
        self.city1.grid(row=0,column=0, padx=10, pady=31,sticky='nw')

        self.temp1 = tk.CTkLabel(self.pointed_minidate, text = "11°", font = ("Roboto Slab", 50),bg_color='transparent',fg_color='transparent',height=1,width=1)
        self.temp1.grid(row=0,column=3, padx=0, pady=3,sticky='ne')

        self.text_temp1 = tk.CTkLabel(self.pointed_minidate, text = "Хмарно з \nпроясненнями", font = ("Roboto Slab", 12),bg_color='transparent',fg_color='transparent',height=1,width=1)
        self.text_temp1.grid(row=0,column=0, padx=10, pady=(60,0),sticky='nw')

        self.text_temp1 = tk.CTkLabel(self.pointed_minidate, text = "\nмакс.: 12 , мін.: 5  ", font = ("Roboto Slab", 12),bg_color='transparent',fg_color='transparent',height=1,width=1)
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

        self.title1 = tk.CTkLabel(self.minidate, text = "Київ", font = ("Roboto Slab", 18), height=0,width=0,fg_color="transparent")
        self.title1.grid(row=0,column=0, padx=10, pady=10,sticky='nw')
                        
        self.city1 = tk.CTkLabel(self.minidate, text = "14:37", font = ("Roboto Slab", 12), bg_color = "transparent", height=1)
        self.city1.grid(row=0,column=0, padx=10, pady=31,sticky='nw')

        self.temp1 = tk.CTkLabel(self.minidate, text = "11°", font = ("Roboto Slab", 50),bg_color='transparent',fg_color='transparent',height=1,width=1)
        self.temp1.grid(row=0,columnspan=10,column=1, padx=10, pady=4,sticky='ne')

        self.text_temp1 = tk.CTkLabel(self.minidate, text = "Хмарно з \nпроясненнями", font = ("Roboto Slab", 12),bg_color='transparent',fg_color='transparent',height=1,width=1)
        self.text_temp1.grid(row=0,column=0, padx=10, pady=(60,0),sticky='nw')

        self.text_temp1 = tk.CTkLabel(self.minidate, text = "\nмакс.: 12 , мін.: 5  ", font = ("Roboto Slab", 12),bg_color='transparent',fg_color='transparent',height=1,width=1)
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

        self.title1 = tk.CTkLabel(self.minidate, text = "Рим", font = ("Roboto Slab", 18), height=0,width=0,fg_color="transparent")
        self.title1.grid(row=0,column=0, padx=10, pady=10,sticky='nw')
                        
        self.city1 = tk.CTkLabel(self.minidate, text = "13:37", font = ("Roboto Slab", 12), bg_color = "transparent", height=1)
        self.city1.grid(row=0,column=0, padx=10, pady=31,sticky='nw')

        self.temp1 = tk.CTkLabel(self.minidate, text = "11°", font = ("Roboto Slab", 50),bg_color='transparent',fg_color='transparent',height=1,width=1)
        self.temp1.grid(row=0,columnspan=10,column=1, padx=10, pady=4,sticky='ne')

        self.text_temp1 = tk.CTkLabel(self.minidate, text = "Хмарно з \nпроясненнями", font = ("Roboto Slab", 12),bg_color='transparent',fg_color='transparent',height=1,width=1)
        self.text_temp1.grid(row=0,column=0, padx=10, pady=(60,0),sticky='nw')

        self.text_temp1 = tk.CTkLabel(self.minidate, text = "\nмакс.: 12 , мін.: 5  ", font = ("Roboto Slab", 12),bg_color='transparent',fg_color='transparent',height=1,width=1)
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

        self.title1 = tk.CTkLabel(self.minidate, text = "Лондон", font = ("Roboto Slab", 18), height=0,width=0,fg_color="transparent")
        self.title1.grid(row=0,column=0, padx=10, pady=10,sticky='nw')
                        
        self.city1 = tk.CTkLabel(self.minidate, text = "12:37", font = ("Roboto Slab", 12), bg_color = "transparent", height=1)
        self.city1.grid(row=0,column=0, padx=10, pady=31,sticky='nw')

        self.temp1 = tk.CTkLabel(self.minidate, text = "11°", font = ("Roboto Slab", 50),bg_color='transparent',fg_color='transparent',height=1,width=1)
        self.temp1.grid(row=0,columnspan=10,column=1, padx=10, pady=4,sticky='ne')

        self.text_temp1 = tk.CTkLabel(self.minidate, text = "Хмарно з \nпроясненнями", font = ("Roboto Slab", 12),bg_color='transparent',fg_color='transparent',height=1,width=1)
        self.text_temp1.grid(row=0,column=0, padx=10, pady=(60,0),sticky='nw')

        self.text_temp1 = tk.CTkLabel(self.minidate, text = "\nмакс.: 12 , мін.: 5  ", font = ("Roboto Slab", 12),bg_color='transparent',fg_color='transparent',height=1,width=1)
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

        self.title1 = tk.CTkLabel(self.minidate, text = "Варшава", font = ("Roboto Slab", 18), height=0,width=0,fg_color="transparent")
        self.title1.grid(row=0,column=0, padx=10, pady=10,sticky='nw')
                        
        self.city1 = tk.CTkLabel(self.minidate, text = "13:37", font = ("Roboto Slab", 12), bg_color = "transparent", height=1)
        self.city1.grid(row=0,column=0, padx=10, pady=31,sticky='nw')

        self.temp1 = tk.CTkLabel(self.minidate, text = "11°", font = ("Roboto Slab", 50),bg_color='transparent',fg_color='transparent',height=1,width=1)
        self.temp1.grid(row=0,columnspan=10,column=1, padx=10, pady=4,sticky='ne')

        self.text_temp1 = tk.CTkLabel(self.minidate, text = "Хмарно з \nпроясненнями", font = ("Roboto Slab", 12),bg_color='transparent',fg_color='transparent',height=1,width=1)
        self.text_temp1.grid(row=0,column=0, padx=10, pady=(60,0),sticky='nw')

        self.text_temp1 = tk.CTkLabel(self.minidate, text = "\nмакс.: 12 , мін.: 5  ", font = ("Roboto Slab", 12),bg_color='transparent',fg_color='transparent',height=1,width=1)
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

        self.title1 = tk.CTkLabel(self.minidate, text = "Прага", font = ("Roboto Slab", 18), height=0,width=0,fg_color="transparent")
        self.title1.grid(row=0,column=0, padx=10, pady=10,sticky='nw')
                        
        self.city1 = tk.CTkLabel(self.minidate, text = "13:37", font = ("Roboto Slab", 12), bg_color = "transparent", height=1)
        self.city1.grid(row=0,column=0, padx=10, pady=31,sticky='nw')

        self.temp1 = tk.CTkLabel(self.minidate, text = "11°", font = ("Roboto Slab", 50),bg_color='transparent',fg_color='transparent',height=1,width=1)
        self.temp1.grid(row=0,columnspan=10,column=1, padx=10, pady=4,sticky='ne')

        self.text_temp1 = tk.CTkLabel(self.minidate, text = "Хмарно з \nпроясненнями", font = ("Roboto Slab", 12),bg_color='transparent',fg_color='transparent',height=1,width=1)
        self.text_temp1.grid(row=0,column=0, padx=10, pady=(60,0),sticky='nw')

        self.text_temp1 = tk.CTkLabel(self.minidate, text = "\nмакс.: 12 , мін.: 5  ", font = ("Roboto Slab", 12),bg_color='transparent',fg_color='transparent',height=1,width=1)
        self.text_temp1.grid(row=0,columnspan=10, column=1,padx=10, pady=(60,0),sticky='ne')










        self.content_up = tk.CTkFrame(self,width=900,height=100,fg_color='red')
        self.content_up.grid(row=0,column=2,sticky='ne',padx=10,pady=10)
        self.content_middle = tk.CTkFrame(self,width=900,height=300,fg_color='blue')
        self.content_middle.grid(row=0,column=2,sticky='ne',padx=10,pady=120)
        self.content_bottom = tk.CTkFrame(self,width=900,height=250,fg_color='green')
        self.content_bottom.grid(row=0,column=2,sticky='ne',padx=10,pady=430)

        
app = App()

app.mainloop()









