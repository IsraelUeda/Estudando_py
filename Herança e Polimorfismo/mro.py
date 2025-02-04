"""
POO - MRO - Method Resolution Order

method resolution order (ordem de resolução de métodos) é a ordem na qual as classes
são chamadas quando você está executando um método.

em Python, a gente pode conferir a ordem de execução dos métodos (MRO) de 3 formas:
    - Via propriedade da classe __mro__
    - Via método mro()
    - Via help


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
    
class pingüim(Terrestre, Aquatico): # o python segue a ordem de herança da esquerda para 
#a direita
    
    def __init__(self, nome):
        super().__init__(nome)
        
# Testando

pinguim = pingüim('Tux')
print(pinguim.comprimentar()) # Method Resolution Order - MRO

