"""
Utilizamos o pip para instalar bibliotecas externas

pip install pandas

Todos os pacotes externos oficiais em : https://pypi.org

colorama --> coloca cores no terminal

#Utilizando o pacote instalado
from colorama import Fore, Back, Style

print(Fore.RED +("israel"))

from colorama import init, Fore

init()

print(Fore.BLUE + "ISRAEL UEDA")
"""

import pydf

pdf = pydf.generate_pdf('<h1>Israel Ueda</h1>')

with open('teste_doc.pdf', 'wb') as f:
    f.write(pdf)