import random

numeros_aleatorios = []


for i in range(5):
    numero = random.randint(1, 100)
    numeros_aleatorios.append(numero)

print(f"Lista com números aleatórios: {numeros_aleatorios}")
