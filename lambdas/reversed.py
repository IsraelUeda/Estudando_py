"""
a Função Reverse( ) sóp funciona em listas

já a reversed() funciona com qualquer iteravel
sendo sua fuynção reverter o proprio

retorna um iteravel chamado list reverse iterator

podemos converter para listas, tupla, ou conjunto

#obs em conjuntos nçao definimos a ordem dos elementos

"""

#lista
lista = [1,2,3,4,5,6,7]

print(list(reversed(lista)))

#tupla

print(tuple(reversed(lista)))

#conjunto(set)

print(set(reversed(lista)))

