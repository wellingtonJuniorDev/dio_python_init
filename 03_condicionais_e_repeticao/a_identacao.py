def sacar(valor: float) -> None:
    saldo = 500

    if (saldo >= valor):
        print("valor sacado!")
        print("retire seu dinheiro")

    print ("Volte sempre!")

def depositar(valor: float) -> None:
    saldo = 500
    saldo += valor

sacar(1000)
