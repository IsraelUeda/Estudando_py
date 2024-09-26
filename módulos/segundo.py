import aulas.módulos.primeirp as primeirp

def funcao2():
    primeirp.funcao1()

if __name__ == '__main__':
    funcao2()
    print('segundo.py está sendo executado diretamente')
else:
    print('segundo.py foi importado')