numeros_1_a_100 = list(range(1, 101))

print("Números pares da lista:")
for numero in numeros_1_a_100:
    if numero % 2 == 0:
        print(numero, end=" ")
print()

#o end=" " serve para imprimir tudo na mesma linha
