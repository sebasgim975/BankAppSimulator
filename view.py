import tkinter as tk
from controller import *
from tkinter import END, messagebox
from model.AdicoesLinkedList import *
from model.Adicoes import *
from model.Cliente import *
from model.ClientLinkedList import *
from model.Orcamento import *
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
    
    self.imagem_1 = tk.PhotoImage(file="inicio.png")
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
    conn=sqlite3.connect('saved_data.db')
    c=conn.cursor()
    #c.execute("DROP TABLE user_data")
    
    c.execute("""CREATE TABLE if not exists user_data (Nome_do_utilizador text, Password text, NIF text, Categoria_de_despesa text ,Descricao_de_despesa text,Valor_da_despesa float,Data_da_despesa text, Orcamento_actual float, Orcamento_inicial float, Gasto_maximo float, Valor_despesa_total float, Valor_despesa_total_gastos float)""")    
    c.execute("SELECT * FROM user_data")
    self.saved_table=c.fetchall()

    self.user_info = Cliente(self.nome_entry.get(), self.password_entry.get(), self.nif_entry.get())
    if self.user_info.find_nome(self.saved_table) == 1:
       messagebox.showerror("Erro", "Username existe")
       self.nova_janela.destroy()
    elif self.user_info.find_nif(self.saved_table) == 1 or len(self.user_info.get_nif())!=9 or self.user_info.get_nif().isnumeric()==False:
      messagebox.showerror("Erro", "NIF invalido")
      self.nova_janela.destroy()
    else:
      c.execute("INSERT INTO user_data (Nome_do_utilizador, Password, NIF, Categoria_de_despesa, Orcamento_actual)VALUES (:Nome_do_utilizador, :Password, :NIF,  :Categoria_de_despesa, :Orcamento_actual)",
            {
              'Nome_do_utilizador': self.nome_entry.get(),
              'Password': self.password_entry.get(),
              'NIF': self.nif_entry.get(),
              'Categoria_de_despesa': '',
              'Orcamento_actual': ''
            }
            )
      conn.commit()
      conn.close()
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
    conn=sqlite3.connect('saved_data.db')
    c=conn.cursor()
    c.execute("""CREATE TABLE if not exists user_data (Nome_do_utilizador text, Password text, NIF text, Categoria_de_despesa text ,Descricao_de_despesa text,Valor_da_despesa float,Data_da_despesa text, Orcamento_actual float, Orcamento_inicial float, Gasto_maximo float, Valor_despesa_total float, Valor_despesa_total_gastos float)""")    
    c.execute("SELECT * FROM user_data")
    self.saved_table=c.fetchall()
    self.user_info = Cliente(self.nome_entry.get(), self.password_entry.get(),None)
    if self.user_info.find_nome_password(self.saved_table) == -1:
      messagebox.showerror("Erro", "Login invalido")
    else:
      self.nome_actual=self.nome_entry.get()
      self.password_actual=self.password_entry.get()
      self.nif_actual=self.user_info.find_user_nif(self.saved_table)
      conn.commit()
      conn.close()
      self.nova_janela.destroy()
      self.despesas()      
    


  def despesas(self):
    self.nova_janela = tk.Toplevel()
    self.nova_janela.title("Despesas")
    self.nova_janela.configure(bg="gray")

    self.orcamento_button = tk.Button(self.nova_janela,text="Orçamento",bg="gray",font=("Arial",12),width=30,command=self.orcamento_mensal)
    self.orcamento_button.grid(row=0,column=0,sticky="w")
      
    self.adicionar_despesas_button = tk.Button(self.nova_janela,text="Adicionar despesas",bg="gray",font=("Arial",12), width=30,command=self.adicionar_despesas)
    self.adicionar_despesas_button.grid(row=1,column=0,sticky="w")

    self.consultar_despesas_button = tk.Button(self.nova_janela,text="Consultar despesas",bg="gray",font=("Arial",12), width=30,command=self.consultar_despesas)
    self.consultar_despesas_button.grid(row=2,column=0,sticky="w")

    self.analise_button = tk.Button(self.nova_janela,text="Analise das despesas",bg="gray",font=("Arial",12),width=30,command= self.analise)
    self.analise_button.grid(row=4,column=0,sticky="w")

  def adicionar_despesas(self):
    self.nova_janela = tk.Toplevel()
    self.nova_janela.title("Adicionar despesas")
    self.nova_janela.configure(bg="gray")

    tk.Label(self.nova_janela,text="Categoria de despesa",bg= "gray",font=("Arial",15)).grid(row=0,column=0,sticky="w")
    self.categoria_de_despesa_entry = tk.Entry(self.nova_janela)
    self.categoria_de_despesa_entry.grid(row=0,column=1,sticky="w")

    tk.Label(self.nova_janela,text="Descrição de despesa",bg= "gray",font=("Arial",15)).grid(row=1,column=0,sticky="w")
    self.descricao_de_despesa_entry = tk.Entry(self.nova_janela)
    self.descricao_de_despesa_entry.grid(row=1,column=1,sticky="w")

    tk.Label(self.nova_janela,text="Valor da despesa",bg= "gray",font=("Arial",15)).grid(row=2,column=0,sticky="w")
    self.valor_da_despesa_entry= tk.Entry(self.nova_janela)
    self.valor_da_despesa_entry.grid(row=2,column=1,sticky="w")

    tk.Label(self.nova_janela,text="Data da despesa",bg= "gray",font=("Arial",15)).grid(row=3,column=0,sticky="w")
    self.data_da_despesa_entry= tk.Entry(self.nova_janela)
    self.data_da_despesa_entry.grid(row=3,column=1,sticky="w")
          
    self.adicionar_button = tk.Button(self.nova_janela,text="Adicionar",bg="gray",font=("Arial",12), width=10,command=self.error_checking_adicoes)
    self.adicionar_button.grid(row=5,column=1,sticky="w")


  def error_checking_adicoes(self): 
    conn=sqlite3.connect('saved_data.db')
    c=conn.cursor()
    self.temp_categoria_de_despesa=self.categoria_de_despesa_entry.get()
    self.temp_descricao_de_despesa=self.descricao_de_despesa_entry.get()
    self.temp_valor_da_despesa=self.valor_da_despesa_entry.get()
    self.temp_data_da_despesa=self.data_da_despesa_entry.get()

    if self.categoria_de_despesa_entry.get() == '' or self.descricao_de_despesa_entry.get() == '' or self.valor_da_despesa_entry.get() == '' or self.data_da_despesa_entry.get() == '':
        messagebox.showerror("Erro", "Preencha todos os campos.")
    elif self.categoria_de_despesa_entry.get().isnumeric() == True or self.descricao_de_despesa_entry.get().isnumeric() == True or self.data_da_despesa_entry.get().isnumeric() == True:
        messagebox.showerror("Erro", "Input invalido")
    elif self.categoria_de_despesa_entry.get() == self.descricao_de_despesa_entry.get() or self.categoria_de_despesa_entry.get() == self.data_da_despesa_entry.get() or self.descricao_de_despesa_entry.get() == self.data_da_despesa_entry.get():
        messagebox.showerror("Erro", "Input invalido")
    else:        
        try:
          if c.execute("SELECT * FROM user_data WHERE Nome_do_utilizador = ?", (self.nome_actual,)).fetchone()[7] == '':
             self.temp_value=0
             self.adicionar_salario()
          else:
             c.execute("SELECT * FROM user_data WHERE Nome_do_utilizador = ?", (self.nome_actual,))
             self.saved_table=c.fetchall()
             self.orcamento_inicial=self.saved_table[0][8]
             self.gasto_maximo=self.saved_table[0][9]
             self.valor_despesa_total=self.saved_table[0][10]
             self.valor_despesa_total_gastos=self.saved_table[0][11]
             self.salario = Orcamento(self.orcamento_inicial,self.gasto_maximo,self.valor_despesa_total,self.valor_despesa_total_gastos)
          self.valor_da_despesa_atual = float(self.temp_valor_da_despesa) 
          self.salario.despesa_adicionar(self.valor_da_despesa_atual)
          self.orcamento_inicial = self.salario.get_orcamento()
          self.orcamento_atual = self.salario.retirar(self.salario.get_orcamento(),self.valor_da_despesa_atual)
          if self.salario.get_gasto_maximo() != 0:
            self.salario.despesa_adicionar_gastos(self.valor_da_despesa_atual)
            x = self.salario.get_gasto_maximo() - self.salario.get_gasto_maximo()*0.1
            if self.salario.get_gasto_maximo() < self.salario.get_valor_despesa_total_gastos() :
              messagebox.showerror("Erro","Ultrapassou do limite máximo de gastos")
            elif x <= self.salario.get_valor_despesa_total_gastos():
              messagebox.showwarning("Aviso","Está próximo de ultrapassar o limite máximo de gastos")
            else:
              conn.commit()
              conn.close()
              self.salario.set_orcamento(self.orcamento_atual)  
              self.confirmar_adicoes()
          else:
            if self.orcamento_atual < 0:
              messagebox.showerror("Erro","Ultrapassou do limite do seu orçamento")
            elif self.orcamento_atual <= self.orcamento_inicial*0.1:
              messagebox.showwarning("Aviso","Está próximo de ultrapassar o limite do seu orçamento")
            else:
              conn.commit()
              conn.close()
              self.salario.set_orcamento(self.orcamento_atual)  
              self.confirmar_adicoes()
          
        except ValueError:
          messagebox.showerror("Erro", "Valor de despesa invalido")

  def confirmar_adicoes(self):
    conn=sqlite3.connect('saved_data.db')
    c=conn.cursor()
    c.execute("SELECT * FROM user_data")
    self.saved_table=c.fetchall()
    if c.execute("SELECT * FROM user_data WHERE Nome_do_utilizador = ?", (self.nome_actual,)).fetchone()[3] == None:
      c.execute("UPDATE user_data SET Categoria_de_despesa = ? WHERE Nome_do_utilizador = ?", (self.temp_categoria_de_despesa, self.nome_actual,))
      c.execute("UPDATE user_data SET Descricao_de_despesa = ? WHERE Nome_do_utilizador = ?", (self.temp_descricao_de_despesa, self.nome_actual,))
      c.execute("UPDATE user_data SET Valor_da_despesa = ? WHERE Nome_do_utilizador = ?", (self.temp_valor_da_despesa, self.nome_actual,))
      c.execute("UPDATE user_data SET Data_da_despesa = ? WHERE Nome_do_utilizador = ?", (self.temp_data_da_despesa, self.nome_actual,))
    else:             
      c.execute("INSERT INTO user_data VALUES (:Nome_do_utilizador, :Password, :NIF, :Categoria_de_despesa, :Descricao_de_despesa, :Valor_da_despesa, :Data_da_despesa, :Orcamento_actual, :Orcamento_inicial, :Gasto_maximo, :Valor_despesa_total, :Valor_despesa_total_gastos)",
        {
          'Nome_do_utilizador': self.nome_actual,
          'Password': self.password_actual,
          'NIF': self.nif_actual,
          'Categoria_de_despesa': self.temp_categoria_de_despesa,
          'Descricao_de_despesa': self.temp_descricao_de_despesa,
          'Valor_da_despesa': self.temp_valor_da_despesa,
          'Data_da_despesa': self.temp_data_da_despesa,
          'Orcamento_actual': self.orcamento_atual,
          'Orcamento_inicial': self.orcamento_inicial,
          'Gasto_maximo': 0,
          'Valor_despesa_total': 0,
          'Valor_despesa_total_gastos': 0
        }
        )
    self.categoria_de_despesa_entry.delete(0, END)
    self.descricao_de_despesa_entry.delete(0, END)
    self.valor_da_despesa_entry.delete(0, END)
    self.data_da_despesa_entry.delete(0, END)
    
    conn.commit()
    conn.close()

        

  def consultar_despesas(self):
    conn=sqlite3.connect('saved_data.db')
    c=conn.cursor()
    self.nova_janela = tk.Toplevel()
    self.nova_janela.title("Consultar despesas")
    self.nova_janela.configure(bg="gray")

    tk.Label(self.nova_janela,text="Categoria de despesa",bg= "gray",font=("Arial",15)).grid(row=2,column=0,sticky="w")
    tk.Label(self.nova_janela,text="Descrição de despesa",bg= "gray",font=("Arial",15)).grid(row=2,column=1,sticky="w")
    tk.Label(self.nova_janela,text="Valor da despesa",bg= "gray",font=("Arial",15)).grid(row=2,column=2,sticky="w")
    tk.Label(self.nova_janela,text="Data da despesa",bg= "gray",font=("Arial",15)).grid(row=2,column=3,sticky="w")

    self.saved_table=c.execute("SELECT * FROM user_data WHERE Nome_do_utilizador = ?", (self.nome_actual,)).fetchall()
    lenght=len(self.saved_table)+1
    conn.commit()
    conn.close()

    temp_categoria=[None]*lenght
    temp_data=[None]*lenght

    for i in range(len(self.saved_table)):
      if i == len(self.saved_table)-1:
         temp_categoria[i+1]="----"
         temp_data[i+1]="----"
      temp_categoria[i]=self.saved_table[i][3]
      temp_data[i]=self.saved_table[i][6]

    self.categorias_de_despesa = []
    [self.categorias_de_despesa.append(x) for x in temp_categoria if x not in self.categorias_de_despesa]
    self.data_da_despesa = []
    [self.data_da_despesa.append(x) for x in temp_data if x not in self.data_da_despesa]

    self.records=[[None for i in range(4)] for j in range(lenght-1)]
    for i in range(lenght-1):
       for k in range(4):
          self.records[i][k]=self.saved_table[i][3+k]

    self.tabela=Adicoes(self.records)

    for i in range(len(self.records)):
          j=0
          for k in self.records[i]:
            consultar_label=tk.Label(self.nova_janela, text=k ,bg="white",foreground="black",font=("Arial",12),width=25, height=1)
            consultar_label.grid(row=i+3, column=j, columnspan=1)
            j+=1

    ascendente_descendente=["ascendente", "descendente", "----"]

    self.clicked_categoria_de_despesa=tk.StringVar()
    self.clicked_categoria_de_despesa.set("----")

    self.clicked_valor_da_despesa=tk.StringVar()
    self.clicked_valor_da_despesa.set("----")

    self.clicked_data_da_despesa=tk.StringVar()
    self.clicked_data_da_despesa.set("----")

    self.drop_categoria_de_despesa=tk.OptionMenu(self.nova_janela, self.clicked_categoria_de_despesa, *self.categorias_de_despesa).grid(row=1, column=0)
    self.drop_valor_da_despesa=tk.OptionMenu(self.nova_janela, self.clicked_valor_da_despesa, *ascendente_descendente).grid(row=1, column=2)
    self.drop_data_da_despesa=tk.OptionMenu(self.nova_janela, self.clicked_data_da_despesa, *self.data_da_despesa).grid(row=1, column=3)

    self.button_configure=tk.Button(self.nova_janela, text="Configurar",bg="gray",font=("Arial",12), width=10, command=self.confirmar_configuracao)
    self.button_configure.grid(row=0, column=1)

    self.nova_janela.mainloop()



  def confirmar_configuracao(self):
    tabela_adicoes=AdicoesLinkedList()

    for i in range(len(self.records)):
           tabela_adicoes.insert(self.tabela.get_record(i), i)

    if self.clicked_categoria_de_despesa.get() != "----" and self.clicked_data_da_despesa.get() == "----":
        for i in range(len(self.records)):
           tabela_adicoes.remove(tabela_adicoes.find(self.clicked_categoria_de_despesa.get(), None, 0, None))
        
      
    if self.clicked_categoria_de_despesa.get() == "----" and self.clicked_data_da_despesa.get() != "----":
        for i in range(len(self.records)):
           tabela_adicoes.remove(tabela_adicoes.find(None, self.clicked_data_da_despesa.get(), None, 3))
                
  
    if self.clicked_categoria_de_despesa.get() != "----" and self.clicked_data_da_despesa.get() != "----":
      for i in range(len(self.records)):
           tabela_adicoes.remove(tabela_adicoes.find(self.clicked_categoria_de_despesa.get(), self.clicked_data_da_despesa.get(), 0, 3))
           
    if self.clicked_valor_da_despesa.get() != "----":
       tabela_adicoes.mergeSort(tabela_adicoes.head, self.clicked_valor_da_despesa.get())

            
    if self.clicked_categoria_de_despesa.get() != "----" or self.clicked_data_da_despesa.get() != "----" or self.clicked_valor_da_despesa.get() != "----":
      
          for i in range(len(self.records)):         # Limpa a tabela
            j=0
            for k in self.records[i]:
                consultar_label=tk.Label(self.nova_janela, text='' ,bg="white",foreground="black",font=("Arial",12),width=25, height=1)
                consultar_label.grid(row=i+3, column=j, columnspan=1)
                j+=1

          for i in range(tabela_adicoes.size):
                if i > 0 and tabela_adicoes.head.next_node != None:
                   tabela_adicoes.head=tabela_adicoes.head.next_node
                for j in range(len(tabela_adicoes.head.element)):
                  consultar_label=tk.Label(self.nova_janela, text=tabela_adicoes.head.element[j] ,bg="white",foreground="black",font=("Arial",12),width=25, height=1)
                  consultar_label.grid(row=i+3, column=j, columnspan=1)


    if self.clicked_categoria_de_despesa.get() == "----" and self.clicked_data_da_despesa.get() == "----" and self.clicked_valor_da_despesa.get() == "----":
      
          for i in range(len(self.records)):         # Limpa a tabela
            j=0
            for k in self.records[i]:
              consultar_label=tk.Label(self.nova_janela, text='' ,bg="white",foreground="black",font=("Arial",12),width=25, height=1)
              consultar_label.grid(row=i+3, column=j, columnspan=1)
              j+=1

          for i in range(len(self.records)):
             j=0
             for k in self.records[i]:
                consultar_label=tk.Label(self.nova_janela, text=k ,bg="white",foreground="black",font=("Arial",12),width=25, height=1)
                consultar_label.grid(row=i+3, column=j, columnspan=1)
                j+=1

      

  def orcamento_mensal(self):
    self.temp_value=1
    self.nova_janela = tk.Toplevel()
    self.nova_janela.title("Orçamento mensal")
    self.nova_janela.configure(bg="gray")

    tk.Label(self.nova_janela,text="Escreva o seu salário mensal",bg="gray",font=("Arial",15)).grid(row=0,column=0,sticky="w")
    self.orcamento_mensal_entry = tk.Entry(self.nova_janela)
    self.orcamento_mensal_entry.grid(row=0,column=1,sticky="w")

    self.orcamento_mensal_button = tk.Button(self.nova_janela,text="Adicionar",bg="gray",font=("Arial",12),width=10,command= self.adicionar_salario)
    self.orcamento_mensal_button.grid(row=1,column=1,sticky="w")


  def adicionar_salario(self):
    conn=sqlite3.connect('saved_data.db')
    c=conn.cursor()
    
    if self.temp_value == 0:
      self.initial_salario = 0
      self.salario = 0
    else:
       self.initial_salario = self.orcamento_mensal_entry.get()
       self.salario = self.orcamento_mensal_entry.get()
       
    if self.salario != float:
      try:
        self.salario = float(self.salario)
        temp_salario = float(self.salario)
        self.salario = Orcamento(self.salario,0,0,0)
        if self.initial_salario !=0:
           c.execute("INSERT INTO user_data (Nome_do_utilizador, Password, NIF, Orcamento_actual, Orcamento_inicial, Gasto_maximo, Valor_despesa_total, Valor_despesa_total_gastos) VALUES (:Nome_do_utilizador, :Password, :NIF, :Orcamento_actual, :Orcamento_inicial, :Gasto_maximo, :Valor_despesa_total, :Valor_despesa_total_gastos)",
            {
              'Nome_do_utilizador': self.nome_actual,
              'Password': self.password_actual,
              'NIF':self.nif_actual,
              'Categoria_de_despesa': '',
              'Orcamento_actual': temp_salario,
              'Orcamento_inicial': temp_salario,
              'Gasto_maximo': 0,
              'Valor_despesa_total': 0,
              'Valor_despesa_total_gastos': 0
            }
            )
           c.execute("DELETE FROM user_data WHERE Nome_do_utilizador = ? AND Orcamento_actual = ''", (self.nome_actual,))
        conn.commit()
        conn.close()
        if self.initial_salario != 0:
           messagebox.showinfo("","Orçamento adicionado.")
        self.nova_janela.destroy()
      except ValueError:
        messagebox.showerror("Erro","Digite o seu salário em valor númerico")
    

  def analise(self):
    conn=sqlite3.connect('saved_data.db')
    c=conn.cursor()
    self.nova_janela = tk.Toplevel()
    self.nova_janela.title("Analise de despesas")
    self.nova_janela.configure(bg="gray")

    self.saved_table=c.execute("SELECT * FROM user_data WHERE Nome_do_utilizador = ?", (self.nome_actual,)).fetchall()
    lenght=len(self.saved_table)+1
    conn.commit()
    conn.close()

    temp_categoria=[None]*lenght
    temp_data=[None]*lenght

    for i in range(len(self.saved_table)):
      if i == len(self.saved_table)-1:
         temp_categoria[i+1]="----"
         temp_data[i+1]="----"
      temp_categoria[i]=self.saved_table[i][3]
      temp_data[i]=self.saved_table[i][6]

    self.categorias_de_despesa = []
    [self.categorias_de_despesa.append(x) for x in temp_categoria if x not in self.categorias_de_despesa]
    self.data_da_despesa = []
    [self.data_da_despesa.append(x) for x in temp_data if x not in self.data_da_despesa]


    self.records=[[None for i in range(4)] for j in range(lenght-1)]
    for i in range(lenght-1):
       for k in range(4):
          self.records[i][k]=self.saved_table[i][3+k]

    self.tabela=Adicoes(self.records)
    tabela_adicoes=AdicoesLinkedList()
    for i in range(len(self.records)):
           tabela_adicoes.insert(self.tabela.get_record(i), i)

    tabela_adicoes.mergeSort(tabela_adicoes.head, "descendente")
    valor_inicial=tabela_adicoes.head.element[2]
    tabela_adicoes.mergeSort(tabela_adicoes.head, "ascendente")
    valor_actual=tabela_adicoes.head.element[2]

    a=0
    for i in range(len(self.categorias_de_despesa)-1):
       if a != 0:
          if categoria_gasto_max < temp_max:
             categoria_gasto_max=temp_max
       for k in range(len(self.categorias_de_despesa)-1):
          if self.tabela.categoria_gasto_total(self.categorias_de_despesa[i]) > self.tabela.categoria_gasto_total(self.categorias_de_despesa[k]):
             temp_max=self.categorias_de_despesa[i]
       if a == 0:
          categoria_gasto_max=temp_max
       a=1



    

    tk.Label(self.nova_janela,text="Orçamento_inicial",bg= "gray",font=("Arial",15)).grid(row=0,column=0,sticky="w")
    tk.Label(self.nova_janela, text=str(valor_inicial) ,bg="white",foreground="black",font=("Arial",12),width=25, height=1).grid(row=0, column=1)
    tk.Label(self.nova_janela,text="Orçamento_actual",bg= "gray",font=("Arial",15)).grid(row=1,column=0,sticky="w")
    tk.Label(self.nova_janela, text=str(valor_actual) ,bg="white",foreground="black",font=("Arial",12),width=25, height=1).grid(row=1, column=1)
    tk.Label(self.nova_janela,text="Categoria mais gasta",bg= "gray",font=("Arial",15)).grid(row=2,column=0,sticky="w")
    tk.Label(self.nova_janela, text=categoria_gasto_max ,bg="white",foreground="black",font=("Arial",12),width=25, height=1).grid(row=2, column=1)
    tk.Label(self.nova_janela, text=self.tabela.sugestao(categoria_gasto_max) ,bg="white",foreground="black",font=("Arial",12),width=25, height=1).grid(row=3)


    for i in range(len(self.categorias_de_despesa)-1):
      tk.Label(self.nova_janela, text=self.categorias_de_despesa[i] ,bg="white",foreground="black",font=("Arial",12),width=25, height=1).grid(row=i+4, column=0)
      tk.Label(self.nova_janela, text=str(self.tabela.media_da_categoria(self.categorias_de_despesa[i])) ,bg="white",foreground="black",font=("Arial",12),width=25, height=1).grid(row=i+4, column=1)