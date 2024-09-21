class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plim plim")

    def parar(self):
        print("Parando...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmmmm...")

    def __str__(self) -> str: # equivalente ao .ToString() do c#
        return f"{self.__class__.__name__}: {", ".join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


caloi = Bicicleta("vermelha", "caloi", 2024, 600)
caloi.buzinar()
caloi.correr()
caloi.parar()

print(caloi.cor, caloi.modelo, caloi.ano, caloi.valor)

Bicicleta.buzinar(caloi) # outra forma de invocar o metodo da classe

print(caloi) # sobrescrever __str__
