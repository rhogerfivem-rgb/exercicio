primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# Conta quantos números primos são menores que 67
contador = 0

for primo in primos:
    if primo < 67:
        contador += 1

print(f"Quantidade de números primos menores que 67: {contador}")
