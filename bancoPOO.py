from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

class Conta:
    def __init__(self, numero, cliente):
        self.saldo = 0
        self.numero = numero
        self.agencia = "0001"
        self.cliente = cliente
        self.historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self.saldo
    
    @property
    def saldo(self):
        return self.numero
    
    @property
    def saldo(self):
        return self.agencia
    
    @property
    def saldo(self):
        return self.cliente
    
    @property
    def saldo(self):
        return self.historico
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo
        if excedeu_saldo:
            print("\n --A operação não pode ser excutada, saldo insufuciente.")
        elif valor > 0:
            self.saldo -= valor
            print("\n --Saque realizado com sucesso!!")
            return True
        else:
            print("\n --A operação não pode ser excutada, o valor informado é inválido!")
        return False
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print("\n --Deposito realizado com sucesso!!")
        else:
            print("\n --A operação não pode ser excutada, o valor informado é inválido!")
            return False
        return True
    
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite = 600, limite_saques = 3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__])
            

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("\n --A operação não pode ser excutada, o valor excede o limite")
        elif excedeu_saques:
            print("\n --A operação não pode ser excutada, número de saques excedido")
        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C: \t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """
    
class Historico:
    def __init__(self):
        self.transacoes = []

        @property
        def transacoes(self):
            return self.transacoes
        
        def adicionar_transacao(self, trasacao):
            self.transacoes.append(
                {
                    "tipo": transacao.__class__.__name__,
                    "valor": transacao.valor,
                    "data": datetime.now().strftime
                    ("%d-%m-%Y  %H:%M:%s"),
                }
            )
class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass
    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    @property
    def valor(self):
        return self.valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor
    
    @property
    def valor(self):
        return self.valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)