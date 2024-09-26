"""
Map
Com map fazemos mapeamento de valores para função, é uma função que recebe 2 parametros
o primeiro é a função, o segundo um iteravel 

import math
 
def area(r):
    #calcula a area de um circulo
    return math.pi * (r ** 2)

print(area(3))

raios = [10, 20 ,30 ,90, 3 , 4, 6]

#forma comum

areas = []
for r in raios:
    areas.append((area(r)))

print(areas)

#forma 2 utilizando maps

areas = map(area,raios)
print(list(areas))

#forma 3 lambda
print(list(map(lambda r:math.pi * (r ** 2) , raios)))

#apos utilizar a função map, depois da primeira utilização do resultado ele zera

"""
