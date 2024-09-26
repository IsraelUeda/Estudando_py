"""
Modulo colletions - Default Dict

recap dicionario, ele apresenta o key error 
Default Dict - ao criar um dicionario usando ele, nos informamos um valor default
podendo utilizar um lambda pra isso, será uitlizado quando sempre q n houver valor definido
caso tentamos acessar uma chave  que não existe, essa chave será criada e o valor default será atribuido a ela.

Lambdas são funções sem nome que podem ou não recebem valores de entradas e retornar valores
"""
from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = ('1')

print(dicionario)

print(dicionario['outro']) #key error no dicionario comum

