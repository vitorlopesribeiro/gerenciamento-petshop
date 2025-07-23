class Servico:

    def __init__(self, tipo, preco):
        self.tipo = tipo
        self.preco = preco

    def __str__(self):
        return f"Serviço: {self.tipo} - Valor: R${self.preco:.2f}"