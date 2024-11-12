"""
Decorators com diferentes assinaturas, ou seja com diferentes parametros de entrada

#relembrando

def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'olá eu sou o/a {nome}'

@gritar
def ordenar(principal, acompanhamento):
    return f'Olá vou quer um {principal} com {acompanhamento}, por favor'

#testando

print(saudacao('israel'))

#o decorador precisa ter o mesmo numero de parametros da função que ele vai decorar
#para resolver utilizamos um padrão de projetos chamado decorator pattern

#refatorando com a decorator pattern

def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args,**kwargs).upper()
    return aumentar

@gritar
def ordenar(principal, acompanhamento):
    return f'Olá vou quer um {principal} com {acompanhamento}, por favor'

print(ordenar("hamburguer", 'fritas'))

A assinatura de uma função é representada pelo seu retorno, nome, e seus parametros de entrada
Vale lembrar que podemos usar parametros nomeados

print(ordenar(acompanhamento='batata fritar', principal='picanha'))

"""

#decorators com argumentos

def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'valor incorreto primeiro argumento precisar ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna

@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)

@verifica_primeiro_argumento(10)
def soma_dez(num1,num2):
    return num1 + num2

#testando

print(soma_dez(10,22))

print(soma_dez(9,10))

print(comida_favorita("pizza",'café'))