import tkinter as tk
from controller import *
from tkinter import *

if __name__ == "__main__":  # Ensures the code only runs if the module is executed as the main program
    root = Tk()  # Creating the main window for the application
    root.title("Financial Control System")  # Setting the title of the main window
    app = Controller(root)  # Creating an instance of Controller, passing the main window (root) as an argument
    root.mainloop()  # Starting the Tkinter event loop to wait for events and update the GUI accordingly


