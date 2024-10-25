"""
Sistemas de arquivos e navegação

Para fazer uso de manipulação de arquivos de sistema operacional, precisamos importar 
e  fazer uso do módulo os

os -> operacional sistemas

#getcwd() -> diretório de trabalho corrente RETORNA O PATH DO CAMINHO ABSOLUTO

print(os.getcwd())

# Para mudar o diretorio podemos utilizar o chdir('..') ele volta 1 diretorio pra tras

os.chdir('..')

print(os.getcwd())

#Podemos checar se um diretório é absoluto ou relativo

print(os.path.isabs('C:\\Users\\israe\\neDrive\\Área de Trabalho\\APRENDENDO PYTHON')) #true, se começar da raiz é absoluto

#podemos identificar o sistema operacional com o módulo os

print(os.name)

#podemos ter mais detalhes do istema operacional

import sys

print(sys.platform)

print(os.getcwd())

res = os.path.join(os.getcwd(), "geek", "university")

os.chdir(res)

print(os.getcwd())

# veja que o os.path.join() recebe 2 parametros, sendo o primeiro o diretorio atual, e o segundo o diretorio que seja juntado ao atual



#podemos listar os arquivos e diretórios com os listdir(

print(len(os.listdir()))

print(os.listdir('c://'))

#podemos listar com mais detalges com o scandir

print(list(os.scandir()))

arquivos  = list(os.scandir())

print(arquivos)

print(dir(arquivos[0]))

print(arquivos[0].name)
"""

#fazer o import

import os

scanner  = os.scandir()

arquivos = list(scanner)
print(arquivos)

print(dir(arquivos[0]))

print(arquivos[0].name) # nome
print(arquivos[0].inode())#
print(arquivos[0].is_dir())# é um diretorio?
print(arquivos[0].is_file())# é um arquivo?
print(arquivos[0].is_symlink())#é um link simbolico?
print(arquivos[0].path)#caminho
print(arquivos[0].stat())# estatisticas sobre o arquivo

#OBS -> quando utilizamos a funcção scandir precisamos fechala, assim como abrimos um arquivo

