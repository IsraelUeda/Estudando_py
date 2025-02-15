"""
escrevendo_csv.py: Escrevendo em arquivos CSV

Neste exemplo, vamos escrever em um arquivo CSV.

O arquivo CSV é um formato de arquivo que armazena dados separados por vírgulas.

reader() e writer() são funções do módulo csv que permitem ler e escrever arquivos CSV.

writerow() é um método do objeto writer que escreve uma linha no arquivo CSV.

from csv import writer

with open('arquivo.csv', 'w') as arquivo:
    escritor_csv = writer(arquivo)
    nome = ''
    escritor_csv.writerow([' Nome', ' Sobrenome', ' Idade'])
    escritor_csv.writerow([' João', ' Silva', 28])
    escritor_csv.writerow([' Maria', ' Santos', 45])
    while nome != 'sair':
        nome = input('Digite o nome: ')
        if nome == 'sair':
            break
        sobrenome = input('Digite o sobrenome: ')
        idade = input('Digite a idade: ')
        escritor_csv.writerow([nome, sobrenome, idade])
        

#dictwriter() é uma função do módulo csv que permite escrever um dicionário em um arquivo CSV.
tem um parametro chamado fieldnames que é uma lista com os nomes das colunas.
"""

from csv import DictWriter

with open('filmes.csv', 'w') as arquivo:
    cabecalho = ['Título', 'Gênero', 'Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = ''
    while filme != 'sair':
        filme = input('Digite o nome do filme: ')
        if filme == 'sair':
            break
        genero = input('Digite o gênero: ')
        duracao = input('Digite a duração em minutos: ')
        escritor_csv.writerow({'Título': filme, 'Gênero': genero, 'Duração': duracao})
        
        #obs as colunas do dicionário devem ser iguais aos nomes das colunas do arquivo CSV
