
from blessed import Terminal

from Varios import nuevo_tema, nuevo_subtema

term = Terminal()


print("hola mundo")


"""
Este es 
un comentario 
de 
muchas líneas
"""



# Se explican las variables en python
nuevo_tema("Variables")
# int: numeros enteros
edad = 21
print("edad: ", edad)

# float: número con punto decimal
estatura = 1.70
print("estatura: ", estatura)

# str: cadena de caracteres
nombre = "toño"
print("nombre: ", nombre)

# bool: variable boleana
fuma = True  #False
print("fuma: ", fuma)
nuevo_tema("Operadores aritméticos")

numero1 = 7
numero2 = 3
print("numero1: ", numero1)
print("numero2: ", numero2)
print("numero1 + numero2:", numero1 + numero2)
print("numero1 - numero2:", numero1 - numero2)
print("numero1 / numero2:", numero1 / numero2)
print("numero1 * numero2:", numero1 * numero2)
print("numero1 % numero2:", numero1 % numero2)
print("numero1 ** numero2:", numero1 ** numero2)


nuevo_tema("Operadores lógicos")
estudia = True
pasara = False
print("estudia: ", estudia)
print("pasara: ", pasara)
print("estudia and pasara: ", estudia and pasara)
print("estudia or pasara: ", estudia or pasara)
print("not estudia: ", not estudia)
print("estudia xor pasara: ", estudia ^ pasara)


nuevo_tema("Intrucciones de control")
print("---------- If-else ")
numero_a = 3
numero_b = 5
print("numero_a:", numero_a)
print("numero_b:", numero_b)

if numero_a > numero_b:
    print(f"El número {numero_a} es MAYOR al numero {numero_b}")
if numero_a >= numero_b:
    print(f"El número {numero_a} es MAYOR O IGUAL al numero {numero_b}")
if numero_a < numero_b:
    print(f"El número {numero_a} es MENOR al numero {numero_b}")
if numero_a <= numero_b:
    print(f"El número {numero_a} es MENOR O IGUAL al numero {numero_b}")
if numero_a == numero_b:
    print(f"El número {numero_a} es IGUAL al numero {numero_b}")

nuevo_tema("cadena de caracteres")
nombre2 = "Arturo"
nombre3 = "José"

print("Hola", nombre2, "'¿Cómo estas?', mi nombre es", nombre3)

saludo = f"Hola {nombre2} '¿Cómo estas?', mi nombre es {nombre3}"
print(saludo)
saludo2 = "Hola {} '¿Cómo estas?', mi nombre es {}".format(nombre2, nombre3)
print(saludo2)


print("Debo venir a clases\n" * 10)
print(nombre2, nombre3)
print(nombre2, nombre3, sep="********", end="--------")
print()

nuevo_tema("funciones")

nuevo_tema("list: Listas")
frutas = ['kiwis', 'naranjas', 'peras', 'manzanas', 'uvas', 'limones']
nuevo_subtema('Imprimiendo la lista')
print("frutas: ", frutas)

nuevo_subtema('Seleccionando un elemento')
print("frutas[2]:", frutas[2])

nuevo_subtema('mostrar el tamaño de la lista')
print("len(frutas):" , len(frutas))

nuevo_subtema('obtener desde el elemento 2 hasta el 3')
print("frutas[2:4]:" , frutas[2:4])

nuevo_subtema('agregando elementos')
frutas.append('papayas')
frutas.append('sandias')
print("frutas: ", frutas)

nuevo_subtema('quitando elementos')
frutas.remove('peras')
print("frutas: ", frutas)

nuevo_subtema('obtener desde el elemento 1 hasta el 5 cada dos elementos')
print("frutas[1:6:2]:" , frutas[1:6:2])

nuevo_subtema('obtener el último elemento')
print("frutas[-1]:" , frutas[-1])

nuevo_subtema('obtener el penúltimo elemento')
print("frutas[-2]:" , frutas[-2])

nuevo_subtema('obtener el anteúltimo elemento')
print("frutas[-3]:" , frutas[-3])

nuevo_subtema('invirtiendo la lista')
print("frutas: ", frutas)
frutas.reverse()
print("frutas: ", frutas)

nuevo_subtema('ordenando la lista')
print("frutas: ", frutas)
frutas.sort()
print("frutas: ", frutas)

nuevo_subtema('quitar elemento')
print("frutas: ", frutas)
elemento_removido = frutas.pop(1)
print("frutas: ", frutas)
print("elemento_removido: ", elemento_removido)

nuevo_subtema('agregar elemento en la posicion 3')
print("frutas: ", frutas)
frutas.insert(3,'cerezas')
print("frutas: ", frutas)

#nuevo_subtema('borrar lista')
#frutas.clear()
print("frutas: ", term.bold_mediumorchid,  frutas, term.normal)