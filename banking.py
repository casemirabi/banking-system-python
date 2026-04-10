from datetime import datetime

def deposito(usuario, valor):

    if valor <= 0:
        print("Valor inválido para depósito.")
        return False

    usuario['saldo'] += valor
    print(f"\n===== Depósito realizado com sucesso. ===== ")
    print(f"Saldo atual: R${usuario['saldo']}")

    return True


def saque(usuario, valor):

    if valor <= 0:
        print("Valor inválido para saque.")
        return False

    if valor > usuario['saldo']:
        print("Saldo insuficiente.")
        return False

    usuario['saldo'] -= valor
    print("\n===== Saque realizado com sucesso. =====")
    print(f"\nSaldo atual: R${usuario['saldo']}")

    return True

