"""
|Função onde o parametro é opcional

ex:

print("aizeda mana")
print()

func onde é obrigatoria

def quadrado(num):
    return num * num

print(quadrado(3))
print(quadrado())

#se eu informar um valor ele se torna opcional, e se for colocado ele substitui

def exponencial(num, pot=2):
    return num ** pot

print(exponencial(3)) #3x3
print(exponencial(2,3))  #2x2x2

em funções python os valores com defaut devem sempre estar ao final da declaração

#exemplo mais complexo

def test(nome='geek', instrutor=False):
    if nome == 'geek' and instrutor:
        return "bem vindo instrutor"
    elif nome == "geek":
        return "achei q era instrutor"
    return f"olá {nome}"


print(test())
print(test(instrutor=True))
print(test(True))
print(test("alex"))

qualquer tipo de dado pode ser um valor defaut

#Váriaveis globais
#Váriaveis locais

instrutor = 'geek' #global

def dizoi():
    instrutor = "ai" #local
    return f'oi {instrutor}'

print(dizoi())

se puder evite variaveis globais

total = 0
def incre():
    global total #avisando q usaremos o valor global

    total = total + 1
    return total

print(incre()) 

"""
