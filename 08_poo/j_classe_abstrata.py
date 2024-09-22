from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractmethod
    def marca(self):
        pass

class ControleTv(ControleRemoto):
    def ligar(self):
        print('Ligando a TV')
   
    def desligar(self):
        print('Desligando a TV')

    @property
    def marca(self):
        return "Philco"


controle_tv = ControleTv()
controle_tv.ligar()
controle_tv.desligar()
print(controle_tv.marca)
