class Cachorro:
    def __init__(self, raca, cor): # construtor
        self.raca = raca
        self.cor = cor

    def latir(self):
        print("Auauauauauaau")

    def __del__(self): # destrutor
        print("Removendo a instancia da classe")

cachorro = Cachorro("Border Collie", "Marrom tricolor")

cachorro.latir()


del cachorro # forcar remocao pelo GC

print("python")
print("python")
