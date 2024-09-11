"""
Função filter() serve pra filtrar dados de uma determinada coleção


media = (sum(valores) / len(valores))

print(media)

import statistics

valores = (1,2,3,4,5,6)


#podemos usar a função mean()

media = statistics.mean(valores)

print(media)

#assim como a função map, a filter recebe 2 parametros, sendo uma função e um iteravel

res = filter(lambda x: x > media, valores)

print(list(res))

print(f"a média é {media}!")

#Assim como no map apos os dados serem utilizados eles são descartados ou seja

print(f"a media é { list(res)}")

#exemplo 1

res = filter(lambda pais: len(pais) > 0, paises_certo)

paises = ["argentina", "brasil", "", "", "EUA", "China", "Russia", "japão", "cuba"]

paises_certo = [i.title() for i in paises]

res = filter(None, paises_certo)
print(list(res))

#exemplo complexo 

usuarios = [
        {"username": "jesgaba", "tweets" : ["eu amo meu namorado", "queria dar beijos no israel"]},
        {"username": "okjit", "tweets" : ["eu amo minha namorada", "queria dar beijos na jessica"]},
        {"username": "seila", "tweets" : ["eu amo meu gato"]},
        {"username": "numsei", "tweets" : []},
        {"username": "aaaa", "tweets" : ["amo pizza", " bolinha de queijo"]},
        {"username": "seinão", "tweets" : []},
]


inativos = list(filter(lambda usuarios: not usuarios['tweets'], usuarios))
                
print(inativos)
"""

#como combinar filter e map

nomes = ["ana", "jessica", "mario"]

lista = list(map(lambda nome : f"sua instrutura é {nome}", filter(lambda nome: len(nome) < 5, nomes)))

print(lista)