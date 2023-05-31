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
        advice=""
        if categoria == "Casa":
            advice="Tente gastar menos na seção da casa evitando gastos desnecessaários."
        if categoria == "Supermercado":
            advice="No supermercado, tente procurar promoções sempre que possível."
        if categoria == "Carro":
            advice="Considere usar mais os transportes públicos, ou outras formas de mobilidade."
        if categoria == "Restaurante":
            advice="Evite fazer diversas refeições fora de casa."
        if categoria == "Lazer":
            advice="Tente não ser muito dispendioso nos seus gastos no lazer, decerto que outras categorias merecem mais investimento."
        if categoria == "Outros":
            advice=f"Tente gastar menos em/na categoria {categoria}"
        return advice