"""
Conjuntos em python
Estamso referenciando a teoria dos conjuntos matematicos

conjunto em python são chamados de Sets:
Dito isso 
-não possuem valores duplicados 
-não possuem valores ordenados
-não são indexados, não são acessados vias indicies

São bons para se utilizar quando precisamos armazenar, elementos mas não nos importamos com a ordenação deles, com chaves, valores e itens duplicados

são referencias em python com chaves {}

diferença entre conjuntos e mapas(dicionarios)

um dicionario tem chave/valor
um set(conjunto) só tem valor


#forma 1

s = set({1, 2, 3, 4, 5, 6, 7, 2, 3})

print(s)
print(type(s))

#ao criar um conjunto, caso seja criado um valor já existente o mesmo será ignorado sem gerar erros e n fara parte do conjunto


#forma 2 mais comum

s = {1, 2, 3, 4, 5, 6, 7, 2, 3}

print(s)
print(type(s))

#importante lembra q além de n termos valores duplicados, n temos ordem

#conjunstos não aceitam valores duplicados ent tera 7 elementos
s = {99, 29, 10, 28, 64, 83, 33, 33, 99, 10}
print(f'conjunto {s} com {len(s)} elementos')

#listas aceitam valores duplicados ent tera 10 elementos
lista = [99, 29, 10, 28, 64, 83, 33, 33, 99, 10]
print(f'Lista: {lista} com {len(lista)} elementos')

#Tupla aceitam valores duplicados ent tera 10 elementos
tupla = 99, 29, 10, 28, 64, 83, 33, 33, 99, 10
print(f'Tupla: {tupla} com {len(tupla)} elementos')

#dicionarios não aceitam valores duplicados ent tera 7 elementos
dicionario = {}.fromkeys([99, 29, 10, 28, 64, 83, 33, 33, 99, 10], 'dict')
print(f'Dicionario: {dicionario} com {len(dicionario)} elementos')

#Podemos misturar tipos de dados

s = {'s', 1, 3.15, True, 44} 

#podemos iterar em um set normalmente
for valor in s:
    print(valor)

#Usos interessantes com sets

#imagine q fizemos um formulario de cadastro de visitantes  em uma feira ou museu, e os visitantes, informam manualmente a cidade de onde vieram
#nos adicionamos cada cidade em uma lista, já q a lista podemos adiconar novos elementos e ter repetição

cidades = ['São Paulo', 'Belo horizonte', 'Cuiaba', 'São Paulo', 'Belo horizonte', 'Cuiaba' ]
print(f'Vieram {len(cidades)} visitantes ao museu')

#precisamos saber quantas cidades unicas temos

print(f'os visitantes vieram de {len(set(cidades))} cidades unicas')

# Lista, tupla, e dict guardam a ordem, já os sets/conjuntos não, ele faz uma ordenação própria 

#Adicionando elementos em um sets

s = {1, 2, 3, 4,}

s.add(5)

print(s)

#remover elementos em um sets
#forma 1

s = {1, 2, 3, 4,}

s.remove(1) 

print(s)

#obs caso o valor n seja encontrado será gerado um keyerror, nenhum valor é retornado

forma 2

s = {1, 2, 3, 4,}

s.discard(2)

print(s)

#obs do discard, se o valor n for encontrado, nenbum erro é gerado

#copiando um conjunto para outrop

#forma 1 Deep copy

s = {1, 2, 3, 4, 5, 6, 7}


novo = s.copy()

novo.add(8)

print(s)

print(novo)

#forma 2 Shallow copy

s = {1, 2, 3, 4, 5, 6, 7}

novo = s

novo.add(8)
print (novo)

#removendo tudo de um conjunto

s = {1, 2, 3, 4, 5, 6, 7}

s.clear()
print(s)

#Métodos matématicos dos conjuntos

estu_py = {'Gabriel', 'Israel', 'Matheus', 'lucas', 'Mayara'}
estu_jv = {'Fernando', 'Israel', 'Ingrid', 'Gabriel'}

#precisamos gerar yum conjunto de nomes unicos

#forma 1 utilizando union

unico1 = estu_py.union(estu_jv)

print(unico1)

#forma 2 utilizando o caractere pipe |

unico2 = estu_jv | estu_py

print(unico2)

#gerar conjunto com os estudantes dos 2 cursos

#forma1 intersection

estu_geral = estu_py.intersection(estu_jv)

print(estu_geral)

#forma 2 utilizando &

estu_geral = estu_py & estu_jv
print (estu_geral)
"""
estu_py = {'Gabriel', 'Israel', 'Matheus', 'lucas', 'Mayara'}
estu_jv = {'Fernando', 'Israel', 'Ingrid', 'Gabriel'}

#estudantes de ´so 1 curso
#forma 1 
jv = estu_jv.difference(estu_py)
print(jv)
py= estu_py.difference(estu_jv)