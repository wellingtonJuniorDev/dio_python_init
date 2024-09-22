from datetime import datetime
from classes_base import Cliente, Print
from classes import Deposito, Saque, PessoaFisica, ContaCorrente

def pausa():
    input("\nApert a tecla ENTER para continuar...")

menu = '''
Escolha uma opção:

[1] Extrato
[2] Depositar
[3] Sacar

[4] Exibir clientes
[5] Cadastrar clientes
[6] Exibir contas
[7] Cadastrar conta

[0] Sair

'''

clientes: list[Cliente] = []

def obter_conta():
    numero = int(input("Informe o numero da conta: "))
    conta = next((conta 
                  for cliente in clientes 
                  for conta in cliente.contas 
                  if conta.numero == numero
                ), None
            )

    if not conta:
        print("Conta não encontrada, tente novamente")
        return
    
    return conta

def obter_contas():
    return [conta 
                for cliente in clientes 
                for conta in cliente.contas
            ]

while True:
    opcao = input(menu)

    if (opcao == '1'):
        conta = obter_conta()
        if (conta):
            Print.exibir_items(conta.historico)
            print(f'\nSaldo: {conta.saldo():.2f}')
            pausa()

    elif (opcao == '2'):
        conta = obter_conta()

        if (conta):
            cliente = next(cliente for cliente in clientes if conta in cliente.contas)

            cliente.realizar_transacao(
                conta, 
                Deposito(float(input("Digite o valor de depósito: ")))
            )
            
    elif (opcao == '3'):
        conta = obter_conta()

        if (conta):
            cliente = next(cliente for cliente in clientes if conta in cliente.contas)

            cliente.realizar_transacao(
                conta,
                Saque(float(input("Digite o valor de saque: ")))
            )      

    elif (opcao == '4'):
        Print.exibir_items(clientes)
        pausa()

    elif (opcao == '5'):
        cpf = input("informe o CPF (somente numeros):") 
        nome = input("informe o nome:")
        data_nascimento= datetime.strptime(
            input("informe a data de nascimento no formato dd/mm/yyyy:"),
            "%d/%m/%Y"
        ).date()
        endereco = input("informe o endereco: logradouro, numero - bairro - cidade/UF: ")

        novo_cliente = PessoaFisica(cpf, nome, data_nascimento, endereco)

        cpf_existente = [cliente for cliente in clientes if cliente.identificador == cpf]

        if (cpf_existente):
            print(f'cliente com cpf {novo_cliente["cpf"]} já existe')
        else:
            clientes.append(novo_cliente)
            print("Cliente cadastrado com sucesso")
        
        pausa()

    elif (opcao == '6'):
        Print.exibir_items(obter_contas())
        pausa()

    elif (opcao == '7'):
        contas = obter_contas()
        cpf = input("informe o CPF do cliente (somente numeros):")

        cliente = next((cliente for cliente in clientes if cliente.identificador == cpf), None)
        
        if not cliente:
            print(f'Cliente com cpf {cpf} não existe')
        else:
            nova_conta = ContaCorrente.nova_conta(cliente, len(contas) + 1)
            cliente.adicionar_conta(nova_conta)
            print("Conta cadastrada com sucesso")
        
        pausa()

    elif (opcao == '0'):
        break

    else: ("Opção inválida, tente novamente")
