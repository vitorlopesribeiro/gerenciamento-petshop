from models.cliente import Cliente
from models.pet import Pet
from models.servico import Servico

clients = []

def menu():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Cadastrar cliente")
        print("2 - Adicionar pet ao cliente")
        print("3 - Listar clientes e seus pets")
        print("4 - Realizar Serviço")
        print("5 - Sair")
        
        op = input("Escolha a opção: ")

        if op == "1":
            print("Cadastro de cliente")
            nome = input("Digite seu nome: ").title().strip()
            cpf = input("Digite seu CPF: ")
            novo_cliente = Cliente(nome, cpf)
            clients.append(novo_cliente)
            print(f"{novo_cliente} \nCadastrado!")

        elif op == "2":
            print("Adicionar pet ao cliente")
            nome_pet = input("Digite o nome do Pet: ").title().strip()
            idade_pet = input("Digite a idade do Pet: ")
            novo_pet = Pet(nome_pet, idade_pet)
            cpf_pet = input("Digite o CPF do dono do Pet: ").title().strip()
            for i,v in enumerate(clients):
                if clients[i].get_cpf() == cpf_pet:
                    clients[i].adicionar_pet(novo_pet)
                    print(f"Pet: {nome_pet}")
                    print(f"Cadastrado ao usuario: {clients[i].get_name()}")
                    print(f"Cadastrado com sucesso")

        elif op == "3":
            for index,value in enumerate(clients):
                print(f"Usuario {index}:", value)

        elif op == "4":
            print("Realizar serviço")
            tipo = input("Escolha o tipo de serviço").title()
            valor = float(input("Digite o valor R$:"))
            novo_servico = Servico(tipo,valor)
            print(novo_servico)
        
        elif op == "5":
            print("Programa encerrado")
            break

        else:
            print("Opção invalida")

menu()