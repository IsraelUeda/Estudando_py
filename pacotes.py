"""
Pacotes

Modulo é apenas um arquivo python que pode ter diversas funções para utilizarmos

pacote é um dirétorio que contem uma coleção de módulos

obs nas versões 2.x um pacote python deveria contem dentro dele um arquivo chamado:
__init__.py

nas versões python 3.x n é obrigatorio a utilização deste arquivo, mas geralmente é utilizado
 para manter compatibilidade
"""
from university import (geek1,
                        geek2
)

print(geek1.funcao1(10,20))

print(geek2.curso)
print(geek2.funcao2)
