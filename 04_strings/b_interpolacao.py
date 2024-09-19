nome = "Maddox"
raca = "Border Collie"

# Old style
print("Olá, meu cão é o %s. Sua raça é %s" % (nome, raca))

# Format
print("Olá, meu cão é o {}. Sua raça é {}".format(nome, raca))
print("Olá, meu cão é o {1}. Sua raça é {0}".format(raca, nome))
print("Olá, meu cão é o {cao}. Sua raça é {raca_cao}".format(cao=nome, raca_cao=raca))

# F string
print(f"Olá, meu cão é o {nome}. Sua raça é {raca}")

PI = 3.14159

print(f"Valor de PI: {PI:.2f}") # PI: 3.14
print(f"Valor de PI: {PI:10.2f}") # PI:          3.14

nome_completo = "Maddox Maciel Rezende"

print(nome_completo[0])
print(nome_completo[:6])
print(nome_completo[7:13])
print(nome_completo[7:13:2])
print(nome_completo[::-1]) # reverse