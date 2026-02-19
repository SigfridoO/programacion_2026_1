

class Persona:
    # constructor
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.calificaciones = []
        #print("Dentro del constructor")

    def mostrar_calificaciones(self):
        texto = ""
        if self.calificaciones:
            for calif in self.calificaciones:
                texto = texto + ", " + str(calif)
            print (texto)
        else:
            print("Sin calificaciones")
    
    def calificar(self):
        print("Ingrese las calificaciones escriba -1 para terminar")
        calif = 0
        while calif != '-1':
            calif = input("Ingresa calificacion: ")
            if calif != '-1':
                self.calificaciones.append(float(calif))


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
