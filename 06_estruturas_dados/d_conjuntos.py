set([1,2,3,1,3,4]) # { 1,2,3,4 }

set('abacaxi') # {b,a,c,x,i} nao garante a ordem

set(("palio", "gol", "celta", "palio")) # {gol,celta, palio}

set_languages = { "python", "java", "python" }

# set eh iteravel, mas nao indexado => set[0] => error
list = list(set_languages)

for indice, language in enumerate(set_languages):
    print(f"{indice}: {language}")

# operacoes de conjuntos
conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

conjunto_a.union(conjunto_b) # {1,2,3,4}
conjunto_a.intersection(conjunto_b) # {2,3}

conjunto_a.difference(conjunto_b) # {1}
conjunto_b.difference(conjunto_a) # {4}

conjunto_a.symmetric_difference(conjunto_b) # {1,4} => itens fora da intersecao

conjunto_a.issubset(conjunto_b) # False => a estah contido em b
conjunto_a.issuperset(conjunto_b) # False => b estah contido em a

conjunto_a.isdisjoint(conjunto_b) # False => nao ha intercesao

conjunto_a.add(5)
conjunto_a.discard(15) # remove se existir