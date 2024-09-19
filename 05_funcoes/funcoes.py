def exibir_mensagem():
    print("Olá mundo!")

def exibir_mensagem2(nome):
    print(f"Seu nome é {nome}!")

def exibir_mensagem3(nome="Maddox"):
    print(f"O nome é {nome}")

exibir_mensagem()
exibir_mensagem2("Theo")
exibir_mensagem3()
exibir_mensagem3("Boi")

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_sucessor(numero):
    return  numero - 1, numero + 1

print(calcular_total([10, 20, 30])) # 60
print(retorna_antecessor_sucessor(30)) # (29,31)

# argumentos nomeados
exibir_mensagem2(nome="Nomeado")
exibir_mensagem2(**{ "nome": "Object" })

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"

    print(mensagem)

exibir_poema(
    "Quarta, 18 de setembro de 2024",
    "Zen of Python",
    "Beaultiful is better than ugly",
    "Explicit is better than implicit",
    autor="Zen",
    ano=2000
)   

def criar_carro_positional(carro, modelo, /, ano, placa): # Positional carro, modelo
    print(carro, modelo, ano, placa)

def criar_carro_keyword(*, modelo, ano, placa): # Keyword only
    print(modelo, ano, placa)