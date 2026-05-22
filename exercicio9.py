import random


alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
            "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

random.shuffle(alfabeto)

letra_alvo = "G"

print("jogo de adivinhação")
print(f"O alfabeto foi embaralhado! As posições vão de 0 a 25.")
print(f"Tente adivinhar: em qual posição está a letra '{letra_alvo}'?")

palpite = int(input("Digite o seu palpite: "))


posicao_correta = alfabeto.index(letra_alvo)

if palpite == posicao_correta:
    print(f"\nParabéns! Você acertou! A letra '{letra_alvo}' está na posição {posicao_correta}.")
else:
    print(f"\nQue pena, você errou.")
    print(f"O seu palpite foi {palpite}, mas a letra '{letra_alvo}' estava na posição {posicao_correta}.")

print("\nComo ficou o alfabeto embaralhado:")
print(alfabeto)
