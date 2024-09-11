"""
o *args é um parametro como outro qualquer, isso significa que vc podera chamar de qualquer coisa
 desde que comece com *

 ex:
 *x

 mas por convenção, utilizamos o nome args para definilo

 mas o que é o args?

 coloca os valores extras informados como entrada em uma tupla

 lembrese que tuplas são imutaveis
 
 def soma_todos_num(num1, num2, num3):
    return num1 + num2 + num3 

print (soma_todos_num(10, 20, 30, 50, 60)) #$typeerror


#entendo o args 

def soma_todos_num(nome, sobrenome, *args):
    return sum(args)

print(soma_todos_num("israel","ueda"))
print(soma_todos_num("israel","ueda",1))
print(soma_todos_num("israel","ueda",1,2,3))
print(soma_todos_num("israel","ueda",1,2,3,4))
print(soma_todos_num("israel","ueda",1,2,3,4,5,6))

def verifica_info(*args):
    if 'geek' in args and 'university' in args:
        return "bem vindo instrutor"
    return "não sei quem tu é"

#salva a lista com 1 elemento, lis dict etc

#desempacotador
usando o *
num = (1,2,3,4,5)
print(soma_todos_num(*num))
 """


