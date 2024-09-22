from datetime import datetime

class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        return datetime.now().year - self._ano_nascimento
    

pessoa = Pessoa("John Doe", 1999)

print(pessoa.nome)
print(pessoa.idade)
