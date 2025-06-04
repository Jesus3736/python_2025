"""
f = open('prueba.txt', 'w+')
f.write ('Hola mundo\n')
f.close()

f = open('prueba.txt', 'r')
contenido = f.read
print(contenido)
f.close()
"""

import csv
with open ('prueba.csv', mode='w', newline="") as f:
     write = csv.writer(f, delimiter=',')
     write.writerow(['Nombre', 'Edad'])
     write.writerow(['Jesus', 17])

with open('prueba.csv', mode='r') as f:
reader =csv.reader(f,delimiter=',')----
     for row in reader:
          print(row)