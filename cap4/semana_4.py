numeros = [5, 10, 15.2, 20]
print(numeros)

print(numeros[1])
numero = numeros[2]
print(numero)

num = 4.3
datos = [num, "palabra", True]
print(datos)

datos = [5, "libro", [48, 'Hola'], True]
print(datos)
print(datos)
print(datos[2])
print(datos[2][1])

datos = [5, 10, 15, 20]
copia_de_datos = datos[:]
datos[0] = 50
print("datos: {}\t copia de datos: {}".format(datos, copia_de_datos))

numeros = [5, 10, 15]
length = len(numeros)
print(length)

print(numeros[1:3])
print(numeros[:2])
print(numeros[::2])
print(numeros[-2:])

numeros = [10, 20]
numeros.append(5)
print(numeros)

palabras = ["ball", "base"]
print(palabras)
palabras.insert(0, "glove")
print(palabras)

items = [5, "ball", True]
items.pop()
item_removido = items.pop()
print(item_removido, "\n", items)

deportes = ["baseball", "soccer", "football", "raquetbol"]
try:
    deportes.remove("tenis")
except ValueError:
    print("Ese elemento no se encuentra en la lista")
print(deportes)

numeros = [5, 8, 0, 2]
print(min(numeros))
print(max(numeros))
print(sum(numeros))
print(sum(numeros)/len(numeros))

numeros.sort()
print(numeros)

nombres = ["jesus", "Ez", "jesus"]
if "Ez" in nombres:
    print("encontrado")