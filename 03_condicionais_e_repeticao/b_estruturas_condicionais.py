MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade: "))

if idade >= 18:
    print("Maior de idade")

else:
    print ("Nao pode tirar a CNH")


if idade >= 18:
    print("Maior de idade")

elif idade == IDADE_ESPECIAL:
    print("Pode fazer somente aulas teóricas")

else:
    print ("Nao pode tirar a CNH")


print("if Ternario: Pode tirar CNH" if idade >= 18 else "if Ternario? Não pode tirar CNH")

status = 1 if idade == IDADE_ESPECIAL else 999
print(f'O status eh {status}')