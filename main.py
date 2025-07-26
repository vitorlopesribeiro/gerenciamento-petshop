from models.cliente import Cliente
from models.pet import Pet

clients = []

def menu():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Cadastrar cliente")
        print("2 - Adicionar pet ao cliente")
        print("3 - Listar clientes e seus pets")
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
            print(F"{novo_pet} \nCadastrado!")
            cpf_pet = input("Digite o CPF do dono do Pet: ").title().strip()
            for i,v in enumerate(clients):
                if clients[i].get_cpf() == cpf_pet:
                    clients[i].adicionar_pet(novo_pet)
                    print(f"Pet: {nome_pet} - Cadastrado ao usuario: {clients[i]}")

        elif op == "3":
            for index,value in enumerate(clients):
                print(f"Usuario {index}:", value)
        
        elif op == "5":
            print("Programa encerrado")
            break

        else:
            print("Opção invalida")

menu()