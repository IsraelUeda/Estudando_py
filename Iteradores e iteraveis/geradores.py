"""
Generators são iterators

obs: o contrario não é verdadeiro, nem todo iterator é um generator

outras informações
    -generators podem ser criados com funções geradores:
    - utilizam a palvra reservada yeld:
    -generators podem ser criados com expressões geradoras

diferença entre funções e generator functions

========================================================================================
/função                                      /Generator Functions
---------------------------------------------------------------------------------------
/utilizam return                             /utilizam yield
---------------------------------------------------------------------------------------
/retorna 1 vez                               / pode utilizar yield multiplas vezes
---------------------------------------------------------------------------------------
/quando executada, retorna um valor          / quanto executada retorna uma generator
--------------------------------------------------------------------------------------
=======================================================================================

#exemplo generator function

def conta_ate():
    valor_maximo = int(input("Qual o valor máximo? "))
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1

for numero in conta_ate():
    print(numero)

#exemplo 2 sem input
def conta_ate(valor_maximo ):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1

gen = list(conta_ate(10))

print(gen)
"""
