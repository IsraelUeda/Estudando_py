"""
Conhecidas por expressões lambdas são funções sem nome ou seja
funções anonimas

#funçãoe m python
def soma(a, b):
    return a + b

    
def func(x):
    return 3 * x + 1

print(func(4))

#expressão lambda

calcular = lambda x: 3 * x + 1

print(calcular(10))

#podemos ter expressões lambdas de várias entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + " " + sobrenome.strip().title()
print(nome_completo("israel","ueda"))


autores = ['ISRAEL U MASSATOSHI','MAYARA UEDA MASSATOSHI', 'JESSICA SILVEIRA']

autores.sort(key =lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)

# função quadratica
#f(x) = a * x ** 2 + b * x + c
"""


#definindio função
def geradora_func_quadratica(a, b, c):
    return lambda x:a * x **2 + b * x + c
    
teste = geradora_func_quadratica(4,5,-6)

print(teste(0))
print(teste(3))
print(teste(5))

print(geradora_func_quadratica(0,3,5)(2))