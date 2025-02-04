"""
POO - polimorfismo

polimorfismo é o princípio que permite que classes derivadas de uma mesma superclasse

métodos abstatos são métodos que as classes filhas são obrigadas a implementar

#overriding é a implementação de um método presente na classe pai em classes filhas

"""

class Animal(object):
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome
    
    def falar(self):
        raise NotImplementedError('A classe filha precisa implementar este método')
    
    def comer(self):
        print(f'{self.nome} está comendo') 

class Gato(Animal):
    
    def __init__(self, nome):
        super().__init__(nome)
        
    def falar(self):
        print(f'{self.nome} está miando')
        
class Cachorro(Animal):
    
    def __init__(self, nome):
        super().__init__(nome)
        
    def falar(self):
            print(f'{self.nome} está latindo')

class Rato(Animal):
    
    def __init__(self, nome):
        super().__init__(nome)
        
    def falar(self):
        print(f'{self.nome} está gritando')
        

# Testando

gato = Gato('Tom')
gato.comer()
gato.falar()

cachorro = Cachorro('Rex')
cachorro.comer()
cachorro.falar()

rato = Rato('Jerry')
rato.comer()
rato.falar()
