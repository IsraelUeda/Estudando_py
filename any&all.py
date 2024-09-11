"""
Any e All

all() --> Retorna true se todos os elementos do iteravel são verdadeiros
ou ainda se o iteravel esta vazio

#ex

print(all([0,1,2,3,4])) # todos os numeros são verdadeiros? não
print(all([1,2,3,4])) # todos os numeros são verdadeiros? sim

print(any([0,1,2,3,4])) # se qualquer iteravel é verdadeiro? sim
print(any([0,0,0,0,0])) # se qualquer iteravel é verdadeiro? não



nomes = ["carlos", "CASSIO", "camila", "carmo", "constantino"]

nome_certo = [i.title() for i in nomes]

print(all(nome[0] == "C" for nome in nome_certo))

#se gerar um iteravel vazio retorna true

print(all([letra for letra in 'adaf' if letra in 'aeoiu']))

print(all([num for num in [3,5,6,7,8,9] if num % 2 == 1]))


# em all ele retorna uma lista vazioa = true
em any se for uma lista vazia = false

"""



