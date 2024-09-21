class Veiculo:
    def __init__(self, cor, placa, numero_rodas) -> None:
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print(f"{self.__class__.__name__}: Ligando o motor")


class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"carregado: {"Sim" if self.carregado else "Não"}")

moto = Motocicleta("preta", "ABC-1234", 2)
moto.ligar_motor()

carro = Carro("branco", "XYZ-4321", 4)
carro.ligar_motor()

caminhao = Caminhao("preto", "ASD-4567", 8, True)
caminhao.ligar_motor()
caminhao.esta_carregado()
caminhao.cor