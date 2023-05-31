class Cliente:
    def __init__(self, nome, password, NIF):
        self.__nome = nome
        self.__password = password
        self.__NIF = NIF
        

    def get_nome(self):
        return self.__nome
        
    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    def find_nome(self, user_data):
        if user_data == None:
            return -1
        else:
            j=0
        for i in user_data:
            j+=1
            if self.__nome == i[0]:
                return 1
        if j == len(user_data):
            return -1
        
        
    def get_password(self):
        return self.__password
        
    def set_password(self, nova_password):
        self.__password = nova_password

    def get_nif(self):
        return self.__NIF
        
    def set_nif(self, novo_nif):
        self.__NIF = novo_nif

    def find_nif(self, user_data):
        if user_data == None:
            return -1
        else:
            j=0
        for i in user_data:
            j+=1
            if self.__NIF == i[0]:
                return 1
        if j == len(user_data):
            return -1
        
        
    def find_nome_password(self, user_data):
        if user_data == None:
            return -1
        else:
            j=0
        for i in user_data:
            j+=1
            if self.__nome == i[0] and self.__password == i[1]:
                return 1
        if j == len(user_data):
            return -1
        
    def find_user_nif(self, user_data):
        for i in user_data:
            if self.__nome == i[0] and self.__password == i[1]:
                return i[2]
        
