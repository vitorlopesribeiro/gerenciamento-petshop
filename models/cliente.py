class Cliente:

    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
        self.__pets = []

    def adicionar_pet(self, pet):
        return self.__pets.append(pet)
    
    def listar_pets(self):
        return [str(pet) for pet in self.__pets]
    

    def get_nome(self):
        return self.__nome
    
    def get_cpf(self):
        return self.__cpf
    
    def __str__(self):
        pets_str = ", ".join(self.listar_pets) if self.__pets else "Nenhum pet cadastrado"
        return f"Cliente: {self.__nome} - Cpf: {self.__cpf} - Pets: {pets_str}"