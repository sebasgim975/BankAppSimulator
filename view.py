import tkinter as tk
from controller import *

class View:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master, bg="gray", padx=75, pady=75)
        self.frame.pack(fill=tk.BOTH, expand=True)


        self.user_label = tk.Label(self.frame, text=("Nome de Utilizador"), bg=("gray"), foreground=("black"), font=("Arial", 15), pady=5)
        self.user_label.pack()
        self.user_entry = tk.Entry(self.frame, width=25)
        self.user_entry.pack()
        self.password = tk.Label(self.frame, text=("Password"), bg=("gray"), foreground=("black"), font=("Arial", 15), pady=5)
        self.password.pack()
        self.password_entry = tk.Entry(self.frame, width=25)
        self.password_entry.pack()

        self.registo_button = tk.Button(self.frame,text="Registo",bg="black",foreground="white",font=("Arial",12),width=10)
        self.registo_button.pack(pady=5)

        self.login_button = tk.Button(self.frame,text="Login",bg="black",foreground="white",font=("Arial",12),width=10)
        self.login_button.pack(pady=5)
