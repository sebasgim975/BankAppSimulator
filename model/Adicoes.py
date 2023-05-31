class Adicoes:
    def __init__(self, record):
        self.__record = record

    def get_record(self, posicao):
        return self.__record[posicao]
    
    def get_categoria(self, posicao):
        return self.__record[posicao][0]
        
    def categoria_gasto_total(self, categoria):
        gasto_total=0
        for i in range(len(self.__record)):
            if self.__record[i][0] == categoria:
                gasto_total+=self.__record[i][2]
        return gasto_total
    
    def media_da_categoria(self, categoria):
        num=0
        for i in range(len(self.__record)):
            if self.__record[i][0] == categoria:
                num+=1
        media=self.categoria_gasto_total(categoria)/num
        return media
    
    def sugestao(self, categoria):
        advice=''
        if categoria == "Casa":
            advice="xxxx"
        if categoria == "Supermercado":
            advice="xxxx"
        if categoria == "Carro":
            advice="xxxx"
        if categoria == "Restaurante":
            advice="xxxx"
        if categoria == "Lazer":
            advice="xxxx"
        if categoria == "Outros":
            advice="xxxx"
        return advice