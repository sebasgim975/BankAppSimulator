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
        self.login_registro()



    def login_registro(self):

        
        self.login_button = tk.Button(self.frame,text="Login",bg="black",foreground="white",font=("Arial",12),width=10)
        self.login_button.pack(pady=5)
         
        self.registo_button = tk.Button(self.frame,text="Registo",bg="black",foreground="white",font=("Arial",12),width=10,command=self.registar)
        self.registo_button.pack(pady=5)



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
            
            self.registo_f_button = tk.Button(self.nova_janela,text="Registar",bg="gray",font=("Arial",12), width=10,command=self.confirmar_registar)
            self.registo_f_button.grid(row=4,column=4,sticky="w")

            
            



    def confirmar_registar(self):
              nome =  self.nome_entry.get()
              password=self.password_entry.get()
              NIF=self.nif_entry.get()
              user_info=[nome, password, NIF]
              if self.users.find_username(user_info[0])!=-1:
                    messagebox.showerror("Erro", "Username existe")
                    self.nova_janela.destroy()
              elif self.users.find_NIF(user_info[2])!=-1 or len(user_info[2])!=9 or user_info[2].isnumeric==False:
                    messagebox.showerror("Erro", "NIF invalido")
                    self.nova_janela.destroy()
              elif self.users.size==0:
                    posicao=self.users.size
                    self.users.insert_first(user_info)
                    messagebox.showinfo("Succeso", "Username registado")
                    self.nova_janela.destroy()
              else:
                    posicao=self.users.size
                    self.users.insert(user_info, posicao)
                    messagebox.showinfo("Succeso", "Username registado")
                    self.nova_janela.destroy()


