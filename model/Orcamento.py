class Orcamento:
    def __init__(self, orcamento, gasto_maximo, valor_despesa_total, valor_despesa_total_gastos):
        self.__orcamento = orcamento
        self.__gasto_maximo = gasto_maximo
        self.__valor_despesa_total = valor_despesa_total
        self.__valor_despesa_total_gastos = valor_despesa_total_gastos

    def get_gasto_maximo(self):
        return self.__gasto_maximo
    
    def set_gasto_maximo(self,gasto_maximo):
        self.__gasto_maximo = gasto_maximo

    def get_orcamento(self):
        return self.__orcamento
    
    def set_orcamento(self,orcamento):
        self.__orcamento = orcamento

    def get_valor_despesa_total(self):
        return self.__valor_despesa_total_orcamento
    
    def set_valor_despesa_total(self, valor_despesa_total_orcamento):
        self.__valor_despesa_total_orcamento = valor_despesa_total_orcamento
    
    def get_valor_despesa_total_gastos(self):
        return self.__valor_despesa_total_gastos
    
    def set_valor_despesa_total_gastos(self, valor_despesa_total_gastos):
        self.__valor_despesa_total_gastos = valor_despesa_total_gastos

    def retirar(self, orcamento, despesa_atual):
        orcamento_atual = orcamento - despesa_atual
        return orcamento_atual

    def despesa_adicionar(self, despesa_atual):
        self.__valor_despesa_total += despesa_atual

    def despesa_adicionar_gastos(self,despesa_atual_gastos):
        self.__valor_despesa_total_gastos += despesa_atual_gastos

