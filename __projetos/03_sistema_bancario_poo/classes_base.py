from abc import ABC, abstractmethod
from datetime import datetime
from classes import Historico

class Print:
    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {", ".join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    
    @staticmethod
    def exibir_items(lista: list):
        if not lista:
            print("Não há registros cadastrados")
            return

        for indice, item in enumerate(lista):
            meta_dados = "\n\t".join([f'{chave.title()}: {valor}' for chave, valor in item.__dict__.items()])
            print(f'{indice + 1}: \n\t{meta_dados}')

class Conta(Print, ABC):
    agencia: str = "0001"

    def __init__(self, numero: int, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = Conta.agencia
        self._cliente: Cliente = cliente
        self._historico: Historico = Historico()

    def saldo(self):
        return self._saldo
    
    @property
    def numero(self) -> int:
        return self._numero

    @property
    def historico(self) -> list:
        return self._historico.transacoes

    @classmethod
    def nova_conta(cls, cliente, numero: int):
        return cls(numero, cliente)

    def sacar(self, valor: float) -> bool:
        if (valor <= 0):
            print("Não é possível sacar valores negativos")            
            return False
        
        if (valor > self._saldo):
            print(f"O valor informado de R${valor:.2f} é superior ao saldo da conta.")
            return False
        
        self._saldo -= valor
        print(f"O saque no valor de R${valor:.2f} foi realizado com sucesso!")

        return True
    
    def depositar(self, valor: float) -> bool:
        if (valor <= 0):
            print("Não é possível depositar valores negativos")
            return False
        
        self._saldo += valor
        
        print(f"Depósito de R${valor:.2f} realizado com sucesso!")

        return True
    
    def registrar_transacao(self, transacao):
        self._historico.adicionar_transacao(transacao)


class Transacao(Print, ABC):
    def __init__(self):
        self._operacao = self.__class__.__name__
        self._timestamp = datetime.now()

    @property
    @abstractmethod
    def valor(self) -> float:
        pass

    @abstractmethod
    def registrar(conta: Conta):
        pass

class Cliente(Print, ABC):
    def __init__(self, endereco: str):
        self._endereco = endereco
        self._contas: list[Conta] = []

    def realizar_transacao(self, conta: Conta, transacao: Transacao):
        transacao.registrar(conta)        

    def adicionar_conta(self, conta: Conta):
        self._contas.append(conta)

    @property
    def contas(self):
        return self._contas
    
    @property
    @abstractmethod
    def identificador(self) -> str:
        pass