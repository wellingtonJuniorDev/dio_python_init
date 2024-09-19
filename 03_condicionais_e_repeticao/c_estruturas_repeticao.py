# FOR
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()
    print("Executa no final do laco")        

# RANGE
print(list(range(4)))

# exibindo a tabuada do 5
for numero in range(0, 51, 5):
    print(numero, end=" ")

# WHILE
opcao = -1

while opcao != 0:
    print("\n\nEscolha uma opcao:")
    opcao = int(input("\n[1] Sacar, \n[2] Depositar, \n[0 Sair]\n"))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Depositando...")
    
else:
    print("\n Saindo do while, comando else opcional.")