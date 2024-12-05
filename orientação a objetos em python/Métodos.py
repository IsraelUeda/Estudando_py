"""
Métodos (funções) -> representam os comportamentos do objeto, ou seja, as ações que esse
objeto pode realizar no seu sistema.

Em python dividmos os métodos em  2 grupos, métodos de instancia ou classes

-> Método de instancia

#método de instancia precisamos de uma instancia da classe para utilizarmos um método

#o método dunder init é um método especial chamado de construtor e sua função é construir
o objeto a partir da classe

#Os métodos dunder em python são chamados de métodos magicos

#atenção, por mais que possamos criar nossas proprias funções utilizando dunder não é 
aconselhado fazer isso. Python possui vários métodos com essa forma de nomenclatura
e pode ser que mudemos o comportamento dessas funções mágicas internas

#testando

p1 = Produto('playstation 4', 'Video Game', 2300)

#print(p1.desconto(50))

print(Produto.desconto(p1, 40))

O self é um parâmetro especial em métodos de classe em Python. Ele é usado para fazer 
referência à instância atual da classe, permitindo acesso aos atributos e métodos de cada 
objeto da classe. Quando você cria um método em uma classe e utiliza self, você está dizendo
 que esse método pode acessar e modificar os atributos da instância específica na qual 
 ele está sendo chamado.

user1= Usuario("João", "Henrique", "João@gmail.com", "joao123")
user2= Usuario("pedro", "lucas", "pedrolucas@gmail.com", "lucas123")

 
print(user1.nome_completo())
print(Usuario.nome_completo(user1))
print(user2.nome_completo())

print(f'senha user1: {user1._Usuario__senha}') #acesso de forma errada 
print(f'senha user2: {user2._Usuario__senha}') #acesso de forma errada 

nome = input('Informe o nome: ')
sobrenome = input('Informe o sobrenome:')
email = input('Informe o email: ')
senha = input('Informe a senha: ')
confirma_senha = input('Confirme sua senha ')

if senha == confirma_senha:
    user =  Usuario(nome, sobrenome, email, senha)
else:
    print("Senha não confere")
    exit(1)
print('Usuario criado com sucesso')

senha = input('Informe a senha para acesso:')

if user.checa_senha(senha):
    print('Acesso permitido')
else:
    print('Acesso negado')

print(f'Senha user criptografada {user._Usuario__senha}')

método de classe n fazer acessos aos atributos

métodos de classe em python são conhecidos como métodos estáticos em outras linguagens

#Métodos de Classe, usa decorators para mostrar que é de classe e n de instancia

user= Usuario("João", "Henrique", "João@gmail.com", "joao123")

Usuario.conta_usuarios()
user.conta_usuarios()

"""

from passlib.hash import pbkdf2_sha256 as cryp

class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

class ContaCorrente:

    contador = 4999

    def __init__(self,  limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador =self.__numero


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao 
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """retorna o valor do produto com desconto"""
        return(self.__valor * (100 - porcentagem)) / 100

class Usuario:

    contador = 0

    #método de classe
    @classmethod
    def conta_usuarios(cls):
        print(F'classe: {cls}')
        if cls.contador == 1:
            print(f'Temos {cls.contador} usuário no sistema')
        else:
            print(f'Temos {cls.contador} usuários no sistema')

    #método estático
    @staticmethod
    def definicao():
        return 'UXR344'

    def __init__(self, nome, sobrenome,email, senha):
        self.__id = Usuario.contador +1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size =16)
        Usuario.contador = self.__id
        print(f'Usuario criado: {self.__gera_usuario()}')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'
    
    def checa_senha(self,senha):
        if cryp.verify(senha,self.__senha):
            return True
        return False
    
    def __gera_usuario(self):
        return self.__email.split('@')[0]

print(Usuario.contador)
