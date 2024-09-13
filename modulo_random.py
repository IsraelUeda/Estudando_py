"""
Modulos são outros arquivos python, cada arquivo são modulos.]

devemos instalarmos e importarmos

módulo random -> Possui várias funções para geração de números pseudo-aleatorio

 #Existem duas formas de utilizar um modulo ou função deste

 #forma 1 -importando todo o modulo (não recomendado)

 import random

 #random() gera um numéro pseudo aleatorio entre 0 e 1 
 # ao realizar o import de todo o modulo todas as funções, atributos, classes e
 proprioedas que estirem dentro do modulo ficarão disponiveis[ficarão em memoria]
caso vc saiba quais funções vc precisa utilizarm então essa n seria a forma ideal de realização

#Para utilizar a função random() do pacote random, nós colocamos o nome do
pacote e o nome da função separados por .

print(random.random())

#forma 2 ->importando uma função especifica

from random import random

for i in range(10):
    print(random())

#uniform() _> gerar um numero real pseudo-aleatorio entre os valores estabelecidos

from random import uniform
for i in range(10):
    print(uniform(3,7))

#randint() -> Gera valores pseudo aleatorios inteiros

from random import randint

for i in range(6):
    print(randint(1,61), end=",") #começa em 1 e vai até 60

#choice() mostra o valor aleatorio entre 1 iteravel

from random import choice

jogadas = ['pedra', 'papel', "tesoura"]

print(choice(jogadas))
"""
#shuffle() --> embaralha dados

from random import shuffle

cartas = ["K", 'Q', 'J', '3', '2' , 'ás']

shuffle(cartas)

print(cartas)