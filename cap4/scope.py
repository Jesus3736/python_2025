def scopTest():
    global numero  # Añadido para acceder a la variable global
    numero += 1    # Corregido el símbolo "@" por operación válida

scopTest()

# ----------------------------
# Accediendo a variables definidas en una función
def scopTest2():
    palabra = "función"
    return palabra

valor = scopTest2()
print(valor)

# ----------------------------
# Cambiando elementos de lista
deportes = ["baseball", "football", "raquetbol", "basketball"]

def cambiar(unalista):
    unalista[2] = "ping pong"  # Reemplazado "@" por índice válido (2)

print("Antes de alterar:", deportes)
cambiar(deportes)
print("Después de alterar:", deportes)