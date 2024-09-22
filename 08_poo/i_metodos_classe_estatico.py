from datetime import datetime

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod # pode acessar propridades da instancia
    def criar_por_data(cls, ano, mes, dia, nome):
        idade = datetime.now().year - ano
        return cls(nome, idade)
    
    @staticmethod # NAO pode acessar propridades da instancia
    def eh_maior_idade(idade):
        return idade >= 18


pessoa = Pessoa.criar_por_data(1990, 5, 23, "Roberto") # metodo de classe

print(Pessoa.eh_maior_idade(pessoa.idade))
