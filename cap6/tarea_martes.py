datos = {}
datos['nombre'] = input("ingrese su nombre: ")
datos['direccion'] = input("ingrese su direccion: ")
datos['direccion'] = input("ingrese su numero de telefono: ")

print ("\nDatos ingresados:")
for valor in datos.values( ):
    print(valor) 

# se usan dos puntos en lugar de coma
"""
persona = {'nombre': 'Enrique Barajas'}
print(persona['nombre'])
"""