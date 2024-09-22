class Estudante:
    escola = "DIO" # variavel de classe

    def __init__(self, nome, matricula):
        self.nome = nome # variavel de instancia
        self.matricula = matricula

    def __str__(self):
        return f'{self.nome} - {self.matricula} - {self.escola}'
    

def exibir_objetos(*args):
    for obj in args: print(obj)

aluno_1 = Estudante("Carlos", 1)
aluno_2 = Estudante("Giovanni", 2)

exibir_objetos(aluno_1, aluno_2)

Estudante.escola = "Udemy" # altera para todas instancias

exibir_objetos(aluno_1, aluno_2)
