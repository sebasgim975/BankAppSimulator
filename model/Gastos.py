class Gastos:
    def __init__(self,gasto_maximo):
        self.__gasto_maximo = gasto_maximo

    def get_gasto_maximo(self):
        return self.__gasto_maximo
    
    def set_gasto_maximo(self,novo_gasto_limite):
        self.__gasto_maximo = novo_gasto_limite