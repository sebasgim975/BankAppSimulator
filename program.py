import tkinter as tk
from controller import *


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sistema de Controlo de Finanças")
    app = Controller(root)
    root.mainloop()
