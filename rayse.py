"""
raise não é uma função, é uma palavbra reservada

ela cria uma excessão

a forma geral de utilização é raise TipoDoError('mensagem de erro')

raise ValueError("valor incorreto")

#exemplo real

def colore(texto,cor):

    if type(texto) is not str:
        raise TypeError("O texto precisa de uma String")
    if type(cor) is not str:
        raise TypeError("O cor precisa de uma String")
    print(f'O texto "{texto}" será impresso na cor {cor}.')

colore(texto = input("qual texto vc gostaria?"), cor = input("qual cor vc gostaria?"))

#exemplo real

def colore(texto, cor):
    cores = ("azul", "vermelho", "amarelo", "rosa", "branco", "preto") 
    if type(texto) is not str:
        raise TypeError("O texto precisa ser uma String")
    if type(cor) is not str:
        raise TypeError("A cor precisa ser uma String")
    if cor.lower() not in cores:
        raise TypeError(f"A cor precisa ser entre {cores}")
    print(f'O texto "{texto}" será impresso na cor {cor.capitalize()}.')

texto = input("Qual texto você gostaria? ")
cor = input("Qual cor você gostaria? ")
colore(texto, cor)

#OBS depois do raise NADA MAIS É EXECUTADO
"""



