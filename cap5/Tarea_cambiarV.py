nombres = ["Jesus", "propio", "Loteng"]

def CambianValor(unalista, nombre, indice):
    if 0 <= indice < len(unalista):
        unalista[indice] = nombre
    else:
        print(f"Índice ({indice}) fuera de rango para la lista de longitud {len(unalista)}")

print("Lista original:", nombres)
CambianValor(nombres, "Apiconio", 1)
print("Lista modificada:", nombres)