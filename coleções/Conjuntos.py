"""
conjuntos

*estamos fazendo referencias aos conjuntos da matematica 
-são chamados de sets
-não possuem valores duplicados
-não possuem valores ordenados
-elementos não são acessados via indices, conjuntos não são indexados

#São bons para se utilizar quando precisamos armazenar elementos mas não nos importamos com a ordenação deles

-são referenciados em {}
diferenças entre conjuntos e mapas
maps= chave=valor;
sets = valor;

#Definindo um conjunto

s = set({1, 2, 3, 4, 5, 6, 7, 2, 3,}) #temos valores repetidos

print(s)
print(type(s))

#caso seja adicionado um valor já existente, ele será ignorado sem gerar erros

#forma 2 mais comum

s = {1, 2, 3, 4, 5, 5,}

print(s)
print(type(s))

#Podemos verificar se tem um elemento nesse conjunto

if 3 in s:
    print('tem o 3')
else:
    print('não tem o 3')

"""
#Importante lembrar que alem de não termos valores duplicados, não temos ordem

s = {99, 12, 34, 1, 98, 65}