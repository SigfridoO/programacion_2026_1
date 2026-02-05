from Varios import nuevo_tema, nuevo_subtema

nuevo_tema("Funciones escenciales")

nuevo_subtema("captura por medio de consola")
# nombre = input("Por favor introduce tu nombre: ")
# print(f"El nombre introducido es : {nombre}")

nuevo_subtema("impresion base")
numero = 912645
print(f"numero en decimal: {numero}")
print(f"numero en hexadecimal: {hex(numero)}")
print(f"numero en binario: {bin(numero)}")
print(f"numero en octal: {oct(numero)}")

nuevo_subtema("cambio de tipo")
numero_string = "342"
print(f"numero en entero: {int(numero_string)  + 88 }")

numero_string_2 = "342.88"
print(f"numero en flotante: {float(numero_string_2)  + 13 }")

numero3 = 3
print(f"numero convertido a cadena de caracteres: {str(numero3) + ' gatos' }")

nuevo_subtema("caracter a ascii")
letra = 'f'
representacion_ascii = ord(letra)
print(f"La representacion ascii de la letra {letra}  \
      es {representacion_ascii}")

nuevo_subtema("ascii a caracter")
codigo = 88
letra = chr(codigo)
print(f"El simbolo del codigo {codigo} es {letra}")