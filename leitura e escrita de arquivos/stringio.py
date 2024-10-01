"""
stringio

ATENÇÃO, para ler ou escrever dados em arquivos de sistema operacional
o software precisa ter permissão:
    - de leitura
    - para escrever

"""

#primeiro fazemos o import
from io import StringIO

mensagem = 'esse é apenas uma string normal'

#Podemos criar um arquivo em memoria já com uma string inserida ou mesmo vázia para inserirmos textos depois

arquivo = StringIO(mensagem)

#ahora tendo o arquivo podemos utilizar tudo que já sabemos

print(arquivo.read())

#escrevendo outros textos

arquivo.write(' outro texto')

#podemos inclusive movimentar o cursor
arquivo.seek(0)

print(arquivo.read())