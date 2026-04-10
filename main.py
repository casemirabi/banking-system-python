import banking
import users
from datetime import datetime

users.carregarUsuarios()
valorEscolhido = 0

def mostrarExtrato(usuario, tipo_filtro=None):
    print("\n==== EXTRATO ====")

    movimentacoes = usuario['extrato']

    if tipo_filtro:
        movimentacoes = [
            item for item in movimentacoes
            if item["tipo"] == tipo_filtro
        ]

    if not movimentacoes:
        print("Nenhuma movimentação encontrada.")
    else:
        for item in movimentacoes:
            print(f"{item['data']} - {item['tipo'].capitalize()} de R${item['valor']}")

    print(f"\nSaldo atual: R${usuario['saldo']}")
    print("===================\n")

def quantidadeDeTransacoes(usuario):
    contador = 0
    hoje = datetime.today().strftime("%d/%m/$Y")

    for extract in usuario["extrato"]:
        data_transacao = extract["data"].split()[0]

        if extract["tipo"] == "deposito" and data_transacao == hoje:
            contador += 1

    if contador >= 10:
        print(f"Excedeu o limite do dia! Você fez {contador} depósitos hoje.")
        return False
    else:
        return True

def formatoDataHora(data):
    mascaraPTBR = "%d/%m/%Y %H:%M"
    return data.strftime(mascaraPTBR)

def valorDaTransacao():
    global valorEscolhido
    valorEscolhido = int(input("Digite um valor: "))
    return valorEscolhido
    
def menu():
    print("\n===== Digite uma opção: =====")
    print("1: Realizar um deposito")
    print("2: Fazer um saque")
    print("3: Extrato")
    print("4: Criar conta")
    print("5: Listar Contas")
    print("6: Sair")
    
while (True):
    menu()
    option = input("\nEscolha uma opção: ")
    
    if option == "1":
        cpf = input("Digite o CPF do usuário: ")
        usuario = users.buscarUsuarioPorCPF(cpf)
        
        if not usuario:
            print("Usuário não encontrado.")
            continue
        
        result = quantidadeDeTransacoes(usuario)
        
        if result:
            valorDaTransacao()
            
            sucesso = banking.deposito(usuario, valorEscolhido)
            
            if sucesso:
                dataHoraAtual = datetime.now()
                dataHoraAtual = formatoDataHora(dataHoraAtual)
                #usuario["extrato"].append(f"{dataHoraAtual} - Deposito de R${valorEscolhido}")
                usuario["extrato"].append({
                    "tipo": "deposito",
                    "valor": valorEscolhido,
                    "data": dataHoraAtual
                })
                
                users.salvarUsuarios()
            
        else:
            print("Você excedeu o limite de depósitos do dia!")
    

    if option == "2":
        
        cpf = input("Digite o CPF do usuário: ")
        usuario = users.buscarUsuarioPorCPF(cpf)
        
        if not usuario:
            print("Usuário não encontrado.")
            continue
        
        valorDaTransacao()
        sucesso = banking.saque(usuario, valorEscolhido)
        
        if sucesso:
            dataHoraAtual = datetime.now()
            dataHoraAtual = formatoDataHora(dataHoraAtual)
            #usuario["extrato"].append(f"{dataHoraAtual} - Saque de R${valorEscolhido}")
            usuario["extrato"].append({
                    "tipo": "saque",
                    "valor": valorEscolhido,
                    "data": dataHoraAtual
                })
            users.salvarUsuarios()



    if option == "3":
        cpf = input("Digite o CPF do usuário: ")
        usuario = users.buscarUsuarioPorCPF(cpf)

        if not usuario:
            print("Usuário não encontrado.")
            continue

        print("\n1 - Mostrar tudo")
        print("2 - Apenas depósitos")
        print("3 - Apenas saques")

        filtro = input("Escolha uma opção: ")

        if filtro == "1":
            mostrarExtrato(usuario)
        elif filtro == "2":
            mostrarExtrato(usuario, "deposito")
        elif filtro == "3":
            mostrarExtrato(usuario, "saque")
        else:
            print("Opção inválida.")
            

    if option == "4":
        print("\n ==== CRIANDO UMA NOVA CONTA ====")
        users.criarUsuario()
        print(users.contas)
                    

    if option == "5":
        print("\n ==== LISTANDO CONTAS ====")
        users.listarContas()
            
    if option == "6":
        print("Saindo...")
        break
    
    

