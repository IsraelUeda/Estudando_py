"""
Com o módulo pickle, podemos serializar objetos Python em arquivos binários.

objeto -> b'objeto serializado'

# Serializando um objeto

# Biblioteca para serializar objetos
import pickle

obs não é seguro usar pickle para arquivos que venham de outras pessoas

"""
import pickle

class Animal:
    
    def __init__(self, nome):
        self.__nome = nome
        
    def comer(self):
        print(f'{self.__nome} está comendo')
        
    @property
    def nome(self):
        return self.__nome
    
    def __str__(self):
        return self.__nome
    
class Gato(Animal):
    
    def __init__(self, nome):
        super().__init__(nome)
        
    def miar(self):
        print(f'{self.nome} está miando')
        
class Cachorro(Animal):
    
    def __init__(self, nome):
        super().__init__(nome)
        
    def latir(self):
        print(f'{self.nome} está latindo')
    

felix = Gato('Felix')
pluto = Cachorro('Pluto')

# Escrevendo no arquivo pickle

with open('arquivo.pkl', 'wb') as arquivo:
    pickle.dump((felix, pluto), arquivo)
    
# Lendo do arquivo pickle

with open('arquivo.pkl', 'rb') as arquivo:
    gato, cachorro = pickle.load(arquivo)
    print(gato)
    gato.miar()
    print(cachorro)
    cachorro.latir()