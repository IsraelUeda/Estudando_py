"""
print(max("israel Ueda Massatoshi"))

nome = ["Israel", "Jessica", "giovanni", "luana", "Mayara", "Adriane", "Ale"]

nome_certo = [i.title() for i in nome]

print(max(nome_certo))
print(min(nome_certo))

print(min(nome_certo, key=lambda nome: len(nome)))
print(max(nome_certo, key=lambda nome: len(nome)))
"""
musicas = [
    {"Titulo": "Thunderstrock", "tocou": 11},
    {"Titulo": "Back in black", "tocou": 22},
    {"Titulo": "lovin you", "tocou": 978},
    {"Titulo": "bohemian rhapsody", "tocou": 4},
    {"Titulo": "old fashion lover boy", "tocou": 768}
]

print(max(musicas, key = lambda musica: musica["tocou"])["Titulo"])
print(min(musicas, key = lambda musica: musica["tocou"])["Titulo"])

#musica_mais_tocada = (max(musicas, key = lambda musica: musica["tocou"]))

#print(musica_mais_tocada["Titulo"])
  

#desafio encontrar a mais e menos tocada sem max() min() e lambda()

    