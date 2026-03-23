saldo = 0


class ExtractManager:

    def __init__(self):
        self.extracts = []
        self.file = "extracts.txt"
        self.load_extracts()

    def add_extract(self, extract):
        self.extracts.append(extract)
        self.save_extracts()

    def list_extracts(self):
        if not self.extracts:
            print("Nenhum registro no extrato.")
            return

        print("\n===== EXTRATO =====")
        for i, extract in enumerate(self.extracts, start=1):
            print(f"{i} - {extract}")
        print("===================\n")

    def remove_extract(self, index):
        if 0 <= index < len(self.extracts):
            self.extracts.pop(index)
            self.save_extracts()
        else:
            print("Índice inválido")

    def save_extracts(self):
        with open(self.file, "w") as f:
            for extract in self.extracts:
                f.write(extract + "\n")

    def load_extracts(self):
        try:
            with open(self.file, "r") as f:
                self.extracts = [line.strip() for line in f]
        except FileNotFoundError:
            self.extracts = []


def deposito(valor):
    global saldo

    if valor <= 0:
        print("Valor inválido para depósito.")
        return saldo

    saldo += valor
    print(f"Depósito realizado com sucesso.")
    print(f"Saldo atual: R${saldo}")
    print("=================")

    return saldo


def saque(valor):
    global saldo

    if valor <= 0:
        print("Valor inválido para saque.")
        return saldo

    if valor > saldo:
        print("Saldo insuficiente.")
        return saldo

    saldo -= valor
    print("Saque realizado com sucesso.")
    print(f"Saldo atual: R${saldo}")
    print("=================")

    return saldo