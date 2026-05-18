class Historico():
    pass

class Transacoes():
    pass

class Deposito():
    pass

class Conta():
    def __init__(self, numero, cliente, agencia='0001'):
        self.saldo = 0.0
        self.numero = numero
        self.cliente = agencia
        self.cliente = cliente
        self.historico = Historico()


class ContaCorrente():
    def __init__(self, numero, cliente, agencia="0001", limite=500.0, limite_saques=3):
        super().__init__(numero, cliente, agencia)
        self.limite = limite
        self.limite_saques = limite_saques
        
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
        
    def adicionar_conta(self, conta):
        self.contas.append(conta)
        
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta) 

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco) 
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

cliente = PessoaFisica("Bianca", "26/03/1997", 44631827899, "Antonio Cordeiro")
Cliente(cliente)
print(cliente)