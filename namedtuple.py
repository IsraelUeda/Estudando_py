"""
São tuplas difenciadas onde especificamos um nome, e a mesma tem parametros

#recap tupla
tupla = (1, 2, 3)


"""

#importando

from collections import namedtuple 

#definir nome e parametro
#forma 1 

cachorro = namedtuple('cachorro', 'idade raça nome')

#forma 2 

cachorro = namedtuple('cachorro', 'idade, raça, nome ')

#forma 3

cachorro = namedtuple('cachorro',['idade', 'raça', 'nome'])

#usando

ray = cachorro(idade=2, raça='chow-chow', nome = 'ray' )

print(ray[0])
print(ray[1])
print(ray[2])

print(ray.idade)
print(ray.raça)
print(ray.nome)