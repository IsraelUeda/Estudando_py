"""
POO - o método super()

O método super() se refere á super clsse.
     
"""

class Animal:
    
    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie
        
    def faz_som(self, som):
        print(f' o {self.__nome} fala {som}')
        
class Gato(Animal):
    
    def __init__(self, nome, especie, raca):
        super().__init__(nome, especie)
        self.__raca = raca
        
felix = Gato("Felix", 'Felino', 'Angorá')

felix.faz_som('miau')

# com o super() consigo acesso a qualkquer elemento da classe pai