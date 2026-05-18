from classes import PessoaFisica, ContaCorrente, Deposito, Saque


clientes = []
contas = []


def buscar_cliente_por_cpf(cpf):
    # Busca um cliente na lista usando o atributo cpf do objeto.
    for cliente in clientes:
        if cliente.cpf == cpf:
            return cliente

    return None


def criar_cliente():
    nome = input("Digite o nome: ")
    cpf = input("Digite o CPF: ")
    data_nascimento = input("Digite a data de nascimento: ")
    endereco = input("Digite o endereço: ")

    cliente_existente = buscar_cliente_por_cpf(cpf)

    if cliente_existente:
        print("Já existe cliente com esse CPF.")
        return

    cliente = PessoaFisica(
        nome=nome,
        cpf=cpf,
        data_nascimento=data_nascimento,
        endereco=endereco
    )

    clientes.append(cliente)
    print("Cliente criado com sucesso!")


def criar_conta():
    cpf = input("Digite o CPF do cliente: ")
    cliente = buscar_cliente_por_cpf(cpf)

    if not cliente:
        print("Cliente não encontrado.")
        return

    numero_conta = len(contas) + 1

    conta = ContaCorrente.nova_conta(
        cliente=cliente,
        numero=numero_conta
    )

    cliente.adicionar_conta(conta)
    contas.append(conta)

    print("Conta criada com sucesso!")


def listar_contas():
    if not contas:
        print("Nenhuma conta cadastrada.")
        return

    for conta in contas:
        print("=" * 30)
        print(f"Agência: {conta.agencia}")
        print(f"Conta: {conta.numero}")
        print(f"Cliente: {conta.cliente.nome}")
        print(f"CPF: {conta.cliente.cpf}")
        print(f"Saldo: R${conta.saldo:.2f}")


def selecionar_conta_por_cpf():
    cpf = input("Digite o CPF do cliente: ")
    cliente = buscar_cliente_por_cpf(cpf)

    if not cliente:
        print("Cliente não encontrado.")
        return None

    if not cliente.contas:
        print("Cliente não possui conta.")
        return None

    return cliente.contas[0]


def depositar():
    conta = selecionar_conta_por_cpf()

    if not conta:
        return

    valor = float(input("Digite o valor do depósito: "))

    transacao = Deposito(valor)
    conta.cliente.realizar_transacao(conta, transacao)


def sacar():
    conta = selecionar_conta_por_cpf()

    if not conta:
        return

    valor = float(input("Digite o valor do saque: "))

    transacao = Saque(valor)
    conta.cliente.realizar_transacao(conta, transacao)


def exibir_extrato():
    conta = selecionar_conta_por_cpf()

    if not conta:
        return

    print("\n========== EXTRATO ==========")

    if not conta.historico.transacoes:
        print("Nenhuma movimentação realizada.")
    else:
        for transacao in conta.historico.transacoes:
            print(
                f"{transacao['data']} - "
                f"{transacao['tipo']} de R${transacao['valor']:.2f}"
            )

    print(f"\nSaldo atual: R${conta.saldo:.2f}")
    print("=============================")


def menu():
    while True:
        print("\n========= MENU =========")
        print("1 - Criar cliente")
        print("2 - Criar conta")
        print("3 - Depositar")
        print("4 - Sacar")
        print("5 - Exibir extrato")
        print("6 - Listar contas")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_cliente()
        elif opcao == "2":
            criar_conta()
        elif opcao == "3":
            depositar()
        elif opcao == "4":
            sacar()
        elif opcao == "5":
            exibir_extrato()
        elif opcao == "6":
            listar_contas()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")


menu()