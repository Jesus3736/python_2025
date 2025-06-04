# Trabajando con diccionarios

# agregando un nuevo par clave/valor a un diccionario
carro = { "año" : 2015 }
carro["color"] = "Rojo"
print( "Year: {} t color: {}".format( carro['año'], carro['color'] ) )
#---------------------------------------------------------

#actualizando el valor para el par clave/valor existente
carro['color'] = 'Negro'
print( "Year: {} t Color: {}".format( carro['año'], carro['color'] ) )
#---------------------------------------------------------
"""
# borrando un par clave/valor de un diccionario
try:

    del carro ['color']
    print (carro)
    except:
        print ("No se puede eliminar el elementos")

        # ------------------------------------------------
        # Bucle de un diccionario
        """


        # interando sobre un diccionario a travez de las claves
        persona = {"nombre": "Yeli", "edad": 17 }
        
           print()


