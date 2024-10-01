"""
Modos de abertura de aquivos

r- > abre para leitura- padrão
w -> abre para escrita, sobrescreve caso o arquivo já exista
x -> abre para escrita somente se o arquivo não existir

Exemplo x

try:
    with open('university.txt','x') as arquivo: # se o arquivo já existir ocorre um erro, o erro fileexistserror
        arquivo.write('teste de conteudo \n')
except FileExistsError:
    print('arquivo já existe')

a -> Abre para escrita, adicionando o conteúdo ao final do arquivo
com o modo a não controlamos o cursor

#exemplo a

with open('frutas.txt', 'a') as arquivo:
    while True:
        fruta = input('informe uma fruta ou sair')
        if fruta != 'sair':
            arquivo.write(fruta + '\n')
        else:
            break


+ -> abre para o modo de atualização, leitura ou escrita, o mais acompanha outras letras
seja r, a, w

with open('teste,txt', 'a+') as arquivo:
    arquivo.seek(0)
    arquivo.write('Novo topo \n')
    arquivo.write('Nova linha \n')
    arquivo.write('Mais uma linha \n')            


with open('teste,txt', 'r+') as arquivo:
    #arquivo.seek(0)
    arquivo.write('adicionada \n')
    arquivo.seek(11)
    arquivo.write('Nova linha \n')
    arquivo.seek(12)
    arquivo.write('Mais uma linha \n')    
"""

