"""
POO - Abstração e encapsulamento

O grande objeto da POO é encapsular nosso código dentro de um grupo lógico e hierárquico
utilizando classes

Encapsular -> cápsula


                         classe
''''''''''''''''''''''''''''''''''''''''''''''''''''''
/                                                     /
/                Atributos e métodos                  /
/                                                     /
''''''''''''''''''''''''''''''''''''''''''''''''''''''

#Relembrando atributos e métodos privados em python

imagine que temos uma classe chamada Pessoa, contendo um atributo
privado chamado __nome e um método privado chamado
__falar()

Esses elementos deveriam ser privados mas n são, acontece um fenomeno chamado
name Mangling, que faz uma alteração na forma de acessar os elementos privados,
conforme:

_Classe__elemento

exemplo acessando elementos privados fora da classe

intancia._Pessoa__nome
intancia._Pessoa__falar()

Abstração em POO é o ato de expor apenas os dados relevantes de uma classe, escondendo
atributos e métodos privados de usuário.

 
print(conta1.__dict__)

conta1.depositar(-150)

print(conta1.__dict__)

conta1.sacar(2000)

print(conta1.__dict__)
"""

class Conta:

    contador = 400

    def __init__(self,titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor precisa ser positivo')
    def sacar(self, valor):
        if valor < self.__saldo:
            self.__saldo -= valor
        else:
            print('Você não tem saldo suficiente')
    
    def transferir(self, valor, conta_destino):
        #1 remover valor da conta de origem
        if valor < self.__saldo:
            self.__saldo -= valor
        else:
            print('Você não tem saldo suficiente')
        self.__saldo -= 10 # taxa de transferencia por quem realizou a transferencia

        #2 adicionar o valor na conta destino
        if valor > 0:
            conta_destino.__saldo += valor
        else:
            print('O valor precisa ser positivo')


#testando


conta1 = Conta('matheus', 150.00, 1500)
conta1.extrato()

conta2 = Conta('Lucas', 1500.00, 15000)
conta2.extrato()

conta2.transferir(100, conta1)

conta1.extrato()
conta2.extrato()