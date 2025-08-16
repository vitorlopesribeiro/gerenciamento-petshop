from datetime import date

class Atendimento:

    def __init__(self, cliente, pet, servico, data=None):
        self.cliente = cliente
        self.pet = pet
        self.servico = servico
        self.data = data if data else date.today()

    def __str__(self):
        return f"{self.data}: {self.servico} para {self.pet} (Cliente: {self.cliente.get_nome()})"