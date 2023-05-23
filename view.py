import tkinter as tk
from controller import *
from tkinter import END, messagebox
from model.AdicoesLinkedList import *
from model.Adicoes import *
from model.Cliente import *
from model.ClientLinkedList import *
import sqlite3


class View:
  def __init__(self, master):
    self.master = master
    self.users = ClientLinkedList()
    self.master.resizable(False, False)
    
    self.frame = tk.Frame(self.master, bg="#92e3a9", padx=300, pady=250)
    self.frame.pack(fill=tk.BOTH, expand=True)
    self.frase = tk.Label(self.frame, text="Sistema de Controlo de Finanças", font=("arial", 20), foreground="black", bg="#92e3a9")
    self.frase.pack()
    
    self.imagem_1 = tk.PhotoImage(file="inico.png")
    self.imagem_1 = self.imagem_1.subsample(2)
    self.imagem_1_label = tk.Label(self.frame, image=self.imagem_1, bg="#92e3a9")
    self.imagem_1_label.pack()
    
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
          
    self.registo_f_button = tk.Button(self.nova_janela,text="Registar",bg="white",font=("Arial",12), width=10,command=self.confirmar_registar)
    self.registo_f_button.grid(row=4,column=4,sticky="w")

            
  def confirmar_registar(self):
    self.user_info = Cliente(self.nome_entry.get(), self.password_entry.get(), self.nif_entry.get())
    if self.users.find_username(self.user_info.get_nome())!=-1:
      messagebox.showerror("Erro", "Username existe")
      self.nova_janela.destroy()
    elif self.users.find_NIF(self.user_info.get_nif())!=-1 or len(self.user_info.get_nif())!=9 or self.user_info.get_nif().isnumeric()==False:
      messagebox.showerror("Erro", "NIF invalido")
      self.nova_janela.destroy()
    elif self.users.size==0:
      posicao=self.users.size
      self.users.insert_first(self.user_info)
      messagebox.showinfo("Succeso", "Username registado")
      self.nova_janela.destroy()
    else:
      posicao=self.users.size
      self.users.insert(self.user_info, posicao)
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
    if self.users.find_login_info(self.nome_entry.get(), self.password_entry.get())==-1:
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

    self.consultar_despesas_button = tk.Button(self.nova_janela,text="Consultar despesas",bg="gray",font=("Arial",12), width=30,command=self.consultar_despesas)
    self.consultar_despesas_button.grid(row=1,column=0,sticky="w")

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
    if self.categoria_de_despesa_entry.get() == '' or self.descricao_de_despesa_entry.get() == '' or self.valor_da_despesa_entry.get() == '' or self.data_da_despesa_entry.get() == '':
        messagebox.showerror("Erro", "Falta prencher adições")
    else:
        conn=sqlite3.connect('despesas.db')
        c=conn.cursor()

        c.execute("INSERT INTO addresses VALUES (:Categoria_de_despesa, :Descricao_de_despesa, :Valor_da_despesa, :Data_da_despesa, :Orçamento)",
          {
            'Categoria_de_despesa': self.categoria_de_despesa_entry.get(),
            'Descricao_de_despesa': self.descricao_de_despesa_entry.get(),
            'Valor_da_despesa': self.valor_da_despesa_entry.get(),
            'Data_da_despesa': self.data_da_despesa_entry.get(),
            'Orçamento': self.salario_entry.get()
          }
          )
        self.categoria_de_despesa_entry.delete(0, END)
        self.descricao_de_despesa_entry.delete(0, END)
        self.valor_da_despesa_entry.delete(0, END)
        self.data_da_despesa_entry.delete(0, END)
        self.salario_entry.delete(0, END)

        c.execute("SELECT * FROM addresses")
        records=c.fetchall()
        print(records)
          
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
    self.records=c.fetchall()

    temp_categoria_de_despesa=[None]*len(self.records)+[None]
    temp_data_da_despesa=[None]*len(self.records)+[None]

    ascendente_descendente=["ascendente", "descendente", "----"]

    for i in range(len(self.records)):
      j=0
      for k in self.records[i]:
        if k == self.records[i][4]:
          break
        consultar_label=tk.Label(self.nova_janela, text=k ,bg="white",foreground="black",font=("Arial",12),width=25, height=1)
        consultar_label.grid(row=i+3, column=j, columnspan=1)
        j+=1

    for i in range(len(self.records)):
      temp_categoria_de_despesa[i]=self.records[i][0]
      temp_data_da_despesa[i]=self.records[i][3]

      temp_categoria_de_despesa[i+1]="----"
      temp_data_da_despesa[i+1]="----"

    categoria_de_despesa = []
    [categoria_de_despesa.append(x) for x in temp_categoria_de_despesa if x not in categoria_de_despesa]
    data_da_despesa = []
    [data_da_despesa.append(x) for x in temp_data_da_despesa if x not in data_da_despesa]

      
    self.clicked_categoria_de_despesa=tk.StringVar()
    self.clicked_categoria_de_despesa.set("----")

    self.clicked_valor_da_despesa=tk.StringVar()
    self.clicked_valor_da_despesa.set("----")

    self.clicked_data_da_despesa=tk.StringVar()
    self.clicked_data_da_despesa.set("----")

    self.drop_categoria_de_despesa=tk.OptionMenu(self.nova_janela, self.clicked_categoria_de_despesa, *categoria_de_despesa).grid(row=1, column=0)
    self.drop_valor_da_despesa=tk.OptionMenu(self.nova_janela, self.clicked_valor_da_despesa, *ascendente_descendente).grid(row=1, column=2)
    self.drop_data_da_despesa=tk.OptionMenu(self.nova_janela, self.clicked_data_da_despesa, *data_da_despesa).grid(row=1, column=3)

    self.button_configure=tk.Button(self.nova_janela, text="Configurar",bg="gray",font=("Arial",12), width=10, command=self.confirmar_configuracao)
    self.button_configure.grid(row=0, column=1)

    self.nova_janela.mainloop()

                
    conn.commit()
    conn.close()


  def confirmar_configuracao(self):
    a=self.clicked_categoria_de_despesa.get()
    b=self.clicked_data_da_despesa.get()
    updated_table=[['' for i in range(4)] for t in range(len(self.records))]
    tabela=Adicoes(self.clicked_categoria_de_despesa.get(), self.clicked_data_da_despesa.get())

    f=0
    for i in range(len(self.records)):         # Limpa a tabela
          j=0
          for k in self.records[i]:
                if k == self.records[i][4]:
                      break
                consultar_label=tk.Label(self.nova_janela, text='' ,bg="white",foreground="black",font=("Arial",12),width=25, height=1)
                consultar_label.grid(row=i+3, column=j, columnspan=1)
                j+=1

    if self.clicked_categoria_de_despesa.get() != "----" and self.clicked_data_da_despesa.get() == "----":
        for i in range(len(self.records)):
            j=0
            for k in self.records[i]:
                if k == self.records[i][4]:
                    break
                elif k == a:
                    for s in self.records[i]:
                        if s == self.records[i][4]:
                            f+=1
                            break
                        else:
                            updated_table[f][j]=s
                            j+=1
                
    f=0
    if self.clicked_categoria_de_despesa.get() == "----" and self.clicked_data_da_despesa.get() != "----":
        for i in range(len(self.records)):
            j=0
            for k in self.records[i]:
                if k == self.records[i][4]:
                    break
                elif k == b:
                    for s in self.records[i]:
                        if s == self.records[i][4]:
                            f+=1
                            break
                        else:
                            updated_table[f][j]=s
                            j+=1
                
    f=0
    if self.clicked_categoria_de_despesa.get() != "----" and self.clicked_data_da_despesa.get() != "----":
      i=0
      j=0
      for k in self.records:
        if k[0] == a and k[3] == b:
          for s in range(len(k)):
            if s == 4:
                i+=1
                f+=1
                j=0
                break
            else:
              updated_table[f][j]=k[j]
              j+=1

    if self.clicked_categoria_de_despesa.get() != "----" or self.clicked_data_da_despesa.get() != "----":
        for i in range(len(updated_table)):
            for k in range(len(updated_table)-i-1):
                if updated_table[k+1][0] == '':
                    break
                if self.clicked_valor_da_despesa.get() == "ascendente":
                  if updated_table[k][2] > updated_table[k+1][2]:
                      temp=updated_table[k+1]
                      updated_table[k+1]=updated_table[k]
                      updated_table[k]=temp
                if self.clicked_valor_da_despesa.get() == "descendente":
                  if updated_table[k][2] < updated_table[k+1][2]:
                      temp=updated_table[k+1]
                      updated_table[k+1]=updated_table[k]
                      updated_table[k]=temp
    elif self.clicked_categoria_de_despesa.get() == "----" and self.clicked_data_da_despesa.get() == "----":
        updated_table=self.records
        for i in range(len(updated_table)):
            for k in range(len(updated_table)-i-1):
                if updated_table[k+1][0] == '':
                    break
                if self.clicked_valor_da_despesa.get() == "ascendente":
                  if updated_table[k][2] > updated_table[k+1][2]:
                      temp=updated_table[k+1]
                      updated_table[k+1]=updated_table[k]
                      updated_table[k]=temp
                if self.clicked_valor_da_despesa.get() == "descendente":
                  if updated_table[k][2] < updated_table[k+1][2]:
                      temp=updated_table[k+1]
                      updated_table[k+1]=updated_table[k]
                      updated_table[k]=temp

    for i in range(len(updated_table)):
          j=0
          for k in updated_table[i]:
                if k == '':
                      break
                consultar_label=tk.Label(self.nova_janela, text=k ,bg="white",foreground="black",font=("Arial",12),width=25, height=1)
                consultar_label.grid(row=i+3, column=j, columnspan=1)
                j+=1








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