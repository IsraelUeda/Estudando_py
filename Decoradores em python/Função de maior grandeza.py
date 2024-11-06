"""
 Função de maaior grandeza - Higher Orden FUnctions - HOF

 O que isso significa?

 -Quando uma Linguagem de programação suporta HOF indica que podemos ter funções
 que retornam outras funções como resultado ou até msm que podemos passar funções
 como argumentos para outras funções, e ate criar variáveis do tipo de funções
 para os nossos programas.

 em python as funções são cidadões de primeira classe, first class citizen

 #Exemplos - Definindo as funções

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a/b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)

#testando as funções
print(calcular(4,3, somar))
      
print(calcular(4, 3, dividir))

print(calcular (10, 9, subtrair))

print(calcular(10 , 29, multiplicar))


#Nested functions - funções aninhadas

em python podemos tbm ter funções dentro de funções, que são conhecidas como Nested functions
ou tambem inner functions

#exemplo
from random import choice

def cumprimento(pessoa):
    def humor():
        return choice(("e, ai ", "suma daqui ", "gosto muito de vc "))
    return humor() + pessoa 

#teste

print(cumprimento("Julia"))

#retornando func de outras func

from random import choice

def faz_me_rir():
    def rir():
        return choice(("HAHAHAHAHAHAH", "KKKKKKKKKKKK", "RSRSRS"))
    return rir

#testando
rindo = faz_me_rir()
print(rindo())


"""

# Inner functions, podem acessar o escopo de funções mais externas

from random import choice

def faz_me_rir_denovo(pessoa):
    def dando_risada():
        risada = choice(("HAHAHAHAHAHAH", "KKKKKKKKKKKK", "RSRSRS"))
        return f"{risada} {pessoa}"
    return dando_risada

#testando

rindo = faz_me_rir_denovo("israel")

print(rindo())

print(rindo())

print(rindo())