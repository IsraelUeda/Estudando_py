"""
TESTE DE VELOCIDADE

#GENERATORS

def nums():
    for num in range(1,10):
        yield num

gel = nums()

print(gel)    

#Generator expressions

ge2 = (num for num in range(1,10))
"""
import time

#generetor expression

gen_ini= time.time()
print(sum(num for num in range(10000000)))
gen_tempo = time.time() - gen_ini

#list comprehension

list_inic = time.time()
print(sum(num for num in range(10000000)))
list_tempo = time.time() - list_inic

print(f'Generator levou {gen_tempo}')
print(f'lista levou {list_tempo}')