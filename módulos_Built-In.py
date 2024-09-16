"""
Módulos built-in --> Módulos que já são padrões do python

Eles são baixados mas n carregados na linguagem

Para utilizarmos precisamos importa-los seja o módulo completo ou somente as funçõen utilizadas(recomenda)

#Utilizando alias (apelidos) para módulos/funções

import random as rdm

from random import randint as rdi

print(rdi(5,89))
print(rdm.random())

#Podemos importar todas as funções de um módulo usando o *

from random import *

#importando todo o módulo

import random 

#importando 2 fuunções

from random import randint as rdi, random as rds

#costumamos utilizazs tuple para colocar multiplos imports
#de um msm modulos
from random import(
    random,
    randint,
    choice,
    shuffle     
)

print(random())
print(randint(1,20))
print(choice("rapaz"))
"""
