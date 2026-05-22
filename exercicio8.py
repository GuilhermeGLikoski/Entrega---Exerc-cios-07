quadrados = []
soma = 0

for i in range(1, 11):
    resultado_quadrado = i ** 2
    quadrados.append(resultado_quadrado)
    soma += resultado_quadrado 

print("Lista dos quadrados:", quadrados)
print("Soma de todos os elementos:", soma)
