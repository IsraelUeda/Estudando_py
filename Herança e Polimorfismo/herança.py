'''
POO - Herança - Inheritance

A ideia de herança é a de reaproveitar código. Tambem extender nossas classes.

obs: Com a herança a partir de uma classe existente, nós extendemos outra classe que passa
a herdar atributos e métodos da classe herdada

Cliente
    - nome;
    - sobrenome;
    - cpf;
    - renda;

Funcionario
    - nome;
    - sobrenome;
    - cpf;
    - renda;
    - matricula

pergunta : Existe alguma entidade generica o suficiente para encapsular o atributos e métodos comuns
a outras entidades?

OBS quando uma classe herdad de outra classe ela herda todos os atributos e métodos da outras
classe

Quando uma classe herda de outra classe, a classe herdada é conhecida por
    classe {pessoa}
    -super classe;
    -classe mãe;
    -classe pai;
    -classe base;
    -classe generica;

quando uma classe herda de outra classe, ela é chamada:
    [cliente, funcionário]
    - Sub classe
    - Classe filha
    - classe especifica;

#forma incomum de acessar dados da super classe

Pessoa.__init__(self,nome, sobrenome, cpf, renda)


#sobrescrita de métodos (Overriding)
    -Ocorre quando reescrevemos/reimplementamos um método presente na super classe em uma
    classe filha

'''

class Pessoa: 
    def __init__(self, nome, sobrenome, cpf): 
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'
               
class Cliente(Pessoa):
    "cliente herda de pessoa"
    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf) #forma incomum de usar 
        self.__renda = renda
                                
class Funcionario(Pessoa):
    "funcionario herda de pessoa"
    def __init__(self,nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def nome_completo(self):
        return f'Funcionário: {self.__matricula} Nome: {super().nome_completo()}'
    
cliente1 = Cliente('Angelina', 'Jolie', 20631908976, 1300)
funcionario1 = Funcionario('João','Jones', 90920792817, 1234)

print(funcionario1.nome_completo())


