"""
#limpar

d.clear()

print(d)

#copiar 
#forma 1 DEEP COPY

novo = d.copy()

print(novo)

novo['d'] = 4
print(d)
print(novo)

#copiar 
#forma 2 shallow copy   

novo = d

print(novo)

novo['d'] = 4
print(d)
print(novo)

d = dict(a=1, b=2, c=3)


print(d)
print(type(d))

#Forma não usual de criação de dicionarioos

outro = {}.fromkeys('a', 'b') 

print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido' )

print(usuario)
print(type(usuario))

#O metodo from keys recebe 2 dados, 1 iteravel e um valor, ele vai gerar para cada valor do iteravel uma chave, e ira atribuir a essa chave o valor informado 


"""


d = dict(a=1, b=2, c=3)


print(d)
print(type(d))
