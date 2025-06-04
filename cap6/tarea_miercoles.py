cuentas = []  

while True:
    print("Introduce un número de cuenta (o 'fin' para terminar): ")
    num = input()
    if num == 'fin':
        break
    cuentas.append(num)

cuentas_unicas = frozenset(cuentas)  
print("Números únicos:", cuentas_unicas)

#2

numeros = [3, 4, 3, 7, 10]

sin_repetir = set(numeros)

print("Números sin repetir:", sin_repetir)