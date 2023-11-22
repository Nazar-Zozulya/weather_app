import tkinter
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
        
        self.fields = tk.CTkFrame(self, fg_color = "red", width = 400, height = 400 )
        self.fields.pack(padx = 0, pady = 0)
        # self.fields.pack(anchor="n", padx=0, pady=270)



Register().mainloop()