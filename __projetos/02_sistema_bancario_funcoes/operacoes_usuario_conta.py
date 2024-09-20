from datetime import datetime

def cadastrar_usuario():
    cpf = input("informe o CPF (somente numeros):")

    usuario = { "cpf": cpf }
    usuario["nome"] = input("informe o nome:")
    usuario["data_nascimento"] = datetime.strptime(
        input("informe a data de nascimento no formato dd/mm/yyyy:"),
        "%d/%m/%Y"
    ).date()
    usuario["endereco"] = input("informe o endereco: logradouro, numero - bairro - cidade/UF: ")

    return usuario

def cadastrar_conta(contas):
    return { 
        "agencia": "0001", 
        "numero": len(contas) + 1, 
        "cpf_usuario": input("informe o CPF do usuário da conta (somente numeros):")
    }

def exibir_items(lista):
    if not lista:
        print("Não há registros cadastrados")
        return

    for indice, item in enumerate(lista):
        meta_dados = "\n\t".join([f'{chave.title()}: {valor}' for chave, valor in item.items()])
        print(f'{indice + 1}: \n\t{meta_dados}')
