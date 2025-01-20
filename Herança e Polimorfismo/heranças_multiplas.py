"""
POO - Herança Múltipla

Herança Múltipla nada mais é do que a possibilidade de uma classe herdar de múltiplas classes,
fazendo com que a classe filha herde todos os atributos e métodos de todas as classes herdadas.
# OBS: A herança múltipla pode ser feita de várias maneiras:
    - Por Multiderivação Direta;
    - Por Multiderivação Indireta;
    - Por Multiderivação Múltipla;
# OBS: Não importa a forma, o que importa é que a classe filha herde todos os atributos e
# métodos


# Exemplo 1 - Multiderivação Direta

class Base1:
    pass

class Base2:
    pass

class Base3:
    pass

class MultiDerivada(Base1, Base2, Base3):
    passSS


# exemplo 2 - Multiderivação Indireta

class Base1:
    pass

class Base2(Base1):
    pass

class Base3(Base2):
    pass

class MultiDerivada(Base3):
    pass
    
#obs não importa se a derivação é direta ou indireta, a classe que está herdando vai 
# ter acesso a todos os métodos e atributos das classes herdadas.
"""

class Animal:
    
    def __init__(self, nome):
        self.__nome = nome
        
    def comprimentar(self):
        return f'Eu sou {self.__nome}'
    
    @property
    def nome(self):
        return self.__nome
    
class Aquatico(Animal):
    
    def __init__(self, nome):
        super().__init__(nome)
        
    def nadar(self):
        return f'{self.nome} está nadando'
    
    def comprimentar(self):
        return f'Eu sou {self.nome} do mar!'
    
class Terrestre(Animal):
    
    def __init__(self, nome):
        super().__init__(nome)
        
    def andar(self):
        return f'{self.nome} está andando'
    
    def comprimentar(self):
        return f'Eu sou {self.nome} da terra!'
    
class pingüim(Aquatico, Terrestre): # o python segue a ordem de herança da esquerda para 
#a direita
    
    def __init__(self, nome):
        super().__init__(nome)
        
# Testando

pinguim = pingüim('Tux')
print(pinguim.nadar())
print(pinguim.andar())
print(pinguim.comprimentar()) # Method Resolution Order - MRO

baleia = Aquatico('Wally')
print(baleia.nadar())
print(baleia.comprimentar())

tatuzinho = Terrestre('tatuzinho')
print(tatuzinho.andar())
print(tatuzinho.comprimentar())

# o objeto pingüim é uma instância de pingüim e também de Aquatico, Terrestre e Animal

print(f'Tux é instância de pingüim? {isinstance(pinguim, pingüim)}')
print(f'Tux é instância de Aquatico? {isinstance(pinguim, Aquatico)}')
print(f'Tux é instância de Terrestre? {isinstance(pinguim, Terrestre)}')
print(f'Tux é instância de Animal? {isinstance(pinguim, Animal)}')
print(f'Tux é instância de object? {isinstance(pinguim, object)}')

# qualquer objeto em python é instância de object