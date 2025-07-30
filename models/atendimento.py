from cliente import Cliente
from datetime import date

class Atendimento:

    def __init__(self, cliente, pet, servico, data="30/07/2025"):
        self.cliente = cliente
        self.pet = pet
        self.servico = servico
        self.data = data if data else date.today()

    def __str__(self):
        return f"{self.data}: {self.servico} para {self.pet} (Cliente: {self.cliente.get_nome()})"