from datetime import datetime

def pausa():
    input("\nApert a tecla ENTER para continuar...")

def obter_timestamp():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if (numero_saques == limite_saques):
        print(f"O limite diário de {limite_saques} saques foi atingido.")
        pausa()
        return (saldo, extrato, numero_saques)

    if (valor <= 0):
        print("Não é possível sacar valores negativos")
        pausa()
        return (saldo, extrato, numero_saques)
    
    if (valor >= limite):
        print(f"O limite de valor por operação deve ser igual ou inferior a R${limite:.2f}.")
        pausa()
        return (saldo, extrato, numero_saques)

    
    if (valor > saldo):
        print(f"O valor informado de R${valor:.2f} é superior ao saldo da conta.")
        pausa()
        return (saldo, extrato, numero_saques)

    
    saldo -= valor
    numero_saques += 1
    extrato += f"\nSaque {obter_timestamp()}: R${valor:.2f}"

    print(f"O valor R${valor:.2f} foi sacado com sucesso!")

    return (saldo, extrato, numero_saques)


def depositar(saldo, extrato, /):
    deposito = float(input("Digite o valor do depósito: "))

    if (deposito <= 0):
        print("Não é possível depositar valores negativos")
        pausa()
        return (saldo, extrato)

    saldo += deposito
    extrato += f"\nDepósito {obter_timestamp()}: R${deposito:.2f}"
    print(f"O valor R${deposito:.2f} foi depositado com sucesso!")

    return (saldo, extrato)

def exibir_extrato(saldo, /, *, extrato):
    print(extrato if extrato else "Não há operações realizadas até o momento.")
    print(f"\nSaldo total: R${saldo:.2f}")
    print(f"\nHora atual: {obter_timestamp()}")
    pausa()