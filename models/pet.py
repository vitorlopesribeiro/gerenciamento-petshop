class Pet:

    def __init__(self, nome, idade, especie):
        self.__nome = nome
        self.__idade = idade
        self.__especie = especie
        self.__historico_de_servico = []

    def adicionar_servico(self, atendimento):
        return self.__historico_de_servico.append(atendimento)
    
    def listar_servico(self):
        return [str(s) for s in self.__historico_de_servico]
    
    def __str__(self):
        return f"Pet: {self.__nome}({self.__especie}, {self.__idade} anos)"

    