# Diccionario

carro ={'año': 2015}
carro['color'] = 'Rojo'
print ('año: {} \t color: {}'.format(carro['año'], carro['color']))

carro['color'] = 'Negro'
print ('año: {} \t color: {}'.format(carro['año'], carro['color']))

# borrando un par clave/valor de un diccionario
try:
    del carro ['color']
    print (carro)
except:
    print ("No se pudo eliminar el elemento")

# iterando sobre un diccionario a traves de las claves 
persona = { "nombre": "yeli", "edad": 17}
for llave in persona.keys( ):
    print(llave)
    print( persona [llave] )
print ('\n')

# iterando solo valores 
for valor in personas.values( ):
    print(valor)
print ('\n')

# iterando sobre un diccionario atraves de las claves
persona = { "nombre": "yeli", "edad": 17 }
for llave in persona.keys( ):
    print(llave)
    print( persona [llave] )
print ('\n')