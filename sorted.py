"""
sorted
Não confunda apesar do nome com a função sort() que já estudamos em listas
o sort só funciona em listas
podemos usar o sorted em qualquer iteravel
ele serve para ordenar elementos 

OBS: O sorted sempre retorna uma lista com o elementos o iteravel ordenados

#exemplos

numeros = [ 1,9,44,34,5,99, 10, 1902301, 1]

print(sorted(numeros)) #ordena do menor para o maior

print(numeros)

#Adicionando parametros ao sorted

numeros = [ 1,9,44,34,5,99, 10, 1902301, 1]

print(sorted(numeros, reverse = True)) #Ordena do maior para o menor

#Podemos utilizar o sorted() para coisas mais complexas

usuarios = [
        {"username": "jesgaba", "tweets" : ["eu amo meu namorado", "queria dar beijos no israel", "amo melancia"]},
        {"username": "okjit", "tweets" : ["eu amo minha namorada", "queria dar beijos na jessica"]},
        {"username": "seila", "tweets" : ["eu amo meu gato"]},
        {"username": "numsei", "tweets" : []},
        {"username": "aaaa", "tweets" : ["amo pizza", " bolinha de queijo"]},
        {"username": "seinão", "tweets" : []},
]

print(usuarios)

#print(sorted(usuarios, key = lambda usuario : usuario["username"])) # Ordena em ordem alfabetica

print(sorted(usuarios, key = lambda usuario : len(usuario["tweets"]), reverse = True))
"""
