import tkinter as tk
from controller import *
from tkinter import END, messagebox
from model.Cliente import *
from model.ClientLinkedList import *
import sqlite3



class View:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master, bg="gray", padx=75, pady=75)
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.users = ClientLinkedList()
        self.login_registro()



    def login_registro(self):

        
        self.login_button = tk.Button(self.frame,text="Login",bg="black",foreground="white",font=("Arial",12),width=10, command=self.login)
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

    
    def login(self):
            self.nova_janela = tk.Toplevel()
            self.nova_janela.title("Login")
            self.nova_janela.configure(bg="gray")

            tk.Label(self.nova_janela,text="Nome de utilizador",bg= "gray",font=("Arial",15)).grid(row=0,column=0,sticky="w")
            self.nome_entry = tk.Entry(self.nova_janela)
            self.nome_entry.grid(row=0,column=1,sticky="w")

            tk.Label(self.nova_janela,text="Password",bg= "gray",font=("Arial",15)).grid(row=1,column=0,sticky="w")
            self.password_entry = tk.Entry(self.nova_janela,show="*")
            self.password_entry.grid(row=1,column=1,sticky="w")
            
            self.registo_f_button = tk.Button(self.nova_janela,text="Login",bg="gray",font=("Arial",12), width=10,command=self.confirmar_login)
            self.registo_f_button.grid(row=4,column=4,sticky="w")

    
    def confirmar_login(self):
              nome =  self.nome_entry.get()
              password=self.password_entry.get()
              user_info=[nome, password]
              if self.users.find_login_info(user_info)==-1:
                    messagebox.showerror("Erro", "Login incorreto")
                    self.nova_janela.destroy()
              else:
                     self.nova_janela.destroy()
                     self.despesas()


    def despesas(self):
        self.nova_janela = tk.Toplevel()
        self.nova_janela.title("Despesas")
        self.nova_janela.configure(bg="gray")
        
        self.adicionar_despesas_button = tk.Button(self.nova_janela,text="Adicionar despesas",bg="gray",font=("Arial",12), width=10,command=self.adicionar_despesas)
        self.adicionar_despesas_button.grid(row=0,column=1,sticky="w")

        self.consultar_despesas_button = tk.Button(self.nova_janela,text="Consultar despesas",bg="gray",font=("Arial",12), width=10,command=self.consultar_despesas)
        self.consultar_despesas_button.grid(row=1,column=1,sticky="w")

    def adicionar_despesas(self):
          self.nova_janela = tk.Toplevel()
          self.nova_janela.title("Adicionar despesas")
          self.nova_janela.configure(bg="gray")

          tk.Label(self.nova_janela,text="Categoria de despesa",bg= "gray",font=("Arial",15)).grid(row=0,column=0,sticky="w")
          self.Categoria_de_despesa_entry = tk.Entry(self.nova_janela)
          self.Categoria_de_despesa_entry.grid(row=0,column=1,sticky="w")

          tk.Label(self.nova_janela,text="Descrição de despesa",bg= "gray",font=("Arial",15)).grid(row=1,column=0,sticky="w")
          self.Descricao_de_despesa_entry = tk.Entry(self.nova_janela,show="*")
          self.Descricao_de_despesa_entry.grid(row=1,column=1,sticky="w")

          tk.Label(self.nova_janela,text="Valor da despesa",bg= "gray",font=("Arial",15)).grid(row=2,column=0,sticky="w")
          self.Valor_da_despesa_entry= tk.Entry(self.nova_janela)
          self.Valor_da_despesa_entry.grid(row=2,column=1,sticky="w")

          tk.Label(self.nova_janela,text="Data da despesa",bg= "gray",font=("Arial",15)).grid(row=3,column=0,sticky="w")
          self.Data_da_despesa_entry= tk.Entry(self.nova_janela)
          self.Data_da_despesa_entry.grid(row=3,column=1,sticky="w")
            
          self.adicionar_button = tk.Button(self.nova_janela,text="Adicionar",bg="gray",font=("Arial",12), width=10,command=self.confirmar_adicao)
          self.adicionar_button.grid(row=4,column=1,sticky="w")


    def confirmar_adicao(self): 
          conn=sqlite3.connect('despesas.db')
          c=conn.cursor()

          self.Categoria_de_despesa_entry.delete(0, END)
          self.Descricao_de_despesa_entry.delete(0, END)
          self.Valor_da_despesa_entry.delete(0, END)
          self.Data_da_despesa_entry.delete(0, END)

          c.execute("INSERT INTO addresses VALUES (:Categoria_de_despesa, :Descricao_de_despesa, :Valor_da_despesa, :Data_da_despesa)",
                    {
                          'Categoria_de_despesa': self.Categoria_de_despesa_entry.get(),
                          'Descricao_de_despesa': self.Descricao_de_despesa_entry.get(),
                          'Valor_da_despesa': self.Valor_da_despesa_entry.get(),
                          'Data_da_despesa': self.Data_da_despesa_entry.get()
                    }
                    )
          
          conn.commit()
          conn.close()

    def consultar_despesas(self):
          a=0

      



      
          
          
          






        


