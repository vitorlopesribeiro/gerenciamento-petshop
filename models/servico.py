class Servico:

    def __init__(self, tipo, valor):
        self.__tipo = tipo
        self.__valor = valor

    def __str__(self):
        return f"Tipo de serviço: {self.__tipo} - Valor do serviço: R${self.__valor:.2f}"