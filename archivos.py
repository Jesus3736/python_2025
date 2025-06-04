# Archivos

# abrir / crear y escribir en un archivo de texto
f = open('prueba.text', 'w+') # abre el archivo en modo lectura y es 
f.write ('Hola mundo/n') # escribe en el archivo
f.close() # cierra el archivo
# leer de un archivo de texto
f = open('prueba.txt', 'r') # abre el archivo en modo lectura
contenido = f.read() # lee el contenido del archivo
print(contenido) # imprimo el contenido del archivo
f.close() # cierra el archivo
# ----------------------------

""
# abrir / crear y escribir en un archivo csv

import csv
with open ('prueba.csv',mode='w', newline="") as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(['Nombre', 'Edad'])
    writer.wrterow(['Yelitza',17])

    # leer de un archivo csv
    with open('prueba.csv',mode='r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            print(row)
            # ---------------------
