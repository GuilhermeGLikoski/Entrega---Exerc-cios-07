palavras = ["computador", "python", "puc", "algoritmo", "ti"]

mais_longa = palavras[0]
mais_curta = palavras[0]

for p in palavras:

    if len(p) > len(mais_longa):
        mais_longa = p
    if len(p) < len(mais_curta):
        mais_curta = p

print("Lista de palavras:", palavras)
print("Palavra mais longa:", mais_longa)
print("Palavra mais curta:", mais_curta)

#len(p) conta quantas letras tem a palavra
