pessoa = { "nome": "Maddox", "idade": 28 }

pessoa = dict(nome="Maddox", idade=28)

pessoa["telefone"] = "3333-1234" # incluir nova chave

nome = pessoa["nome"] # lendo

pessoa["nome"] = "Border" # sobrescrevendo valor

contatos = {
    "maddox@gmail.com": {"nome": "Maddox", "telefone": "3333-1234"}
}
print(contatos["maddox@gmail.com"]["nome"])

for chave in pessoa:
    print(chave, pessoa[chave])

for chave, valor in pessoa.items(): # recomendado, .itens retorna lista de tuplas
    print(chave, valor)
 
pessoa.fromkeys(["sobrenome"]) # adiciona chave sobrenome com valor None
pessoa.fromkeys(["sobrenome"], "teste") # adiciona chave sobrenome com valor teste

chave_inexistente = pessoa.get("chave_inexistente") #  None
chave_inexistente = pessoa.get("chave_inexistente", "default") #  "default"

pessoa.keys() # lista todas as chaves
pessoa.values() # lista todos os values

pessoa.pop("telefone") # remove chave
remocao = pessoa.pop("telefone", "nao removido")

del pessoa["telefone"] # remove chave
del pessoa # remove todo dicionario

pessoa.setdefault("nome", "Teste") # adiciona a chave/valor caso a chave nao exista

pessoa.update({ "nome", "novo_nome"})

print("chave existe") if "nome" in pessoa else print("chave nao existe")
