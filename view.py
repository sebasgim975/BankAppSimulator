import tkinter as tk
from controller import *
from tkinter import messagebox
from model.Cliente import *
from model.ClientLinkedList import *

class View:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master, bg="gray", padx=75, pady=75)
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.users = ClientLinkedList()


        self.user_label = tk.Label(self.frame, text=("Nome de Utilizador"), bg=("gray"), foreground=("black"), font=("Arial", 15), pady=5)
        self.user_label.pack()
        self.user_entry = tk.Entry(self.frame, width=25)
        self.user_entry.pack()

        self.password_label = tk.Label(self.frame, text=("Password"), bg=("gray"), foreground=("black"), font=("Arial", 15), pady=5)
        self.password_label.pack()
        self.password_entry = tk.Entry(self.frame, width=25, show=("*"))
        self.password_entry.pack()

        self.registo_button = tk.Button(self.frame,text="Registo",bg="black",foreground="white",font=("Arial",12),width=10)
        self.registo_button.pack(pady=5)

        self.login_button = tk.Button(self.frame,text="Login",bg="black",foreground="white",font=("Arial",12),width=10)
        self.login_button.pack(pady=5)

    def registar(self):
        nome = self.user_entry.get()
        if self.users.find_username(nome) != -1:
            messagebox.showerror("Erro", "Username existe")
        elif self.user_entry.size==0:
            posicao = self.users.size
            

