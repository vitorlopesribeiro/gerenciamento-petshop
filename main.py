from models.cliente import Cliente

clients = []

def menu():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Cadastrar cliente")
        print("2 - Adicionar pet ao cliente")
        print("3 - Listar clientes e seus pets")
        print("4 - Criar serviço")
        print("5 - Sair")
        
        op = input("Escolha a opção: ")

        if op == "1":
            print("Cadastro de cliente")
            nome = input("Digite seu nome: ").title().strip()
            cpf = input("Digite seu CPF: ")
            novo_cliente = Cliente(nome, cpf)  
            clients.append(novo_cliente.to_dict())
            print(clients)
            print(f"{novo_cliente} \nCadastrado!")

        
        elif op == "5":
            print("Programa encerrado")
            break

        else:
            print("Opção invalida")

menu()