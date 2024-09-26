""""
Algumas linguagens chamam de arrays/vetores para unidimensionais
e matrizes para multidimensionais


listas em python

numeros = [1, 'b', 3.22, True, 5]

# Como fazemos para acessar os dados?

print(listas[0][1]) #ACESSO AO NUMERO 2
print(listas[2][1]) #ACESSO AO NUMERO 8


#exemplo

listas = [[1, 2, 3], [4, 5, 6], [7, 8 ,9]] #matriz 3x3

print(type(listas))
print(listas)


#Iterando em uma lista aninhada

for lista in listas:
    for numero in lista:
        print(numero)

[[print(valor) for valor in lista]for lista in listas]

#Gerando um tabuleiro

tabuleiro = [[numero for numero in range(1,4)]for valor in range(1,4)]
print(tabuleiro)

#gerando jogadas para o jogo da velha 

velha =[['X' if numero % 2 == 0 else 'O' for numero in range(1,4)]for valor in range(1,4)]

print(velha)
"""
#gerando valroes inciias 


tabuleiro = [[numero for numero in range(1,4)]for valor in range(1,4)]
print(tabuleiro)

#gerando jogadas para o jogo da velha 

velha =[['X' if numero % 2 == 0 else 'O' for numero in range(1,4)]for valor in range(1,4)]

print([['*' for i in range(1,4)]for j in range(1,4)])