'''Cliente → faz → Transação (Deposito/Saque)
Transação → usa → Conta
Conta → guarda → Histórico'''

from abc import ABC, abstractmethod #   ABC: permite criar classes abstratas (não podem ser instanciadas diretamente) | abstractmethod: obriga subclasses a implementarem certos métodos
from datetime import datetime


class Historico:
    def __init__(self):
        self.transacoes = [] #  é iniciado junto com a classe

    def adicionar_transacao(self, transacao):
        # self.transacoes.append(transacao) # adiciona na lista/objetvo
        self.transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
        })
                
        
class Transacao(ABC):
    @property   #   permite acessar como atributo (obj.valor)
    @abstractmethod #   obriga subclasses a implementare
    def valor(self):
        pass

    @abstractmethod #   obriga subclasses a implementar
    def registrar(self, conta):
        pass
    
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor #   _valor: convenção de atributo “protegido”
        
    @property # Permite acessar com obj.valor
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso = conta.depositar(self.valor)
        if sucesso:
            # conta.historico.adicionar_transacao({
            #     "tipo": "deposito",
            #     "valor": self.valor,
            #     "data": datetime.now().strftime("%d/%m/%Y %H:%M")
            # })
            conta.historico.adicionar_transacao(self)
    
class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
        
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso = conta.sacar(self.valor)
        if sucesso:
            # conta.historico.adicionar_transacao({
            #     "tipo": "saque",
            #     "valor": self.valor,
            #     "data": datetime.now().strftime("%d/%m/%Y %H:%M")
            # })
            conta.historico.adicionar_transacao(self)
                
class Conta:
    def __init__(self, numero, cliente, agencia="0001"):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()
    
    # def saldo_atual(self):
    #     return self.saldo
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero=numero, cliente=cliente)
    
    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido para saque.")
            return False
        if valor > self.saldo:
            print("Saldo insuficiente.")
            return False
        
        self.saldo -= valor
        print(f"Saque realizado com sucesso. Saldo atual: R${self.saldo:.2f}")
        return True

    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido para depósito.")
            return False
        
        self.saldo += valor
        print(f"Depósito realizado com sucesso. Saldo atual: R${self.saldo:.2f}")
        return True
        
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, agencia="0001", limite=500.0, limite_saques=3):
        super().__init__(numero, cliente, agencia)
        self.limite = limite
        self.limite_saques = limite_saques    
        
    def sacar(self, valor):
        quantidade_saques = len([
            transacao for transacao in self.historico.transacoes
            if transacao["tipo"] == "Saque"
        ])   
        
        if valor > self.limite:
            print(f"O valor do saque excede o limite de R${self.limite:.2f}.")
            return False
        
        if quantidade_saques >= self.limite_saques:
            print("Limite diário de saques excedido.")
            return False
        
        return super().sacar(valor)
        
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = [] #  Um cliente pode ter várias contas
        
    def realizar_transacao(self, conta, transacao):  #   Delega a execução para a transação
        transacao.registrar(conta)
        
    def adicionar_conta(self, conta):
        self.contas.append(conta)
        
class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
    
        
        

cliente = PessoaFisica(
    nome="Bianca",
    data_nascimento="01/01/2000",
    cpf="12345678900",
    endereco="Rua A"
)

conta = Conta.nova_conta(cliente, "0001")
cliente.adicionar_conta(conta)

# Testes
cliente.realizar_transacao(conta, Deposito(200))
cliente.realizar_transacao(conta, Saque(50))

print("\nSaldo final:", conta.saldo)
print("\nHistórico:")
for t in conta.historico.transacoes:
    print(t)