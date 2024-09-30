"""
Para ler o counteudo de um arquivo usamos a função integrada open()

open() passamos apenas um parametro de entrada, que no caso é o nome do arquivo
essa função retorna um _io.TextIOWrapper E é com ele que trabalhamos

name - 'texto.txt' mode = 'r' encodinge 'utf-8'

"""

#exemplo

arquivo = open('texto.txt')

print(arquivo)

print(type(arquivo))

#para ler um arquivos precisamos usasr o read()
print(arquivo.read())

#obs o python usa um cursos para trabalhar com arquivos, ele funciona como um cursor quando estamos
#escrevendo, a função read() le todo conteudo do arquivo, retornando o conteudo do arquivo em uma string