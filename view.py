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

    self.orcamento_button = tk.Button(self.nova_janela,text="Orçamento",bg="gray",font=("Arial",12),width=30,command=self.orcamento_mensal)
    self.orcamento_button.grid(row=0,column=0,sticky="w")
      
    self.adicionar_despesas_button = tk.Button(self.nova_janela,text="Adicionar despesas",bg="gray",font=("Arial",12), width=30,command=self.adicionar_despesas)
    self.adicionar_despesas_button.grid(row=1,column=0,sticky="w")

    self.consultar_despesas_button = tk.Button(self.nova_janela,text="Consultar despesas",bg="gray",font=("Arial",12), width=30,command=self.consultar_despesas)
    self.consultar_despesas_button.grid(row=2,column=0,sticky="w")

    self.gasto_mensal_button = tk.Button(self.nova_janela,text="Limite máximo de gastos",bg="gray",font=("Arial",12),width=30,command= self.limitar_gastos)
    self.gasto_mensal_button.grid(row=3,column=0,sticky="w")

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
          
    self.adicionar_button = tk.Button(self.nova_janela,text="Adicionar",bg="gray",font=("Arial",12), width=10,command=self.confirmar_adicao)
    self.adicionar_button.grid(row=5,column=1,sticky="w")


  def confirmar_adicao(self): 
    if self.categoria_de_despesa_entry.get() == '' or self.descricao_de_despesa_entry.get() == '' or self.valor_da_despesa_entry.get() == '' or self.data_da_despesa_entry.get() == '':
        messagebox.showerror("Erro", "Preencha todos os campos.")
    elif self.categoria_de_despesa_entry.get().isnumeric() == True or self.descricao_de_despesa_entry.get().isnumeric() == True or self.data_da_despesa_entry.get().isnumeric() == True:
        messagebox.showerror("Erro", "Input invalido")
    elif self.categoria_de_despesa_entry.get() == self.descricao_de_despesa_entry.get() or self.categoria_de_despesa_entry.get() == self.data_da_despesa_entry.get() or self.descricao_de_despesa_entry.get() == self.data_da_despesa_entry.get():
        messagebox.showerror("Erro", "Input invalido")
    else:        
        try:
          self.valor_da_despesa_atual = float(self.valor_da_despesa_entry.get()) 
        except ValueError:
          messagebox.showerror("Erro", "Valor de despesa invalido")
        
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
            self.salario.set_orcamento(self.orcamento_atual)  

        else:
          if self.orcamento_atual < 0:
            messagebox.showerror("Erro","Ultrapassou do limite do seu orçamento")
          elif self.orcamento_atual <= self.orcamento_inicial*0.1:
            messagebox.showwarning("Aviso","Está próximo de ultrapassar o limite do seu orçamento")
          else:
            self.salario.set_orcamento(self.orcamento_atual)  
             

        conn=sqlite3.connect('despesas.db')
        c=conn.cursor()

        c.execute("INSERT INTO addresses VALUES (:Categoria_de_despesa, :Descricao_de_despesa, :Valor_da_despesa, :Data_da_despesa)",
          {
            'Categoria_de_despesa': self.categoria_de_despesa_entry.get(),
            'Descricao_de_despesa': self.descricao_de_despesa_entry.get(),
            'Valor_da_despesa': self.valor_da_despesa_entry.get(),
            'Data_da_despesa': self.data_da_despesa_entry.get()
          }
          )
        self.categoria_de_despesa_entry.delete(0, END)
        self.descricao_de_despesa_entry.delete(0, END)
        self.valor_da_despesa_entry.delete(0, END)
        self.data_da_despesa_entry.delete(0, END)
          
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
    print(self.records)

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
    tabela_adicoes=AdicoesLinkedList()
    tabela=Adicoes(self.records)

    for i in range(len(self.records)):
           tabela_adicoes.insert(tabela.get_record(i), i)

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
                if k == self.records[i][4]:
                   break
                consultar_label=tk.Label(self.nova_janela, text='' ,bg="white",foreground="black",font=("Arial",12),width=25, height=1)
                consultar_label.grid(row=i+3, column=j, columnspan=1)
                j+=1

          for i in range(tabela_adicoes.size):
                if i > 0 and tabela_adicoes.head.next_node != None:
                   tabela_adicoes.head=tabela_adicoes.head.next_node
                for j in range(len(tabela_adicoes.head.element) - 1):
                  consultar_label=tk.Label(self.nova_janela, text=tabela_adicoes.head.element[j] ,bg="white",foreground="black",font=("Arial",12),width=25, height=1)
                  consultar_label.grid(row=i+3, column=j, columnspan=1)


    if self.clicked_categoria_de_despesa.get() == "----" and self.clicked_data_da_despesa.get() == "----" and self.clicked_valor_da_despesa.get() == "----":
      
          for i in range(len(self.records)):         # Limpa a tabela
            j=0
            for k in self.records[i]:
              if k == self.records[i][4]:
                break
              consultar_label=tk.Label(self.nova_janela, text='' ,bg="white",foreground="black",font=("Arial",12),width=25, height=1)
              consultar_label.grid(row=i+3, column=j, columnspan=1)
              j+=1

          for i in range(len(self.records)):
             j=0
             for k in self.records[i]:
                if k == self.records[i][4]:
                   break
                consultar_label=tk.Label(self.nova_janela, text=k ,bg="white",foreground="black",font=("Arial",12),width=25, height=1)
                consultar_label.grid(row=i+3, column=j, columnspan=1)
                j+=1

      


  def orcamento_mensal(self):
    self.nova_janela = tk.Toplevel()
    self.nova_janela.title("Orçamento mensal")
    self.nova_janela.configure(bg="gray")

    tk.Label(self.nova_janela,text="Escreva o seu salário mensal",bg="gray",font=("Arial",15)).grid(row=0,column=0,sticky="w")
    self.orcamento_mensal_entry = tk.Entry(self.nova_janela)
    self.orcamento_mensal_entry.grid(row=0,column=1,sticky="w")

    self.orcamento_mensal_button = tk.Button(self.nova_janela,text="Adicionar",bg="gray",font=("Arial",12),width=10,command= self.adicionar_salario)
    self.orcamento_mensal_button.grid(row=1,column=1,sticky="w")
  
  def limitar_gastos(self):
    self.nova_janela = tk.Toplevel()
    self.nova_janela.title("Limite máximo de gastos")
    self.nova_janela.configure(bg="gray")

    tk.Label(self.nova_janela,text="Defina um gasto máximo",bg="gray",font=("Arial",15)).grid(row=0,column=0,sticky="w")
    self.gastos_maximos_entry = tk.Entry(self.nova_janela)
    self.gastos_maximos_entry.grid(row=0,column=1,sticky="w")

    self.gastos_maximos_button = tk.Button(self.nova_janela,bg="gray", text="Confirmar", font=("Arial",12),width=10,command=self.gastar)
    self.gastos_maximos_button.grid(row=1,column=1,sticky="w")

  def adicionar_salario(self):
    self.salario = self.orcamento_mensal_entry.get()
    if self.salario != float:
      try:
        self.salario = float(self.salario)
        self.salario = Orcamento(self.salario,0,0,0)
        messagebox.showinfo("","Orçamento adicionado.")
        self.nova_janela.destroy()
      except ValueError:
        messagebox.showerror("Erro","Digite o seu salário em valor númerico")
    
  def gastar(self):
    self.gastos = self.gastos_maximos_entry.get()
    if self.gastos != int or float:
      try:
        self.gastos = float(self.gastos)
        if self.gastos > self.salario.get_orcamento():
          messagebox.showerror("Erro","Orçamento insuficiente.")
        elif self.gastos == self.salario.get_orcamento():
          self.salario.set_gasto_maximo(self.gastos)
          messagebox.showwarning("Aviso","Valor máximo atingido.")
          self.nova_janela.destroy()
        else:
          self.salario.set_gasto_maximo(self.gastos)
          messagebox.showinfo("","Gasto máximo definido com sucesso.")
          self.nova_janela.destroy()
      except ValueError:
        messagebox.showerror("ERRO","O orçamento tem que ser dado númericamente!")
        


      #conn=sqlite3.connect('despesas.db')
      #c=conn.cursor()
      #c.execute("SELECT *, oid FROM addresses")  
      #records=c.fetchall()   <---------- Adições das despesas guardadas no records
      #print(records)
      #conn.commit()
      #conn.close()

      