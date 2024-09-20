from datetime import datetime

menu = '''
Escolha uma opção:

[e] Extrato
[d] Depositar
[s] Sacar

[q] Sair

'''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

def pausa():
    input("\nApert a tecla ENTER para continuar...")

def obter_timestamp():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def exibir_extrato():
    print(extrato if extrato else "Não há operações realizadas até o momento.")
    print(f"\nSaldo total: R${saldo:.2f}")
    print(f"\nHora atual: {obter_timestamp()}")
    pausa()

def depositar():
    deposito = float(input("Digite o valor do depósito: "))

    if (deposito <= 0):
        print("Não é possível depositar valores negativos")
        pausa()
        return

    global saldo, extrato

    saldo += deposito
    extrato += f"\nDepósito {obter_timestamp()}: R${deposito:.2f}"
    print(f"O valor R${deposito:.2f} foi depositado com sucesso!")


def sacar():
    global saldo, extrato, numero_saques

    if (numero_saques == LIMITE_SAQUES):
        print(f"O limite diário de {LIMITE_SAQUES} saques foi atingido.")
        pausa()
        return

    saque = float(input("Digite o valor de saque: "))

    if (saque <= 0):
        print("Não é possível sacar valores negativos")
        pausa()
        return 
    
    if (saque >= limite):
        print(f"O limite de saque por operação deve ser igual ou inferior a R${limite:.2f}.")
        pausa()
        return
    
    if (saque > saldo):
        print(f"O valor informado de R${saque:.2f} é superior ao saldo da conta.")
        pausa()
        return
    
    saldo -= saque
    numero_saques += 1
    extrato += f"\nSaque {obter_timestamp()}: R${saque:.2f}"

    print(f"O valor R${saque:.2f} foi sacado com sucesso!")

while True:
    opcao = input(menu)

    if (opcao == 'e'):
        exibir_extrato()

    elif (opcao == 'd'):
        depositar()

    elif (opcao == 's'):
        sacar()

    elif (opcao == 'q'):
        break

    else: ("Opção inválida, tente novamente")