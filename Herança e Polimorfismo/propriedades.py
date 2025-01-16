'''
POO - Propriedades or propertiers

soma = conta1._Conta__saldo + conta2._Conta__saldo #Não deveria fazer acesso dessa forma

OBS EM linguagens de programação como o Java, ao declararmos atributos provados nas classes,
costumamos a criar métodos públicos para manipulação de desses atrivutos. Esses métodos são conhecidos
por getters e setters, onde os getters retornam o valor do atributo e os setter alteram o valor
do mesmo.

class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
            return f'Saldo de {self.__saldo} do cliente {self.__titular}'
        
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
            
    def get_numero(self):
        return self.__numero  
        
    def get_titular(self):
        return self.__titular
    
    def set_titular(self, titular):
        self.__titular = titular
    
    def get_saldo(self):
        return self.__saldo
    
    def get_limite(self):
        return self.__limite
    
    def set_limite(self, limite):
        self.__limite = limite
    
#Por padrão o @property é um getter
SEMPRE CRIAMOS NOSSOS ATRIUTOS DE FORMAS PRIVADAS


É POSSIVEL CRIAR MÉTODOS COMO PROPRIEDADES
'''

#Refatorando usando propriedades do python

class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1
        
    @property
    def numero(self):
        return self.__numero
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def limite(self):
        return self.__limite
    
    #Criando um setter da maneira correta
    
    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    def extrato(self):
            return f'Saldo de {self.__saldo} do cliente {self.__titular}'
        
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
            
    @property
    def valor_total(self):
        return self.__saldo + self.__limite
        
    
    
    
conta1 = Conta('Matheus', 1000, 2000)
conta2 = Conta('Lucas', 500, 5000)

soma = conta1.saldo + conta2. saldo


print(conta1.extrato())
print(conta2.extrato())
print(f'A soma do saldo das duas contas é {soma}')

print(conta1.__dict__)
conta1.limite = 99991
print(conta1.__dict__)

print(conta1.limite)

print(conta1.valor_total)