class Pet:

    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
    
    def emitir_som(self):
        return "Som genérico de Pet"
    
    def __str__(self):
        return f"Nome: {self.__nome}, Idade: {self.__idade} anos"