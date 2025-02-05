"""
Lendo arquivos CSV

CSV - Comma Separated Values - Valores Separados por Vírgula

# Separador por vírgula
1, 2, 3, 4, 5, 6

# Separador por ponto e vírgula
1; 2; 3; 4; 5; 6

# Separador por espaço
1 2 3 4 5 6

# Separador por tab
1   2   3   4   5   6

# Separador por dois pontos

1:2:3:4:5:6

# Podemos usar o separador que quisermos

# A linguagem Python possui duas formas diferentes para ler dados em arquivos CSV:

    - reader -> Permite que iteremos sobre as linhas do arquivo CSV como listas;
    
    - DictReader -> Permite que iteremos sobre as linhas do arquivo CSV como OrderedDicts;
    
# Para ler um arquivo CSV com o reader:

with open('lutadores.csv', encoding='utf-8') as arquivo:
    dados = arquivo.read()
    dados = dados.split('\n')[
        #mt trabalhoso nesse metodo

from csv import reader
with open('lutadores.csv', encoding='utf-8') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv)  # Pula o cabeçalho
    for linha in leitor_csv:
        # Cada linha é uma lista
        print(f'{linha[0]} nasceu no(a) {linha[1]} e mede {linha[2]} cm')
from csv import DictReader

with open('lutadores.csv', encoding='utf-8') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(f"{linha['Nome']} nasceu no(a) {linha['País']} e mede {linha['Altura (em cm)']} cm")

# OBS: O leitor_csv é um iterator, ou seja, só podemos utilizar ele uma vez
#delimiter=';' -> mudar o separador
"""
