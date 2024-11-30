"""
POO - Atributos 

atributos -> representam as carateristicas do objeot, ou seja, pelos atrivutos nos conseguimos
representar computacionalmente os estados de um objeot

em python, dividimos os atributos em 3 grupos:
    - Atributos de Instância;
    - Atributos de Classe;
    - Atributos Dinâmicos;

 # Atributos de instância:



        

Tudo que estiver dentro de uma classe será um método

#OBS: método construtor é um método especial usadao para construção do objeto

#Basicamente o self serve os atributos que foram definidos

em python por vonvenção, todo atributo de uma classe é público
Ou seja, pode ser acessado em todo o projeto<
Caso queira mostrar que determinado atributo deve ser tratado como privado
utilizasse duplo ___  no inicio do seu nome, ou seja name MangLING

#OBS lembre-se que isso é apenas uma convenção, ou seja a linguagem python n vai impedir
#que nos façamos acesso aos atributos sinalizados como privados fora da Classe

#exemplo

user = Acesso("user@gmail.com", "mochilão123")

#print(user.__email)
#print(user.__senha) # AttributeError

#print(user._Acesso__senha)
user.mostra_senha()
user.mostra_email()

#O que significa atributo de instancia?

# Significa que ao criarmos instancias/objetos de uma classe, todas as instãncias terão
#esses atributos

user1 = Acesso("123@gmail.com", "123")
user2 = Acesso("456@gmail.com", "321")

user1.mostra_email()
user2.mostra_email()


#Classes com atributo de instancia publicos
class Lampada:
    
    def __init__(self, voltagem, cor):
        self.__voltagem = voltagem
        self.__cor = cor
        self.__ligada = False


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:

    def  __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

# Atributos públicos e atributos privados:

class Acesso:

    def __init__(self, email, senha):
        self.__email = email
        self.__senha = senha
        
    def mostra_senha(self):
        print(self.__senha)
    
    def mostra_email(self):
        print(self.__email)

p1 = Produto('Playstation','Videogame', 2300)
p2 = Produto('Xbox', 'Videogame', 3200)

print(p1.valor) #Acesso possivel mas incorreto de um atributo de classe
print(p2.valor)

#Não precisamos criar a instancia de uma classe para fazer acesso a umn atributo de classe

print(Produto.imposto) #Acesso corretor de um atributo de classe


print(p1.id)
print(p2.id)


#Em java os atributos conhecidos como atributos de classe são chamados de atributos estaticos

"""


#Atributos de classe

#atributos de classse, são atributos que são declarados diretamento na classse, fora do
#construtor, geralmente já iniciamos um valor, e este calor é compartilhado entre todas
#as intâncias com os atributos de classe


#refatorando a classe produto
class Produto:

    #Atributo de classe
    imposto = 1.05 #0.05 de imposto
    contador = 0

    def  __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id

#atributos dinâmicos
#é uma atributo de instancia que pode ser criado em tempo de execução
#obs-> o atributo dinâmico será exclusivo da instancia que o criou.

p1 = Produto('Playstation','Videogame', 2300)

p2 = Produto("Arroz", "Mercearia", 32)

#Criando um atributo dinâmico em tempo de execução

p2.peso = "5 Kg" #note que na clkasse produto n existe o atributo peso

print(f'Produto: {p2.nome}\nDescrição: {p2.descricao}\nValor: {p2.valor}\nPeso: {p2.peso}')

# Deletando Atributos

print(p1.__dict__)
print(p2.__dict__)

#print(Produto.__dict__)

del p2.peso

print(p2.__dict__)