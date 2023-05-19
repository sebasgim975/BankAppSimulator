import tkinter as tk
from controller import *
from tkinter import END, messagebox
from model.Cliente import *
from model.ClientLinkedList import *
import sqlite3


class View:
    def __init__(self, master):
      self.master = master
      self.frame = tk.Frame(self.master, bg="#92e3a9", padx=350, pady=300)
      self.frame.pack(fill=tk.BOTH, expand=True)
      self.users = ClientLinkedList()
      self.login_registro()



    def login_registro(self):  
        self.login_button = tk.Button(self.frame,text="Login",bg="white",foreground="black",font=("Arial",12),width=20, height=2,command=self.login)
        self.login_button.pack(pady=5)
         
        self.registo_button = tk.Button(self.frame,text="Registo",bg="white",foreground="black",font=("Arial",12),width=20, height=2,command=self.registar)
        self.registo_button.pack(pady=5)


    def registar(self):
            self.nova_janela = tk.Toplevel(self.master, bg="#92e3a9", padx=200, pady=150)
            self.nova_janela.title("Registo")

            tk.Label(self.nova_janela,text="Nome de utilizador",bg= "#92e3a9",font=("Arial",15)).grid(row=0,column=0,sticky="w")
            self.nome_entry = tk.Entry(self.nova_janela)
            self.nome_entry.grid(row=0,column=1,sticky="w")

            tk.Label(self.nova_janela,text="Password",bg= "#92e3a9",font=("Arial",15)).grid(row=1,column=0,sticky="w")
            self.password_entry = tk.Entry(self.nova_janela,show="*")
            self.password_entry.grid(row=1,column=1,sticky="w")

            tk.Label(self.nova_janela,text="NIF",bg= "#92e3a9",font=("Arial",15)).grid(row=2,column=0,sticky="w")
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
        
        self.adicionar_despesas_button = tk.Button(self.nova_janela,text="Adicionar despesas",bg="gray",font=("Arial",12), width=30,command=self.adicionar_despesas)
        self.adicionar_despesas_button.grid(row=0,column=0,sticky="w")

        #self.consultar_despesas_button = tk.Button(self.nova_janela,text="Consultar despesas",bg="gray",font=("Arial",12), width=30,command=self.consultar_despesas)
        #self.consultar_despesas_button.grid(row=1,column=0,sticky="w")

        self.orcamento_mensal_button = tk.Button(self.nova_janela,text="Orçamento mensal",bg="gray",font=("Arial",12),width=30,command= self.orcamento_mensal)
        self.orcamento_mensal_button.grid(row=2,column=0,sticky="w")

    def adicionar_despesas(self):
          self.nova_janela = tk.Toplevel()
          self.nova_janela.title("Adicionar despesas")
          self.nova_janela.configure(bg="gray")

          tk.Label(self.nova_janela,text="Categoria de despesa",bg= "gray",font=("Arial",15)).grid(row=0,column=0,sticky="w")
          self.categoria_de_despesa_entry = tk.Entry(self.nova_janela)
          self.categoria_de_despesa_entry.grid(row=0,column=1,sticky="w")

          tk.Label(self.nova_janela,text="Descrição de despesa",bg= "gray",font=("Arial",15)).grid(row=1,column=0,sticky="w")
          self.descricao_de_despesa_entry = tk.Entry(self.nova_janela,show="*")
          self.descricao_de_despesa_entry.grid(row=1,column=1,sticky="w")

          tk.Label(self.nova_janela,text="Valor da despesa",bg= "gray",font=("Arial",15)).grid(row=2,column=0,sticky="w")
          self.valor_da_despesa_entry= tk.Entry(self.nova_janela)
          self.valor_da_despesa_entry.grid(row=2,column=1,sticky="w")

          tk.Label(self.nova_janela,text="Data da despesa",bg= "gray",font=("Arial",15)).grid(row=3,column=0,sticky="w")
          self.data_da_despesa_entry= tk.Entry(self.nova_janela)
          self.data_da_despesa_entry.grid(row=3,column=1,sticky="w")

          tk.Label(self.nova_janela,text="Orçamento",bg="gray",font=("Arial",15)).grid(row=4,column=0,sticky="w")
          self.salario_entry= tk.Entry(self.nova_janela)
          self.salario_entry.grid(row=4,column=1,sticky="w")
            
          self.adicionar_button = tk.Button(self.nova_janela,text="Adicionar",bg="gray",font=("Arial",12), width=10,command=self.confirmar_adicao)
          self.adicionar_button.grid(row=5,column=1,sticky="w")


    def confirmar_adicao(self): 
          
          conn=sqlite3.connect('despesas.db')
          c=conn.cursor()

          c.execute("INSERT INTO addresses VALUES (:Categoria_de_despesa, :Descricao_de_despesa, :Valor_da_despesa, :Data_da_despesa, :Orcamento)",
                    {
                          'Categoria_de_despesa' : self.categoria_de_despesa_entry.get(),
                          'Descricao_de_despesa' : self.descricao_de_despesa_entry.get(),
                          'Valor_da_despesa' : self.valor_da_despesa_entry.get(),
                          'Data_da_despesa' : self.data_da_despesa_entry.get(),
                          'Orcamento' : self.salario_entry.get()
                    })
          self.categoria_de_despesa_entry.delete(0, END)
          self.descricao_de_despesa_entry.delete(0, END)
          self.valor_da_despesa_entry.delete(0, END)
          self.data_da_despesa_entry.delete(0, END)
          self.salario_entry.delete(0, END)
          
          conn.commit()
          conn.close()

    def consultar_despesas(self):
          self.nova_janela = tk.Toplevel()
          self.nova_janela.title("Consultar despesas")
          self.nova_janela.configure(bg="gray")

          tk.Label(self.nova_janela,text="Categoria de despesa",bg= "gray",font=("Arial",15)).grid(row=2,column=0,sticky="w")
          tk.Label(self.nova_janela,text="Descrição de despesa",bg= "gray",font=("Arial",15)).grid(row=2,column=1,sticky="w")
          tk.Label(self.nova_janela,text="Valor da despesa",bg= "gray",font=("Arial",15)).grid(row=2,column=2,sticky="w")
          tk.Label(self.nova_janela,text="Data da despesa",bg= "gray",font=("Arial",15)).grid(row=2,column=3,sticky="w")

          conn=sqlite3.connect('despesas.db')
          c=conn.cursor()
          c.execute("SELECT * FROM addresses")
          records=c.fetchall()

          categoria_de_despesa=[None]*len(records)
          descrição_de_despesa=[None]*len(records)
          valor_da_despesa=[None]*len(records)
          data_da_despesa=[None]*len(records)

          for i in range(len(records)):
                j=0
                for k in records[i]:
                      if k == records[i][4]:
                            break
                      consultar_label=tk.Label(self.nova_janela, text=k)
                      consultar_label.grid(row=i+3, column=j)
                      j+=1

          for i in range(len(records)):
                categoria_de_despesa[i]=records[i][0]

          for i in range(len(records)):
                descrição_de_despesa[i]=records[i][1]

          for i in range(len(records)):
                valor_da_despesa[i]=records[i][2]

          for i in range(len(records)):
                data_da_despesa[i]=records[i][3]


          self.clicked=tk.StringVar()
          self.clicked.set("----")

          self.drop=tk.OptionMenu(self.nova_janela, self.clicked, *categoria_de_despesa)
          self.drop.pack()

          self.button_configure=tk.Button(self.nova_janela, text="Configurar",bg="gray",font=("Arial",12), width=10, command=self.confirmar_configuracao)
          self.button_configure.grid(row=0, column=1)
          self.button_configure.pack()


          
                      
          conn.commit()
          conn.close()


    def confirmar_configuracao(self):
          conn=sqlite3.connect('despesas.db')
          c=conn.cursor()


          self.label=tk.Label(self.nova_janela, text=self.clicked.get()).pack()


          conn.commit()
          conn.close()






    def orcamento_mensal(self):
      self.nova_janela = tk.Toplevel()
      self.nova_janela.title("Orçamento mensal")
      self.nova_janela.configure(bg="gray")

      tk.Label(self.nova_janela,text="Defina um gasto máximo",bg="gray",font=("Arial",15)).grid(row=0,column=0,sticky="w")
      self.gasto_mensal_entry = tk.Entry(self.nova_janela)
      self.gasto_mensal_entry.grid(row=0,column=1,sticky="w")

      self.gastos_mensais_button = tk.Button(self.nova_janela,text="Confirmar",bg="gray",font=("Arial",12),width=10)
      self.gastos_mensais_button.grid(row=1,column=1,sticky="w")


      #def gastar(self):
      #  salario = self.salario_entry

      #  if gastos > salario:
      #      messagebox.showinfo("Erro","Salário insuficiente.")
      #  elif gastos == salario:
      #      messagebox.showinfo("Aviso","Valor máximo atingido.")
      #  else:
      #      messagebox.showinfo("","Concluido.")


      #conn=sqlite3.connect('despesas.db')
      #c=conn.cursor()
      #c.execute("SELECT *, oid FROM addresses")  
      #records=c.fetchall()   <---------- Adições das despesas guardadas no records
      #print(records)
      #conn.commit()
      #conn.close()