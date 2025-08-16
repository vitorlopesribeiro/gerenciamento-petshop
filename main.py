from models.cliente import Cliente
from models.pet import Pet
from models.servico import Servico
from models.atendimento import Atendimento

clientes = []

def buscar_cliente_por_cpf(cpf: str):
    for cliente in clientes:
        if cliente.get_cpf() == cpf:
            return cliente
        
    return None

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

        if op == "1":
            print("Cadastrar Cliente")
            nome = input("Nome do cliente: ").title().strip()
            cpf = input("CPF do cliente: ").strip()
            cliente = Cliente(nome, cpf)
            clientes.append(cliente)
            print(f"Cliente {nome} cadastrado!")

        elif op == "2":
            print("Adicionar pet ao cliente")
            cpf = input("Cpf do cliente:").strip()
            cliente = buscar_cliente_por_cpf(cpf)
            if cliente:
                nome_pet = input("Nome do pet:").title().strip()
                idade_pet = input("Idade do pet:")
                especie_pet = input("Espécie do pet:").title().strip()
                pet = Pet(nome_pet, idade_pet, especie_pet)
                cliente.adicionar_pet(pet)
                print(f"✅ Pet {nome_pet} cadastrado ao {cliente.get_nome()}!")
            else:
                print("⚠ Cliente não cadastrado.")

        elif op == "3":
            print("Listar clientes e seus pets")
            if not clientes:
                print("⚠ Nenhum cliente cadastrado.")
            for cliente in clientes:
                print(cliente)

        elif op == "4":
            print("Realizar Atendimento")
            cpf = input("CPF do cliente: ").strip()
            cliente = buscar_cliente_por_cpf(cpf)
            if cliente:
                pets_enumerados = cliente.listar_pets_enumerados()
                if not pets_enumerados:
                    print("⚠ Cliente não possui pets cadastrados.")
                    continue
                print("\nPets do cliente:")
                for p in pets_enumerados:
                    print(p)
                escolha = int(input("Escolha o pet: "))
                pet = cliente.get_pet_por_indice(escolha)

                if pet:
                    tipo_servico = input("Tipo de serviço: ").title().strip()
                    valor_servico = float(input("Valor do serviço: "))
                    servico = Servico(tipo_servico, valor_servico)
                    atendimento = Atendimento(cliente, pet, servico)
                    print(f"✅ Atendimento registrado: {atendimento}")
                    pet.adicionar_servico(atendimento)
                else:
                    print("⚠ Pet inválido.")
            else:
                print("⚠ Cliente não encontrado.")
        
        elif op == "5":
            cpf = input("CPF do cliente: ").strip()
            cliente = buscar_cliente_por_cpf(cpf)
            if cliente:
                pets_numerados = cliente.listar_pets_enumerados()
                if not pets_numerados:
                    print("⚠ Cliente não possui pets cadastrados.")
                    continue
                for p in pets_numerados:
                    print(p)
                escolha = int(input("Escolha o pet: "))
                pet = cliente.get_pet_por_indice(escolha)

                if pet:
                    historico = pet.listar_servico()
                    if historico:
                        print("\nHistórico de atendimentos:")
                        for h in historico:
                            print(h)
                    else:
                        print("⚠ Nenhum atendimento para este pet.")
                else:
                    print("⚠ Pet inválido.")
            else:
                print("⚠ Cliente não encontrado.")

        elif op == "6":
            print("👋 Saindo do sistema.")
            break

        else:
            print("⚠ Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()

    