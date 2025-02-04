"""
POO - Métodos Mágicos

Métodos Mágicos são todos os métodos que utilizam dunder (__).

dunder init -> __init__

Dunder > Double Underscore

dunder repr -> Representação do objeto

def __repr__(self):
        return f'{self.titulo} escrito por {self.autor}'
        
__str__ -> Uma representação do objeto para o usuário final tem preferencia sobre o __repr__

print(livro1)
print(livro2)

print(len(livro1))
print(len(livro2))

print(livro1 + livro2)
print(livro1 * 3)

quando vc sobrescreve um método mágico, vc pode alterar o comportamento padrão da classe

"""

class Livro:
    
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        
    def __str__(self):
        return self.titulo
        
    def __len__(self):
        return self.paginas
    
    def __del__(self):
        print('Um objeto do tipo Livro foi deletado da memória')
    
    def __add__(self, outro):
        return f'{self} - {outro}'
    
    def __mul__(self, outro):
        if isinstance(outro, int):
            msg = ''
            for n in range(outro):
                msg += ' ' + str(self)
            return msg
        return 'Não posso multiplicar'
        
    
livro1 = Livro('Python Rocks!', 'Geek University', 400)
livro2 = Livro('Inteligência Artificial com Python', 'Geek University', 350)


