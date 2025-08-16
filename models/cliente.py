class Cliente:

    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
        self.__pets = []

    def adicionar_pet(self, pet):
        return self.__pets.append(pet)
    
    def listar_pets(self):
        return [str(pet) for pet in self.__pets]
    
    def listar_pets_enumerados(self):
        return [f"{i+1} - {str(pet)}" for i, pet in enumerate(self.__pets)]
    
    def get_pet_por_indice(self, indice):
        indice_real = indice - 1
        if 0 <= indice_real < len(self.__pets):
            return self.__pets[indice_real]
        return None

    def get_nome(self):
        return self.__nome
    
    def get_cpf(self):
        return self.__cpf
    
    def __str__(self):
        pets_str = ", ".join(self.listar_pets()) if self.__pets else "Nenhum pet cadastrado"
        return f"Cliente: {self.__nome} - Cpf: {self.__cpf} - Pets: {pets_str}"