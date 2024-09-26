"""
**kwargs

e mais um parametro
exige parametros nomeados e transforma parametros extras em um dicionario
Parâmetros Nomeados: Permitem especificar os argumentos pelo nome do parâmetro seguido por um valor correspondente

def cores_fav(**kwargs):
    for pessoa,cor in kwargs.items():
        print(f'A cor favorita de {pessoa} é {cor}')

cores_fav(marcos = "verde", julia = "amarelo", israel = "preto", gabriel = "branco")

#nem os parametros em args nem em kwargs são obrigatórios 

#exemplo mais complexo

def comprimento(**kwargs):
    if 'geek' in kwargs and kwargs["geek"] =='Python':
        return "Você recebeu um cumprimento pythonico"
    elif 'geek' in kwargs:
        return f"{kwargs ['geek']} geek!"
    return "não tenho certeza de quem você é"

print(comprimento())
print(comprimento(geek ='Python'))
print(comprimento(geek ='oi'))
print(comprimento(geek = 'especial'))

NAS NOSSAS FUNÇÕES PODEMOS TER (NESSA ORDEM)
- PARAMETROS OBRIGATÓRIOS
- *ARGS
- PARAMETROS DEFAULT
- **KWARGS

def minha_func(num, nome, *args, solteiro = False, **kwargs ):
    print(f"{nome} tem {num} anos" )
    print(args)
    if solteiro:
        print("solteiro")
    else:
        print("casado")
    print(kwargs)

minha_func(8, 'julia')
minha_func(18, "felicity", 4, 5, 6, solteiro=True)
minha_func(34, "julio", eu="Não", você = "vai", )
minha_func(19, "carla", 9, 4, 5, java=False, Python=True)

#func com a ordem correta de parametros
def mostra_info(a, b, *args, instrutor = "geek", **kwargs):
    return[a, b, args, instrutor, kwargs]


a= 1
b = 2
args = (3,)
instrutor= geek
kwargs = {'sobrenome': 'ueda', 'cargo': 'instrutor'}


print(mostra_info(1,2,3, sobrenome="ueda", cargo="instrutor"))


#func com a ordem correta de parametros
def mostra_info(a, b, *args, instrutor = "geek", **kwargs):
    return[a, b, args, instrutor, kwargs]


a= 1
b = 2
args = (3,)
instrutor= geek
kwargs = {'sobrenome': 'ueda', 'cargo': 'instrutor'}

# Desempacotar com **kwargs

def mostra_nomes(**kwargs):
    return f'{kwargs["nome"]} {kwargs["sobrenome"]}'

nomes = {"nome" : 'israel', "sobrenome" : "ueda"}

print(mostra_nomes(**nomes))

"""
def soma_multiplos(a, b, c):
    print (a + b + c)

lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}

soma_multiplos(*lista)
soma_multiplos(*tupla)
soma_multiplos(*conjunto)

dicionario = dict (a = 1, b = 2, c = 3)

soma_multiplos(**dicionario)
#os nomes da chave nos dict precisa ser os mesmos do parametros 