from operacoes_iniciais import pausa, sacar, depositar, exibir_extrato
from operacoes_usuario_conta import cadastrar_usuario, cadastrar_conta, exibir_items

menu = '''
Escolha uma opção:

[1] Extrato
[2] Depositar
[3] Sacar

[4] Exibir usuarios
[5] Cadastrar usuario
[6] Exibir contas
[7] Cadastrar conta

[0] Sair

'''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

usuarios = []
contas = []

while True:
    opcao = input(menu)

    if (opcao == '1'):
        exibir_extrato(saldo, extrato=extrato)

    elif (opcao == '2'):
        (novo_saldo, novo_extrato) = depositar(saldo, extrato)
        saldo = novo_saldo
        extrato = novo_extrato

    elif (opcao == '3'):
        valor = float(input("Digite o valor de saque: "))
        
        (novo_saldo, novo_extrato, novo_numero_saques) = sacar(
            saldo=saldo, 
            valor=valor, 
            extrato=extrato, 
            limite=limite, 
            numero_saques=numero_saques, 
            limite_saques=LIMITE_SAQUES
        )
        saldo = novo_saldo
        extrato = novo_extrato
        numero_saques = novo_numero_saques

    elif (opcao == '4'):
        exibir_items(usuarios)
        pausa()

    elif (opcao == '5'):
        novo_usuario = cadastrar_usuario()

        cpf_existente = [usuario for usuario in usuarios if usuario["cpf"] == novo_usuario["cpf"]]

        if (cpf_existente):
            print(f'usuario com cpf {novo_usuario["cpf"]} já existe')
        else:
            usuarios.append(novo_usuario)
            print("Usuário cadastrado com sucesso")
        
        pausa()

    elif (opcao == '6'):
        exibir_items(contas)
        pausa()

    elif (opcao == '7'):
        nova_conta = cadastrar_conta(contas)

        cpf_existente = [usuario for usuario in usuarios if usuario["cpf"] == nova_conta["cpf_usuario"]]

        if not cpf_existente:
            print(f'usuario com cpf {nova_conta["cpf_usuario"]} não existe')
        else:
            contas.append(nova_conta)
            print("Conta cadastrada com sucesso")

        pausa()

    elif (opcao == '0'):
        break

    else: ("Opção inválida, tente novamente")