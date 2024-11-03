"""
Criando sua própria versão de loop

for num in range(1,6):
    print(num)

for letra in "Geek university":
    print(letra)

"""


def meu_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break