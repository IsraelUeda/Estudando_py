"""
podemos colocar estruturas condicionais lógicas dentro da list comprehension

exemplos

"""

num = (range(1, 100))

pares = [numeros for numeros in num if numeros % 2==0]

impares = [numeros for numeros in num if numeros % 2 !=0]

print(pares)
print(impares)

#refatorar
#qualquer numero par o resultado vai ser 0 e 0 em python é False, ou seja not False = True
pares = [numeros for numeros in num if not numeros % 2]

#qualquer numero impar módulo de 2 o resultado é 1, e 1 em python é True
impares = [numeros for numeros in num if numeros % 2]

print(pares)
print(impares)