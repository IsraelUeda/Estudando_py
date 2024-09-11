"""
Definindo funções

num = [1, 2, 3, 4]

ret_pop = num.pop()

print(f'retorno de pop {ret_pop}')

ret_pr = print(num)

print(f'retorno de print {ret_pr}')

#obs em python, quando uma função não retorna nenhum valor, o retorno é none

vamo refatorar esta função para que ela retorne o valor

OBS palavra *return* executa o retorno da função
OBS não precisamos criar uma variavel para receber esse retorno, podemos passar a execução
para outras funções.

#exemplo

def quadradro_de_7():
    return 7 * 7

#criamos uma variavel para receber o retorno da função

ret = quadradro_de_7()

print(f'retorno {ret}')

print(f'Retorno {quadradro_de_7()}')


#refatorando a primeira função

def diz_oi():
    return 'oi '

print(diz_oi())

alguem = 'pedro'

print(diz_oi() + alguem)

OBS sobre a palavra reservada return;
1- Ela finaliza o função, saindo da execução da função;
2- Podemos ter em uma função, diferentes returns;
3- Podemos em uma função, retornar qualquer tipo de dado e até mesmos multiplos 
valores;

#exemplo 1

def diz_oi():
    return 'oi! '
    print("estou sendo")

print(diz_oi())

#exemplo 2

def nova_fun():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

print(nova_fun())

#exemplo 3

def outr_func():
    return 2, 3, 4, 5

print(outr_func())
"""

#criar função de jogar moeda

from random import random 

def joga_moeda():
    #gera um numero randomico entre 0 e 1
    valor = random()
    if valor > 0.5:
        return "Cara"
    return "Coroa"

print(joga_moeda())