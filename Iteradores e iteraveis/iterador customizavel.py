"""
escrevendo um iterador customizado

#errado
class Contador:
    def __int__(self, menor, maior):
        self.menor = menor
        self.maior = maior


con = Contador()

print(Contador(1,80))
"""

class Contador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self
    def __next__(self):
        try:
            if self.menor < self.maior:
                numero = self.menor
                self.menor = self.menor + 1
                return numero
            raise StopIteration
        except StopIteration:
            print("Foram todos os numeros")

con = Contador(1, 61)

it = iter(con)

for n in range(1,61):
    print(n)