"""
Funções que recebem dados para serem processados dentro da mesma;

Geralmente em um programa qualquer temos:

Entrada-->processamento--> saida

se pensar em função, sabemos que temos funções que:

-Não possuem entrada;
-Não possuem saida;
-possuem entrada mas n saida;
-não possuem enrtada mas possuem saida;
-possuem entrada e saida;

#Refatorando uma função

def quadrado(num):
    #return num * num
    return num ** 100

print(quadrado(7))
print(quadrado(5))
print(quadrado(2))

#refatorando a função

def cantar_para(aniversariante):
    print('Parábens pra você')
    print('Nesta data querida')
    print('Muitos anos de vida')
    print(f'Viva o(a) {aniversariante}')

cantar_para("israel")

#executar sem paramentos = typererror

#funções podem ter n parametros de entrada, ou seja podemos receber como entrada
#em uma função quantos parametros forem necessarios. eles são separados por virgula.

def soma(a, b):
    return a + b

def mult(a, b):
    return a * b 

def otra(num1, b, msg):
    return (num1 + b) * msg

print (soma(1,10))
print (soma(10,20))

print(mult(10,2))
print(mult(10,10))

print(otra(1,2,"python "))

#obs se informarmos um numero errado de parametro ou argumento teremos typeerror

#nomeando parametros

def nome_completo(nome, sobrenome):
    return f"Seu nome completo é {nome} {sobrenome}"

print(nome_completo("israel", "Ueda"))  

#diferença entre parametros e argumentos

#Parametros são variaveis declaradas na definição de uma função;

#argumentos são dados passados durante a execução da função;

#a ordem dos parametros importa.;

#argumentos nomeados ou keyword arguments

#caso utilizamos nome dos parametros nos argumentos para informa-los podemos, utilizar qualquer ordem
nome= "israel"
sobrenome="massatoshi"

print(nome_completo(nome="Angelina", sobrenome="Jolie"))

print(nome_completo(nome=nome, sobrenome=sobrenome))

print(nome_completo(sobrenome="Boal", nome="felipe"))

#Erro comum na utilização do return

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total

lista = [1, 2, 3, 4, 5, 6, 7]

print (soma_impares(lista))

#return finaliza a função e não terminara o codigo

""" 

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total

lista = [1, 2, 3, 4, 5, 6, 7]

print (soma_impares(lista))

#return finaliza a função e não terminara o codigo