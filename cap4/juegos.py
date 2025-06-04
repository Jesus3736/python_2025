# juego.py

palabra = "toño"
vidas = 8
progreso = ["_"] * len(palabra)

while vidas > 0:
    print(" ".join(progreso))
    intento = input("Escribe una letra: ").lower()

    acierto = False
    for i, letra in enumerate(palabra):
        if intento == letra:
            progreso[i] = intento
            acierto = True

    if not acierto:
        vidas -= 1
        print("Incorrecto.")

    if "_" not in progreso:
        print(f"¡Ganaste! La palabra era: {palabra}")
        break

if "_" in progreso:
    print(f"Perdiste. La palabra era: {palabra}")