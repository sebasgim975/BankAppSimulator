class Adicoes:
    def __init__(self, record):
        self.__record = record

    def get_record(self, posicao):
        return self.__record[posicao]
    
    def get_categoria(self, elemento):
        for i in range(len(self.__record)):
            if self.__record[i][0] == elemento:
                return elemento
        
        