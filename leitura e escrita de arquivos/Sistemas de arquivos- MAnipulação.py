"""
Sistemas de arquivos manipulação

import os 

#descobrindo se um arquivo existe

#paths relativos
print(os.path.exists('APRENDENDO PYTHON'))
print(os.path.exists('APRENDENDO PYTHON\\aulas\\leitura e escrita de arquivos'))
print(os.path.exists('APRENDENDO PYTHON\\...\teste.txt'))
print(os.path.exists('APRENDENDO PYTHON\\aulas\\arquivo.txt'))

 #paths absolutos

print(os.path.exists('C:\\Users\\israe\\OneDrive\\Área de Trabalho\\APRENDENDO PYTHON\aulas\\leitura e escrita de arquivos'))

#criando arquivos

#forma 1
open('arquivoteste.txt', 'w').close()

#Forma 2 
open('arquivoteste2.txt', 'a').close()

#Forma 3

with open('arquivo_teste3.txt', 'w') as arquivo:
    pass

#Melhor forma

os.mk("arquivoteste4")

#se o arquivo ja existir teremos o erro fileexisterror

import os

#criando arvore de diretórios

os.makedirs("tamplates/geek/university")


os.makedirs("tamplates2/geek2/university2", exist_ok=True)

#exist_ok=True ignora o erro

#renomear arquivos e diretorios

#arquivos 
os.rename('tamplates/geek/university/teste.txt', 'gow.txt')

#atenção cuidado com comandos de delção, ao deletarmos um arquivo ou diretório,
#eles somem

#removendo arquivos

os.remove("geek.txt")

#se vc estiver no windows e o arquivo estiver aberto ele fera um errro

#CASO N EXISTA vai gerar um filenotfounderror
#se vc informar um diretorio ao invez de um arquivo, teremos um IsADirectoryError

#removendo diretórios vázios

os.rmdir("tamplates")

#obs se o diretório estiver qualquer conteúdo teremos um OSError
#OBS se o diretório n existir termos um FileNotFoundError

#removendo uma arvore de arquivos

for arquivo in os.scandir("tamplates2\\geek2\\university2"):
    if arquivo.is_file():
        os.remove(arquivo.path)


#podemos remover um arvóre de dirétorios vázios
#send 2 trash envia tanto arquivos, como diretórios
os.removedirs("tamplates2\\geek2\\university2")

from send2trash import send2trash

send2trash('cesta2') #vai pra lixeira

#se o arquivo n existir teremos o OSError

#trabalhando com arquivos e diretorios temporarios

with tempfile.TemporaryDirectory() as tmp:
    print(f'criei o diretório temporario em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write("geek university\n")
    input()
          
#estamos criando um diretorio temporario, abrindo o msm e dentro dele
#criando um arquivo de texto, no final usamos um input( ) para mantermos os
#arquivos 'vivos' dentro do bloco with
 
#criando um arquivo temporario

with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Geekkk\n')
    tmp.seek(0)
    print(tmp.read())

#b transforma a string em binarios

import tempfile

#sem o bloco with, sem o bloco with precisamos sempre fechar o arquivo

arquivo = tempfile.TemporaryFile()
arquivo.write(b'oloco meu\n')
arquivo.seek(0)
print(arquivo.read())
arquivo.close()
"""

import os
