"""
Não vimos tuple comprehension

pois elas se chama generators

nomes = ["Carlos", "carla", "cassiano", "cassio", "cassia", "cristina", "vanessa"]

print(any([nome[0] == "c" or "C" for nome in nomes]))

se os 2 fazem a msm coisa, opte por generators pois ele ocupa menos recurso na memoria

nomes = ["Carlos", "carla", "cassiano", "cassio", "cassia", "cristina", "vanessa"]


print(any(nome[0] == "c" or "C" for nome in nomes))#generators

#list comprehension

res = [nome[0] == "c" or "C" for nome in nomes]

#generators

res = (nome[0] == "c" or "C" for nome in nomes)

from sys import getsizeof
# getsizeof retorna o tamanho em bytes em memoria do elemento passado como parametro

print(getsizeof("geek"))

from sys import getsizeof
#Gerando uma lista de numeros com list comprehension
list_comp = getsizeof([x * 10 for x in range(1,100)])

#Gerando uma lista de numeros com set comprehension
set_comp = getsizeof({x * 10 for x in range(1,100)})

#Gerando uma lista de numeros com dictionary comprehension
dictonary_comp = getsizeof({x: x * 10  for x in range(1,100)})

#Gerando uma lista de numeros com generators
generators_comp = getsizeof((x * 10 for x in range(1,100)))


print(f"Para fazer a mesma tarefa gastamos em memória:\n"
      f"List comprehension: {list_comp}\n"
      f"Set comprehension: {set_comp}\n"
      f"Dictionary comprehension: {dictonary_comp}\n"
      f"Generators: {generators_comp}")
"""
#posso iterar com generators?

gen = (x * 10 for x in range(1,1000))

#print(f"{gen} \n"
 #     "o tipo é "type(gen))
print("{} \no tipo é {}".format(gen, type(gen)))

for num in gen:
    print(num)