"""
São criados por chaves
#Iterar sobre dict
for chave in receita:
    print(chave)

for chave in receita:
    print(f'Em {chave} recebi r$ {receita[chave]}')

#MODO CERTO


for chave in receita.keys():
    print(receita[chave])]

#ACESSANDO VALORES 

print(receita.values())

for valor in receita.values():
    print(valor)

Desempacotamentos de dicionarios

for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')
"""

