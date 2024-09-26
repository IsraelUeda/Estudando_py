"""
Python debuugerrr

def dividir(a,b):
    print(f"a={num1}, b= {num2}")
    try:
        return int(a) / int(b)
    except(ValueError, ZeroDivisionError) as err:
        return(f'ocorreu o problema {err}')

num1 = input('Informe o primeiro número')
num2 = input('Informe o segundo número')

print(dividir(num1,num2))

#Existem formas  mais profissionais de fazer isso utilizando o debugger

#Exemplo com pdb 1
#Para utilizar o pdb precisamos importar o biblioteca pdb*e então utilizaar a função
#set_trace()
#comandos basicos 
#l lista onde estamos no codigo
#n(proxima linha)
#p(imprime varaivel)
#c(continua a execução)
import pdb
nome = "israel"
sobrenome = 'ueda'
pdb.set_trace()
curso = 'cicomp'
nome_completo = nome + '' + sobrenome

#exemplo 2

nome = "israel"
sobrenome = 'ueda'
import pdb; pdb.set_trace()
curso = 'cicomp'
nome_completo = nome + " " + sobrenome
final = nome_completo + " faz o curso " + curso

print(final)

pq utilizar esse formato?
o debugger é utilizado durante o desenvolvivmento, costumamos realizar todos os imports no inicio do arquivo, por isso
ao invez de colocarmos no inicio do arquivos colocamos somente onde vamos usar, e ao finalizarmos removemos essa linha

A partir do python 3,7 n é mais necessario importar a biblioteca pdb, agr é build-in, chamada breakpoint


"""
#exemplo 3

nome = "israel"
sobrenome = 'ueda'
breakpoint()
curso = 'cicomp'
nome_completo = nome + " " + sobrenome
final = nome_completo + " faz o curso " + curso

#obs cuidado com conflitos entre nomes de variveis e comandos do pdb

#Não coloque nomes não representativos na variavel
