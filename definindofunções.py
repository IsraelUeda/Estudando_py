"""
Funções são pequenos trechos de codigos que realizam tarefaz especificas

-realizam tarefas especificas
-pode ou não recerber entrada de dados e retornar uma saida
-muito uteis para executar procedimentos similares por repetidadas vezes 

OBS- SE ESCREVER UMA FUNÇÃO QUE REALIZA VÁRIAS TAREFAS DENTRO DELA É BOM FAZER UMA VERIFICAÇÃO PARA QUE A FUNÇÃO SEJA SIMPLIFICADA

já utilizando várias funções, como:
-print()
-len()
-max()
-min()
-count()

#Exemplo de utilizações de funções

cores = ['verde','amarelo','azul','branco']

#utilizando  a função integrada (build-in) do python print

curso = 'programação em python essencial'

print(cores)

cores.append('roxo')

print(cores)

#DRY Don't Repet Yourself

#como definir funções?

em python a forma geral de definição de função é 

def nome_da_função(parametros _de_entrada):
    bloco_da_função

onde- nome da função -sempre com letras minusculas e se for nome composto, separadas por underline(_)

parametros de entrada- são opcionais, onde tendo mais de uma, sendo separados por virgula, podendo ser opcionais ou não

bloco da função- também chamado de corpo da função, é onde o processamento acontece, podendo ter retorno ou não

obs- precisamos informar que estamos começand uma função com o def, e ent usamos o : para a abrir o bloco de codigo
"""
#Definição da função

#def diz_oi():
    #print('oi!')

"""
OBS
1- Veja q dentro das nossas funções podemos usar outras funções;
2- Veja q nossa função só executa 1 tarefa, ou seja a unica coisa q ela faz é dizer oi
3- Veja q essa função n recebe nenhum parametro de entrada;
4- Veja q essa função n retorna nada;
"""

#Utilizando funções- chamada da execução
#diz_oi()

"""
#ATENÇÃO, NUNCA ESQUEÇA DE UTILIZAR O () AO UTILIZAR UMA FUNÇÃO

EXEMPLO
ERRADO- diz_oi
certo- diz_oi()
"""

#exemplo 2

def cantar_para():
    print('parabens pra voce')
    print('Nesta data querida')
    print('Muitos anos de vida')
    print('Viva o aniversariante')

#for n in range(5):
    #cantar_para()

# em python podemos inclusive criar variaveis do tipo de uma função e executar essa função atraves da variavel

canta = cantar_para

canta()
