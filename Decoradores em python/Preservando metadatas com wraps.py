"""
Preservabdo meta datas com wraps

Metadatas -> são dados intrisecos em arquivos

wraps _> são funções que envolvem elementos com diversas finalidades

#problema

def ver_log(funcao):
    def logar(*args, **kwargs):
       Eu sou uma função(logar) dentro de outra
        print(f'Você esta chamando: {funcao, __name__}')
        print(f'Aqui está a documentação: {funcao, __doc__}')
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a, b):
        soma 2 numeros
    return a + b

#testando

print(soma(10, 30))

print(soma, __name__)
print(soma, __doc__)
"""

# resoluição do problema

from functools import wraps

def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Eu sou uma função(logar) dentro de outra"""
        print(f'Você esta chamando: {funcao.__name__}')
        print(f'Aqui está a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a, b):
    """soma 2 numeros"""
    return a + b

#testando

print(soma(10, 30))

print(soma.__name__)
print(soma.__doc__)