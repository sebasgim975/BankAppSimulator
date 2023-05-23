class Cliente:
    def __init__(self, nome, password, NIF):
        self.__nome = nome
        self.__password = password
        self.__NIF = NIF

    def get_nome(self):
        return self.__nome
        
    def set_nome(self, novo_nome):
        self.__nome = novo_nome
        
    def get_password(self):
        return self.__password
        
    def set_password(self, nova_password):
        self.__password = nova_password

    def get_nif(self):
        return self.__NIF
        
    def set_nif(self, novo_nif):
        self.__NIF = novo_nif






