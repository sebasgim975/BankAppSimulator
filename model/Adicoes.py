class Cliente:
    def __init__(self, categoria, data):
        self.__categoria = categoria
        self.__data = data

    def get_categoria(self):
        return self.__categoria
        
    def get_data(self):
        return self.__data
        