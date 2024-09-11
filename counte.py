"""
Módulo colletions - counter

colletions- high performace container datetypes

Counter- recebe um iteravel como parametro e cria um objeto do tipo collections
é parecido com um dicionario, countendo como chave o elementos da lista e o valor o numero de ocorrencias desse elemento 

#Utilizando o counter

from collections import Counter

#exemplo 1

#podemos utilizar qualquer iteravel

lista = [1, 1, 2, 2, 3, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 8, 8, 9, 9]

res = Counter(lista)

print(res)

#veja que o counter criou uma chave e colocou a quantidade de ocorrencias como valor delas

forma 2

print(Counter("Israel Ueda Massatoshi"))

forma 3

texto = Metafísica é um conjunto de livros diferentes sobre o mesmo assunto escritos por Aristóteles. Andrônico de Rodes, um dos últimos discípulos do Liceu de Aristóteles, foi quem organizou e classificou esses escritos, dando a eles o nome pelo qual os conhecemos hoje. O quarto livro desses escritos traz, logo em seu início, as seguintes palavras:

“Existe uma ciência que considera o ser enquanto ser e as competências que lhe competem enquanto tal. Ela não se identifica com nenhuma das ciências particulares: de fato, nenhuma das outras ciências considera universalmente o ser enquanto ser, mas delimitando uma parte dele, cada uma estuda as características dessa parte.” |1|

Essa definição de Aristóteles pode ser uma primeira e mais geral elucidação do que é Metafísica: uma área da Filosofia ou, como ele chamou, uma ciência geral, uma espécie de ciência mestra ou ciência mãe de todas as ciências. Antes da classificação de Andrônico de Rodes, o próprio Aristóteles chamava os seus estudos de Metafísica de “Filosofia Primeira” por se tratar de um conjunto de conhecimentos independentes de qualquer atividade empírica e de qualquer experiência sensorial.

Não pare agora... Tem mais depois da publicidade ;)
Enquanto as áreas do conhecimento, divididas em suas especialidades, estudam apenas uma determinada especialidade, ou seja, uma parte do todo, a Metafísica seria responsável por estudar o todo. Podemos dizer, também de maneira geral, que a Filosofia é o estudo do ser enquanto ser, ou seja, é o estudo das relações de como as coisas são, como elas se organizam racionalmente para além da vontade humana e da existência material do mundo.

Apesar de Aristóteles ser considerado um pensador sistemático que ficou conhecido por classificar as áreas do conhecimento no mundo antigo, devemos reconhecer que existem relações entre tais áreas. Os estudos de Filosofia Primeira de Aristóteles relacionam-se, por diversas vezes, com a lógica aristotélica, que também é uma filosofia a priori ou um tipo de filosofia que independe da experiência sensível e da prática. Mais adiante, no livro quatro da Metafísica, Aristóteles diz que:

“é evidente, portanto, que a uma mesma ciência pertence o estudo do ser enquanto ser e das propriedades que a ele se referem, e que a mesma ciência deve estudar não só as substâncias, mas também suas propriedades, os contrários de que se falou, e também o anterior e posterior, o gênero e a espécie, o todo e a parte e as outras noções desse tipo.” |2|

Noções como gênero, espécie, partes e todo não só aparecem na Metafísica, mas também no livro Categorias, um pequeno tratado de lógica escrito por Aristóteles. O trecho da Metafísica citado acima também nos aponta para temas centrais da Filosofia Primeira, ou Metafísica, que se dedicariam ao entendimento da noção de substância, que seria uma espécie de conexão que encaixa os objetos do mundo em suas respectivas formas metafísicas.

palavras = texto.split()

print(palavras)

res = Counter(palavras)

print(res)
"""

#encontro as 5 palavras mais utilizadas
from collections import Counter

texto = """Metafísica é um conjunto de livros diferentes sobre o mesmo assunto escritos por Aristóteles. Andrônico de Rodes, um dos últimos discípulos do Liceu de Aristóteles, foi quem organizou e classificou esses escritos, dando a eles o nome pelo qual os conhecemos hoje. O quarto livro desses escritos traz, logo em seu início, as seguintes palavras:

“Existe uma ciência que considera o ser enquanto ser e as competências que lhe competem enquanto tal. Ela não se identifica com nenhuma das ciências particulares: de fato, nenhuma das outras ciências considera universalmente o ser enquanto ser, mas delimitando uma parte dele, cada uma estuda as características dessa parte.” |1|

Essa definição de Aristóteles pode ser uma primeira e mais geral elucidação do que é Metafísica: uma área da Filosofia ou, como ele chamou, uma ciência geral, uma espécie de ciência mestra ou ciência mãe de todas as ciências. Antes da classificação de Andrônico de Rodes, o próprio Aristóteles chamava os seus estudos de Metafísica de “Filosofia Primeira” por se tratar de um conjunto de conhecimentos independentes de qualquer atividade empírica e de qualquer experiência sensorial.

Não pare agora... Tem mais depois da publicidade ;)
Enquanto as áreas do conhecimento, divididas em suas especialidades, estudam apenas uma determinada especialidade, ou seja, uma parte do todo, a Metafísica seria responsável por estudar o todo. Podemos dizer, também de maneira geral, que a Filosofia é o estudo do ser enquanto ser, ou seja, é o estudo das relações de como as coisas são, como elas se organizam racionalmente para além da vontade humana e da existência material do mundo.

Apesar de Aristóteles ser considerado um pensador sistemático que ficou conhecido por classificar as áreas do conhecimento no mundo antigo, devemos reconhecer que existem relações entre tais áreas. Os estudos de Filosofia Primeira de Aristóteles relacionam-se, por diversas vezes, com a lógica aristotélica, que também é uma filosofia a priori ou um tipo de filosofia que independe da experiência sensível e da prática. Mais adiante, no livro quatro da Metafísica, Aristóteles diz que:

“é evidente, portanto, que a uma mesma ciência pertence o estudo do ser enquanto ser e das propriedades que a ele se referem, e que a mesma ciência deve estudar não só as substâncias, mas também suas propriedades, os contrários de que se falou, e também o anterior e posterior, o gênero e a espécie, o todo e a parte e as outras noções desse tipo.” |2|

Noções como gênero, espécie, partes e todo não só aparecem na Metafísica, mas também no livro Categorias, um pequeno tratado de lógica escrito por Aristóteles. O trecho da Metafísica citado acima também nos aponta para temas centrais da Filosofia Primeira, ou Metafísica, que se dedicariam ao entendimento da noção de substância, que seria uma espécie de conexão que encaixa os objetos do mundo em suas respectivas formas metafísicas."""

palavras = texto.split()

print(palavras)

res = Counter(palavras)

print(res)

print(res.most_common(5))