"""
O bloco try/except

Utilizamos ele para tratar erros que podem ocorrer no nosso codigo. Previnindo
assim que o programa para de funcionar, e o usuario seja notificado  de erros inesperados

a forma geral mais simples é 

try:
    //execução problematica
except:
    //o que deve ser feito em caso de problemas


# Exemplo 1 - erro generico
try:
    geek()
except:
    print("Deu algum problema") 

#Tente executar a função geek( ) caso encontre erros print()
#OBs tratar o erro de forma generica nunca é bom, devemos sempre fazer de forma
expecifica

#exemplo 2 tratando erro expecifico 

try:
    geek()
except NameError:
    print("Você esta utilizando uma função inexistente") 

#exemplo 3

try:
    geek()
except NameError as err:
    print(f"A aplicação gerou o sequinte erro {err}") 

#exemplo 4

try:
    geek()
except NameError as err:
    print(f"A aplicação gerou o sequinte erro {err}") 
except TypeError as err1:
    print(f"a função gerou o sequinte erro {err1}")


#exemplo 5 
def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None

dic = {"nome":"Israel"}

print(pega_valor(dic, "nome"))

"""
