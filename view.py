import tkinter as tk
from controller import *
from tkinter import END, messagebox
from model.LinkedListAdditions import *
from model.Additions import *
from model.Client import *
from model.ClientLinkedList import *
from model.Budget import *
import sqlite3
from tkinter import ttk
from tkcalendar import *


class View:
    def __init__(self, master):
        self.master = master  # The main window of the application
        self.users = ClientLinkedList()  # Initializes a linked list to manage user data

        self.master.resizable(False, False)  # Disables resizing for the window

        # Setting up the main frame with a specific background color and padding
        self.frame = tk.Frame(self.master, bg="#92e3a9", padx=300, pady=250)
        self.frame.pack(fill=tk.BOTH, expand=True)  # Packs the frame to fill the whole window and expand as needed

        # Creating and packing a label with the title of the application
        self.frase = tk.Label(self.frame, text="Financial Control System", font=(
            "Elephant", 30), foreground="#1f453b", bg="#92e3a9")
        self.frase.pack()  # Displays the label in the frame

        # Loading, resizing, and displaying an image labeled as "2.png"
        self.image_2 = tk.PhotoImage(file="2.png")
        self.image_2 = self.image_2.subsample(3)  # Resizes the image by reducing its size

        # Loading, resizing, and setting up another image labeled as "start.png"
        self.image_1 = tk.PhotoImage(file="start.png")
        self.image_1 = self.image_1.subsample(2)  # Resizes the image to half its original size
        self.image_1_label = tk.Label(
            self.frame, image=self.image_1, bg="#92e3a9")  # Places the image in a label
        self.image_1_label.pack()  # Displays the image label in the frame

        # Creating and packing a login button with specific styling and functionality
        self.login_button = tk.Button(self.frame, text="Login", bg="#2e5448", foreground="white", font=(
            "Elephant", 16), width=20, height=2, command=self.login)
        self.login_button.pack(pady=5)  # Adds vertical padding around the button

        # Creating and packing a sign-up button similar to the login button
        self.signUp_button = tk.Button(self.frame, text="Sign Up", bg="#2e5448", foreground="white", font=(
            "Elephant", 16), width=20, height=2, command=self.signing_up)
        self.signUp_button.pack(pady=5)  # Also with vertical padding

    def signing_up(self):
        # Creates a new top-level window with specified background color and padding
        self.new_window = tk.Toplevel(
            self.master, bg="#92e3a9", padx=200, pady=150)
        self.new_window.title("Sign Up")  # Sets the title of the new window

        # Adds a label for the username field
        tk.Label(self.new_window, text="Username", bg="#92e3a9", font=(
            "Times New Roman", 15)).grid(row=0, column=0, sticky="w")
        # Adds an entry widget for inputting the username
        self.name_entry = tk.Entry(self.new_window)
        self.name_entry.grid(row=0, column=1, sticky="w")

        # Adds a label for the password field
        tk.Label(self.new_window, text="Password", bg="#92e3a9", font=(
            "Times New Roman", 15)).grid(row=1, column=0, sticky="w")
        # Adds an entry widget for inputting the password, with characters masked by '*'
        self.password_entry = tk.Entry(self.new_window, show="*")
        self.password_entry.grid(row=1, column=1, sticky="w")

        # Adds a label for the NIF field
        tk.Label(self.new_window, text="NIF", bg="#92e3a9", font=(
            "Times New Roman", 15)).grid(row=2, column=0, sticky="w")
        # Adds an entry widget for inputting the NIF
        self.nif_entry = tk.Entry(self.new_window)
        self.nif_entry.grid(row=2, column=1, sticky="w")

        # Adds a button to submit the sign-up form, linked to the 'confirm_signing_up' method
        self.signUp_f_button = tk.Button(self.new_window, text="Sign Up", bg="#2e5448", foreground="white", font=(
            "Times New Roman", 12), width=10, command=self.confirm_signing_up)
        self.signUp_f_button.grid(row=4, column=4, sticky="w")

    def confirm_signing_up(self):
        # Connects to an SQLite database or creates it if it doesn't exist
        conn = sqlite3.connect('saved_data.db')
        c = conn.cursor()

        # Creates a new table if it does not already exist
        c.execute("""CREATE TABLE if not exists user_data (
                        Username text, Password text, NIF text, Expense_Category text,
                        Expense_Description text, Expense_Amount float, Expense_Date text,
                        Current_Budget float, Initial_Budget float, Maximum_Expenditure float,
                        Total_Expense_Amount float, Total_Expense_Amount_Spent float)""")

        # Fetches all existing user records from the database
        c.execute("SELECT * FROM user_data")
        self.saved_table = c.fetchall()

        # Retrieves user input from the form
        self.user_info = Client(self.name_entry.get(), self.password_entry.get(), self.nif_entry.get())

        # Check if the username already exists in the database
        if self.user_info.find_name(self.saved_table) == 1:
            messagebox.showerror("Error", "Username exists")
            self.new_window.destroy()

        # Validate NIF: check if it exists, has correct length, and is numeric
        elif self.user_info.find_nif(self.saved_table) == 1 or len(
                self.user_info.get_nif()) != 9 or not self.user_info.get_nif().isnumeric():
            messagebox.showerror("Error", "Invalid NIF")
            self.new_window.destroy()

        else:
            # Inserts new user data into the database
            c.execute(
                "INSERT INTO user_data (Username, Password, NIF, Expense_Category, Current_Budget) VALUES (:Username, :Password, :NIF, :Expense_Category, :Current_Budget)",
                {
                    'Username': self.name_entry.get(),
                    'Password': self.password_entry.get(),
                    'NIF': self.nif_entry.get(),
                    'Expense_Category': '',
                    'Current_Budget': ''
                })
            conn.commit()  # Commits changes to the database
            conn.close()  # Closes the connection to the database
            messagebox.showinfo("Success", "User Registered")
            self.new_window.destroy()  # Closes the registration window

    def login(self):
        # Creates a new top-level window for the login interface
        self.new_window = tk.Toplevel(
            self.master, bg="#92e3a9", padx=200, pady=150)
        self.new_window.title("Login")  # Sets the window title to 'Login'

        # Adds a label for the username field and places it using grid layout
        tk.Label(self.new_window, text="Username", bg="#92e3a9", font=(
            "Times New Roman", 15)).grid(row=0, column=0, sticky="w")
        # Creates an entry widget for the username input
        self.name_entry = tk.Entry(self.new_window)
        self.name_entry.grid(row=0, column=1, sticky="w")

        # Adds a label for the password field and places it using grid layout
        tk.Label(self.new_window, text="Password", bg="#92e3a9", font=(
            "Times New Roman", 15)).grid(row=1, column=0, sticky="w")
        # Creates an entry widget for the password input, with characters masked by '*'
        self.password_entry = tk.Entry(self.new_window, show="*")
        self.password_entry.grid(row=1, column=1, sticky="w")

        # Adds a login button, which triggers the confirm_login method when clicked
        self.signUp_f_button = tk.Button(self.new_window, text="Login", bg="#2e5448", foreground="white", font=(
            "Times New Roman", 12), width=10, command=self.confirm_login)
        self.signUp_f_button.grid(row=4, column=4)

    def confirm_login(self):
        # Connect to the SQLite database or create it if it doesn't exist
        conn = sqlite3.connect('saved_data.db')
        c = conn.cursor()

        # Create a table if it doesn't already exist to store user data
        c.execute("""CREATE TABLE if not exists user_data (
                     Username text, Password text, NIF text, Expense_Category text,
                     Expense_Description text, Expense_Amount float, Expense_Date text,
                     Current_Budget float, Initial_Budget float, Maximum_Expenditure float,
                     Total_Expense_Amount float, Total_Expense_Amount_Spent float)""")

        # Retrieve all records from the user_data table
        c.execute("SELECT * FROM user_data")
        self.saved_table = c.fetchall()

        # Create a Client object with the username and password from the entry fields
        self.user_info = Client(
            self.name_entry.get(), self.password_entry.get(), None)

        # Check if the username and password combination exists in the saved data
        if self.user_info.find_name_password(self.saved_table) == -1:
            # Display an error message if the login is invalid
            messagebox.showerror("Error", "Invalid Login")
        else:
            # Retrieve and store current user information upon successful login
            self.current_name = self.name_entry.get()
            self.current_password = self.password_entry.get()
            self.current_nif = self.user_info.find_user_nif(self.saved_table)
            conn.commit()
            conn.close()
            self.new_window.destroy()  # Close the login window
            self.expenses()  # Proceed to the next part of the application

    def expenses(self):
        # Creates a new top-level window for managing expenses
        self.new_window = tk.Toplevel(
            self.master, bg="#92e3a9", padx=200, pady=150)
        self.new_window.title("Expenses")  # Sets the title of the window

        # Displays an image in the new window
        self.image_2_label = tk.Label(
            self.new_window, image=self.image_2, bg="#92e3a9")
        self.image_2_label.pack(pady=10)  # Pads the image vertically for better layout

        # Button to set the budget
        self.budget_button = tk.Button(self.new_window, text="Set Budget", bg="#2e5448", foreground="white", font=(
            "Times New Roman", 14), width=30, command=self.monthly_budget)
        self.budget_button.pack(pady=5)  # Packs the button with vertical padding

        # Button to add new expenses
        self.add_expenses_button = tk.Button(self.new_window, text="Add Expenses", bg="#2e5448", foreground="white",
                                             font=("Times New Roman", 14), width=30, command=self.add_expenses)
        self.add_expenses_button.pack(pady=5)  # Similar padding and styling as the budget button

        # Button to view existing expenses
        self.view_expenses_button = tk.Button(self.new_window, text="View Expenses", bg="#2e5448", foreground="white",
                                              font=("Times New Roman", 14), width=30, command=self.view_expenses)
        self.view_expenses_button.pack(pady=5)

        # Button to set the maximum spending limit
        self.monthly_expenditure_button = tk.Button(self.new_window, text="Maximum Spending Limit", bg="#2e5448",
                                                    foreground="white", font=("Times New Roman", 14), width=30, command=self.limit_spending)
        self.monthly_expenditure_button.pack(pady=5)

        # Button for expense analysis
        self.analysis_button = tk.Button(self.new_window, text="Expense Analysis", bg="#2e5448", foreground="white",
                                         font=("Times New Roman", 14), width=30, command=self.analysis)
        self.analysis_button.pack(pady=5)

    def add_expenses(self):
        # Create a new top-level window for adding expenses
        self.new_window = tk.Toplevel(
            self.master, bg="#92e3a9", padx=200, pady=150)
        self.new_window.title("Add Expenses")  # Set the title of the window

        # Create and grid a label and combobox for selecting the expense category
        tk.Label(self.new_window, text="Expense Category", bg="#92e3a9", font=(
            "Times New Roman", 15)).grid(row=0, column=0, sticky="w")
        self.expense_category_entry = ttk.Combobox(self.new_window, values=[
            "Housing", "Food", "Transportation", "Health", "Leisure"])
        self.expense_category_entry.grid(row=0, column=1, sticky="w")

        # Create and grid a label and entry widget for inputting the expense description
        tk.Label(self.new_window, text="Expense Description", bg="#92e3a9", font=(
            "Times New Roman", 15)).grid(row=1, column=0, sticky="w")
        self.expense_description_entry = tk.Entry(self.new_window)
        self.expense_description_entry.grid(row=1, column=1, sticky="w")

        # Create and grid a label and entry widget for inputting the expense amount
        tk.Label(self.new_window, text="Expense Amount", bg="#92e3a9", font=(
            "Times New Roman", 15)).grid(row=2, column=0, sticky="w")
        self.expense_amount_entry = tk.Entry(self.new_window)
        self.expense_amount_entry.grid(row=2, column=1, sticky="w")

        # Create and grid a label and date entry widget for selecting the expense date
        tk.Label(self.new_window, text="Expense Date", bg="#92e3a9", font=(
            "Times New Roman", 15)).grid(row=3, column=0, sticky="w")
        self.expense_date_entry = DateEntry(self.new_window)
        self.expense_date_entry.grid(row=3, column=1, sticky="w")

        # Create and grid a button to submit the form
        self.add_button = tk.Button(self.new_window, text="Add", bg="gray", font=(
            "Arial", 12), width=10, command=self.error_checking_additions)
        self.add_button.grid(row=5, column=1, sticky="w")

    def error_checking_additions(self):
        # Connect to the SQLite database or create it if it doesn't exist
        conn = sqlite3.connect('saved_data.db')
        c = conn.cursor()

        # Retrieve user input from GUI fields
        self.temp_expense_category = self.expense_category_entry.get()
        self.temp_expense_description = self.expense_description_entry.get()
        self.temp_expense_amount = self.expense_amount_entry.get()
        self.temp_expense_date = self.expense_date_entry.get()

        # Check for empty input fields and display an error message if any field is empty
        if (self.expense_category_entry.get() == '' or self.expense_description_entry.get() == '' or
                self.expense_amount_entry.get() == '' or self.expense_date_entry.get() == ''):
            messagebox.showerror("Error", "Fill in all the fields.")

        # Check for numeric input in non-numeric fields and display an error message
        elif (self.expense_category_entry.get().isnumeric() or self.expense_description_entry.get().isnumeric() or
              self.expense_date_entry.get().isnumeric()):
            messagebox.showerror("Error", "Invalid input")

        # Check for repeated data among fields and display an error message
        elif (self.expense_category_entry.get() == self.expense_description_entry.get() or
              self.expense_category_entry.get() == self.expense_date_entry.get() or
              self.expense_description_entry.get() == self.expense_date_entry.get()):
            messagebox.showerror("Error", "Avoid Repeating Data.")

        else:
            try:
                # Check if the user's budget is set, add salary if not
                if c.execute("SELECT * FROM user_data WHERE Username = ?", (self.current_name,)).fetchone()[7] == '':
                    self.temp_value = 0
                    self.add_salary()
                else:
                    # Fetch user's budget-related data from the database
                    c.execute("SELECT * FROM user_data WHERE Username = ?", (self.current_name,))
                    self.saved_table = c.fetchall()
                    self.Initial_Budget = self.saved_table[0][8]
                    self.maximum_expenditure = self.saved_table[0][9]
                    self.total_expense_amount = self.saved_table[0][10]
                    self.total_expense_amount_spent = self.saved_table[0][11]
                    self.salary = Budget(self.Initial_Budget, self.maximum_expenditure, self.total_expense_amount,
                                         self.total_expense_amount_spent)

                # Convert expense amount to float and update budget
                self.current_expense_amount = float(self.temp_expense_amount)
                self.salary.add_expense(self.current_expense_amount)
                self.Initial_Budget = self.salary.get_budget()
                self.current_budget = self.salary.remove(self.salary.get_budget(), self.current_expense_amount)

                # Check spending against maximum expenditure limit
                if self.salary.get_maximum_expenditure() != 0:
                    self.salary.expense_add_spendings(self.current_expense_amount)
                    x = self.salary.get_maximum_expenditure() - self.salary.get_maximum_expenditure() * 0.1
                    if self.salary.get_maximum_expenditure() < self.salary.get_total_expense_amount_spent():
                        messagebox.showerror("Error", "Exceeded the Maximum Spending Limit")
                    elif x <= self.salary.get_total_expense_amount_spent():
                        messagebox.showwarning("Warning", "You are close to exceeding the maximum spending limit")
                    else:
                        conn.commit()
                        conn.close()
                        self.salary.set_budget(self.current_budget)
                        self.confirm_additions()

                # Check if the current budget is negative or close to limit
                else:
                    if self.current_budget < 0:
                        messagebox.showerror("Error", "You have exceeded your budget limit")
                    elif self.current_budget <= self.Initial_Budget * 0.1:
                        messagebox.showwarning("Warning", "You are close to exceeding your budget limit")
                    else:
                        conn.commit()
                        conn.close()
                        self.salary.set_budget(self.current_budget)
                        self.confirm_additions()

            # Handle exceptions for invalid expense amount entries
            except ValueError:
                messagebox.showerror("Error", "Invalid Expense Amount")

    def confirm_additions(self):
        # Connect to the SQLite database or create it if it doesn't exist
        conn = sqlite3.connect('saved_data.db')
        c = conn.cursor()

        # Fetch all records from user_data to check the current state
        c.execute("SELECT * FROM user_data")
        self.saved_table = c.fetchall()

        # Check if there's already an expense entry for this user
        if c.execute("SELECT * FROM user_data WHERE Username = ?", (self.current_name,)).fetchone()[3] == None:
            # If no previous expense entries exist, update the existing user record with new expense details
            c.execute("UPDATE user_data SET Expense_Category = ? WHERE Username = ?",
                      (self.temp_expense_category, self.current_name,))
            c.execute("UPDATE user_data SET Expense_Description = ? WHERE Username = ?",
                      (self.temp_expense_description, self.current_name,))
            c.execute("UPDATE user_data SET Expense_Amount = ? WHERE Username = ?",
                      (self.temp_expense_amount, self.current_name,))
            c.execute("UPDATE user_data SET Expense_Date = ? WHERE Username = ?",
                      (self.temp_expense_date, self.current_name,))
        else:
            # If other entries exist, insert a new record for the new expense
            c.execute(
                "INSERT INTO user_data VALUES (:Username, :Password, :NIF, :Expense_Category, :Expense_Description, :Expense_Amount, :Expense_Date, :Current_Budget, :Initial_Budget, :Maximum_Expenditure, :Total_Expense_Amount, :Total_Expense_Amount_Spent)",
                {
                    'Username': self.current_name,
                    'Password': self.current_password,
                    'NIF': self.current_nif,
                    'Expense_Category': self.temp_expense_category,
                    'Expense_Description': self.temp_expense_description,
                    'Expense_Amount': self.temp_expense_amount,
                    'Expense_Date': self.temp_expense_date,
                    'Current_Budget': self.current_budget,
                    'Initial_Budget': self.Initial_Budget,
                    'Maximum_Expenditure': 0,  # Default values for new record
                    'Total_Expense_Amount': 0,
                    'Total_Expense_Amount_Spent': 0
                })

        # Clear the form fields after submission
        self.expense_category_entry.delete(0, tk.END)
        self.expense_description_entry.delete(0, tk.END)
        self.expense_amount_entry.delete(0, tk.END)
        self.expense_date_entry.delete(0, tk.END)

        # Commit changes to the database and close the connection
        conn.commit()
        conn.close()

        # Notify the user of successful addition
        messagebox.showinfo("Success", "Expenses Added")

    def view_expenses(self):
        # Connect to the SQLite database or create it if it doesn't exist
        conn = sqlite3.connect('saved_data.db')
        c = conn.cursor()

        # Create a new window for viewing expenses
        self.new_window = tk.Toplevel(
            self.master, bg="#92e3a9", padx=200, pady=150)
        self.new_window.title("View Expenses")  # Title of the new window

        # Setup labels for expense details in the grid
        tk.Label(self.new_window, text="Expense Category", bg="#92e3a9", font=(
            "Times New Roman", 15)).grid(row=2, column=0, sticky="w")
        tk.Label(self.new_window, text="Expense Description", bg="#92e3a9", font=(
            "Times New Roman", 15)).grid(row=2, column=1, sticky="w")
        tk.Label(self.new_window, text="Expense Amount", bg="#92e3a9", font=(
            "Times New Roman", 15)).grid(row=2, column=2, sticky="w")
        tk.Label(self.new_window, text="Expense Date", bg="#92e3a9", font=(
            "Times New Roman", 15)).grid(row=2, column=3, sticky="w")

        # Fetch all expense records for the current user
        self.saved_table = c.execute(
            "SELECT * FROM user_data WHERE Username = ?", (self.current_name,)).fetchall()
        lenght = len(self.saved_table) + 1
        conn.commit()
        conn.close()

        # Initialize arrays for storing unique categories and dates
        temp_category = [None] * lenght
        temp_data = [None] * lenght

        # Fill arrays with data from the database
        for i in range(len(self.saved_table)):
            if i == len(self.saved_table) - 1:
                temp_category[i + 1] = "----"
                temp_data[i + 1] = "----"
            temp_category[i] = self.saved_table[i][3]
            temp_data[i] = self.saved_table[i][6]

        # Extract unique categories and dates to display as options
        self.expenses_category = []
        [self.expenses_category.append(x) for x in temp_category if x not in self.expenses_category]
        self.expense_date = []
        [self.expense_date.append(x) for x in temp_data if x not in self.expense_date]

        # Arrange the data into a grid for display
        self.records = [[None for i in range(4)] for j in range(lenght - 1)]
        for i in range(lenght - 1):
            for k in range(4):
                self.records[i][k] = self.saved_table[i][3 + k]

        # Initialize the table widget
        self.table = Additions(self.records)

        # Create labels for displaying each record
        for i in range(len(self.records)):
            j = 0
            for k in self.records[i]:
                view_label = tk.Label(self.new_window, text=k, bg="white", foreground="black", font=(
                    "Arial", 12), width=25, height=1)
                view_label.grid(row=i + 3, column=j, columnspan=1)
                j += 1

        # Create dropdown menus for sorting or filtering expenses
        ascending_descending = ["ascending", "descending", "----"]
        self.clicked_expense_category = tk.StringVar()
        self.clicked_expense_category.set("----")
        self.clicked_expense_amount = tk.StringVar()
        self.clicked_expense_amount.set("----")
        self.clicked_expense_date = tk.StringVar()
        self.clicked_expense_date.set("----")
        self.drop_expense_category = tk.OptionMenu(
            self.new_window, self.clicked_expense_category, *self.expenses_category).grid(row=1, column=0)
        self.drop_expense_amount = tk.OptionMenu(
            self.new_window, self.clicked_expense_amount, *ascending_descending).grid(row=1, column=2)
        self.drop_expense_date = tk.OptionMenu(
            self.new_window, self.clicked_expense_date, *self.expense_date).grid(row=1, column=3)

        # Button to confirm the selected configurations for filtering or sorting
        self.button_configure = tk.Button(self.new_window, text="Configure", bg="#2e5448", foreground="white", font=(
            "Arial", 12), width=10, command=self.confirm_configuration, padx=5)
        self.button_configure.grid(row=2, column=4)

        # Start the window's main event loop
        self.new_window.mainloop()

    def confirm_configuration(self):
        # Initialize a linked list to handle the sorting and filtering of table records
        table_additions = LinkedListAdditions()

        # Insert all current records into the linked list
        for i in range(len(self.records)):
            table_additions.insert(self.table.get_record(i), i)

        # Filter out records by category if a specific category is selected and no specific date is set
        if self.clicked_expense_category.get() != "----" and self.clicked_expense_date.get() == "----":
            for i in range(len(self.records)):
                table_additions.remove(table_additions.find(
                    self.clicked_expense_category.get(), None, 0, None))

        # Filter out records by date if a specific date is selected and no specific category is set
        if self.clicked_expense_category.get() == "----" and self.clicked_expense_date.get() != "----":
            for i in range(len(self.records)):
                table_additions.remove(table_additions.find(
                    None, self.clicked_expense_date.get(), None, 3))

        # Filter by both category and date if both are selected
        if self.clicked_expense_category.get() != "----" and self.clicked_expense_date.get() != "----":
            for i in range(len(self.records)):
                table_additions.remove(table_additions.find(
                    self.clicked_expense_category.get(), self.clicked_expense_date.get(), 0, 3))

        # Sort the records by amount if a sort order is selected
        if self.clicked_expense_amount.get() != "----":
            table_additions.mergeSort(
                table_additions.head, self.clicked_expense_amount.get())

        # Update the display if any filters or sorting is applied
        if (self.clicked_expense_category.get() != "----" or
                self.clicked_expense_date.get() != "----" or
                self.clicked_expense_amount.get() != "----"):

            # Clear the table display before showing filtered results
            for i in range(len(self.records)):
                j = 0
                for k in self.records[i]:
                    view_label = tk.Label(self.new_window, text='', bg="white", foreground="black", font=(
                        "Arial", 12), width=25, height=1)
                    view_label.grid(row=i + 3, column=j, columnspan=1)
                    j += 1

            # Display the filtered records
            for i in range(table_additions.size):
                if i > 0 and table_additions.head.next_node != None:
                    table_additions.head = table_additions.head.next_node
                for j in range(len(table_additions.head.element)):
                    view_label = tk.Label(self.new_window, text=table_additions.head.element[j], bg="white",
                                          foreground="black", font=(
                            "Arial", 12), width=25, height=1)
                    view_label.grid(row=i + 3, column=j, columnspan=1)

        # Reset the display to show all records if no filters or sorting are applied
        if (self.clicked_expense_category.get() == "----" and
                self.clicked_expense_date.get() == "----" and
                self.clicked_expense_amount.get() == "----"):

            # Clear the table display
            for i in range(len(self.records)):
                j = 0
                for k in self.records[i]:
                    view_label = tk.Label(self.new_window, text='', bg="white", foreground="black", font=(
                        "Arial", 12), width=25, height=1)
                    view_label.grid(row=i + 3, column=j, columnspan=1)
                    j += 1

            # Redisplay all records
            for i in range(len(self.records)):
                j = 0
                for k in self.records[i]:
                    view_label = tk.Label(self.new_window, text=k, bg="white", foreground="black", font=(
                        "Arial", 12), width=25, height=1)
                    view_label.grid(row=i + 3, column=j, columnspan=1)
                    j += 1

    def monthly_budget(self):
        # This variable may be used to indicate a new budget entry or some specific condition handling
        self.temp_value = 1

        # Create a new top-level window for setting the monthly budget
        self.new_window = tk.Toplevel(
            self.master, bg="#92e3a9", padx=200, pady=150)
        self.new_window.title("Monthly Budget")  # Set the window's title

        # Display a label asking the user to input their available monthly budget
        tk.Label(self.new_window, text="Indicate your available monthly budget:",
                 bg="#92e3a9", font=("Times New Roman", 18)).grid(row=0, column=0, sticky="w")

        # Create an entry widget for the user to input their budget
        self.monthly_budget_entry = tk.Entry(self.new_window)
        self.monthly_budget_entry.grid(row=0, column=1, sticky="w")

        # Create a button that will trigger the addition of the budget to the system
        self.monthly_budget_button = tk.Button(self.new_window, text="Add", bg="#2e5448", foreground="white", font=(
            "Times New Roman", 14), width=10, command=self.add_salary)
        self.monthly_budget_button.grid(row=1, column=1, sticky="w")

    def limit_spending(self):
        # Create a new top-level window to set the maximum spending limit
        self.new_window = tk.Toplevel(
            self.master, bg="#92e3a9", padx=200, pady=150)
        self.new_window.title("Maximum spending limit")  # Title of the window

        # Add a label to the window instructing the user to set a maximum spending limit
        tk.Label(self.new_window, text="Set a Maximum Spending", bg="#92e3a9", font=(
            "Times New Roman", 18)).grid(row=0, column=0, sticky="w")

        # Create an entry widget for the user to input their maximum spending limit
        self.max_spending_entry = tk.Entry(self.new_window)
        self.max_spending_entry.grid(row=0, column=1, sticky="w")

        # Create a button that will save the maximum spending limit when clicked
        self.max_spending_button = tk.Button(self.new_window, bg="#2e5448", foreground="white", text="Confirm", font=(
            "Arial", 12), width=10, command=self.spend)
        self.max_spending_button.grid(row=1, column=1, sticky="w")

    def add_salary(self):
        # Connect to the SQLite database or create it if it doesn't exist
        conn = sqlite3.connect('saved_data.db')
        c = conn.cursor()

        # Check if this is the initial setting of the salary or budget
        if self.temp_value == 0:
            self.initial_salary = 0
            self.salary = 0
        else:
            # Retrieve the salary or budget amount from the entry widget
            self.initial_salary = self.monthly_budget_entry.get()
            self.salary = self.monthly_budget_entry.get()

        # Attempt to convert the salary to a float and update the database
        if self.salary != float:
            try:
                self.salary = float(self.salary)  # Convert the salary to float
                temp_salary = float(self.salary)
                # Create a Budget object, assuming it handles budget-related calculations
                self.salary = Budget(self.salary, 0, 0, 0)
                if self.initial_salary != 0:
                    # Insert the new budget information into the database
                    c.execute(
                        "INSERT INTO user_data (Username, Password, NIF, Current_Budget, Initial_Budget, Maximum_Expenditure, Total_Expense_Amount, Total_Expense_Amount_Spent) VALUES (:Username, :Password, :NIF, :Current_Budget, :Initial_Budget, :Maximum_Expenditure, :Total_Expense_Amount, :Total_Expense_Amount_Spent)",
                        {
                            'Username': self.current_name,
                            'Password': self.current_password,
                            'NIF': self.current_nif,
                            'Current_Budget': temp_salary,
                            'Initial_Budget': temp_salary,
                            'Maximum_Expenditure': 0,
                            'Total_Expense_Amount': 0,
                            'Total_Expense_Amount_Spent': 0
                        })
                    # Clean up any old budget entries that might have been incorrectly saved
                    c.execute(
                        "DELETE FROM user_data WHERE Username = ? AND Current_Budget = ''", (self.current_name,))
                conn.commit()  # Commit changes to the database
                conn.close()  # Close the database connection
                # Inform the user that the budget has been added successfully
                if self.initial_salary != 0:
                    messagebox.showinfo("", "Budget Added.")
                self.new_window.destroy()  # Close the configuration window
            except ValueError:
                # Handle cases where the salary entry is not a valid number
                messagebox.showerror(
                    "Error", "Enter your salary as a numeric value")

    def spend(self):
        # Retrieve the spending limit input by the user from the entry widget
        self.spending = self.max_spending_entry.get()

        # Check if the input is a number, attempting to convert it to a float
        if self.spending != int or float:  # This condition will always evaluate to True; see note below
            try:
                self.spending = float(self.spending)  # Try converting the spending input to a float
                # Check if the entered spending exceeds the available budget
                if self.spending > self.salary.get_budget():
                    messagebox.showerror("Error", "Insufficient Budget.")
                # Check if the spending amount matches the exact budget amount
                elif self.spending == self.salary.get_budget():
                    self.salary.set_maximum_expenditure(self.spending)  # Set the spending as the maximum expenditure
                    messagebox.showwarning("Warning", "Maximum Value Reached.")
                    self.new_window.destroy()  # Close the window after setting the value
                else:
                    self.salary.set_maximum_expenditure(self.spending)  # Set the spending as the maximum expenditure
                    messagebox.showinfo("", "Maximum Spending Set Successfully.")
                    self.new_window.destroy()  # Close the window after successful operation
            except ValueError:
                # Handle the case where the conversion to float fails, indicating non-numeric input
                messagebox.showerror("Error", "The budget must be provided numerically!")

    def analysis(self):
        # Connect to the SQLite database or create it if it doesn't exist
        conn = sqlite3.connect('saved_data.db')
        c = conn.cursor()

        # Create a new top-level window for displaying the expense analysis results.
        self.new_window = tk.Toplevel()
        self.new_window.title("Expense Analysis")
        self.new_window.configure(bg="#92e3a9")

        # Execute a SQL query to fetch all records related to the current user.
        self.saved_table = c.execute(
            "SELECT * FROM user_data WHERE Username = ?", (self.current_name,)).fetchall()
        lenght = len(self.saved_table) + 1
        conn.commit()
        conn.close()

        # Prepare arrays to hold categories and data temporally.
        temp_category = [None] * lenght
        temp_data = [None] * lenght

        # Populate the category and data arrays with values from the saved table.
        for i in range(len(self.saved_table)):
            if i == len(self.saved_table) - 1:
                temp_category[i + 1] = "----"
                temp_data[i + 1] = "----"
            temp_category[i] = self.saved_table[i][3]
            temp_data[i] = self.saved_table[i][6]

        # Deduplicate and store unique categories and dates from transactions.
        self.expenses_category = []
        [self.expenses_category.append(x) for x in temp_category if x not in self.expenses_category]
        self.expense_date = []
        [self.expense_date.append(x) for x in temp_data if x not in self.expense_date]

        # Create a record list based on the length of saved table and fill it.
        self.records = [[None for i in range(4)] for j in range(lenght - 1)]
        for i in range(lenght - 1):
            for k in range(4):
                self.records[i][k] = self.saved_table[i][3 + k]

        # Initialize an Additions object and a linked list to manage sorting.
        self.table = Additions(self.records)
        table_additions = LinkedListAdditions()
        for i in range(len(self.records)):
            table_additions.insert(self.table.get_record(i), i)

        # Perform descending and ascending merge sort operations to analyze expenses.
        table_additions.mergeSort(table_additions.head, "descending")
        initial_value = table_additions.head.element[2]
        table_additions.mergeSort(table_additions.head, "ascending")
        current_value = table_additions.head.element[2]

        # Determine the category with the most spending.
        a = 0
        temp_max = ""
        for i in range(len(self.expenses_category) - 1):
            if a != 0:
                if max_spending_category < temp_max:
                    max_spending_category = temp_max
            for k in range(len(self.expenses_category) - 1):
                if self.table.category_total_spending(self.expenses_category[i]) > self.table.category_total_spending(
                        self.expenses_category[k]):
                    temp_max = self.expenses_category[i]
            if a == 0:
                max_spending_category = temp_max
            a = 1

        # Display various budget and expense analysis results on the new window.
        tk.Label(self.new_window, text="Starting Budget", bg="#92e3a9", font=(
            "Times New Roman", 15)).grid(row=0, column=0, sticky="w")
        tk.Label(self.new_window, text=str(initial_value), bg="white", foreground="black", font=(
            "Times New Roman", 12), width=25, height=1).grid(row=0, column=1)
        tk.Label(self.new_window, text="Current Budget", bg="#92e3a9", font=(
            "Times New Roman", 15)).grid(row=1, column=0, sticky="w")
        tk.Label(self.new_window, text=str(current_value), bg="white", foreground="black", font=(
            "Times New Roman", 12), width=25, height=1).grid(row=1, column=1)
        tk.Label(self.new_window, text="Category with the Most Spending", bg="#92e3a9", font=(
            "Times New Roman", 15)).grid(row=2, column=0, sticky="w")
        tk.Label(self.new_window, text=max_spending_category, bg="white", foreground="black", font=(
            "Times New Roman", 12), width=25, height=1).grid(row=2, column=1)
        tk.Label(self.new_window, text=self.table.suggestion(max_spending_category), bg="#92e3a9",
                 foreground="black", font=("Times New Roman", 12), width=25, height=1).grid(row=3)

        # Loop through expense categories to display individual category statistics.
        for i in range(len(self.expenses_category) - 1):
            tk.Label(self.new_window, text=self.expenses_category[i], bg="#92e3a9", foreground="black", font=(
                "Arial", 12), width=25, height=1).grid(row=i + 4, column=0)
            tk.Label(self.new_window, text=str(self.table.category_average(
                self.expenses_category[i])), bg="#92e3a9", foreground="black", font=("Arial", 12), width=25, height=1).grid(row=i + 4, column=1)