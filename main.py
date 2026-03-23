import banking
from banking import ExtractManager

valorEscolhido = 0 
manager = ExtractManager()

def valorDaTranzacao():
    global valorEscolhido
    valorEscolhido = int(input("Digite um valor: "))
    return valorEscolhido
    
def menu():
    print("Digite uma opção:")
    print("1: Realizar um deposito")
    print("2: Fazer um saque")
    print("3: Extrato")
    print("4: Sair")
    

while (True):
    menu()
    option = input("Escolha:")
    
    if option == "1":
        valorDaTranzacao()
        banking.deposito(valorEscolhido)
        manager.add_extract(f"Depositando de R${valorEscolhido}")


    if option == "2":
        valorDaTranzacao()
        banking.saque(valorEscolhido)
        manager.add_extract(f"Sacando de R${valorEscolhido}")


    if option == "3":
        manager.list_extracts()    

    if option == "4":
        print("Saindo...")
        break
    
    
