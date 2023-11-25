# import tkinter
import customtkinter as tk

class Register(tk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("460x645")
        self.title("Регистрація")
        self.resizable(False, False)
        self.config(bg="#5DA7B1",)
        
        self.title = tk.CTkLabel(self, text = "Реєстрація користувача", font = ("Inter", 28), fg_color = "#5DA7B1")
        self.title.pack(anchor="n", padx=0, pady=50)
        
        self.fields = tk.CTkFrame(self, fg_color = "5DA7B1", width = 400, height = 700, )
        self.fields.pack(padx = 0, pady = 0, anchor='ns')
        # self.fields.pack(anchor="n", padx=0, pady=270)

        self.city = tk.CTkTextbox(master=self.fields,
                                #  text="City",
                                width = 240,
                                height = 100, 
                                fg_color = "transparent",
                                bg_color = "transparent",
                                
                                
                                 )
        self.city.insert("0.0", "herherherheherh")
        self.city.pack(padx = 24, pady = 24)

Register().mainloop()