class Budget:
    def __init__(self, budget, maximum_expenditure, total_expense_amount, total_expense_amount_spent):
        # Initializer that sets up the budget object with initial values for budget,
        # maximum allowable expenditures, total planned expenses, and actual spending.
        self.__budget = budget
        self.__maximum_expenditure = maximum_expenditure
        self.__total_expense_amount = total_expense_amount
        self.__total_expense_amount_spent = total_expense_amount_spent

    def get_maximum_expenditure(self):
        # Returns the maximum expenditure limit.
        return self.__maximum_expenditure

    def set_maximum_expenditure(self, maximum_expenditure):
        # Updates the maximum expenditure limit to a new value.
        self.__maximum_expenditure = maximum_expenditure

    def get_budget(self):
        # Returns the current budget.
        return self.__budget

    def set_budget(self, budget):
        # Sets the current budget to a new value.
        self.__budget = budget

    def get_total_expense_amount(self):
        # Returns the total planned expense amount. (Note: Fix getter method name consistency)
        return self.__total_expense_amount

    def set_total_expense_amount(self, total_expense_amount):
        # Sets the total planned expense amount to a new value.
        self.__total_expense_amount = total_expense_amount

    def get_total_expense_amount_spent(self):
        # Returns the total amount spent.
        return self.__total_expense_amount_spent

    def set_total_expense_amount_spent(self, total_expense_amount_spent):
        # Updates the total amount spent to a new value.
        self.__total_expense_amount_spent = total_expense_amount_spent

    def remove(self, budget, current_expenses):
        # Calculates the remaining budget after deducting current expenses.
        current_budget = budget - current_expenses
        return current_budget

    def add_expense(self, current_expenses):
        # Adds new expenses to the total planned expenses.
        self.__total_expense_amount += current_expenses

    def expense_add_spendings(self, current_expense_spendings):
        # Adds new actual spending to the total amount spent.
        self.__total_expense_amount_spent += current_expense_spendings
