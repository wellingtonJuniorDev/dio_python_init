class Animal:
    def __init__(self, numero_patas) -> None:
        self.numero_patas = numero_patas

    def __str__(self) -> str: # equivalente ao .ToString() do c#
        return f"{self.__class__.__name__}: {", ".join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kwargs) -> None:
        super().__init__(**kwargs)
        self.cor_pelo = cor_pelo

class Ave(Animal):
    def __init__(self, cor_bico, **kwargs) -> None:
        super().__init__(**kwargs)
        self.cor_bico = cor_bico

class Cachoro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave): # heranca multipla
    def __init__(self, cor_pelo, cor_bico, numero_patas) -> None:

        print(Ornitorrinco.__mro__) # Ornitorrinco.mro()

        super().__init__(
            cor_pelo=cor_pelo, 
            cor_bico=cor_bico, 
            numero_patas=numero_patas
        )

gato = Gato(numero_patas=4, cor_pelo="preto")
print(gato)

ornitorrinco = Ornitorrinco(numero_patas=4, cor_pelo="marrom", cor_bico="laranja")
print(ornitorrinco)
