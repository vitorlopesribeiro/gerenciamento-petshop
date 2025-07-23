class Cliente:

    def __init__(self, nome,cpf):
        self.__nome = nome
        self.__cpf = cpf
        self.__pets = []

    def adicionar_pet(self, pet):
        self.__pets.append(pet)

    def listar_pets(self):
        return [str(p) for p in self.__pets]
    
    def __str__(self):
        return f"Cliente: {self.__nome} - CPF: {self.__cpf}"
    
    def __len__(self):
        return len(self.__pets)
    
    def to_dict(self):
        return{
            "nome":self.__nome,
            "cpf":self.__cpf,
        }
        
