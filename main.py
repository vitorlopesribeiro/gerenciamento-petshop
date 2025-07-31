def menu ():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Cadastrar cliente")
        print("2 - Adicionar pet ao cliente")
        print("3 - Listar clientes e seus pets")
        print("4 - Realizar atendimento")
        print("5 - Listar histórico de atendimentos de um pet")
        print("6 - Sair")

        op = input("Escolha a opção: ")

        if op == "6":
            print("Saindo do sistema.")
            break

        else:
            print("Você escolheu a opção", op)

menu()

    