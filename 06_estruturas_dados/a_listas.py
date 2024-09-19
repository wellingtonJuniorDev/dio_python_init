frutas = []
frutas = ["laranja", "maca", "uva"]

letras = list("python")
numeros = list(range(10))

carro = ["Ferrari", 2020, 11, "São Paulo", True]

print(frutas[-1]) # ultimo item

matriz = [
    [1, "a", 4],
    [2, "b", 5],
    [3, "c", 6],
]
matriz[0] # [1, "a", 4]
matriz[0][0] # 1
matriz[0][-1] # 4

lista = ["p", "y", "t", "h", "o", "n"]
lista[2:] # [t,h,o,n]
lista[:2] # [p,y]
lista[1:3] # [y,t,h]
lista[0:3:2] # [p,t]
lista[::] # ["p", "y", "t", "h", "o", "n"]
lista[::-1] # [n,o,h,t,y,p]

carros = ["gol", "palio", "uno"]

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

numeros = [1, 39, 2, 6, 9, 34]
pares = []

for numero in numeros: # modo 1
    if numero % 2 == 0:
        pares.append(numero)

pares = [numero for numero in numeros if numero % 2 == 0] # modo 2 + performatico

