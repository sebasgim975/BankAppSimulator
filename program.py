import tkinter as tk
from controller import *
from tkinter import *
import sqlite3

conn=sqlite3.connect('despesas.db')
c=conn.cursor()
c.execute("DROP TABLE addresses")
c.execute("""CREATE TABLE if not exists addresses (Categoria_de_despesa text ,Descricao_de_despesa text,Valor_da_despesa float,Data_da_despesa text)""")
conn.commit()
conn.close()



if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sistema de Controlo de Finanças")
    app = Controller(root)
    root.mainloop()



