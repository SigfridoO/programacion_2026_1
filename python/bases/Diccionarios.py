from Varios import nuevo_tema, nuevo_subtema

nuevo_tema("Dicccionarios")
nuevo_subtema("Creando diccionario")

alumno ={
    "nombre": "Coco", 
    "apellido": "Cruz",
    "edad": 27,
    "Hobbys": ["Coleccionar dinosaurios", "Jugar"]
         }

print("alumno:", alumno)

nuevo_subtema("Obteniendo claves")
print("alumno.keys():", alumno.keys())

nuevo_subtema("Obteniendo valores")
print("alumno.values():", alumno.values())

nuevo_subtema("Obteniendo elementos")
print("alumno.items():", alumno.items())

nuevo_subtema("Obteniendo el valor de una clave")
print("alumno.get('nombre'):", alumno.get('nombre'))
print("alumno['nombre']:", alumno['nombre'])


# nuevo_subtema("Obteniendo el valor de una clave que no existe")
# print("alumno.get('telefono'):", alumno.get('telefono'))
# print("alumno['telefono']:", alumno['telefono'])

nuevo_subtema("anexando elementos")
print("alumno.update({'telefono': 911}):", 
      alumno.update({'telefono': 911}))
print("alumno:", alumno)

nuevo_subtema("quitando un elementos")
valor_extraido = alumno.pop('nombre')
print("alumno_extraido'", valor_extraido)
print("alumno:", alumno)

nuevo_subtema("recorriendo los elementos (for)")
for clave, valor in alumno.items():
    print(f"{clave}, {valor}")

nuevo_subtema("eliminando todos los elementos")
alumno.clear()
print("alumno:", alumno)