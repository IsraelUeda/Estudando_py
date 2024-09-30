"""
escrevendo em arquivos

se quiser escrever nesse arquivo o primeiro passo é abrir o arquivo
porem teremos uma diferença

obs se abrirmos para escrever não poderemos ler, se abrirmos para ler, não poderemos
escrever

abrindo uma função com o write() ela recebe uma string como parametro
e cria um arquivo, caso já existe um novo será criado e todo o conteudo no arquivo anterior
é perdido


#exeplo de escrita

with open('teste.txt', 'w') as arquivo:
    arquivo.write("escrevendo dados. \n") 
    arquivo.write("podemos colocar quantas linhas quisermos. \n") 
    arquivo.write("essa é a ultima linha. \n") 

with open('geek.txt', 'w') as arquivo:
    arquivo.write('geek \n' * 1000)
"""
with open('frutas.txt', 'w') as arquivo:
    while True:
        fruta = input("informe uma fruta ou digitar sair: ")
        if fruta != 'sair':
            arquivo.write(fruta + "\n")
        else:
            break