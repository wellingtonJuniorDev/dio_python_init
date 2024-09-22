from datetime import datetime
from classes_base import Print, Transacao, Conta, Cliente

class Historico(Print):
    def __init__(self):
        self._transacoes: list[Transacao] = []

    @property
    def transacoes(self) -> list[Transacao]:
        return self._transacoes

    def adicionar_transacao(self, transacao: Transacao):
        self._transacoes.append(transacao)

class Deposito(Transacao):
    def __init__(self, valor):
        super().__init__()
        self._valor = valor

    @property
    def valor(self):
        self._valor

    def registrar(self, conta: Conta):
        if conta.depositar(self._valor):
            conta.registrar_transacao(self)

class Saque(Transacao):
    def __init__(self, valor):
        super().__init__()
        self._valor = valor

    @property
    def valor(self):
        self._valor
    
    def registrar(self, conta: Conta):
        if conta.sacar(self._valor):
            conta.registrar_transacao(self)

class ContaCorrente(Conta):
    limite: float = 500
    limite_saques: int = 3

    def numero_saques_diarios(self) -> int:
        return len(
            [transacao for transacao in self._historico.transacoes 
                if transacao.__class__.__name__ == Saque.__name__
                    and transacao._timestamp.date() == datetime.now().date()
            ]
        )

    def sacar(self, valor: float) -> bool:

        if (self.numero_saques_diarios() == ContaCorrente.limite_saques):
            print(f"O limite diário de {ContaCorrente.limite_saques} saques foi atingido.")
            return False
        
        if (valor >= ContaCorrente.limite):
            print(f"O limite de valor por operação deve ser igual ou inferior a R${ContaCorrente.limite:.2f}.")
            return False
        
        return super().sacar(valor) 
    

class PessoaFisica(Cliente):
    def __init__(self, cpf: str, nome: str, data_nascimento: datetime, endereco: str):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

    @property
    def identificador(self):
        return self._cpf
