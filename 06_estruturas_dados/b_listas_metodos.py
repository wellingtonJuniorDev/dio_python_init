lista = []

lista.append(1) # adicionar item
lista.clear() # esvaziar lista
lista.copy() # cria outra instancia da lista
lista.count("azul")
lista.extend(["amarelo", "branco"]) # concatena outra lista, mas nao remove duplicados
lista.index("azul") # primeira ocorrencia do item

ultimoIndice = lista.pop()
itemNoIndice = lista.pop(0)

lista.remove("amarelo")
lista.reverse() # o mesmo que lista[::-1]
lista.sort()
lista.sort(reverse=True)
lista.sort(key=lambda x: len(x)) #ordenar pela quantidade de caracteres

len(lista) # quantidade itens

sorted(lista)
sorted(lista, key=lambda x: len(x))
sorted(lista, key=lambda x: len(x), reverse=True)
