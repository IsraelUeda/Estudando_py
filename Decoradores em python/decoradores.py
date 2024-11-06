"""
Decorators

O que são decorators?

- Decorators são funções;
- Decorators envolvem outras funções e aprimoram seus comportamentos;
- Decorators são exemplos de HOF
- Decorators tem uma sintaxe própria, usando @


#decorators como funções (sintaxe não recomendada sem o @)

def seja_educado(funcao):
    def sendo():
        print("Foi um prazer conhecer você")
        funcao()
        print('Tenha um otímo dia!')
    return sendo

def saudacao():
    print("seja bem-vindo a minha casa")

#testando 1

teste = seja_educado(saudacao)

teste()

#testando 2

def raiva():
    print("EU TE ODEIO")

raiva_educada = seja_educado(raiva)

raiva_educada()

#Decorators com @(chamado sintax sugar)

def seja_educado(funcao):
    def sendo():
        print("Foi um prazer conhecer você")
        funcao()
        print('Tenha um otímo dia!')
    return sendo

@seja_educado
def apresentando():
    print('meu nome é Israel')
#testando

apresentando()
"""

