# declaramos una variable tipo Diccionario
vacio = {}
persona = {'nombre' : 'jesus'}
cliente = {
   'nombre' : 'toño',
   'edad' : 17,
}
print (persona)
print (cliente)

"""
# Accediendo a la informacion del diccionario
print (persona['nombre'])

#Usando el metodo get para acceder al diccionario
print (persona.get('nombre'))
print (persona.get ('edad))

# almacenado una lista en un diccionario y accesandola
datos = { 'deportes' : ['fut' , 'basquet', 'raquet' , 'voli', 'gotcha']}
print(datos ['deportes'])

# almacenandoun diccionario dentro de una lista y accediendo a el
lista =['Andrea', 'Luis',{'nombre': 'Estrella'}]
print(lista[2]['nombre'])
"""

# diccionarios en diccionarios 
datos = {
   'equipo': 'Toluca',
   'victorias': {'2024':11, '2025':10}
}
print(datos['victorias'])
print (datos['victorias']['2025'])






# almacenado una lista en un diccionario y accesandola