# ordem: 1 Parenteses
#        2 Potencia **
#        3 Divisao e multiplicacao (da esquerda pra direita)
#        4 soma e subtracao (da esquerda pra direita)

# Igualdade
saldo = 450
saque = 200

print(saldo == saque)
print(saldo != saque)

print(saldo >= saque)
print(saldo > saque)

print(saldo <= saque)
print(saldo < saque)

# Atribuicao
saldo = 500
saldo += 200
saldo *= 2
saldo /= 4
saldo %= 2
saldo **=2

# Logicos
saldo >= saque and saque <= 100 # AND
saldo >= saque or saque <= 100  # OR
not 1000 > 1500                 # NOT    

contatos_emergencia = []
not contatos_emergencia # results True, EMPTY SEQUENCE IN PYTHON IS FALSE
not "saque" # results False
not "" # results True

# Identidade
curso = "Curso de Python"
nome_curso = curso

saldo, limite = 200, 200

curso is nome_curso # True
curso is not nome_curso # False

saldo is limite # True

# Associacao
frutas = ["laranja", "uva", "limao"]
saques = [1500, 100]

"Python" in curso # True
"maca" not in frutas # True
200 in saques # False
