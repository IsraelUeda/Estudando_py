"""
Passos para se trabalhar com arquvios

1 abrimos o arquivo
2 manipulamos o arquivo
3 fechamos o arquivo 
    
"""

with open('texto.txt') as arquivo:
    print(arquivo.readlines())

