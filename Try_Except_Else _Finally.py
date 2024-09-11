"""
Try / Except / Else / Finally

TODA ENTRADA DE DADO DEVE SER TRATADA

#EXEMPLO 1

#else --> é executado somente se o erro n ocorrer
try:
    num = int(input("Informe um número: "))
except ValueError:
    print("A entrada precisa ser um número")
else:
    print(f"Você digitou o numero {num}")

#Exemplo 2

try:
    num = int(input("Informe um número: "))
except ValueError:
    print("A entrada precisa ser um número")
else:
    print(f"Você digitou o numero {num}")
finally:
    print("finally")

# O bloco finally é sempre executado, idependente se houve execessão ou não

# o finally geralmente é utilizado para fechar ou desalocar recursos

#Exemplo complexo errado

def dividir(a,b):
    return a / b

num1 = int(input("Informe o primeiro número"))

try:
    num2 = int(input("Informe o segundo numero"))  
except ValueError:
    print("O valor precisa ser um número inteiro")
else:
    print(dividir(num1,num2))

#Exemplo complexo CERTO
#OBS, vc é responsavel pelas entradas da sua função, então trate-as

def dividir(a,b):
    try:
        return int(a) / int(b)
    except ValueError:
        print('Valor incorreto')
    except ZeroDivisionError:
        print('Não é possivel fazer uma divisão por 0')

num1 = input('Informe o primeiro número')
num2 = input('Informe o segundo número')
    
print(dividir(num1, num2))
"""

#Exemplo complexo CERTO
#OBS, vc é responsavel pelas entradas da sua função, então trate-as

def dividir(a,b):
    try:
        return int(a) / int(b)
    except(ValueError, ZeroDivisionError) as err:
        return(f'ocorreu o problema {err}')

num1 = input('Informe o primeiro número')
num2 = input('Informe o segundo número')
    
print(dividir(num1, num2))