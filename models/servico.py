class Servico:

    def __init__(self, tipo, valor):
        self.__tipo = tipo
        self.__valor = valor

    def __str__(self):
        return f"{self.__tipo} - R$ {self.__valor:.2f}"