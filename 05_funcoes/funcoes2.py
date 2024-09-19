def somar(a,b):
    return a + b

def subtrair(a,b):
    return a - b

def exibir_resultado(a,b,funcao):
    resultado = funcao(a,b)
    print(f"O resultado da operação é = {resultado}")

exibir_resultado(6,4, somar)
exibir_resultado(6,4, subtrair)

op = somar

print(op(22, 3))

salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus

salario_bonus(200)
print(salario)