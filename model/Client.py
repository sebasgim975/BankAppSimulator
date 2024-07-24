class Client:
    def __init__(self, name, password, NIF):
        # Initialize with name, password, and NIF, all set as private attributes.
        self.__name = name
        self.__password = password
        self.__NIF = NIF

    def get_name(self):
        # Return the client's name.
        return self.__name

    def set_name(self, new_name):
        # Update the client's name.
        self.__name = new_name

    def find_name(self, user_data):
        # Check if the client's name exists in the given data; return 1 if found, -1 if not.
        if user_data is None:
            return -1
        for index, user in enumerate(user_data):
            if self.__name == user[0]:
                return 1
        return -1

    def get_password(self):
        # Return the client's password.
        return self.__password

    def set_password(self, new_password):
        # Update the client's password.
        self.__password = new_password

    def get_nif(self):
        # Return the client's NIF.
        return self.__NIF

    def set_nif(self, new_nif):
        # Update the client's NIF.
        self.__NIF = new_nif

    def find_nif(self, user_data):
        # Check if the client's NIF exists in the given data; return 1 if found, -1 if not.
        if user_data is None:
            return -1
        for index, user in enumerate(user_data):
            if self.__NIF == user[0]:
                return 1
        return -1

    def find_name_password(self, user_data):
        # Check if the client's name and password match the given data; return 1 if a match is found, -1 if not.
        if user_data is None:
            return -1
        for index, user in enumerate(user_data):
            if self.__name == user[0] and self.__password == user[1]:
                return 1
        return -1

    def find_user_nif(self, user_data):
        # Return the NIF for the client with a matching name and password in the given data.
        for user in user_data:
            if self.__name == user[0] and self.__password == user[1]:
                return user[2]
