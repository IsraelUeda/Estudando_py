"""
Reduce
A partir do python 3 a função reduce(), não é mais uma função integrada(built-in). Agora temos
que importar e utilizar essa função a partir do modulo 'functools'

utulize o modulo reduce() se for extritamente necessario, na maioria dos casos um 
loop for sera mais legivel

imagine que vc tem uma função de dados

dados = [a1, a2, a3, a4, a5, a6]

e vc tem uma função que  recvebe 2 parametros

def função(x, y):
    return x * y 

a função reduce() funciona da seguinte forma:
ela recebe 2 parametos, a função e o iteravel
reduce(func,dados)

passo 1: res1 = f(a1,a2) #aplica a função nos 2 primeiros elementos da coleção e guarda o resultado
passo 2: res2 = f(res1, a3) #aplica a função passando o resultado do passo 1 + o receiro elemento e guarda o resultado
#repetindo até o final

alternativamente poderiamso ver a função reduce():


from functools import reduce

dados = [1,2,3,4,5,6,7,8,9,119, 200, 300]

#precisa de função que use 2 parametros

função(função(função(a1,a2), a3), a4)
multi = lambda x,y : x * y
res = reduce(multi,dados)

print(res)

#Utilizando um loop normal
res = 1
for n in dados:
    res= res * n

print(res)
"""






