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
        self.side_frame.grid(row = 275, column = 800,)

        self.border_frame = tk.CTkFrame(self, 
                                width =2, 
                                height=800,
                                fg_color='#FFFFFF',
                                bg_color='#FFFFFF',
                                corner_radius=0,
                                #    border_color='white',
                                    )
        self.border_frame.grid(row = 275, column = 1800,padx=1,)

        self.pointed_minidate = tk.CTkFrame(self.side_frame,
                                            width = 240,
                                            height = 300,
                                            fg_color = "red",
                                            border_color = 'white',
                                            border_width=2.5,
                                            corner_radius=20
                                            )
        self.pointed_minidate.grid(row = 240, column = 1000, padx = 23, pady = 22,)

        self.title = tk.CTkLabel(self.pointed_minidate, text = "Дніпро", font = ("Inter", 58), fg_color = "transparent")
        self.title.grid(row=0,column=0, padx=0, pady=50)

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









