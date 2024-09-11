"""
List comprehension

-Utilizando list comprehension podemos gerar novas listas com dados processados
a partir de outro iteravel

#sintaxe
[dado for dado in iteravel]

#Exemplos

num = [1, 2, 3, 4, 5]

res = [num * 10 for num in num] 

print(res)

#para entender melhor devemos dividir em 2 partes

def func(valor):
    return valor * valor

res = [func(num) for num in num]

print(res)

#loops vs lists
 
 #loop

numeros = [1, 2, 3, 4]
numeros_dobrados = []

for numero in numeros:
    numeros_dobrados = numero * 2
    #numeros_dobrados.append(numeros_dobrados)
 
print(numeros_dobrados)

#list comprehension

print([numero * 2 for numero in [1, 2, 3, 4]])

amigos = ["cesár", "italo", "gabriel", "matheus"]

def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome
    print(nome)

print([caixa_alta(amigo) for amigo in amigos])

print([numero * 3 for numero in range(1,10)])

print([bool(valor) for valor in [0,[], '', True, 1, 3.14,]])
"""
