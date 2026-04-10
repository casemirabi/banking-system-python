import json
contas = []

class ListarContas:
    def __init__(self, contas): #Recebe a lista de contas e começa no índice 0.
        self.contas = contas
        self.indice = 0
    
    def __iter__(self): #Retorna o próprio objeto para ele funcionar em for.
        return self
    
    def __next__(self):
        '''A cada chamada:
            pega a conta atual
            avança o índice
            devolve só os campos que você quer listar
        Quando acabar:
            lança StopIteration'''
        
        if self.indice >= len(self.contas):
            raise StopIteration
        conta = self.contas[self.indice]
        self.indice += 1
        
        return {
            "agencia": conta.get("agencia", "0001"),
            "numero": conta.get("numero", "N/A"),
            "nome": conta.get("nome", "Sem nome"),
            "saldo": conta.get("saldo", 0)
        }
        
def listarContas():
    print("\n==== LISTA DE CONTAS ====")
    iterador = ListarContas(contas)
    for conta in iterador:
        print(f"Agência: {conta['agencia']}")
        print(f"Número: {conta['numero']}")
        print(f"Nome: {conta['nome']}")
        print(f"Saldo: R${conta['saldo']}")
        print("---------------------------")

def cpfJaExiste(cpf):
    for usuario in contas:
        if usuario['cpf'] == cpf:
            return True
    return False

def salvarUsuarios():
    with open("contas.js", "w") as f:
        json.dump(contas, f, indent=4)

def carregarUsuarios():
    global contas
    try:
        with open("contas.js", "r") as f:
            contas = json.load(f)
    except FileNotFoundError:
        contas = []

def buscarUsuarioPorCPF(cpf):
    for usuario in contas:
        if usuario['cpf'] == cpf:
            return usuario
    return None

def confirmacao():
    while True:
        resposta = input("\nConfirma os dados? (S/N): ").strip().upper()
        if resposta == "S":
            return True
        elif resposta == "N":
            return False
        else:
            print("Digite 'S' para sim ou 'N' para não.")
            

def gerarNumeroConta():
    '''se não existir nenhuma conta, começa em 000001
        percorre todas as contas existentes
        pega o maior número salvo
        gera o próximo'''

    if not contas:
        return "000001"

    maior_numero = 0

    for conta in contas:
        numero_atual = int(conta.get("numero", 0))
        if numero_atual > maior_numero:
            maior_numero = numero_atual

    proximo_numero = maior_numero + 1
    return str(proximo_numero).zfill(6)

def criarUsuario():
    while True:
        nome = input("Digite o nome completo: ")
        cpf = input("Digite o CPF: ")
        
        while True: 
            if not cpf:
                print("\nCPF não identificado... Tente novamente!")
                cpf = input("Digite o CPF: ")
            else:
                break
            

        if cpfJaExiste(cpf):
            print("\n==== ATENÇÃO ====")
            print("Já existe um usuário com esse CPF.")
            continue

        endereco = input("Digite o endereço: ")

        agencia = "0001"
        numero = gerarNumeroConta()

        print("\n==== CONFIRMAÇÃO ====")
        print(f"""Os dados recebidos são:
Nome: {nome}
CPF: {cpf}
Endereço: {endereco}
Agência: {agencia}
Número: {numero}
""")

        if confirmacao():
            usuario = {
                "nome": nome,
                "cpf": cpf,
                "endereco": endereco,
                "agencia": agencia,
                "numero": numero,
                "saldo": 0,
                "extrato": []
            }
            contas.append(usuario)
            salvarUsuarios()
            print("\nUsuário cadastrado com sucesso!")
            break
        else:
            print("\nDigite os dados novamente.\n")