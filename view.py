import tkinter as tk
from controller import *

class View:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master, bg="black", padx=75, pady=75)
        self.frame.pack(fill=tk.BOTH, expand=True)


        self.user_label = tk.Label(self.frame, text=("Nomem de Utilizador"), bg=("black"), foreground=("white"), font=("Arial", 15), pady=5)
        self.user_label.pack()
        self.user_entry = tk.Entry(self.frame, width=25)
        self.user_entry.pack()
        self.password = tk.Label(self.frame, text=("Password"), bg=("black"), foreground=("white"), font=("Arial", 15), pady=5)
        self.password.pack()

