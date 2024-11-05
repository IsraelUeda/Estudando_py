"""
Teste de memoria

sequencia de fibonacci
1,2,3,4,5,8,13.......

#função usando listas 449MB

def fib_list(max):
    numeros = []
    a, b = 0, 1
    while len(numeros) < max:
        numeros.append(b)
        a, b = b, a + b
    return numeros

#teste

for n in fib_list(100000):
    print(n)
"""

#teste 2 generators 3MB

def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador = contador + 1

#Teste

for n in fib_gen(100000):
    print(n)