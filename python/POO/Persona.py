

class Persona:
    # constructor
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        #print("Dentro del constructor")

    def saludar (self):
        print(f"Hola como estas soy {self.nombre}")

    # toString: representacion en cadena de caracteres del objeto
    def __str__(self):
        return f"Mi nombre es {self.nombre} {self.apellido}"

def main():
    gael = Persona("Gael", "Garrido")
    gael.saludar()
    print(gael)

    print("-----")
    oliver = Persona("Oliver", "Romero")
    oliver.saludar()
    print(oliver)

if __name__ == '__main__':
    main()
