"""
zip() cria uma iteravel (zip object) qye agrega o elementoded cada um dos iteraveis passados como
entrada em pares

lista1 = [1, 2, 3 ,4]

lista2 =[4, 6, 7]

lista3 = ["a", "b", "c"]

zip1 = zip(lista1, lista2, lista3)

print(zip1)

zip1 = zip(lista1,lista2, lista3)
print(list(zip1))

zip1 = zip(lista1,lista2, lista3)
print(set(zip1))

zip1 = zip(lista1,lista2, lista3)
print(tuple(zip1))

zip1 = zip(lista1,lista2)
print(dict(zip1))

# o zip usa o menor iteravel como parametro, ou seja se tiver trabalhando com vários tamanhos de iteraveis, ele ira parar com o acabar os lementos do menor iteravel
#podemos usar diferentes iteraveis como zip

dados = [(1,2), (3,4),(5,6),(99,100)]

print(list(zip(*dados)))

#exemplo complexo

"""

prova1 = [99,100,89]
prova2 = [89,100,30]
prova3 = [78,99, 76]
alunos = ["Israel", "Jésicca", "Gabriel"]

nota_final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos,prova1,prova2)}
print(nota_final)
#podemos utilizar o map

final = zip(alunos, map(lambda nota: max(nota), zip(prova1,prova2)))

print(dict(final))