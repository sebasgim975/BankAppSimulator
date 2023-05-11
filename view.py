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

        self.registo_button = tk.Button(self.frame,text="Registo",bg="black",foreground="white",font=("Arial",12),width=10,command=self.registar)
        self.registo_button.pack(pady=5)

        self.login_button = tk.Button(self.frame,text="Login",bg="black",foreground="white",font=("Arial",12),width=10)
        self.login_button.pack(pady=5)

    def registar(self):
            self.nova_janela = tk.Toplevel()
            self.nova_janela.title("Registo")
            self.nova_janela.configure(bg="gray")

            tk.Label(self.nova_janela,text="Nome de utilizador",bg= "gray",font=("Arial",15)).grid(row=0,column=0,sticky="w")
            self.nome_entry = tk.Entry(self.nova_janela)
            self.nome_entry.grid(row=0,column=1,sticky="w")

            tk.Label(self.nova_janela,text="Password",bg= "gray",font=("Arial",15)).grid(row=1,column=0,sticky="w")
            self.password_entry = tk.Entry(self.nova_janela,show="*")
            self.password_entry.grid(row=1,column=1,sticky="w")

            tk.Label(self.nova_janela,text="NIF",bg= "gray",font=("Arial",15)).grid(row=2,column=0,sticky="w")
            self.nif_entry= tk.Entry(self.nova_janela)
            self.nif_entry.grid(row=2,column=1,sticky="w")
            
            self.registo_f_button = tk.Button(self.nova_janela,text="Registar",bg="gray",font=("Arial",12),command=self.registar)
            self.registo_f_button.grid(row=4,column=4,sticky="w")
            self.registo_f_button.pack()

            username = self.nome_entry.get()
            password = self.password_entry.get()
            nif = self.nif_entry.get()
            if self.users.find_username(username) != -1:
                messagebox.showinfo("Erro","Este nome já está registado")
            else:
                 self.users.insert_last(username,password,nif)
                 messagebox.showinfo("","Registo sucedido.")

