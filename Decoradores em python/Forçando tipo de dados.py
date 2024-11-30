"""
Forçando tipo de dados com decoradores

"""

def forca_tipo(*tipos):
    def decorador(funcao):
        def converte(*args, **kwargs):
            novo_args = []
            for (valor, tipo) in zip(args, tipos):
                novo_args.append(tipo(valor))  #str("oi, tudo vem?"), int(20)
            return funcao(*novo_args, **kwargs)
        return converte
    return decorador

@forca_tipo(str, int)
def repete_msg(msg, vezes):
    for vez in range(vezes):
        print(msg)

print(repete_msg("Oi, tudo bem?", 20))

@forca_tipo(float, float)

def dividir(a,b):
    print(a/b)

dividir("1", 2)