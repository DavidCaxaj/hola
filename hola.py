def calcular_serie(N):
    if N < 2 or N > 8:
        return 0

    resultado = 0
    i = 1

    while i <= N + 1:
        resultado += i ** (i + 1)
        i += 1

    return resultado

# Ejemplos de uso
numeros = [2, 3, 4, 5, 6, 7, 8]

for numero in numeros:
    resultado = calcular_serie(numero)
    print(f"Para N = {numero}, el resultado es: {resultado}")
