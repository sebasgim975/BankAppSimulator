class Additions:
    def __init__(self, record):
        # Constructor that initializes the class with a record.
        self.__record = record

    def get_record(self, position):
        # Returns a specific record from the stored records by its position (index).
        return self.__record[position]

    def get_category(self, position):
        # Returns the category of a specific record.
        return self.__record[position][0]

    def category_total_spending(self, category):
        # Calculates the total spending for a specific category.
        total_spending = 0
        for i in range(len(self.__record)):
            # Iterates through the records, summing the spending amounts if they match the specified category.
            if self.__record[i][0] == category:
                total_spending += self.__record[i][2]
        return total_spending

    def category_average(self, category):
        # Calculates the average spending for a specific category.
        num = 0
        for i in range(len(self.__record)):
            # Count how many records are in the specified category.
            if self.__record[i][0] == category:
                num += 1
        # Compute the average by dividing the total spending by the count of records in the category.
        average = self.category_total_spending(category) / num
        return average

    def suggestion(self, category):
        # Provides advice based on the category of spending.
        advice = ""
        # Each if condition checks the category and assigns specific advice accordingly.
        if category == "Housing":
            advice = "Try implementing energy-saving measures to lower your utility bills."
        if category == "Food":
            advice = "In the supermarket, always try to look for promotions whenever possible."
        if category == "Transportation":
            advice = "Consider using public transportation more often, or other forms of mobility."
        if category == "Health":
            advice = "Maintain a healthy diet and regular exercise routine to reduce the risk of chronic diseases."
        if category == "Leisure":
            advice = "Plan and book activities in advance to take advantage of early bird discounts and lower prices."
        if category == "Outros":
            # Provides a general piece of advice for categories not specifically mentioned.
            advice = f"Try to be more cautious with spending on category {category}"
        return advice
